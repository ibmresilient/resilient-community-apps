# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, RequestsCommon, ResultPayload
from fn_exchange_online.lib.ms_graph_helper import MSGraphHelper

CONFIG_DATA_SECTION = 'fn_exchange_online'
LOG = logging.getLogger(__name__)

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
        super(FunctionComponent, self).__init__(opts)
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
                             'exo_meeting_subject', 'exo_meeting_body', 'exo_meeting_required_attendees'], kwargs)

            # Get the function parameters:
            email_address = kwargs.get("exo_meeting_email_address")  # text
            start_time = kwargs.get("exo_meeting_start_time")  # datetimepicker
            end_time = kwargs.get("exo_meeting_end_time")  # datetimepicker
            subject = kwargs.get("exo_meeting_subject")  # text
            body = kwargs.get("exo_meeting_body")  # text
            required_attendees = kwargs.get("exo_meeting_required_attendees")  # text
            optional_attendees = kwargs.get("exo_meeting_optional_attendees")  # text

            LOG.info(u"exo_meeting_email_address: %s", email_address)
            LOG.info(u"exo_meeting_start_time: %s", start_time)
            LOG.info(u"exo_meeting_end_time: %s", end_time)
            LOG.info(u"exo_meeting_subject: %s", subject)
            LOG.info(u"exo_meeting_body: %s", body)
            LOG.info(u"exo_meeting_required_attendees: %s", required_attendees)
            LOG.info(u"exo_meeting_optional_attendees: %s", optional_attendees)

            yield StatusMessage(u"Starting create meeting for email address: {}".format(email_address))

            # Get the MS Graph helper class
            MS_graph_helper = MSGraphHelper(self.options.get("microsoft_graph_token_url"),
                                            self.options.get("microsoft_graph_url"),
                                            self.options.get("tenant_id"),
                                            self.options.get("client_id"),
                                            self.options.get("client_secret"),
                                            self.options.get("max_messages"),
                                            self.options.get("max_users"),
                                            RequestsCommon(self.opts, self.options).get_proxies())

            # Call MS Graph API to get the user profile
            response = MS_graph_helper.create_meeting(email_address, start_time, end_time, subject, body,
                                                      required_attendees, optional_attendees)

            if response.status_code == 204:
                success = True
                response_json = {'value': success}
            else:
                success = False
                response_json = response.json()

            results = rp.done(success, response_json)

            yield StatusMessage(u"Returning create meeting results for email address: {}".format(email_address))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

        except Exception as err:
            LOG.error(err)
            yield FunctionError(err)
