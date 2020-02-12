# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

"""Function implementation"""

import logging
from dateutil.parser import parse
import time
from fn_twilio.lib.common import get_interval, clean_phone_number, get_ts_from_datetime
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, ResultPayload, get_workflow_status, readable_datetime
from twilio.rest import Client

CONFIG_DATA_SECTION = 'fn_twilio_send_sms'
DEFAULT_WAIT_TIMEOUT = '2m'  # 2 minutes
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
        """Function: Receive messages based on a destination number and a timeframe"""
        try:
            # Get the workflow_instance_id so we can raise an error if the workflow was terminated by the user
            workflow_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            res_payload = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Get the function parameters:
            twilio_phone_number = kwargs.get("twilio_phone_number")  # text
            twilio_date_sent = kwargs.get("twilio_date_sent")  # text
            twilio_date_sent_ts = kwargs.get("twilio_date_sent_ts")  # number
            twilio_wait_timeout = kwargs.get("twilio_wait_timeout")  # text
            if not twilio_wait_timeout:
                twilio_wait_timeout = DEFAULT_WAIT_TIMEOUT

            log = logging.getLogger(__name__)
            log.info("twilio_phone_number: %s", twilio_phone_number)
            log.info("twilio_date_sent: %s", twilio_date_sent)
            log.info("twilio_date_sent_ts: %s", twilio_date_sent_ts)
            log.info("twilio_wait_timeout: %s", twilio_wait_timeout)

            # Get configs
            validate_fields(['twilio_account_sid', 'twilio_auth_token', 'twilio_src_address'], self.options)
            account_sid = self.options.get("twilio_account_sid")
            auth_token = self.options.get("twilio_auth_token")
            src_address = self.options.get("twilio_src_address")

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")
            phone_number = clean_phone_number(twilio_phone_number)

            # timestamp date has precedence over string version
            if twilio_date_sent_ts and not twilio_date_sent:
                twilio_date_sent = readable_datetime(twilio_date_sent_ts)

            client = Client(account_sid, auth_token)

            # calculate timeout value
            wait_timeout = time.time() + get_interval(twilio_wait_timeout)

            continue_flg = True

            result_err_msg = None
            result_payload = []
            result_rc = True
            wf_status = None
            rest_client = self.rest_client()

            converted_date = parse(twilio_date_sent) if twilio_date_sent else None

            # continue while the workflow is still active, no messages have been received and timeout period active
            while continue_flg and time.time() <= wait_timeout:
                # get the messages based on phone number and date sent
                messages = client.messages.list(
                    date_sent=converted_date,
                    to=src_address,
                    from_=phone_number
                )

                if messages:
                    continue_flg = False
                    log.debug(str(messages))

                    # format messages for payload return
                    for message in messages:
                        entry = {
                            "phone_number": message.from_,
                            "messaging_service_sid": message.sid,
                            "date_created": str(message.date_created),
                            "date_created_ts": get_ts_from_datetime(message.date_created),
                            "direction": message.direction,
                            "message_body": message.body,
                            "status": message.status,
                            "error_message": message.error_message
                        }
                        result_payload.append(entry)

                # if no messages, delay and try again
                if not result_payload:
                    result_rc = False
                    time.sleep(SLEEP_TIME)

                    # check to see if the workflow is still active
                    wf_status = get_workflow_status(rest_client, workflow_instance_id)
                    continue_flg = not wf_status.is_terminated

            if wf_status and wf_status.is_terminated:
                result_err_msg = u"Workflow was terminated: {}".format(wf_status.reason)
                yield StatusMessage(result_err_msg)
                log.warning(result_err_msg)
                result_rc = False
            elif not result_payload:
                result_err_msg = u"Timeout waiting for responses for phone number: {} since {}".format(twilio_phone_number, twilio_date_sent)
                yield StatusMessage(result_err_msg)
                log.warning(result_err_msg)

            yield StatusMessage("done...")

            results = res_payload.done(result_rc, result_payload, reason=result_err_msg)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
