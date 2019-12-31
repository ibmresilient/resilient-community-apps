# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import sys
import json
import logging
from io import BytesIO
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import write_file_attachment, validate_fields, RequestsCommon, ResultPayload
from fn_exchange_online.lib.ms_graph_helper import MSGraphHelper

CONFIG_DATA_SECTION = 'fn_exchange_online'
LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'exchange_online_write_message_as_attachment"""
    def load_options(self, opts):
        # Get app.config parameters.
        self.opts = opts
        self.options = opts.get(CONFIG_DATA_SECTION, {})

        required_fields = ["microsoft_graph_token_url", "microsoft_graph_url", "tenant_id", "client_id",
                           "client_secret", "max_messages", "max_users"]
        validate_fields(required_fields, self.options)

        # Get the MS Graph helper class
        self.MS_graph_helper = MSGraphHelper(self.options.get("microsoft_graph_token_url"),
                                             self.options.get("microsoft_graph_url"),
                                             self.options.get("tenant_id"),
                                             self.options.get("client_id"),
                                             self.options.get("client_secret"),
                                             self.options.get("max_messages"),
                                             self.options.get("max_users"),
                                             RequestsCommon(self.opts, self.options).get_proxies())
    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.load_options(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.load_options(opts)

    @function("exchange_online_write_message_as_attachment")
    def _exchange_online_write_message_as_attachment_function(self, event, *args, **kwargs):
        """Function: This function will get the mime content of an Exchange Online message and write it as an attachment."""
        try:
            # Initialize the results payload
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Validate fields
            validate_fields(['incident_id'], kwargs)
            validate_fields(['exo_email_address'], kwargs)
            validate_fields(['exo_messages_id'], kwargs)

            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            task_id = kwargs.get("task_id")  # number
            email_address = kwargs.get("exo_email_address")  # text
            message_id = kwargs.get("exo_messages_id")  # text
            attachment_name = kwargs.get("exo_attachment_name")  # text

            LOG.info(u"incident_id: %s", incident_id)
            LOG.info(u"task_id: %s", task_id)
            LOG.info(u"exo_email_address: %s", email_address)
            LOG.info(u"exo_messages_id: %s", message_id)
            LOG.info(u"exo_attachment_name: %s", attachment_name)

            yield StatusMessage(u"Start get message mime for email address: {}".format(email_address))

            # Call MS Graph API to get the user profile
            response = self.MS_graph_helper.get_message_mime(email_address, message_id)

            datastream = BytesIO(response.content)

            if attachment_name is None:
                attachment_name = u"message-{}-{}.eml".format(email_address, message_id)

            # add as an attachment
            rest_client = self.rest_client()

            # failures will raise an exception
            write_file_attachment(rest_client, attachment_name, datastream,
                                  incident_id, task_id)

            results_data = {"attachment_name": attachment_name}
            results = rp.done(True, results_data)

            yield StatusMessage(u"Returning results for get message mime for email address: {}".format(email_address))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            LOG.error(err)
            yield FunctionError(err)