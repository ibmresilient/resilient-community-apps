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
# OPTIONAL: use the 'verify' config to set a value for SSL verification
# if 'False', no SSL will be used. if 'True' or unset, the default SSL root cert
# will be used. if 'verify' is a path, the value of the path will override the
# root cert bundle and the file found at the path will be used for server-side SSL.
verify = True
# OPTIONAL: polling filters that can be applied when querying Salesforce for 
# new cases to cases to be updated. The app uses SOQL (Salesforce Object Query Language) 
# to form a SELECT statement to query cases based on the last poll time.  
# Additional filters can be added to the query by translating polling_filters tuples into 
# AND clauses added to the WHERE clause of the SELECT statement.
# 
# Each filter is a tuple in the following format: ("field","operator","value")
# Where:
#   "field" in the Salesforce case field to be queried
#   "operator" is a comparison operator as defined in Salesforce (for example: "<", "<=", "=", "!=") 
#   "value" is the value to be compared against in the query
# If more than one filter is needed separate each tuple with a comma.
# Note that strings that needs to be single quoted in an SOQL query, need to be escaped.
# Here are some examples:
# polling_filters=("Priority","=","\'High\'"),("Status","IN",["\'New\'","\'Working\'","\'In Progress\'"])
# ("IsClosed","=","false"),("CreatedDate",">","YESTERDAY")
polling_filters=
# 
# # Specify paths to files if client certs are needed to authenticate
# client_auth_cert = <path_to_cert.pem>
# client_auth_key = <path_to_cert_private_key.pem>
# """
    return config_data
