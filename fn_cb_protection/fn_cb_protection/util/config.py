# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_cb_protection"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_cb_protection]
    
# Name or IP address of your CbProtect server
server=10.200.1.1

# Access token issued by the CbProtect administrator
token=XXXXX-XXXX-XXXXX-XXXX

# If your CbProtect server has a self-signed TLS certificate, you cannot verify it:
# verify=false
"""
    return config_data