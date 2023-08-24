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
# OPTIONAL: Case Record Type Names used to by the poller to search for cases Salesforce.
# If no record type names are provided, all case record types are searched when the poller runs.
# This parameter is a comma separated list of record type names that must exist 
# in the Salesforce platform.
# For example: 
# polling_record_type_names="Security Incident","Incident"
polling_record_type_names=
# OPTIONAL: Use the case_fields_to_query parameter to list the Salesforce Case field names
# to retrieve when querying for cases on each poll interval.  The default parameter lists the
# fields that are used in the jinja templates that are shipped with the integration.
# If you use custom fields in Salesforce that you want to import into SOAR, add them to 
# this comma separated list. 
# If this parameter is not defined, the app will use SOQL SELECT FIELDS(ALL) clause to retrieve 
# all case fields in a the case query each polling interval.  The limitation here is that 
# Salesforce only returned LIMIT=200 cases each poll when getting cases with ALL fields.
# case_fields_to_query=Id,CaseNumber,Type,CreatedDate,Description,Subject,Priority,OwnerId,AccountId,ContactId,Origin,ContactPhone,ContactEmail,ContactFax,SuppliedName,SuppliedEmail,SuppliedPhone,SuppliedCompany
# 
# OPTIONAL: Specify a timeout value value for accessing the Salesforce REST API
# timeout=60
#
# OPTIONAL: Override value for templates used for creating/updating/closing SOAR cases
# soar_create_case_template=
# soar_close_case_template=
# soar_update_case_template=
#
# OPTIONAL: use the 'verify' config to set a value for SSL verification
# if 'False', no SSL will be used. if 'True' or unset, the default SSL root cert
# will be used. if 'verify' is a path, the value of the path will override the
# root cert bundle and the file found at the path will be used for server-side SSL.
# verify = True
# # Specify paths to files if client certs are needed to authenticate
# client_auth_cert = <path_to_cert.pem>
# client_auth_key = <path_to_cert_private_key.pem>
# """
    return config_data
