# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.0.4423

"""Generate a default configuration-file section for fn_salesforce"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_salesforce when called by `resilient-circuits config [-c|-u]`
    """
    config_data = None

#     config_data = u"""[fn_salesforce]
# api_key=xxx
# api_secret=xxx
# endpoint_url=https://xxx/
# # Number of seconds between poller cycles. A value of 0 disables the poller
# polling_interval=60
# # Number of minutes to lookback for queries the first time the poller runs.
# polling_lookback=120
#
# setting=xxx
# 
# # Specify paths to files if client certs are needed to authenticate
# client_auth_cert = <path_to_cert.pem>
# client_auth_key = <path_to_cert_private_key.pem>
# """
    return config_data
