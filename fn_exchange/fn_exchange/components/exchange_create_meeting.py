# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'exchange_create_meeting"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_exchange", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_exchange", {})

    @function("exchange_create_meeting")
    def _exchange_create_meeting_function(self, event, *args, **kwargs):
        """Function: Creates a meeting and sends out invitation to required attendees and optional attendees."""
        try:
            # Get the function parameters:
            exchange_email = kwargs.get("exchange_email")  # text
            exchange_meeting_start_time = kwargs.get("exchange_meeting_start_time")  # datetimepicker
            exchange_meeting_end_time = kwargs.get("exchange_meeting_end_time")  # datetimepicker
            exchange_meeting_subject = kwargs.get("exchange_meeting_subject")  # text
            exchange_message_body = kwargs.get("exchange_message_body")  # text
            exchange_required_attendees = kwargs.get("exchange_required_attendees")  # text
            exchange_optional_attendees = kwargs.get("exchange_optional_attendees")  # text

            log = logging.getLogger(__name__)
            log.info("exchange_email: %s", exchange_email)
            log.info("exchange_meeting_start_time: %s", exchange_meeting_start_time)
            log.info("exchange_meeting_end_time: %s", exchange_meeting_end_time)
            log.info("exchange_meeting_subject: %s", exchange_meeting_subject)
            log.info("exchange_message_body: %s", exchange_message_body)
            log.info("exchange_required_attendees: %s", exchange_required_attendees)
            log.info("exchange_optional_attendees: %s", exchange_optional_attendees)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            #  yield StatusMessage("starting...")
            #  yield StatusMessage("done...")

            results = {
                "value": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()