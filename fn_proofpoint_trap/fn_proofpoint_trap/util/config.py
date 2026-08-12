# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Generate a default configuration-file section for fn_proofpoint_trap"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_proofpoint_trap]
# Base URL of Proofpoint TRAP API
base_url=
# API Key for Proofpoint TRAP
api_key=
# Interval to poll TRAP in minutes
polling_interval=2
# Initial Import Look-back Interval in minutes (default: 1 hour)
startup_interval=60
# State of Incidents to Query
state=open
# Comma separated list of host categories to check for artifacts 
# to import into Resilient. The default is forensics.
# other options include attacker, cnc and url.
# e.g. host_categories=attacker,cnc,forensics,url
host_categories=forensics
# Optional setting to use a ca certificate to access Proofpoint TRAP.
# Specify the path to the certificate e.g. cafile=<path_name>/cert.cer.
#cafile=
# Optional settings for access to Proofpoint TRAP via a proxy.
#http_proxy=http://proxyhost:8080
#https_proxy=https://proxyhost:8080
"""
    return config_data
