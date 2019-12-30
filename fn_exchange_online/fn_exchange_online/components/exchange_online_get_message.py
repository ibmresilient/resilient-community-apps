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
    """Component that implements Resilient function 'exchange_online_get_message"""
    def load_options(self, opts):
        # Get app.config parameters.
        self.opts = opts
        self.options = opts.get(CONFIG_DATA_SECTION, {})

        # Validate required fields in app.config are set
        required_fields = ["microsoft_graph_token_url", "microsoft_graph_url", "tenant_id", "client_id",
                           "client_secret", "max_messages_retrieved_in_query"]
        validate_fields(required_fields, self.options)

        # Get the MS Graph helper class
        self.MS_graph_helper = MSGraphHelper(self.options.get("microsoft_graph_token_url"),
                                             self.options.get("microsoft_graph_url"),
                                             self.options.get("tenant_id"),
                                             self.options.get("client_id"),
                                             self.options.get("client_secret"),
                                             self.options.get("max_messages_retrieved_in_query"),
                                             RequestsCommon(self.opts, self.options).get_proxies())
    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.load_options(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.load_options(opts)

    @function("exchange_online_get_message")
    def _exchange_online_get_message_function(self, event, *args, **kwargs):
        """Function: This function returns the contents of an Exchange Online message."""
        try:
            # Initialize the results payload
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Validate fields
            validate_fields(['exo_email_address'], kwargs)
            validate_fields(['exo_messages_id'], kwargs)

            # Get the function parameters:
            email_address = kwargs.get("exo_email_address")  # text
            messages_id = kwargs.get("exo_messages_id")  # text

            LOG.info(u"exo_email_address: %s", email_address)
            LOG.info(u"exo_messages_id: %s", messages_id)

            yield StatusMessage(u"Start get message for email address: {}".format(email_address))

            # Call MS Graph API to get the user profile
            response = self.MS_graph_helper.get_message(email_address, messages_id)

            response_json = response.json()
            results = rp.done(True, response_json)

            # Add pretty printed string for easier to read output text in note.
            pretty_string = json.dumps(response_json, sort_keys=True, indent=4, separators=(',', ': '))
            results['pretty_string'] = pretty_string

            yield StatusMessage(u"Returning results for get message for email address: {}".format(email_address))

            LOG.debug(json.dumps(results['content']))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            LOG.error(err)
            yield FunctionError(err)