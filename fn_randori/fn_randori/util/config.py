# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_randori"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_randori when called by `resilient-circuits config [-c|-u]`
    """
    config_data = None

    config_data = u"""[fn_randori]
# Randori API token
api_token=xxx
# Randori REST API endpoint
endpoint_url=https://app.randori.io
# Randori tenant name
tenant_name=xxx
# Randori REST API version
api_version=v1
# Number of seconds between poller cycles. A value of 0 disables the poller
polling_interval=60
# Number of minutes to lookback for queries the first time the poller runs.
polling_lookback=120
verify= false | /path/to/cafile.crt
"""
    return config_data
