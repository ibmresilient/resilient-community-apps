# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

"""Generate a default configuration-file section for fn_twilio"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
      when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_twilio_send_sms]
twilio_account_sid=
twilio_auth_token=
# This is the number that will originate the SMS and must be an active SMS phone number on your Twilio Account 
# The format should be as per the Twilio console properties for your number, e.g. +1234567890
twilio_src_address=
"""
    return config_data
