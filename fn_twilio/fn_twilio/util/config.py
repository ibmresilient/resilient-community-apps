# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_grr"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
      when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_twilio_send_sms]
twilio_account_sid=
twilio_auth_token=
twilio_src_address=
"""
    return config_data