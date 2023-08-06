/*
 *   Copyright 2016-2022. Couchbase, Inc.
 *   All Rights Reserved.
 *
 *   Licensed under the Apache License, Version 2.0 (the "License");
 *   you may not use this file except in compliance with the License.
 *   You may obtain a copy of the License at
 *
 *       http://www.apache.org/licenses/LICENSE-2.0
 *
 *   Unless required by applicable law or agreed to in writing, software
 *   distributed under the License is distributed on an "AS IS" BASIS,
 *   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *   See the License for the specific language governing permissions and
 *   limitations under the License.
 */

#pragma once

#include "Python.h" // NOLINT
#include <core/utils/binary.hxx>
#include <couchbase/persist_to.hxx>
#include <couchbase/replicate_to.hxx>
#include <couchbase/durability_level.hxx>
#include <stdexcept>
#include <string>
#include <chrono>

constexpr std::chrono::seconds FIFTY_YEARS{ 50 * 365 * 24 * 60 * 60 };

couchbase::core::utils::binary
PyObject_to_binary(PyObject*);
PyObject*
binary_to_PyObject(couchbase::core::utils::binary value);
std::size_t py_ssize_t_to_size_t(Py_ssize_t);
Py_ssize_t size_t_to_py_ssize_t(std::size_t);

couchbase::persist_to
PyObject_to_persist_to(PyObject* pyObj_persist_to);
couchbase::replicate_to
PyObject_to_replicate_to(PyObject* pyObj_replicate_to);
std::pair<couchbase::persist_to, couchbase::replicate_to>
PyObject_to_durability(PyObject*);
couchbase::durability_level
PyObject_to_durability_level(PyObject*);
