# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_isitPhishing"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_isitPhishing]
# Specify the endpoint for the Vade Secure isitPhishing API requests.
#
isitphishing_api_url=https://ws.isitphishing.org/api/v2
#
# You need a license key to use the Vade Secure IsItPhishing API. 
# This key will be provided to you by Vade Secure, and has the following format:
# <NAME>:<LICENSE>
isitphishing_name=xxxx
isitphishing_license=xxxx

"""
    return config_data