# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

"""Generate a default configuration-file section for fn_grpc_interface"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """

    config_data = u"""[fn_grpc_interface]
interface_dir=<<path to the parent directory of your Protocol Buffer (pb2) files>>
# The channel is OPTIONAL if filled in by function parameters the function value takes precendence over the config value
#grpc_channel=<<host>>:<<port>> 
# 'package_name' is a CSV list of length 3, where each possible value is described in the documentation
#<<package_name>>=<<communication_type>>, <<secure connection type>>, <<certificate_path or google API token>>

"""
    return config_data