/*
 *  This file is part of resolve.
 *
 *  resolve is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  resolve is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with resolve; if not, write to the Free Software
 *  Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
 */

/* Copyright (C) 2022 Max-Planck-Society, Philipp Arras
   Authors: Philipp Arras */

#ifndef DUCC0_SYCL_UTILS_H
#define DUCC0_SYCL_UTILS_H

#if defined(DUCC0_USE_SYCL)
#include "CL/sycl.hpp"

using namespace std;
using namespace cl;


bool sycl_active()
  {
#if defined(DUCC0_USE_SYCL)
  return true;
#else
  return false;
#endif
  }

#endif
