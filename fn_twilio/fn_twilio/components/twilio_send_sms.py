# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

"""Function implementation"""

import logging
import re
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

CONFIG_DATA_SECTION = 'fn_twilio_send_sms' 

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function(s)"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts)

        # Get app.config parameters.
        self.options = opts.get(CONFIG_DATA_SECTION, {})

        if self.options == {}:
            raise ValueError("{} section is not set in the config file".format(CONFIG_DATA_SECTION))

        self.account_sid = self.options.get("twilio_account_sid")
        self.auth_token = self.options.get("twilio_auth_token")
        self.src_address = self.options.get("twilio_src_address")

        # Check that config parameters are defined.
        if not self.account_sid:
            raise ValueError("twilio_account_sid is not set. You must set this value to run {}".format(CONFIG_DATA_SECTION))
        if not self.auth_token:
            raise ValueError("twilio_auth_token is not set. You must set this value to run {}".format(CONFIG_DATA_SECTION))
        if not self.src_address:
            raise ValueError("twilio_src_address is not set. You must set this value to run {}".format(CONFIG_DATA_SECTION)) 


    @function("twilio_send_sms")
    def _twilio_send_sms_function(self, event, *args, **kwargs):
        """Function: Send an SMS message via a Twilio account"""
        try:
            # Get the function parameters:
            twilio_sms_destination = kwargs.get("twilio_sms_destination")  # text
            twilio_sms_message = kwargs.get("twilio_sms_message")  # text

            log = logging.getLogger(__name__)
            log.info("twilio_sms_destination: %s", twilio_sms_destination)
            log.info("twilio_sms_message: %s", twilio_sms_message)

            try:
                phone_numbers_unstripped = [s.strip() for s in
                                            twilio_sms_destination.split(',')]  # Split commas ignoring any whitespace
                phone_numbers = []
                for phone_number_unstripped in phone_numbers_unstripped:
                    phone_numbers.append('+' + re.sub("[^0-9]", "", phone_number_unstripped))  # Strip all non-numeric chars and prefix with +

            except Exception:
                raise FunctionError("Invalid phone numbers provided, failed to decode.")

            # Create Twilio Client
            client = Client(self.account_sid, self.auth_token)

            # Status
            status = []

            # Send SMS to each number
            for phone_number in phone_numbers:
                try:
                    message = client.messages \
                    .create(
                        body=twilio_sms_message,
                        from_= self.src_address,
                        to=phone_number
                    )

                    if message.error_code is None:
                        entry = { 
                            "phone_number": phone_number,
                            "success": True
                        }
                        status.append(entry)
                        log.info("Sent to %s", phone_number)
                    else:
                        entry = { 
                            "phone_number": phone_number,
                            "error_message": message.error_message,
                            "success": False
                        }
                        status.append(entry)
                        log.error("Failed to send to %s [%s]", phone_number, message.error_message)
                except TwilioRestException as e:
                        entry = { 
                            "phone_number": phone_number,
                            "error_message": e.msg,
                            "success": False
                        }
                        status.append(entry)
                        log.error("Failed to send to %s [%s]", phone_number, e.msg)

            # Produce a FunctionResult with the results
            results = {
                "twilio_sms_message": twilio_sms_message,
                "twilio_status": status
            }

            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
