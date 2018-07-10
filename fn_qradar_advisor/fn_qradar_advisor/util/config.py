# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_qradar_advisor"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_qradar_advisor]
qradar_host=myhost
qradar_advisor_token=
qradar_advisor_app_id=
verify_cert=
"""
    return config_data
