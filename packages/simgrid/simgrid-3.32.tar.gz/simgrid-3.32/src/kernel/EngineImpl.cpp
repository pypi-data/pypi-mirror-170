/* Copyright (c) 2016-2022. The SimGrid Team. All rights reserved.          */

/* This program is free software; you can redistribute it and/or modify it
 * under the terms of the license (GNU LGPL) which comes with this package. */

#include <simgrid/Exception.hpp>
#include <simgrid/kernel/Timer.hpp>
#include <simgrid/kernel/routing/NetPoint.hpp>
#include <simgrid/kernel/routing/NetZoneImpl.hpp>
#include <simgrid/s4u/Host.hpp>
#include <simgrid/sg_config.hpp>

#include "mc/mc.h"
#include "src/kernel/EngineImpl.hpp"
#include "src/kernel/resource/StandardLinkImpl.hpp"
#include "src/kernel/resource/profile/Profile.hpp"
#include "src/mc/mc_record.hpp"
#include "src/mc/mc_replay.hpp"
#include "src/smpi/include/smpi_actor.hpp"
#include "src/surf/xml/platf.hpp"
#include "xbt/module.h"
#include "xbt/xbt_modinter.h" /* whether initialization was already done */

#include <boost/algorithm/string/predicate.hpp>
#ifndef _WIN32
#include <dlfcn.h>
#endif /* _WIN32 */

#if SIMGRID_HAVE_MC
#include "src/mc/remote/AppSide.hpp"
#endif

XBT_LOG_NEW_DEFAULT_CATEGORY(ker_engine, "Logging specific to Engine (kernel)");

namespace simgrid::kernel {
double EngineImpl::now_           = 0.0;
EngineImpl* EngineImpl::instance_ = nullptr; /* That singleton is awful too. */

config::Flag<double> cfg_breakpoint{"debug/breakpoint",
                                    "When non-negative, raise a SIGTRAP after given (simulated) time", -1.0};
config::Flag<bool> cfg_verbose_exit{"debug/verbose-exit", "Display the actor status at exit", true};

constexpr std::initializer_list<std::pair<const char*, context::ContextFactory* (*)()>> context_factories = {
#if HAVE_RAW_CONTEXTS
    {"raw", &context::raw_factory},
#endif
#if HAVE_UCONTEXT_CONTEXTS
    {"ucontext", &context::sysv_factory},
#endif
#if HAVE_BOOST_CONTEXTS
    {"boost", &context::boost_factory},
#endif
    {"thread", &context::thread_factory},
};

static_assert(context_factories.size() > 0, "No context factories are enabled for this build");

// Create the list of possible contexts:
static inline std::string contexts_list()
{
  std::string res;
  std::string sep = "";
  for (auto const& [factory_name, _] : context_factories) {
    res += sep + factory_name;
    sep = ", ";
  }
  return res;
}

static config::Flag<std::string> context_factory_name("contexts/factory",
                                                      (std::string("Possible values: ") + contexts_list()).c_str(),
                                                      context_factories.begin()->first);

} // namespace simgrid::kernel

XBT_ATTRIB_NORETURN static void inthandler(int)
{
  if (simgrid::kernel::cfg_verbose_exit) {
    XBT_INFO("CTRL-C pressed. The current status will be displayed before exit (disable that behavior with option "
             "'debug/verbose-exit').");
    simgrid::kernel::EngineImpl::get_instance()->display_all_actor_status();
  } else {
    XBT_INFO("CTRL-C pressed, exiting. Hiding the current process status since 'debug/verbose-exit' is set to false.");
  }
  exit(1);
}

