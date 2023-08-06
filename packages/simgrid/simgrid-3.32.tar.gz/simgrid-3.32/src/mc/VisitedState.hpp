/* Copyright (c) 2007-2022. The SimGrid Team. All rights reserved.          */

/* This program is free software; you can redistribute it and/or modify it
 * under the terms of the license (GNU LGPL) which comes with this package. */

#ifndef SIMGRID_MC_VISITED_STATE_HPP
#define SIMGRID_MC_VISITED_STATE_HPP

#include "src/mc/api/State.hpp"
#include "src/mc/sosp/Snapshot.hpp"

#include <cstddef>
#include <memory>

namespace simgrid::mc {

class XBT_PRIVATE VisitedState {
public:
  std::shared_ptr<simgrid::mc::Snapshot> system_state = nullptr;
  std::size_t heap_bytes_used = 0;
  int actor_count_;
  long num;               // unique id of that state in the storage of all stored IDs
  long original_num = -1; // num field of the VisitedState to which I was declared equal to (used for dot_output)

  explicit VisitedState(unsigned long state_number, unsigned int actor_count);
};

class XBT_PRIVATE VisitedStates {
  std::vector<std::unique_ptr<simgrid::mc::VisitedState>> states_;
public:
  void clear() { states_.clear(); }
  std::unique_ptr<simgrid::mc::VisitedState> addVisitedState(unsigned long state_number,
                                                             simgrid::mc::State* graph_state);

private:
  void prune();
};

} // namespace simgrid::mc

#endif
