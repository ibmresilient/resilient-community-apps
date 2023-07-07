# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.0.4423

"""Generate a default configuration-file section for fn_salesforce"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_salesforce when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_salesforce]
# Current My Domain Name found in the Salesforce My Domain Setup page
# For example: company-name
my_domain_name=xxx
# Current My Domain URL found in the Salesforce My Domain Setup page
# For example: company-name.develop.my.salesforce.com
my_domain_url=xxx
# Salesforce REST API version
api_version=v58.0
# Salesforce consumer key
consumer_key=xxx
# Salesforce consumer secret
consumer_secret=xxx
# Number of seconds between poller cycles. A value of 0 disables the poller
polling_interval=60
# Number of minutes to lookback for queries the first time the poller runs
polling_lookback=120
# 
verify = True
# Optional - polling filters that can be applied when querying Salesforce for new cases or cases to be updated.
# polling_filters=
# 
# # Specify paths to files if client certs are needed to authenticate
# client_auth_cert = <path_to_cert.pem>
# client_auth_key = <path_to_cert_private_key.pem>
# """
    return config_data
