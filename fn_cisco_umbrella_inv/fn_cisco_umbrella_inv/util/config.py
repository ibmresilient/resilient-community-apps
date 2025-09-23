# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_cisco_umbrella_inv"""
from __future__ import print_function

def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    return """[fn_cisco_umbrella_inv]
base_url=https://api.umbrella.com/investigate/v2/
# Either an inv_api_key and inv_api_secret have to be given or an api_token has to be given.
# The Investigate API key and secret that will be used to create access tokens
inv_api_key=<cisco_umbrella_investigate_api_key>
inv_api_secret=<cisco_umbrella_investigate_api_secret>
# The api_token will be supplied by Cisco will be in uuid format.
# This will soon be deprecated.
api_token=<api token>
results_limit=200
verify=True
# uncomment to specify proxy settings
#https_proxy=https://your.proxy.com
#http_proxy=http://your.proxy.com
"""
