# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_cisco_umbrella_inv"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_cisco_amp4ep]
base_url=https://api.amp.cisco.com/
api_version=v1
# The client id will be generated on the Cisco AMP for endpoints dashboard.
client_id=<client id>
# The api_token will be generated on the Cisco AMP for endpoints dashboard and will be will be in uuid format.
api_token=<api token>
# Settings for access to cisco website via a proxy
#http_proxy=http':'http://proxy:80
#https_proxy=https':'http://proxy:80
# Query results global limit override for the integration global default which is set to 1000.
#query_limit=1000
# Max number of retry attempts on Rate Limit exception
max_retries=3
"""
    return config_data