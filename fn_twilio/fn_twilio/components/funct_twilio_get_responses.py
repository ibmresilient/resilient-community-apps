# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

"""Function implementation"""

import logging
from dateutil.parser import parse
import time
from fn_twilio.lib.common import get_interval, clean_phone_number
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, ResultPayload
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

CONFIG_DATA_SECTION = 'fn_twilio_send_sms'
SLEEP_TIME = 30

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'twilio_receive_messages"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    @function("twilio_get_responses")
    def _twilio_receive_messages_function(self, event, *args, **kwargs):
        """Function: Receive messages based on a message Id (SID)"""
        try:
            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            res_payload = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Get the function parameters:
            twilio_phone_number = kwargs.get("twilio_phone_number")  # text
            twilio_after_date = kwargs.get("twilio_after_date")  # text
            twilio_wait_timeout = kwargs.get("twilio_wait_timeout")  # text

            log = logging.getLogger(__name__)
            log.info("twilio_phone_number: %s", twilio_phone_number)
            log.info("twilio_after_date: %s", twilio_after_date)
            log.info("twilio_wait_timeout: %s", twilio_wait_timeout)

            # Get configs
            validate_fields(['twilio_account_sid', 'twilio_auth_token', 'twilio_src_address'], self.options)
            account_sid = self.options.get("twilio_account_sid")
            auth_token = self.options.get("twilio_auth_token")
            src_address = self.options.get("twilio_src_address")

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")
            phone_number = clean_phone_number(twilio_phone_number)

            client = Client(account_sid, auth_token)

            # calculate timeout value
            wait_timeout = time.time() + get_interval(twilio_wait_timeout)

            continue_flg = True

            err_msg = None
            payload = []
            rc = True
            while continue_flg and time.time() <= wait_timeout:
                # get the messages
                messages = client.messages.list(
                    date_sent=parse(twilio_after_date),
                    to=src_address,
                    from_=phone_number
                )

                # if no messages, delay and try again
                if messages:
                    continue_flg = False
                    log.debug(str(messages))

                    for message in messages:
                        entry = {
                            "phone_number": message.from_,
                            "sid": message.sid,
                            "date_created": str(message.date_created),
                            "direction": message.direction,
                            "message_body": message.body,
                            "status": message.status,
                            "error_message": message.error_message
                        }
                        payload.append(entry)

                if not payload:
                    rc = False
                    time.sleep(SLEEP_TIME)

            if not payload:
                err_msg = "Timeout waiting for responses for phone number: {} since {}".format(twilio_phone_number, twilio_after_date)
                log.warning(err_msg)

            yield StatusMessage("done...")

            results = res_payload.done(rc, payload, reason=err_msg)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
