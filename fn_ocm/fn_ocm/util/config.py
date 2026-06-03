# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# Generated with resilient-sdk v51.0.5.0.1475

"""Generate a default configuration-file section for fn_ocm"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_ocm when called by `resilient-circuits config [-c|-u]`
    """
    return """[fn_ocm]
# On Call Manager REST API URL
ocm_url = https://oncallmanager.ibm.com/api/
# The API key name
ocm_api_key_name =
# The API key password
ocm_api_key_pass =

# OPTIONAL: use the 'verify' config to set a value for SSL verification
# if 'False', no SSL will be used. if 'True' or unset, the default SSL root cert
# will be used. if 'verify' is a path, the value of the path will override the
# root cert bundle and the file found at the path will be used for server-side SSL.
# verify=

# OPTIONAL: Specify paths to files if client certs are needed to authenticate
# client_auth_cert = <path_to_cert.pem>
# client_auth_key = <path_to_cert_private_key.pem>
"""
