# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_trusteer_ppd"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_trusteer_ppd when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_trusteer_ppd]
# Trusteer API token
api_token=xxx
# Trusteer REST API endpoint
endpoint_url=https://trusteer.com
# Trusteer REST API version
api_version=v1
verify=true
# 
# # Specify paths to files if client certs are needed to authenticate
# client_auth_cert = <path_to_cert.pem>
# client_auth_key = <path_to_cert_private_key.pem>
 """
    return config_data
