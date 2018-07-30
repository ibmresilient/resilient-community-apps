# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_pagerduty"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[pagerduty]
api_token=<api_token>
from_email=<from_email_address>
# bypass https certificate validation (only set to False for testing purposes)
verifyFlag=False
"""

    return config_data