#ifndef _WIN32
static void segvhandler(int signum, siginfo_t* siginfo, void* /*context*/)
{
  if ((siginfo->si_signo == SIGSEGV && siginfo->si_code == SEGV_ACCERR) || siginfo->si_signo == SIGBUS) {
    fprintf(stderr,
            "Access violation or Bus error detected.\n"
            "This probably comes from a programming error in your code, or from a stack\n"
            "overflow. If you are certain of your code, try increasing the stack size\n"
            "   --cfg=contexts/stack-size:XXX (current size is %u KiB).\n"
            "\n"
            "If it does not help, this may have one of the following causes:\n"
            "a bug in SimGrid, a bug in the OS or a bug in a third-party libraries.\n"
            "Failing hardware can sometimes generate such errors too.\n"
            "\n"
            "If you think you've found a bug in SimGrid, please report it along with a\n"
            "Minimal Working Example (MWE) reproducing your problem and a full backtrace\n"
            "of the fault captured with gdb or valgrind.\n",
            simgrid::kernel::context::stack_size / 1024);
  } else if (siginfo->si_signo == SIGSEGV) {
    fprintf(stderr, "Segmentation fault.\n");
#if HAVE_SMPI
    if (SMPI_is_inited() && smpi_cfg_privatization() == SmpiPrivStrategies::NONE) {
#if HAVE_PRIVATIZATION
      fprintf(stderr, "Try to enable SMPI variable privatization with --cfg=smpi/privatization:yes.\n");
#else
      fprintf(stderr, "Sadly, your system does not support --cfg=smpi/privatization:yes (yet).\n");
#endif /* HAVE_PRIVATIZATION */
    }
#endif /* HAVE_SMPI */
  }
  std::raise(signum);
}

/**
 * Install signal handler for SIGSEGV.  Check that nobody has already installed
 * its own handler.  For example, the Java VM does this.
 */
static void install_segvhandler()
{
  stack_t old_stack;

  if (simgrid::kernel::context::Context::install_sigsegv_stack(&old_stack, true) == -1) {
    XBT_WARN("Failed to register alternate signal stack: %s", strerror(errno));
    return;
  }
  if (not(old_stack.ss_flags & SS_DISABLE)) {
    XBT_DEBUG("An alternate stack was already installed (sp=%p, size=%zu, flags=%x). Restore it.", old_stack.ss_sp,
              old_stack.ss_size, (unsigned)old_stack.ss_flags);
    sigaltstack(&old_stack, nullptr);
  }

  struct sigaction action;
  struct sigaction old_action;
  action.sa_sigaction = &segvhandler;
  action.sa_flags     = SA_ONSTACK | SA_RESETHAND | SA_SIGINFO;
  sigemptyset(&action.sa_mask);

  /* Linux tend to raise only SIGSEGV where other systems also raise SIGBUS on severe error */
  for (int sig : {SIGSEGV, SIGBUS}) {
    if (sigaction(sig, &action, &old_action) == -1) {
      XBT_WARN("Failed to register signal handler for signal %d: %s", sig, strerror(errno));
      continue;
    }
    if ((old_action.sa_flags & SA_SIGINFO) || old_action.sa_handler != SIG_DFL) {
      XBT_DEBUG("A signal handler was already installed for signal %d (%p). Restore it.", sig,
                (old_action.sa_flags & SA_SIGINFO) ? (void*)old_action.sa_sigaction : (void*)old_action.sa_handler);
      sigaction(sig, &old_action, nullptr);
    }
  }
}

#endif /* _WIN32 */

