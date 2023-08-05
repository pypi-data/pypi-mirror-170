# Copyright 2020 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""For conversion of raw files to tool data.

Usage:
    data = xspace_to_tool_data(xplane, tool, params)
    data = tool_proto_to_tool_data(tool_proto, tool, params)
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging

from tensorflow.python.profiler.internal import _pywrap_profiler  # pylint: disable=g-direct-tensorflow-import
from tensorboard_plugin_profile.convert import input_pipeline_proto_to_gviz
from tensorboard_plugin_profile.convert import kernel_stats_proto_to_gviz
from tensorboard_plugin_profile.convert import overview_page_proto_to_gviz
from tensorboard_plugin_profile.convert import tf_data_stats_proto_to_gviz
from tensorboard_plugin_profile.convert import tf_stats_proto_to_gviz
from tensorboard_plugin_profile.convert import trace_events_json
from tensorboard_plugin_profile.protobuf import trace_events_pb2

logger = logging.getLogger('tensorboard')


def process_raw_trace(raw_trace):
  """Processes raw trace data and returns the UI data."""
  trace = trace_events_pb2.Trace()
  trace.ParseFromString(raw_trace)
  return ''.join(trace_events_json.TraceEventsJsonStream(trace))


def xspace_to_tools_data_from_byte_string(xspace_byte_list, filenames, tool,
                                          params):
  """Helper function for getting an XSpace tool from a bytes string.

  Args:
    xspace_byte_list: A list of byte strings read from a XSpace proto file.
    filenames: Names of the read files.
    tool: A string of tool name.
    params: user input parameters.

  Returns:
    Returns a string of tool data.
  """

  def xspace_wrapper_func(xspace_arg, tool_arg):
    return _pywrap_profiler.xspace_to_tools_data_from_byte_string(
        xspace_arg, filenames, tool_arg)

  return xspace_to_tool_data(xspace_byte_list, tool, params,
                             xspace_wrapper_func)


def xspace_to_tool_names(xspace_paths):
  """Converts XSpace to all the available tool names.

  Args:
    xspace_paths: A list of XSpace paths.

  Returns:
    Returns a list of tool names.
  """
  raw_data, success = _pywrap_profiler.xspace_to_tools_data(
      xspace_paths, 'tool_names')
  if success:
    return [tool + '^' for tool in raw_data.decode().split(',')]
  return []


def xspace_to_tool_data(
    xspace_paths,
    tool,
    params,
    xspace_wrapper_func=_pywrap_profiler.xspace_to_tools_data):
  """Converts XSpace to tool data string.

  Args:
    xspace_paths: A list of XSpace paths.
    tool: A string of tool name.
    params: user input parameters.
    xspace_wrapper_func: A callable that takes a list of strings and a tool and
      returns the raw data.

  Returns:
    Returns a string of tool data and the content type for the response.
  """
  assert tool[-1] == '^'
  tool = tool[:-1]  # xplane tool name ends with '^'
  data = None
  content_type = 'application/json'
  # tqx: gViz output format
  tqx = params.get('tqx', '')
  if tool == 'trace_viewer':
    # Trace viewer handles one host at a time.
    assert len(xspace_paths) == 1
    raw_data, success = xspace_wrapper_func(xspace_paths, tool)
    if success:
      data = process_raw_trace(raw_data)
  elif tool == 'overview_page':
    raw_data, success = xspace_wrapper_func(xspace_paths, tool)
    if success:
      data = overview_page_proto_to_gviz.to_json(raw_data)
  elif tool == 'input_pipeline_analyzer':
    raw_data, success = xspace_wrapper_func(xspace_paths, tool)
    if success:
      data = input_pipeline_proto_to_gviz.to_json(raw_data)
  elif tool == 'tensorflow_stats':
    raw_data, success = xspace_wrapper_func(xspace_paths, tool)
    if success:
      if tqx == 'out:csv':
        data = tf_stats_proto_to_gviz.to_csv(raw_data)
      else:
        data = tf_stats_proto_to_gviz.to_json(raw_data)
  elif tool == 'kernel_stats':
    raw_data, success = xspace_wrapper_func(xspace_paths, tool)
    if success:
      if tqx == 'out:csv;':
        data = kernel_stats_proto_to_gviz.to_csv(raw_data)
      else:
        data = kernel_stats_proto_to_gviz.to_json(raw_data)
  elif tool == 'memory_profile':
    # Memory profile handles one host at a time.
    assert len(xspace_paths) == 1
    raw_data, success = xspace_wrapper_func(xspace_paths, tool)
    if success:
      data = raw_data
  elif tool == 'pod_viewer':
    raw_data, success = xspace_wrapper_func(xspace_paths, tool)
    if success:
      data = raw_data
  elif tool == 'tf_data_bottleneck_analysis':
    raw_data, success = xspace_wrapper_func(xspace_paths, tool)
    if success:
      data = tf_data_stats_proto_to_gviz.to_json(raw_data)
  elif tool == 'op_profile':
    raw_data, success = xspace_wrapper_func(xspace_paths, tool)
    if success:
      data = raw_data
  elif tool == 'graph_viewer':
    options = params.get('graph_viewer_options', {})
    raw_data, success = xspace_wrapper_func(xspace_paths, tool, options)
    if success:
      data = raw_data
      content_type = 'text/html'
  elif tool == 'memory_viewer':
    options = {'module_name': params.get('host')}
    raw_data, success = xspace_wrapper_func(xspace_paths, tool, options)
    if success:
      data = raw_data
  else:
    logger.warning('%s is not a known xplane tool', tool)
  return data, content_type


def tool_proto_to_tool_data(tool_proto, tool, params):
  """Converts the serialized tool proto to tool data string.

  Args:
    tool_proto: A serialized tool proto string.
    tool: A string of tool name.
    params: user input parameters.

  Returns:
    Returns a string of tool data.
  """
  data = ''
  # tqx: gViz output format
  tqx = params.get('tqx', '')
  if tool == 'trace_viewer':
    data = process_raw_trace(tool_proto)
  elif tool == 'tensorflow_stats':
    if tqx == 'out:csv;':
      data = tf_stats_proto_to_gviz.to_csv(tool_proto)
    else:
      data = tf_stats_proto_to_gviz.to_json(tool_proto)
  elif tool == 'overview_page@':
    data = overview_page_proto_to_gviz.to_json(tool_proto)
  elif tool == 'input_pipeline_analyzer@':
    data = input_pipeline_proto_to_gviz.to_json(tool_proto)
  elif tool == 'kernel_stats':
    if tqx == 'out:csv;':
      data = kernel_stats_proto_to_gviz.to_csv(tool_proto)
    else:
      data = kernel_stats_proto_to_gviz.to_json(tool_proto)
  else:
    logger.warning('%s is not a known tool', tool)
  return data
