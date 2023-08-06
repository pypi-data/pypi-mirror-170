/* Copyright (c) 2013-2022. The SimGrid Team. All rights reserved.          */

/* This program is free software; you can redistribute it and/or modify it
 * under the terms of the license (GNU LGPL) which comes with this package. */

#include <simgrid/kernel/routing/NetPoint.hpp>
#include <simgrid/kernel/routing/NetZoneImpl.hpp>
#include <simgrid/s4u/Engine.hpp>
#include <simgrid/s4u/Host.hpp>

#include "src/kernel/EngineImpl.hpp"
#include "src/kernel/lmm/maxmin.hpp"
#include "src/kernel/resource/profile/Event.hpp"
#include "src/surf/disk_s19.hpp"

XBT_LOG_EXTERNAL_DEFAULT_CATEGORY(res_disk);

/*********
 * Model *
 *********/

void surf_disk_model_init_default()
{
  auto disk_model = std::make_shared<simgrid::kernel::resource::DiskS19Model>("Disk");
  auto* engine    = simgrid::kernel::EngineImpl::get_instance();
  engine->add_model(disk_model);
  engine->get_netzone_root()->set_disk_model(disk_model);
}

namespace simgrid::kernel::resource {

DiskImpl* DiskS19Model::create_disk(const std::string& name, double read_bandwidth, double write_bandwidth)
{
  return (new DiskS19(name, read_bandwidth, write_bandwidth))->set_model(this);
}

void DiskS19Model::update_actions_state(double /*now*/, double delta)
{
  for (auto it = std::begin(*get_started_action_set()); it != std::end(*get_started_action_set());) {
    auto& action = *it;
    ++it; // increment iterator here since the following calls to action.finish() may invalidate it
    action.update_remains(rint(action.get_rate() * delta));
    action.update_max_duration(delta);

    if (((action.get_remains_no_update() <= 0) && (action.get_variable()->get_penalty() > 0)) ||
        ((action.get_max_duration() != NO_MAX_DURATION) && (action.get_max_duration() <= 0))) {
      action.finish(Action::State::FINISHED);
    }
  }
}

DiskAction* DiskS19Model::io_start(const DiskImpl* disk, sg_size_t size, s4u::Io::OpType type)
{
  auto* action = new DiskS19Action(this, static_cast<double>(size), not disk->is_on());
  get_maxmin_system()->expand(disk->get_constraint(), action->get_variable(), 1.0);
  switch (type) {
    case s4u::Io::OpType::READ:
      get_maxmin_system()->expand(disk->get_read_constraint(), action->get_variable(), 1.0);
      break;
    case s4u::Io::OpType::WRITE:
      get_maxmin_system()->expand(disk->get_write_constraint(), action->get_variable(), 1.0);
      break;
    default:
      THROW_UNIMPLEMENTED;
  }
  if (const auto& factor_cb = disk->get_factor_cb()) { // handling disk variability
    action->set_rate_factor(factor_cb(size, type));
  }
  return action;
}

/************
 * Resource *
 ************/
void DiskS19::set_read_bandwidth(double value)
{
  DiskImpl::set_read_bandwidth(value);
  if (get_read_constraint()) {
    get_model()->get_maxmin_system()->update_constraint_bound(get_read_constraint(), get_read_bandwidth());
  }
}

void DiskS19::set_write_bandwidth(double value)
{
  DiskImpl::set_write_bandwidth(value);
  if (get_write_constraint()) {
    get_model()->get_maxmin_system()->update_constraint_bound(get_write_constraint(), get_write_bandwidth());
  }
}

void DiskS19::set_readwrite_bandwidth(double value)
{
  DiskImpl::set_readwrite_bandwidth(value);
  if (get_constraint()) {
    get_model()->get_maxmin_system()->update_constraint_bound(get_constraint(), get_readwrite_bandwidth());
  }
}

void DiskS19::apply_event(kernel::profile::Event* triggered, double value)
{
  /* Find out which of my iterators was triggered, and react accordingly */
  if (triggered == get_read_event()) {
    set_read_bandwidth(value);
    unref_read_event();
  } else if (triggered == get_write_event()) {
    set_write_bandwidth(value);
    unref_write_event();
  } else if (triggered == get_state_event()) {
    if (value > 0)
      turn_on();
    else
      turn_off();
    unref_state_event();
  } else {
    xbt_die("Unknown event!\n");
  }

  XBT_DEBUG("There was a resource state event, need to update actions related to the constraint (%p)",
            get_constraint());
}

/**********
 * Action *
 **********/

DiskS19Action::DiskS19Action(Model* model, double cost, bool failed)
    : DiskAction(model, cost, failed, model->get_maxmin_system()->variable_new(this, 1.0, -1.0, 3))
{
}

void DiskS19Action::update_remains_lazy(double /*now*/)
{
  THROW_IMPOSSIBLE;
}
} // namespace simgrid::kernel::resource
