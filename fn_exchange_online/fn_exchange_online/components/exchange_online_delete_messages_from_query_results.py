# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
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
    """Component that implements Resilient function 'exchange_online_delete_messages_from_query_results"""

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

    @function("exchange_online_delete_messages_from_query_results")
    def _exchange_online_delete_messages_from_query_results_function(self, event, *args, **kwargs):
        """Function: This Exchange Online function will delete a list of messages returned from the
        Query Message function.  The input to the function is a string containing the JSON results
        from the Query Messages function."""
        try:
            # Initialize the results payload
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Validate fields
            validate_fields(['exo_query_messages_results'], kwargs)

            # Get the function parameters
            query_messages_results = kwargs.get('exo_query_messages_results')  # text

            # Convert string to JSON.
            query_messages_results_json = json.loads(query_messages_results)

            LOG.info(u"exo_query_messages_results: %s", query_messages_results)

            yield StatusMessage(u"Starting delete messages for query results")

            # Get the MS Graph helper class
            MS_graph_helper = MSGraphHelper(self.options.get("microsoft_graph_token_url"),
                                            self.options.get("microsoft_graph_url"),
                                            self.options.get("tenant_id"),
                                            self.options.get("client_id"),
                                            self.options.get("client_secret"),
                                            self.options.get("max_messages"),
                                            self.options.get("max_users"),
                                            RequestsCommon(self.opts, self.options).get_proxies())

            delete_results = []

            for user in query_messages_results_json:
                email_address = user["email_address"]
                deleted_list = []
                not_deleted_list = []
                for message in user["email_list"]:

                    # Call MS Graph API to get the user profile
                    response = MS_graph_helper.delete_message(email_address, None, message["id"])

                    # If message was deleted a 204 code is returned.
                    if response.status_code == 204:
                        deleted_list.append(message)
                    else:
                        not_deleted_list.append(message)

                user_delete_results = {'email_address': email_address,
                                       'deleted_list': deleted_list,
                                       'not_deleted_list': not_deleted_list}
                delete_results.append(user_delete_results)

            results = rp.done(True, delete_results)

            yield StatusMessage(u"Returning delete message from query results")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            LOG.error(err)
            yield FunctionError(err)