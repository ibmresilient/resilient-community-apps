# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_rest_api"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_rest_api when called by `resilient-circuits config [-c|-u]`
    """
    config_data = None

#    config_data = u"""[fn_rest_api]
#
#setting=xxx
# 
# # Specify paths to files if client certs are needed to authenticate
# client_auth_cert = <path_to_cert.pem>
# client_auth_key = <path_to_cert_private_key.pem>
# """
    return config_data
