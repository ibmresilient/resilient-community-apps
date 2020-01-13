# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_twilio.lib.common import clean_phone_number
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

CONFIG_DATA_SECTION = 'fn_twilio_send_sms'

class FunctionPayload(object):
    """Class that contains the payload sent back to UI and
    available in the post-processing script"""
    def __init__(self, inputs):
        self.success = True
        self.inputs = inputs
        self.twilio_status = None

    def as_dict(self):
        """Return this class as a Dictionary"""
        return self.__dict__


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function(s)"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    @function("twilio_send_sms")
    def _twilio_send_sms_function(self, event, *args, **kwargs):
        """Function: Send an SMS message via a Twilio account"""
        log = logging.getLogger(__name__)
            
        def get_config_option(option_name, optional=False):
            """Given option_name, checks if it is in appconfig. Raises ValueError if a mandatory option is missing"""
            option = self.options.get(option_name)

            if not option and optional is False:
                err = "'{0}' is mandatory and is not set in the app.config file. You must set this value to run this function".format(option_name)
                raise ValueError(err)
            else:
                return option

        def get_function_input(inputs, input_name, optional=False):
            """Given input_name, checks if it defined. Raises ValueError if a mandatory input is None"""
            this_input = inputs.get(input_name)

            if this_input is None and optional is False:
                err = "'{0}' is a mandatory function input".format(input_name)
                raise ValueError(err)
            else:
                return this_input

        try:

            inputs = {
                "twilio_sms_destination": get_function_input(kwargs, "twilio_sms_destination"),
                "twilio_sms_message": get_function_input(kwargs, "twilio_sms_message")
            }

            # Create payload dict with inputs
            payload = FunctionPayload(inputs)

            yield StatusMessage("Function Inputs OK")
            
            # Get configs
            account_sid = get_config_option("twilio_account_sid")
            auth_token = get_config_option("twilio_auth_token")
            src_address = get_config_option("twilio_src_address")

            try:
                phone_numbers_unstripped = [s.strip() for s in
                                            payload.inputs["twilio_sms_destination"].split(',')]  # Split commas ignoring any whitespace
                phone_numbers = []
                for phone_number_unstripped in phone_numbers_unstripped:
                    phone_numbers.append(clean_phone_number(phone_number_unstripped))  # Strip all non-numeric chars and prefix with +

            except Exception:
                raise FunctionError("Invalid phone numbers {0} provided, failed to decode.".format(payload.inputs["twilio_sms_destination"]))

            # Create Twilio Client
            client = Client(account_sid, auth_token)

            # Status
            payload.twilio_status = []

            # Send SMS to each number
            for phone_number in phone_numbers:
                try:
                    message = client.messages \
                    .create(
                        body=payload.inputs["twilio_sms_message"],
                        from_= src_address,
                        to=phone_number
                    )

                    entry = {
                        "phone_number": phone_number,
                        "messaging_service_sid": message.messaging_service_sid,
                        "date_created": str(message.date_created),
                        "direction": message.direction,
                        "message_body": message.body,
                        "status": message.status,
                        "error_message": None
                    }

                    if message.error_code is None:
                        entry['success'] = True
                        log.info('Sent to {0}'.format(phone_number))
                    else:
                        entry['success'] = False
                        entry["error_message"]: message.error_message
                        log.error('Failed to send to {0} [{1}]'.format(phone_number, message.error_message))

                    payload.twilio_status.append(entry)
                except TwilioRestException as e:
                        entry = { 
                            "phone_number": phone_number,
                            "error_message": e.msg,
                            "success": False
                        }
                        payload.twilio_status.append(entry)
                        log.error('Failed to send to {0} [{1}]'.format(phone_number, e.msg))


            # Produce a FunctionResult with the results
            results = payload.as_dict()

            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
