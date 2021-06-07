# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_hibp"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_hibp]
## Proxy settings if needed
#hibp_proxy_http=
#hibp_proxy_https=

#As of recent July 2019 changes, HIBP released v3 of the API (deprecating v2) and now requires a for-fee API Key (see https://haveibeenpwned.com/API/Key)
hibp_api_key=< Have I Been Pwned API Key>
"""
    return config_data
