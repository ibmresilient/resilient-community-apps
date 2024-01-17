# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use, line-too-long
"""Function implementation
   test with: resilient-circuits selftest -l fn_twilio
"""

import logging
from twilio.rest import Client

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
LOG.addHandler(logging.StreamHandler())


def get_config_option(option_name, opts, optional=False):
    """Given option_name, checks if it is in appconfig. Raises ValueError if a mandatory option is missing"""
    option = opts.get(option_name)

    if not option and optional is False:
        err = "'{0}' is mandatory and is not set in the app.config file. You must set this value to run this function".format(option_name)
        raise ValueError(err)
    else:
        return option


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get("fn_twilio_send_sms", {})

    account_sid = get_config_option("twilio_account_sid", options)
    auth_token = get_config_option("twilio_auth_token", options)
    src_address = get_config_option("twilio_src_address", options)

    try:
        client = Client(account_sid, auth_token)

        incoming_phone_numbers = client.incoming_phone_numbers \
                               .list(phone_number=src_address)

        if(incoming_phone_numbers):
            return {"state": "success"}

        return {
            "state": "failure",
            "reason": "twilio_src_address {0} is not valid for this account".format(src_address)
        }

    except Exception as exp:
        LOG.error(exp)
        return {
            "state": "failure",
            "reason": exp
        }
