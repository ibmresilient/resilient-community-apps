# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_rest_api"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_rest_api when called by `resilient-circuits config [-c|-u]`
    """
    return u"""[fn_rest_api]
#
# Uncomment to add proxies
# https_proxy = https://<your_proxy>:<port>
# http_proxy = http://<your_proxy>:<port>
#
# Values can be assigned here in app.config and reference them in application
# auth_header = sampleAPIToken123
#
# Alternatively, sensitive values can be stored as a SECRET in the Resilient platform
# and assigned to a key as shown below.
# auth_header = $SECRET_EXAMPLE
#
# This auth_header can later be accessed in a playbook or a workflow as {{auth_header}}
#
# configure a URL for testing based on company requirements using the GET method
#selftest_url= https://postman-echo.com/get
"""
