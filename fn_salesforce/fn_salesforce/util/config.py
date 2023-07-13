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
lightning_link = True
# 
verify = True
# Optional: polling filters that can be applied when querying Salesforce for new cases to cases to be updated.
# Each filter is a tuple in the following format: ("field","operator","value")
# Where:
#   "field" in the Salesforce case field to be queried
#   "operator" is a string operator as defined in Salesforce (for example: "less", "less_or_equal", "equal") 
#   "value" is the value to be compared against in the query
# If more than one filter is needed separate each tuple with a comma
#polling_filters=("Priority","=","\'High\'"),("Status","=",),("IsClosed","=","false")
#
# 
# # Specify paths to files if client certs are needed to authenticate
# client_auth_cert = <path_to_cert.pem>
# client_auth_key = <path_to_cert_private_key.pem>
# """
    return config_data
