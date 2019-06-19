# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.

"""Generate a default configuration-file section for fn_url_void"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_url_void]
api_key=<urlvoid_api_key>

# Identifier located on the same page the api key is found (https://api.urlvoid.com/dashboard/). Defaults to 'api1000'
#identifier=
"""
    return config_data
