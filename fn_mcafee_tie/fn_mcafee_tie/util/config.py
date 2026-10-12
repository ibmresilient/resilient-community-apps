# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_mcafee_tie_functions"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = '''[fn_mcafee_tie]
# The absolute file path of the DxlClient configuration file created by the 
# OpenDXL Python Client's command line provisionconfig operation.  
# This parameter is mandatory.
# On an integration server it will typically be defined like this:
# dxlclient_config=/home/integration/.resilient/fn_mcafee_tie/dxlclient.config
# In App Host environment it will typically be defined like this:
# dxlclient_config = /etc/rescircuits/fn_mcafee_tie/dxlclient.config
#
dxlclient_config=
'''
    return config_data
