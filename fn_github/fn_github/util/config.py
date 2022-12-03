# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_github"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_github when called by `resilient-circuits config [-c|-u]`
    """

    config_data = u"""[fn_github]
# specify base_url for enterprise versions of GitHub. Otherwise leave blank for public github
base_url=<https://base-url>
api_token=
# Specify paths to files if client certs are needed to authenticate
client_auth_cert = <path_to_cert.pem>
client_auth_key = <path_to_cert_private_key.pem>
# Enable/Disable ssl-certificate verification
verify=True
"""
    return config_data
