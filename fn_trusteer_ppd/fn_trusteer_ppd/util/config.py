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
# Trusteer REST API version
api_version=v1
# Trusteer customer name used to form the URLs for REST API calls and links back to Trusteer
customer_name = 
# 
# Mandatory: specify paths to cert and key files used to for REST API authentication.
client_auth_cert = <path_to_cert.pem>
client_auth_key = <path_to_cert_private_key.pem>
 """
    return config_data
