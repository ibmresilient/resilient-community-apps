# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_isitPhishing"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_isitphishing]
# Specify the endpoint for the Vade Secure IsItPhishing API requests.
# use https://iip.eu.vadesecure.com/api/v2 or https://iip.us.vadesecure.com/api/v2 based on your region
isitphishing_api_url=https://iip.eu.vadesecure.com/api/v2
authentication_url=https://api.vadesecure.com/oauth2/v2/token
#
# You need a license key to use the Vade Secure IsItPhishing API. 
# This key will be provided to you by Vade Secure, and has the following format:
# <NAME>:<LICENSE>
isitphishing_id=
isitphishing_secret=
#
# Uncomment to specify proxy settings
#https_proxy=https://your.proxy.com
#http_proxy=http://your.proxy.com
"""
    return config_data
