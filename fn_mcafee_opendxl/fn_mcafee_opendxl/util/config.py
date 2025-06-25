# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_mcafee_opendxl"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_mcafee_opendxl]
# The absolute file path of the DxlClient configuration file created by the 
# OpenDXL Python Client's command line provisionconfig operation.  
# This parameter is mandatory.
# On an integration server it will typically be defined like this:
# dxlclient_config=/home/integration/.resilient/fn_mcafee_opendxl/dxlclient.config
# In App Host environment it will typically be defined like this:
# dxlclient_config = /etc/rescircuits/fn_mcafee_opendxl/dxlclient.config
dxlclient_config=

# Set topic_listener to False to prevent it from listening on any topics
topic_listener_on=False

## custom_template_dir is optional and used to specify the directory where new 
## templates can be found/to override any default templates
custom_template_dir=
"""
    return config_data
