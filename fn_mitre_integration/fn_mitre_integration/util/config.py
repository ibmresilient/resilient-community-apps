# -*- coding: utf-8 -*-
"""Generate a default configuration-file section for fn_mitre_integration"""

def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    return """[fn_mitre_integration]
verify=True
# Settings for access to Mitre via a proxy
#http_proxy=http://proxy:80
#https_proxy=https://proxy:80
"""
