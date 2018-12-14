# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_isitPhishing"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_isitPhishing]
# You need a license key to use the Vade Secure IsItPhishing API. 
# This key will be provided to you by Vade Secure, and has the following format:
# <NAME>:<LICENSE>
#isitPhishing_name=xxxx
#isitPhishing_license=xxx

"""
    return config_data