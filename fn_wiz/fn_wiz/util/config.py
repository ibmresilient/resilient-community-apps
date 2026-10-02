# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.1.0.695

"""Generate a default configuration-file section for fn_wiz"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_wiz when called by `resilient-circuits config [-c|-u]`
    """
    config_data = None

    config_data = u"""[fn_wiz]
# Wiz GraphQL API URL
# Specify <region>, which may be us1, us2, eu1, or eu2, for example
api_url=https://api.<region>.app.wiz.io/graphql

# Wiz app URL to access Issue data
endpoint_url=https://app.wiz.io

# Wiz URL to retrieve authentication token
# For gov tenants, set to the token URL to https://auth.gov.wiz.io/oauth/token
token_url=https://auth.app.wiz.io/oauth/token

# Wiz provided client ID and secret
client_id=xxx
client_secret=xxx

# Number of seconds between poller cycles - A value of 0 disables the poller
# Default to once a day
polling_interval=86400

# Number of minutes to lookback when querying for issues the first time the poller runs
# Default to 2 hours
polling_lookback=120

# OPTIONAL: use the 'verify' config to set a value for SSL verification
# if 'False', no SSL will be used. if 'True' or unset, the default SSL root cert
# will be used. if 'verify' is a path, the value of the path will override the
# root cert bundle and the file found at the path will be used for server-side SSL.
# verify=

# OPTIONAL: override value for templates used for creating/updating/closing SOAR cases.
# See documentation section "Templates for SOAR Cases" for more details
#soar_create_case_template=
#soar_update_case_template=
#soar_close_case_template=

"""
    return config_data
