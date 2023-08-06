/* mc::remote::AppSide: the Application-side of the channel                 */

/* Copyright (c) 2015-2022. The SimGrid Team. All rights reserved.          */

/* This program is free software; you can redistribute it and/or modify it
 * under the terms of the license (GNU LGPL) which comes with this package. */

#ifndef SIMGRID_MC_CLIENT_H
#define SIMGRID_MC_CLIENT_H

#include "src/mc/remote/Channel.hpp"

#include <memory>

namespace simgrid::mc {

/** Model-checked-side of the communication protocol
 *
 *  Send messages to the model-checker and handles message from it.
 */
class XBT_PUBLIC AppSide {
private:
  Channel channel_;
  static std::unique_ptr<AppSide> instance_;

public:
  AppSide();
  explicit AppSide(int fd) : channel_(fd) {}
  void handle_messages() const;

private:
  void handle_deadlock_check(const s_mc_message_t* msg) const;
  void handle_simcall_execute(const s_mc_message_simcall_execute_t* message) const;
  void handle_finalize(const s_mc_message_int_t* msg) const;
  void handle_actors_status() const;

public:
  Channel const& get_channel() const { return channel_; }
  Channel& get_channel() { return channel_; }
  XBT_ATTRIB_NORETURN void main_loop() const;
  void report_assertion_failure() const;
  void ignore_memory(void* addr, std::size_t size) const;
  void ignore_heap(void* addr, std::size_t size) const;
  void unignore_heap(void* addr, std::size_t size) const;
  void declare_symbol(const char* name, int* value) const;
#if HAVE_UCONTEXT_H
  void declare_stack(void* stack, size_t size, ucontext_t* context) const;
#endif

  // Singleton :/
  // TODO, remove the singleton antipattern.
  static AppSide* initialize();
  static AppSide* get() { return instance_.get(); }
};
} // namespace simgrid::mc

#endif
