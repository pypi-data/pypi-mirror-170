/* Copyright (c) 2016-2022. The SimGrid Team. All rights reserved.          */

/* This program is free software; you can redistribute it and/or modify it
 * under the terms of the license (GNU LGPL) which comes with this package. */

#include "src/mc/explo/UdporChecker.hpp"
#include <xbt/log.h>

XBT_LOG_NEW_DEFAULT_SUBCATEGORY(mc_udpor, mc, "Logging specific to MC safety verification ");

namespace simgrid::mc {

UdporChecker::UdporChecker(const std::vector<char*>& args) : Exploration(args) {}

void UdporChecker::run() {}

RecordTrace UdporChecker::get_record_trace()
{
  RecordTrace res;
  return res;
}

std::vector<std::string> UdporChecker::get_textual_trace()
{
  std::vector<std::string> trace;
  return trace;
}

Exploration* create_udpor_checker(const std::vector<char*>& args)
{
  return new UdporChecker(args);
}

} // namespace simgrid::mc
