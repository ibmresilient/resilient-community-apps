# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.0.2.575

"""Generate a default configuration-file section for fn_axonius"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_axonius when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_axonius]
# Axonius endpoint URL 
endpoint_url = <Axonius server URL>
# Axonius API key
api_key = <Axonius api-key>
# Axonius API secret
api_secret = <Axonius api-secret>
# Axonius REST API version
api_version = v2
# 
# # Specify paths to files if client certs are needed to authenticate
# client_auth_cert = <path_to_cert.pem>
# client_auth_key = <path_to_cert_private_key.pem>
# """
    return config_data
