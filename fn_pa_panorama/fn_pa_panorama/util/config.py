# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_pa_panorama"""

from __future__ import print_function

def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    return """
# V1.2.0+ have the option to have multiple servers configured.
# By default two examples of servers are given, example one is labeled `panorama_label1` and example two is labeled `panorama_label2`.
# The label for a server is placed after `[fn_pa_panorama:` and then followed by `]`.
# To add additional servers copy the below example server configuration from `[fn_pa_panorama:panorama_label1]` to `verify_cert=false|/path/to/cert`.
# Then paste it at the bottom of the app.config.
# Change the server label, `panorama_label1`, to a label helpful to define that server.
# Then change the setting to those of the server you wish to add.

[fn_pa_panorama:panorama_label1]
# URL/IP of Panorama
panorama_host=<https://0.0.0.0>
# Versions of panorama can be used by changing the api_version to use a different API version
api_version=v9.1
api_key=<Panorama_api_key>
cert=[True|False]
# Selftest options
sf_location=vsys
sf_vsys=vsys1
# optional settings to access Panorama via proxies
#http_proxy=http://proxy.domain:3128
#https_proxy=https://proxy.domain:3128

[fn_pa_panorama:panorama_label2]
# URL/IP of Panorama
panorama_host=<https://0.0.0.0>
# Versions of panorama can be used by changing the api_version to use a different API version
api_version=v9.1
api_key=<Panorama_api_key>
cert=[True|False]
# Selftest options
sf_location=vsys
sf_vsys=vsys1
# optional settings to access Panorama via proxies
#http_proxy=http://proxy.domain:3128
#https_proxy=https://proxy.domain:3128
"""
