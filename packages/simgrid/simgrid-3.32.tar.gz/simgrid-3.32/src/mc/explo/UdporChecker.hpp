/* Copyright (c) 2007-2022. The SimGrid Team.
 * All rights reserved.                                                     */

/* This program is free software; you can redistribute it and/or modify it
 * under the terms of the license (GNU LGPL) which comes with this package. */

#ifndef SIMGRID_MC_UDPOR_CHECKER_HPP
#define SIMGRID_MC_UDPOR_CHECKER_HPP

#include "src/mc/explo/Exploration.hpp"
#include "src/mc/mc_record.hpp"

namespace simgrid::mc {

class XBT_PRIVATE UdporChecker : public Exploration {
public:
  explicit UdporChecker(const std::vector<char*>& args);
  void run() override;
  RecordTrace get_record_trace() override;
  std::vector<std::string> get_textual_trace() override;
};

} // namespace simgrid::mc

#endif
