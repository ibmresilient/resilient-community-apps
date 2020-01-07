# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_phish_tank"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_phish_tank]
# PhishTank API Access URL
phish_tank_api_url=http://checkurl.phishtank.com/checkurl/
# PhishTank API Key.
phish_tank_api_key=
# Proxy Server by Default it will be None.
proxy=
"""
    return config_data
