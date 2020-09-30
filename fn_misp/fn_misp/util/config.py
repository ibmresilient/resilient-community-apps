# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_misp"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_misp]
misp_url=http://localhost
misp_key=<your key>
# used to bypass cerification validation for self signed instances of MISP
verify_cert=true
# Depending on your MISP version and configuration - your tag can be different, the default is below.
mitre_tag=misp-galaxy:mitre-attack-pattern
# Optional: access MISP via an http/https proxy
#http_proxy=<http_proxy_server>
#https_proxy=<https_proxy_server>
"""
    return config_data