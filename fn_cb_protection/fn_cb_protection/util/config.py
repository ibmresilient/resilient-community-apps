# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

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
# verify_cert=false

# Interval (seconds) for automatic escalation of approval requests, set 0 to disable
# Suggest 300 as a starting point, which will check CbProtect every 5 minutes
escalation_interval=0

# Optional: query for which requests to escalate; default is to escalate all open approval requests
# escalation_query=resolution:0

# Optional: path to a custom template file for the escalated incident
# template_file=/usr/integration/bit9_escalation.jinja

# Optional: set this to only escalate a single request ID, e.g. when testing a custom template 
# test_single_request=999

"""
    return config_data