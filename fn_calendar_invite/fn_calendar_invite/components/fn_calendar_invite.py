# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_calendar_invite"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_calendar_invite", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_calendar_invite", {})

    @function("fn_calendar_invite")
    def _fn_calendar_invite_function(self, event, *args, **kwargs):
        """Function: A function to invite people to a meeting via a calendar invite"""
        try:
            # Get the function parameters:
            calendar_invite_datetime = kwargs.get("calendar_invite_datetime")  # datetimepicker
            calendar_invite_subject = kwargs.get("calendar_invite_subject")  # text
            calendar_invite_description = kwargs.get("calendar_invite_description")  # text
            calendar_incident_id = kwargs.get("calendar_incident_id")  # text

            log = logging.getLogger(__name__)
            log.info("calendar_invite_datetime: %s", calendar_invite_datetime)
            log.info("calendar_invite_subject: %s", calendar_invite_subject)
            log.info("calendar_invite_description: %s", calendar_invite_description)
            log.info("calendar_incident_id: %s", calendar_incident_id)

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