# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_rest_api"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_rest_api when called by `resilient-circuits config [-c|-u]`
    """


    config_data = u"""[fn_rest_api]

# uncomment to add proxies
# https_proxy=https://<your_proxy>:<port>
# http_proxy=http://<your_proxy>:<port>
"""

    return config_data
