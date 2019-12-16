# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import json
import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, RequestsCommon, ResultPayload
from fn_exchange_online.lib.ms_graph_helper import MSGraphHelper

CONFIG_DATA_SECTION = 'fn_exchange_online'
LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'exchange_online_query_emails"""

    def load_options(self, opts):
        # Get app.config parameters.
        self.opts = opts
        self.options = opts.get(CONFIG_DATA_SECTION, {})

        # Validate required fields in app.config are set
        required_fields = ["microsoft_graph_token_url", "microsoft_graph_url", "tenant_id", "client_id",
                           "client_secret", "max_emails_retrieved_in_query"]
        validate_fields(required_fields, self.options)

        # Get the MS Graph helper class
        self.MS_graph_helper = MSGraphHelper(self.options.get("microsoft_graph_token_url"),
                                             self.options.get("microsoft_graph_url"),
                                             self.options.get("tenant_id"),
                                             self.options.get("client_id"),
                                             self.options.get("client_secret"),
                                             self.options.get("max_emails_retrieved_in_query"),
                                             RequestsCommon(self.opts, self.options).get_proxies())

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.load_options(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.load_options(opts)

    @function("exchange_online_query_emails")
    def _exchange_online_query_emails_function(self, event, *args, **kwargs):
        """Function: This function will query Exchange Online to find emails matching the specified input parameters."""
        try:
            # Initialize the results payload
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Validate fields
            validate_fields(['exo_email_address'], kwargs)
            validate_fields(['exo_email_address_sender'], kwargs)
            validate_fields(['exo_start_date'], kwargs)
            validate_fields(['exo_end_date'], kwargs)
            validate_fields(['exo_has_attachments'], kwargs)
            validate_fields(['exo_message_subject'], kwargs)
            validate_fields(['exo_message_body'], kwargs)

            # Get the function parameters
            email_address = kwargs.get('exo_email_address')  # text
            email_address_sender = kwargs.get('exo_email_address_sender')  # text
            start_date       = kwargs.get('exo_start_date')  # datetime
            end_date         = kwargs.get('exo_end_date')  # datetime
            has_attachments  = kwargs.get('exo_has_attachments')  # bool
            message_subject  = kwargs.get('exo_message_subject')  # text
            message_body     = kwargs.get('exo_message_body')  # text

            LOG.info(u"exo_email_address: %s", email_address)
            LOG.info(u"exo_email_address_sender: %s", email_address_sender)
            LOG.info(u"exo_start_date: %s", start_date)
            LOG.info(u"exo_end_date: %s", end_date)
            LOG.info(u"exo_email_has_attachments: %s", has_attachments)
            LOG.info(u"exo_message_subject: %s", message_subject)
            LOG.info(u"exo_message_body: %s", message_body)

            if (email_address == "ALL USERS"):
                email_results = self.MS_graph_helper.query_emails_all_users(email_address_sender, start_date, end_date,
                                                                       has_attachments, message_subject, message_body)
            else:
                # Call MS Graph API to get the user profile
                email_results = self.MS_graph_helper.query_emails(email_address, email_address_sender, start_date, end_date,
                                                         has_attachments, message_subject, message_body)

            #response_json = response.json()
            results = rp.done(True, email_results)

            yield StatusMessage(u"Returning results for email address: {}".format(email_address))

            LOG.debug(json.dumps(results['content']))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            LOG.error(err)
            yield FunctionError(err)