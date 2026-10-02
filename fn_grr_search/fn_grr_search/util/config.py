# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_grr_search"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_grr_search]
grr_server=127.0.0.1
grr_user=user
grr_pwd=password
#Can be True/False
verify_cert=False
"""
    return config_data