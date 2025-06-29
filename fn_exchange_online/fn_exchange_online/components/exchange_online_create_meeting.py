# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, line-too-long, too-many-locals, too-many-function-args, too-many-function-args
"""Function implementation"""

import json
import logging
import datetime
import pytz
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, RequestsCommon, ResultPayload
from resilient_lib.components.integration_errors import IntegrationError
from fn_exchange_online.lib.ms_graph_helper import MSGraphHelper, MAX_RETRIES_TOTAL, MAX_RETRIES_BACKOFF_FACTOR, MAX_BATCHED_REQUESTS

CONFIG_DATA_SECTION = 'fn_exchange_online'
LOG = logging.getLogger(__name__)
LOG.info("test")
class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'exchange_online_create_meeting"""

    def load_options(self, opts):
        """ Get app.config parameters and validate them. """
        self.opts = opts
        self.options = opts.get(CONFIG_DATA_SECTION, {})

        required_fields = ["microsoft_graph_token_url", "microsoft_graph_url", "tenant_id", "client_id",
                           "client_secret", "max_messages", "max_users"]
        validate_fields(required_fields, self.options)

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super().__init__(opts)
        self.load_options(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.load_options(opts)

    @function("exchange_online_create_meeting")
    def _exchange_online_create_meeting_function(self, event, *args, **kwargs):
        """Function: This function will create a meeting event and sent a mail message to the meeting participants."""
        try:
            # Initialize the results payload
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Validate fields
            validate_fields(['exo_meeting_email_address', 'exo_meeting_start_time', 'exo_meeting_end_time',
                             'exo_meeting_subject', 'exo_meeting_body'], kwargs)

            # Get the function parameters:
            email_address = kwargs.get("exo_meeting_email_address")  # text
            start_time = kwargs.get("exo_meeting_start_time")  # datetimepicker
            end_time = kwargs.get("exo_meeting_end_time")  # datetimepicker
            subject = kwargs.get("exo_meeting_subject")  # text
            body = kwargs.get("exo_meeting_body")  # text
            required_attendees = kwargs.get("exo_meeting_required_attendees")  # text
            optional_attendees = kwargs.get("exo_meeting_optional_attendees")  # text
            location = kwargs.get("exo_meeting_location")  # text

            LOG.info("exo_meeting_email_address: %s", email_address)
            LOG.info("exo_meeting_start_time: %s", start_time)
            LOG.info("exo_meeting_end_time: %s", end_time)
            LOG.info("exo_meeting_subject: %s", subject)
            LOG.info("exo_meeting_body: %s", body)
            LOG.info("exo_meeting_required_attendees: %s", required_attendees)
            LOG.info("exo_meeting_optional_attendees: %s", optional_attendees)
            LOG.info("exo_meeting_location: %s", location)

            # Validate the meeting start/end time
            if start_time >= end_time:
                raise IntegrationError("Exchange Online meeting start time is behind end time.")

            # Check meeting time is not in the past.
            now_utc = pytz.utc.localize(datetime.datetime.now())
            meeting_time_utc = datetime.datetime.fromtimestamp(start_time/1000).replace(tzinfo=pytz.utc)
            if now_utc > meeting_time_utc:
                raise IntegrationError("Exchange Online meeting start date/time is in the past.")

            yield StatusMessage("Starting create meeting for email address: {}".format(email_address))

            # Get the MS Graph helper class
            MS_graph_helper = MSGraphHelper(self.options.get("microsoft_graph_token_url"),
                                            self.options.get("microsoft_graph_url"),
                                            self.options.get("tenant_id"),
                                            self.options.get("client_id"),
                                            self.options.get("client_secret"),
                                            self.options.get("max_messages"),
                                            self.options.get("max_users"),
                                            self.options.get("max_retries_total", MAX_RETRIES_TOTAL),
                                            self.options.get("max_retries_backoff_factor", MAX_RETRIES_BACKOFF_FACTOR),
                                            self.options.get("max_batched_requests", MAX_BATCHED_REQUESTS),
                                            RequestsCommon(self.opts, self.options).get_proxies())

            # Call MS Graph API to get the user profile
            response = MS_graph_helper.create_meeting(email_address, start_time, end_time, subject, body,
                                                      required_attendees, optional_attendees, location)

            if response.status_code == 201:
                success = True
            else:
                success = False

            response_json = response.json()

            results = rp.done(success, response_json)

            # Add pretty printed string for easier to read output text in note.
            pretty_string = json.dumps(response_json, ensure_ascii=False, indent=4, separators=(',', ': '))
            results['pretty_string'] = pretty_string

            yield StatusMessage("Starting create meeting for email address: {}".format(email_address))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

        except Exception as err:
            LOG.error(err)
            yield FunctionError(err)