namespace simgrid::kernel {

EngineImpl::~EngineImpl()
{
  /* Also delete the other data */
  delete netzone_root_;
  for (auto const& [_, netpoint] : netpoints_)
    delete netpoint;

  for (auto const& [_, mailbox] : mailboxes_)
    delete mailbox;

  /* Kill all actors (but maestro) */
  maestro_->kill_all();
  run_all_actors();
  empty_trash();

  delete maestro_;
  delete context_factory_;

  /* clear models before freeing handle, network models can use external callback defined in the handle */
  models_prio_.clear();
}

void EngineImpl::initialize(int* argc, char** argv)
{
  xbt_assert(EngineImpl::instance_ == nullptr,
             "It is currently forbidden to create more than one instance of kernel::EngineImpl");
  EngineImpl::instance_ = this;
#if SIMGRID_HAVE_MC
  // The communication initialization is done ASAP, as we need to get some init parameters from the MC for different
  // layers. But instance_ needs to be created, as we send the address of some of its fields to the MC that wants to
  // read them directly.
  simgrid::mc::AppSide::initialize();
#endif

  if (xbt_initialized == 0) {
    xbt_init(argc, argv);

    sg_config_init(argc, argv);
  }

  instance_->context_mod_init();

  /* Prepare to display some more info when dying on Ctrl-C pressing */
  std::signal(SIGINT, inthandler);

#ifndef _WIN32
  install_segvhandler();
#endif

  /* register a function to be called by SURF after the environment creation */
  sg_platf_init();
  s4u::Engine::on_platform_created_cb([this]() { this->presolve(); });

  if (config::get_value<bool>("debug/clean-atexit"))
    atexit(shutdown);
}

void EngineImpl::context_mod_init() const
{
  xbt_assert(not instance_->has_context_factory());

#if HAVE_SMPI && defined(__NetBSD__)
  smpi_init_options_internal(false);
  std::string priv = config::get_value<std::string>("smpi/privatization");
  if (context_factory_name == "thread" && (priv == "dlopen" || priv == "yes" || priv == "default" || priv == "1")) {
    XBT_WARN("dlopen+thread broken on Apple and BSD. Switching to raw contexts.");
    context_factory_name = "raw";
  }
#endif

#if HAVE_SMPI && defined(__FreeBSD__)
  smpi_init_options_internal(false);
  if (context_factory_name == "thread" && config::get_value<std::string>("smpi/privatization") != "no") {
    XBT_WARN("mmap broken on FreeBSD, but dlopen+thread broken too. Switching to dlopen+raw contexts.");
    context_factory_name = "raw";
  }
#endif

  /* select the context factory to use to create the contexts */
  if (context::ContextFactory::initializer) { // Give Java a chance to hijack the factory mechanism
    instance_->set_context_factory(context::ContextFactory::initializer());
    return;
  }
  /* use the factory specified by --cfg=contexts/factory:value */
  for (auto const& [factory_name, factory] : context_factories)
    if (context_factory_name == factory_name) {
      instance_->set_context_factory(factory());
      break;
    }

  if (not instance_->has_context_factory()) {
    XBT_ERROR("Invalid context factory specified. Valid factories on this machine:");
#if HAVE_RAW_CONTEXTS
    XBT_ERROR("  raw: high performance context factory implemented specifically for SimGrid");
#else
    XBT_ERROR("  (raw contexts were disabled at compilation time on this machine -- check configure logs for details)");
#endif
#if HAVE_UCONTEXT_CONTEXTS
    XBT_ERROR("  ucontext: classical system V contexts (implemented with makecontext, swapcontext and friends)");
#else
    XBT_ERROR("  (ucontext was disabled at compilation time on this machine -- check configure logs for details)");
#endif
#if HAVE_BOOST_CONTEXTS
    XBT_ERROR("  boost: this uses the boost libraries context implementation");
#else
    XBT_ERROR("  (boost was disabled at compilation time on this machine -- check configure logs for details. Did you "
              "install the libboost-context-dev package?)");
#endif
    XBT_ERROR("  thread: slow portability layer using pthreads as provided by gcc");
    xbt_die("Please use a valid factory.");
  }
}

void EngineImpl::shutdown()
{
  if (EngineImpl::instance_ == nullptr)
    return;
  XBT_DEBUG("EngineImpl::shutdown() called. Simulation's over.");
#if HAVE_SMPI
  if (not instance_->actor_list_.empty()) {
    if (smpi_process() && smpi_process()->initialized()) {
      xbt_die("Process exited without calling MPI_Finalize - Killing simulation");
    } else {
      XBT_WARN("Process called exit when leaving - Skipping cleanups");
      return;
    }
  }
#endif

  if (instance_->has_actors_to_run() && simgrid_get_clock() <= 0.0) {
    XBT_CRITICAL("   ");
    XBT_CRITICAL("The time is still 0, and you still have processes ready to run.");
    XBT_CRITICAL("It seems that you forgot to run the simulation that you setup.");
    xbt_die("Bailing out to avoid that stop-before-start madness. Please fix your code.");
  }

  while (not timer::kernel_timers().empty()) {
    delete timer::kernel_timers().top().second;
    timer::kernel_timers().pop();
  }

  tmgr_finalize();
  sg_platf_exit();

  delete instance_;
  instance_ = nullptr;
}

void EngineImpl::seal_platform() const
{
  /* Seal only once */
  static bool sealed = false;
  if (sealed)
    return;
  sealed = true;

  /* seal netzone root, recursively seal children netzones, hosts and disks */
  netzone_root_->seal();
}

void EngineImpl::load_platform(const std::string& platf)
{
  double start = xbt_os_time();
  if (boost::algorithm::ends_with(platf, ".so") || boost::algorithm::ends_with(platf, ".dylib")) {
#ifdef _WIN32
    xbt_die("loading platform through shared library isn't supported on windows");
#else
    void* handle = dlopen(platf.c_str(), RTLD_LAZY);
    xbt_assert(handle, "Impossible to open platform file: %s", platf.c_str());
    platf_handle_           = std::unique_ptr<void, std::function<int(void*)>>(handle, dlclose);
    using load_fct_t = void (*)(const simgrid::s4u::Engine&);
    auto callable           = (load_fct_t)dlsym(platf_handle_.get(), "load_platform");
    const char* dlsym_error = dlerror();
    xbt_assert(not dlsym_error, "Error: %s", dlsym_error);
    callable(*simgrid::s4u::Engine::get_instance());
#endif /* _WIN32 */
  } else {
    parse_platform_file(platf);
  }

  double end = xbt_os_time();
  XBT_DEBUG("PARSE TIME: %g", (end - start));
}

void EngineImpl::load_deployment(const std::string& file) const
{
  sg_platf_exit();
  sg_platf_init();

  surf_parse_open(file);
  surf_parse();
  surf_parse_close();
}

void EngineImpl::register_function(const std::string& name, const actor::ActorCodeFactory& code)
{
  registered_functions[name] = code;
}
void EngineImpl::register_default(const actor::ActorCodeFactory& code)
{
  default_function = code;
}

void EngineImpl::add_model(std::shared_ptr<resource::Model> model, const std::vector<resource::Model*>& dependencies)
{
  auto model_name = model->get_name();
  xbt_assert(models_prio_.find(model_name) == models_prio_.end(),
             "Model %s already exists, use model.set_name() to change its name", model_name.c_str());

  for (const auto* dep : dependencies) {
    xbt_assert(models_prio_.find(dep->get_name()) != models_prio_.end(),
               "Model %s doesn't exists. Impossible to use it as dependency.", dep->get_name().c_str());
  }
  models_.push_back(model.get());
  models_prio_[model_name] = std::move(model);
}

/** Wake up all actors waiting for a Surf action to finish */
void EngineImpl::handle_ended_actions() const
{
  for (auto const& model : models_) {
    XBT_DEBUG("Handling the failed actions (if any)");
    while (auto* action = model->extract_failed_action()) {
      XBT_DEBUG("   Handling Action %p", action);
      if (action->get_activity() != nullptr) { // Skip vcpu actions
        // Action failures are not automatically reported when the action is started by maestro (as in SimDAG)
        if (action->get_activity()->get_actor() == maestro_)
          action->get_activity()->get_iface()->complete(s4u::Activity::State::FAILED);

        activity::ActivityImplPtr(action->get_activity())->post();
      }
    }
    XBT_DEBUG("Handling the terminated actions (if any)");
    while (auto* action = model->extract_done_action()) {
      XBT_DEBUG("   Handling Action %p", action);
      if (action->get_activity() != nullptr) {
        // Action termination are not automatically reported when the action is started by maestro (as in SimDAG)
        action->get_activity()->set_finish_time(action->get_finish_time());

        if (action->get_activity()->get_actor() == maestro_)
          action->get_activity()->get_iface()->complete(s4u::Activity::State::FINISHED);

        activity::ActivityImplPtr(action->get_activity())->post();
      }
    }
  }
}
/**
 * @brief Executes the actors in actors_to_run.
 *
 * The actors in actors_to_run are run (in parallel if possible). On exit, actors_to_run is empty, and actors_that_ran
 * contains the list of actors that just ran.  The two lists are swapped so, be careful when using them before and after
 * a call to this function.
 */
void EngineImpl::run_all_actors()
{
  instance_->get_context_factory()->run_all(actors_to_run_);

  for (auto const& actor : actors_to_run_)
    if (actor->to_be_freed())
      actor->cleanup_from_kernel();

  actors_to_run_.swap(actors_that_ran_);
  actors_to_run_.clear();
}

actor::ActorImpl* EngineImpl::get_actor_by_pid(aid_t pid)
{
  auto item = actor_list_.find(pid);
  return item == actor_list_.end() ? nullptr : item->second;
}

void EngineImpl::remove_daemon(actor::ActorImpl* actor)
{
  auto it = daemons_.find(actor);
  xbt_assert(it != daemons_.end(), "The dying daemon is not a daemon after all. Please report that bug.");
  daemons_.erase(it);
}

void EngineImpl::add_actor_to_run_list_no_check(actor::ActorImpl* actor)
{
  XBT_DEBUG("Inserting [%p] %s(%s) in the to_run list", actor, actor->get_cname(), actor->get_host()->get_cname());
  actors_to_run_.push_back(actor);
}

void EngineImpl::add_actor_to_run_list(actor::ActorImpl* actor)
{
  if (std::find(begin(actors_to_run_), end(actors_to_run_), actor) != end(actors_to_run_)) {
    XBT_DEBUG("Actor %s is already in the to_run list", actor->get_cname());
  } else {
    XBT_DEBUG("Inserting [%p] %s(%s) in the to_run list", actor, actor->get_cname(), actor->get_host()->get_cname());
    actors_to_run_.push_back(actor);
  }
}
void EngineImpl::empty_trash()
{
  while (not actors_to_destroy_.empty()) {
    actor::ActorImpl* actor = &actors_to_destroy_.front();
    actors_to_destroy_.pop_front();
    XBT_DEBUG("Getting rid of %s (refcount: %d)", actor->get_cname(), actor->get_refcount());
    intrusive_ptr_release(actor);
  }
}

void EngineImpl::display_all_actor_status() const
{
  XBT_INFO("%zu actors are still running, waiting for something.", actor_list_.size());
  /*  List the actors and their state */
  XBT_INFO("Legend of the following listing: \"Actor <pid> (<name>@<host>): <status>\"");
  for (auto const& [_, actor] : actor_list_) {
    if (actor->waiting_synchro_) {
      const char* synchro_description = "unknown";

      if (boost::dynamic_pointer_cast<kernel::activity::ExecImpl>(actor->waiting_synchro_) != nullptr)
        synchro_description = "execution";

      if (boost::dynamic_pointer_cast<kernel::activity::CommImpl>(actor->waiting_synchro_) != nullptr)
        synchro_description = "communication";

      if (boost::dynamic_pointer_cast<kernel::activity::SleepImpl>(actor->waiting_synchro_) != nullptr)
        synchro_description = "sleeping";

      if (boost::dynamic_pointer_cast<kernel::activity::SynchroImpl>(actor->waiting_synchro_) != nullptr)
        synchro_description = "synchronization";

      if (boost::dynamic_pointer_cast<kernel::activity::IoImpl>(actor->waiting_synchro_) != nullptr)
        synchro_description = "I/O";

      XBT_INFO("Actor %ld (%s@%s): waiting for %s activity %#zx (%s) in state %s to finish", actor->get_pid(),
               actor->get_cname(), actor->get_host()->get_cname(), synchro_description,
               (xbt_log_no_loc ? (size_t)0xDEADBEEF : (size_t)actor->waiting_synchro_.get()),
               actor->waiting_synchro_->get_cname(), actor->waiting_synchro_->get_state_str());
    } else {
      XBT_INFO("Actor %ld (%s@%s) simcall %s", actor->get_pid(), actor->get_cname(), actor->get_host()->get_cname(),
               actor->simcall_.get_cname());
    }
  }
}

void EngineImpl::presolve() const
{
  XBT_DEBUG("Consume all trace events occurring before the starting time.");
  double next_event_date;
  while ((next_event_date = profile::future_evt_set.next_date()) != -1.0) {
    if (next_event_date > now_)
      break;

    double value                 = -1.0;
    resource::Resource* resource = nullptr;
    while (auto* event = profile::future_evt_set.pop_leq(next_event_date, &value, &resource)) {
      if (value >= 0)
        resource->apply_event(event, value);
    }
  }

  XBT_DEBUG("Set every models in the right state by updating them to 0.");
  for (auto const& model : models_)
    model->update_actions_state(now_, 0.0);
}

double EngineImpl::solve(double max_date) const
{
  double time_delta            = -1.0; /* duration */
  double value                 = -1.0;
  resource::Resource* resource = nullptr;

  if (max_date != -1.0) {
    xbt_assert(max_date >= now_, "You asked to simulate up to %f, but that's in the past already", max_date);

    time_delta = max_date - now_;
  }

  XBT_DEBUG("Looking for next event in all models");
  for (auto model : models_) {
    if (not model->next_occurring_event_is_idempotent()) {
      continue;
    }
    double next_event = model->next_occurring_event(now_);
    if ((time_delta < 0.0 || next_event < time_delta) && next_event >= 0.0) {
      time_delta = next_event;
    }
  }

  XBT_DEBUG("Min for resources (remember that NS3 don't update that value): %f", time_delta);

  XBT_DEBUG("Looking for next trace event");

  while (true) { // Handle next occurring events until none remains
    double next_event_date = profile::future_evt_set.next_date();
    XBT_DEBUG("Next TRACE event: %f", next_event_date);

    for (auto model : models_) {
      /* Skip all idempotent models, they were already treated above
       * NS3 is the one to handled here */
      if (model->next_occurring_event_is_idempotent())
        continue;

      if (next_event_date != -1.0) {
        time_delta = std::min(next_event_date - now_, time_delta);
      } else {
        time_delta = std::max(next_event_date - now_, time_delta); // Get the positive component
      }

      XBT_DEBUG("Run the NS3 network at most %fs", time_delta);
      // run until min or next flow
      double model_next_action_end = model->next_occurring_event(time_delta);

      XBT_DEBUG("Min for network : %f", model_next_action_end);
      if (model_next_action_end >= 0.0)
        time_delta = model_next_action_end;
    }

    if (next_event_date < 0.0 || (next_event_date > now_ + time_delta)) {
      // next event may have already occurred or will after the next resource change, then bail out
      XBT_DEBUG("no next usable TRACE event. Stop searching for it");
      break;
    }

    XBT_DEBUG("Updating models (min = %g, NOW = %g, next_event_date = %g)", time_delta, now_, next_event_date);

    while (auto* event = profile::future_evt_set.pop_leq(next_event_date, &value, &resource)) {
      if(value<0)
	      continue;
      if (resource->is_used() || (watched_hosts().find(resource->get_cname()) != watched_hosts().end())) {
        time_delta = next_event_date - now_;
        XBT_DEBUG("This event invalidates the next_occurring_event() computation of models. Next event set to %f",
                  time_delta);
      }
      // FIXME: I'm too lame to update now_ live, so I change it and restore it so that the real update with surf_min
      // will work
      double round_start = now_;
      now_               = next_event_date;
      /* update state of the corresponding resource to the new value. Does not touch lmm.
         It will be modified if needed when updating actions */
      XBT_DEBUG("Calling update_resource_state for resource %s", resource->get_cname());
      resource->apply_event(event, value);
      now_ = round_start;
    }
  }

  /* FIXME: Moved this test to here to avoid stopping simulation if there are actions running on cpus and all cpus are
   * with availability = 0. This may cause an infinite loop if one cpu has a trace with periodicity = 0 and the other a
   * trace with periodicity > 0.
   * The options are: all traces with same periodicity(0 or >0) or we need to change the way how the events are managed
   */
  if (time_delta < 0) {
    XBT_DEBUG("No next event at all. Bail out now.");
    return -1.0;
  }

  XBT_DEBUG("Duration set to %f", time_delta);

  // Bump the time: jump into the future
  now_ += time_delta;

  // Inform the models of the date change
  for (auto const& model : models_)
    model->update_actions_state(now_, time_delta);

  s4u::Engine::on_time_advance(time_delta);

  return time_delta;
}

void EngineImpl::run(double max_date)
{
  seal_platform();

  if (MC_is_active()) {
#if SIMGRID_HAVE_MC
    mc::AppSide::get()->main_loop();
#else
    xbt_die("MC_is_active() is not supposed to return true in non-MC settings");
#endif
    THROW_IMPOSSIBLE; // main_loop never returns
  }

  if (MC_record_replay_is_active()) {
    mc::RecordTrace::replay(MC_record_path());
    empty_trash();
    return;
  }

  double elapsed_time = -1;
  const std::set<s4u::Activity*>* vetoed_activities = s4u::Activity::get_vetoed_activities();

  do {
    XBT_DEBUG("New Schedule Round; size(queue)=%zu", actors_to_run_.size());

    if (cfg_breakpoint >= 0.0 && simgrid_get_clock() >= cfg_breakpoint) {
      XBT_DEBUG("Breakpoint reached (%g)", cfg_breakpoint.get());
      cfg_breakpoint = -1.0; // Let the simulation continue without hiting the breakpoint again and again
#ifdef SIGTRAP
      std::raise(SIGTRAP);
#else
      std::raise(SIGABRT);
#endif
    }

    while (not actors_to_run_.empty()) {
      XBT_DEBUG("New Sub-Schedule Round; size(queue)=%zu", actors_to_run_.size());

      /* Run all actors that are ready to run, possibly in parallel */
      run_all_actors();

      /* answer sequentially and in a fixed arbitrary order all the simcalls that were issued during that sub-round.
       * The order must be fixed for the simulation to be reproducible (see RR-7653). It's OK here because only maestro
       * changes the list. Killer actors are moved to the end to let victims finish their simcall before dying, but
       * the order remains reproducible (even if arbitrarily). No need to sort the vector for sake of reproducibility.
       */
      for (auto const& actor : actors_that_ran_)
        if (actor->simcall_.call_ != actor::Simcall::Type::NONE)
          actor->simcall_handle(0);

      handle_ended_actions();

      /* If only daemon actors remain, cancel their actions, mark them to die and reschedule them */
      if (actor_list_.size() == daemons_.size())
        for (auto const& dmon : daemons_) {
          XBT_DEBUG("Kill %s", dmon->get_cname());
          maestro_->kill(dmon);
        }
    }

    // Compute the max_date of the next solve.
    // It's either when a timer occurs, or when user-specified deadline is reached, or -1 if none is given
    double next_time = timer::Timer::next();
    if (next_time < 0 && max_date > -1) {
      next_time = max_date;
    } else if (next_time > -1 && max_date > -1) { // either both <0, or both >0
      next_time = std::min(next_time, max_date);
    }

    XBT_DEBUG("Calling solve(%g) %g", next_time, now_);
    elapsed_time = solve(next_time);
    XBT_DEBUG("Moving time ahead. NOW=%g; elapsed: %g", now_, elapsed_time);

    // Execute timers until there isn't anything to be done:
    bool again = false;
    do {
      again = timer::Timer::execute_all();
      handle_ended_actions();
    } while (again);

    /* Clean actors to destroy */
    empty_trash();

    XBT_DEBUG("### elapsed time %f, #actors %zu, #to_run %zu, #vetoed %d", elapsed_time, actor_list_.size(),
              actors_to_run_.size(), (vetoed_activities == nullptr ? -1 : static_cast<int>(vetoed_activities->size())));

    if (elapsed_time < 0. && actors_to_run_.empty() && not actor_list_.empty()) {
      if (actor_list_.size() <= daemons_.size()) {
        XBT_CRITICAL("Oops! Daemon actors cannot do any blocking activity (communications, synchronization, etc) "
                     "once the simulation is over. Please fix your on_exit() functions.");
      } else {
        XBT_CRITICAL("Oops! Deadlock detected, some activities are still around but will never complete. "
                     "This usually happens when the user code is not perfectly clean.");
      }
      display_all_actor_status();
      simgrid::s4u::Engine::on_deadlock();
      for (auto const& [_, actor] : actor_list_) {
        XBT_DEBUG("Kill %s", actor->get_cname());
        maestro_->kill(actor);
      }
    }
  } while ((vetoed_activities == nullptr || vetoed_activities->empty()) &&
           ((elapsed_time > -1.0 && not double_equals(max_date, now_, 0.00001)) || has_actors_to_run()));

  if (not actor_list_.empty() && max_date < 0 && not(vetoed_activities == nullptr || vetoed_activities->empty()))
    THROW_IMPOSSIBLE;

  simgrid::s4u::Engine::on_simulation_end();
}

double EngineImpl::get_clock()
{
  return now_;
}
} // namespace simgrid::kernel
