/* Copyright (c) 2013-2022. The SimGrid Team. All rights reserved.          */

/* This program is free software; you can redistribute it and/or modify it
 * under the terms of the license (GNU LGPL) which comes with this package. */

#include <simgrid/s4u/Engine.hpp>

#include "src/kernel/EngineImpl.hpp"
#include "src/kernel/resource/StandardLinkImpl.hpp"
#include <numeric>

XBT_LOG_EXTERNAL_DEFAULT_CATEGORY(res_network);

/*********
 * Model *
 *********/

namespace simgrid::kernel::resource {

StandardLinkImpl::StandardLinkImpl(const std::string& name) : LinkImpl(name), piface_(this)
{
  if (name != "__loopback__")
    xbt_assert(not s4u::Link::by_name_or_null(name), "Link '%s' declared several times in the platform.", name.c_str());

  XBT_DEBUG("Create link '%s'", name.c_str());
}

void StandardLinkImpl::Deleter::operator()(resource::StandardLinkImpl* link) const
{
  link->destroy();
}

/** @brief Fire the required callbacks and destroy the object
 *
 * Don't delete directly a Link, call l->destroy() instead.
 */
void StandardLinkImpl::destroy()
{
  s4u::Link::on_destruction(piface_);
  delete this;
}

constexpr kernel::lmm::Constraint::SharingPolicy to_maxmin_policy(s4u::Link::SharingPolicy policy)
{
  switch (policy) {
    case s4u::Link::SharingPolicy::NONLINEAR:
      return kernel::lmm::Constraint::SharingPolicy::NONLINEAR;
    case s4u::Link::SharingPolicy::FATPIPE:
      return kernel::lmm::Constraint::SharingPolicy::FATPIPE;
    default:
      return kernel::lmm::Constraint::SharingPolicy::SHARED;
  }
}

void StandardLinkImpl::set_sharing_policy(s4u::Link::SharingPolicy policy, const s4u::NonLinearResourceCb& cb)
{
  get_constraint()->set_sharing_policy(to_maxmin_policy(policy), cb);
  sharing_policy_ = policy;
}

void StandardLinkImpl::latency_check(double latency) const
{
  static double last_warned_latency = sg_surf_precision;
  if (latency != 0.0 && latency < last_warned_latency) {
    XBT_WARN("Latency for link %s is smaller than surf/precision (%g < %g)."
             " For more accuracy, consider setting \"--cfg=surf/precision:%g\".",
             get_cname(), latency, sg_surf_precision, latency);
    last_warned_latency = latency;
  }
}

StandardLinkImpl* StandardLinkImpl::set_englobing_zone(routing::NetZoneImpl* englobing_zone)
{
  englobing_zone_ = englobing_zone;
  return this;
}

void StandardLinkImpl::turn_on()
{
  if (not is_on()) {
    Resource::turn_on();
    s4u::Link::on_state_change(piface_);
  }
}

void StandardLinkImpl::turn_off()
{
  if (is_on()) {
    Resource::turn_off();
    s4u::Link::on_state_change(piface_);

    const kernel::lmm::Element* elem = nullptr;
    double now                       = EngineImpl::get_clock();
    while (const auto* var = get_constraint()->get_variable(&elem)) {
      Action* action = var->get_id();
      if (action->get_state() == Action::State::INITED || action->get_state() == Action::State::STARTED) {
        action->set_finish_time(now);
        action->set_state(Action::State::FAILED);
      }
    }
  }
}

void StandardLinkImpl::seal()
{
  if (is_sealed())
    return;

  xbt_assert(this->get_model(), "Cannot seal Link(%s) without setting the Network model first", this->get_cname());
  Resource::seal();
}

void StandardLinkImpl::on_bandwidth_change() const
{
  s4u::Link::on_bandwidth_change(piface_);
}

void StandardLinkImpl::set_bandwidth_profile(profile::Profile* profile)
{
  if (profile) {
    xbt_assert(bandwidth_.event == nullptr, "Cannot set a second bandwidth profile to Link %s", get_cname());
    bandwidth_.event = profile->schedule(&profile::future_evt_set, this);
  }
}

void StandardLinkImpl::set_latency_profile(profile::Profile* profile)
{
  if (profile) {
    xbt_assert(latency_.event == nullptr, "Cannot set a second latency profile to Link %s", get_cname());
    latency_.event = profile->schedule(&profile::future_evt_set, this);
  }
}

void StandardLinkImpl::set_concurrency_limit(int limit) const
{
  if (limit != -1) {
    get_constraint()->reset_concurrency_maximum();
  }
  get_constraint()->set_concurrency_limit(limit);
}

} // namespace simgrid::kernel::resource
