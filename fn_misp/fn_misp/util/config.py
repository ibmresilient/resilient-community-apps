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
"""
    return config_data