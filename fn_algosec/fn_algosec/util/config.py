# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.2.1096

"""Generate a default configuration-file section for fn_algosec"""

def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_algosec when called by `resilient-circuits config [-c|-u]`
    """

    return """[fn_algosec]
server_ip=local.algosec.com
username=admin
password=algosec
verify=true
https_proxy="""
