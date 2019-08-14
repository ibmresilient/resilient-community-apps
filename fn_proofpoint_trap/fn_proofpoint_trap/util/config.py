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
# Interval to poll TRAP in Minutes
polling_interval=2
# Initial Import Look-back Interval (default: 2 weeks)
startup_interval=20160
# State of Incidents to Query
state=open
"""
    return config_data
