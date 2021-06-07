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
#<<package_name>>=<<communication_type>>, <<secure connection type>>, <<certificate_path or google API token>>

# 'package_name' is a CSV list of length 3, where each possible value is described in the documentation

# Note: to setup, in your interface_dir, create a sub-directory that has
# the same name as your package, and copy the Protocol Buffer pb2 files
# into that directory.
#
# If the package_name was 'helloworld', your app.config would look like:
# [fn_grpc_interface]
# interface_dir=/home/admin/integrations/grpc_interface_files
# helloworld=unary, None, None"""
    return config_data