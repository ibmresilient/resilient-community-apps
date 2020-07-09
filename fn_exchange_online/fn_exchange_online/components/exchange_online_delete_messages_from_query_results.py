# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""
import json
import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, RequestsCommon, ResultPayload, IntegrationError
from fn_exchange_online.lib.ms_graph_helper import MSGraphHelper, MAX_RETRIES_TOTAL, MAX_RETRIES_BACKOFF_FACTOR
from fn_exchange_online.lib.resilient_helper import create_incident_comment, create_incident_attachment

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

            query_results = kwargs.get('exo_query_messages_results')  # text

            LOG.info(u"exo_query_messages_results: %s", query_results)

            yield StatusMessage(u"Starting delete messages for query results")

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
                                            RequestsCommon(self.opts, self.options).get_proxies())

            # Convert string to JSON.
            try:
                query_results_json = json.loads(query_results)
                query_message_results = query_results_json.get('email_results')
                query_output_format = query_results_json.get('exo_query_output_format')
                incident_id = int(query_results_json.get('incident_id'))
            except ValueError as err:
                raise IntegrationError("Invalid JSON string in Delete Message from Query Results.")

            # Delete messages found in the query.
            delete_results = MS_graph_helper.delete_messages_from_query_results(query_message_results)

            delete_message_results = {"incident_id": incident_id,
                                      "exo_query_output_format": query_output_format,
                                      "delete_results": delete_results}

            # Write delete messages from query results to an attachment or note as specified by the user
            # in activity field.
            # Writing results to the data table takes place in the post processor script.
            self.write_results_to_note_or_attachment(delete_message_results)

            results = rp.done(True, delete_message_results)

            yield StatusMessage(u"Returning Delete Messages From Query Results results.")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            LOG.error(err)
            yield FunctionError(err)

    def write_results_to_note_or_attachment(self, delete_message_results):
        """
        Write the output results of a delete messages from query results to an incident note and/or an
        incident attachment.  Results that go to the Exchange Online data table are written in the
        workflow post-processor script.
        :param delete_message_results: json results containing: incident id,
        output_format: multiselect field where to send results: "Exchange Online data table",
        "Incident note" or "Incident attachment"; delete_message results from delte messages from query results.
        :return True or False note or attachment is created
        """
        try:
            output_format = delete_message_results.get('exo_query_output_format')

            # Write the requests to attachment or note if the user requests it.
            if "Incident attachment" not in output_format and "Incident note" not in output_format:
                return False

            incident_id = delete_message_results.get('incident_id')
            delete_results = delete_message_results.get('delete_results')

            note = u""
            total_deleted = 0
            for user in delete_results:
                email_address = user.get('email_address')
                number_deleted = len(user.get('deleted_list'))

                total_deleted = total_deleted + number_deleted
                number_not_deleted = len(user.get('not_deleted_list'))
                note = u"{0} {1}: {2} deleted, {3} not found.\n".format(note, email_address, number_deleted,
                                                                        number_not_deleted)
            # Put the total deleted messages number in the note.
            note = "Exchange Online Delete Message from Query Results:\n\nTotal messages deleted: {0}\n\n{1}".format(
                    total_deleted, note)

            if "Incident attachment" in output_format:
                LOG.info('Writing query results to incident attachment.')
                create_incident_attachment(self.rest_client(), incident_id, note, 'exo-delete-results')
            if "Incident note" in output_format:
                note = note.replace('\n', '<br>')
                LOG.info('Writing query results to incident note.')
                create_incident_comment(self.rest_client(), incident_id, note)

            return True

        except Exception as err:
            raise IntegrationError(err)
