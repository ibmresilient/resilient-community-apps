# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, line-too-long, too-many-locals, too-many-function-args, too-many-function-args
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, RequestsCommon, ResultPayload
from fn_exchange_online.lib.ms_graph_helper import MSGraphHelper, MAX_RETRIES_TOTAL, MAX_RETRIES_BACKOFF_FACTOR, MAX_BATCHED_REQUESTS

CONFIG_DATA_SECTION = 'fn_exchange_online'
LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'exchange_online_move_message_to_folder"""

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

    @function("exchange_online_move_message_to_folder")
    def _exchange_online_move_message_to_folder_function(self, event, *args, **kwargs):
        """Function: This function will move an Exchange Online message to the specified folder in the users mailbox."""
        try:
            # Initialize the results payload
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Validate fields
            validate_fields(['exo_email_address', 'exo_messages_id', 'exo_destination_mailfolder_id'], kwargs)

            # Get the function parameters:
            email_address = kwargs.get("exo_email_address")  # text
            message_id = kwargs.get("exo_messages_id")  # text
            mailfolders_id = kwargs.get("exo_mailfolders_id")  # text
            destination_id = kwargs.get("exo_destination_mailfolder_id")  # text

            LOG.info("exo_email_address: %s", email_address)
            LOG.info("exo_messages_id: %s", message_id)
            LOG.info("exo_mailfolders_id: %s", mailfolders_id)
            LOG.info("exo_destination_id: %s", destination_id)

            yield StatusMessage("Starting move message for email address: {} to mail folder {}".format(email_address, destination_id))

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
            response = MS_graph_helper.move_message(email_address, mailfolders_id, message_id, destination_id)

            # If message was deleted a 201 code is returned.
            if response.status_code == 201:
                success = True
                new_message_id = response.json().get('id')
                new_web_link = response.json().get('webLink')
                response_json = {'new_message_id': new_message_id,
                                 'new_web_link': new_web_link}
            else:
                success = False
                response_json = response.json()

            results = rp.done(success, response_json)

            yield StatusMessage("Returning delete results for email address: {}".format(email_address))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            LOG.error(err)
            yield FunctionError(err)
