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
    """Component that implements Resilient function 'exchange_online_send_message"""
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

    @function("exchange_online_send_message")
    def _exchange_online_send_message_function(self, event, *args, **kwargs):
        """Function: This function will create a message and send to the specified recipients."""
        try:
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Validate fields
            validate_fields(['exo_email_address', 'exo_recipients'], kwargs)

            # Get the function parameters:
            email_address = kwargs.get("exo_email_address")  # text
            recipients = kwargs.get("exo_recipients")  # text
            message_subject = kwargs.get("exo_message_subject")  # text
            message_body = kwargs.get("exo_message_body")  # text

            log = logging.getLogger(__name__)
            log.info(u"exo_email_address: %s", email_address)
            log.info(u"exo_recipients: %s", recipients)
            log.info(u"exo_message_subject: %s", message_subject)
            log.info(u"exo_message_body: %s", message_body)

            yield StatusMessage(u"Starting send message from email address: {}".format(email_address))

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
            response = MS_graph_helper.send_message(email_address, recipients, message_subject, message_body)

            # If message was sent a 202 code is returned...nothing is returned in the response.
            if response.status_code == 202:
                success = True
                response_json = {'value': success}
            else:
                success = False
                response_json = response.json()

            results = rp.done(success, response_json)

            yield StatusMessage(u"Returning send mail results by email address: {}".format(email_address))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            LOG.error(err)
            yield FunctionError(err)