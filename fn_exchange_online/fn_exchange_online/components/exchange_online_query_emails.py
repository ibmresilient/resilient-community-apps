# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import json
import datetime
import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, RequestsCommon, ResultPayload, IntegrationError
from fn_exchange_online.lib.ms_graph_helper import MSGraphHelper, MAX_RETRIES_TOTAL, MAX_RETRIES_BACKOFF_FACTOR, MAX_BATCHED_REQUESTS
from fn_exchange_online.lib.resilient_helper import create_incident_comment, create_incident_attachment

CONFIG_DATA_SECTION = 'fn_exchange_online'
LOG = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'exchange_online_query_emails"""

    def load_options(self, opts):
        """ Get app.config parameters and validate them. """
        self.opts = opts
        self.options = opts.get(CONFIG_DATA_SECTION, {})

        # Validate required fields in app.config are set
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

    @function("exchange_online_query_emails")
    def _exchange_online_query_emails_function(self, event, *args, **kwargs):
        """Function: This function will query Exchange Online to find emails matching the specified input parameters."""
        try:
            # Initialize the results payload
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Validate fields
            validate_fields(['exo_email_address', 'exo_query_output_format'], kwargs)

            # Get the function parameters
            incident_id = kwargs.get('incident_id')  # number
            email_address = kwargs.get('exo_email_address')  # text
            mail_folders = kwargs.get('exo_mail_folders')  # text
            sender = kwargs.get('exo_email_address_sender')  # text
            start_date = kwargs.get('exo_start_date')  # datetime
            end_date = kwargs.get('exo_end_date')  # datetime
            has_attachments = kwargs.get('exo_has_attachments')  # bool
            message_subject = kwargs.get('exo_message_subject')  # text
            message_body = kwargs.get('exo_message_body')  # text
            query_output_format = self.get_select_param(kwargs.get('exo_query_output_format'))  # select values: "Exchange Online data table", "Incident attachment", "Incident note"

            LOG.info(u"incident_id: %s", str(incident_id))
            LOG.info(u"exo_email_address: %s", email_address)
            LOG.info(u"exo_mailfolders: %s", mail_folders)
            LOG.info(u"exo_email_address_sender: %s", sender)
            LOG.info(u"exo_start_date: %s", start_date)
            LOG.info(u"exo_end_date: %s", end_date)
            LOG.info(u"exo_email_has_attachments: %s", has_attachments)
            LOG.info(u"exo_message_subject: %s", message_subject)
            LOG.info(u"exo_message_body: %s", message_body)
            LOG.info(u"exo_query_output_format: %s", query_output_format)

            yield StatusMessage(u"Starting message query.")

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

            email_results = MS_graph_helper.query_messages(email_address, mail_folders, sender, start_date, end_date,
                                                           has_attachments, message_subject, message_body)

            query_results = {"incident_id": incident_id,
                             "exo_query_output_format": query_output_format,
                             "email_results": email_results}



            # Put query results in the results payload.
            results = rp.done(True, query_results)

            metrics = results.get("metrics")
            query_time_ms = metrics.get("execution_time_ms")
            # Write query results to an attachment or note as specified by the user in activity field.
            # Writing results to the data table takes place in the post processor script.
            self.write_results_to_note_or_attachment(email_address, mail_folders, sender, start_date, end_date,
                                                     has_attachments, message_subject, message_body, query_results,
                                                     query_time_ms)

            yield StatusMessage(u"Returning results from query.")

            LOG.debug(json.dumps(results['content']))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

        except Exception as err:
            LOG.error(err)
            yield FunctionError(err)

    def write_results_to_note_or_attachment(self, email_address, mail_folders, sender, start_date, end_date,
                                            has_attachments, message_subject, message_body, query_results,
                                            query_time_ms):
        """
        Write the output results of a query to an incident note and/or an incident attachment.
        Results that go to the Exchange Online data table are written in the workflow post-processor script.
        :param email_address: search criteria emails address
        :param mail_folders: search criteria mail_folders
        :param sender:  search criteria sender
        :param start_date:  search criteria start_data
        :param end_date:  search criteria end_date
        :param has_attachments:  search criteria has_attachments
        :param message_subject:  search criteria message_subject
        :param message_body:  search criteria  message_body
        :param query_results: json results containing: incident id, output_format: multiselect field where to
        send results: "Exchange Online data table", "Incident note" or "Incident attachment";
        email results of the query
        :return: return True or False note or attachment is created
        """
        try:
            output_format = query_results.get('exo_query_output_format')

            # Write the requests to attachment or note if the user requests it.
            if "Incident attachment" not in output_format and "Incident note" not in output_format:
                return False

            incident_id = query_results.get('incident_id')
            email_results = query_results.get('email_results')

            note = u"<b>Exchange Online Message Query Criteria:</b><br><br>"
            if email_address:
                note = u"{0}    <b>email address:</b>   {1}<br>".format(note, email_address)
            if mail_folders:
                note = u"{0}    <b>mail folder:</b>     {1}<br>".format(note, mail_folders)
            if sender:
                note = u"{0}    <b>email sender:</b>    {1}<br>".format(note, sender)
            if start_date:
                utc_time = datetime.datetime.fromtimestamp(start_date / 1000).strftime('%Y-%m-%dT%H:%M:%SZ')
                note = u"{0}    <b>start date:</b>      {1}<br>".format(note, utc_time)
            if end_date:
                utc_time = datetime.datetime.fromtimestamp(end_date / 1000).strftime('%Y-%m-%dT%H:%M:%SZ')
                note = u"{0}    <b>end date:</b>  {1}<br>".format(note, utc_time)
            if has_attachments:
                note = u"{0}    <b>has attachments:</b> {1}<br>".format(note, has_attachments)
            if message_subject:
                note = u"{0}    <b>message subject:</b> {1}<br>".format(note, message_subject)
            if message_body:
                note = u"{0}    <b>message body:</b>    {1}<br>".format(note, message_body)

            total_emails = 0
            email_note = u""
            for email in email_results:
                num_emails_found = len(email.get('email_list'))
                if num_emails_found > 0:
                    email_note = u"{0} {1}:  {2}<br>".format(email_note, email.get('email_address'), num_emails_found)
                    total_emails = total_emails + num_emails_found

            # Add the query execution time
            email_note = u"{0}<b>Query execution time:</b>  {1}ms.".format(email_note, query_time_ms)

            # Add total messages found to the note text.
            note = u"{0}<br><b>Total messages matching search criteria:</b>  {1}<br>{2}".format(note, total_emails,
                                                                                              email_note)

            if "Incident note" in output_format:
                LOG.info('Writing query results to incident note.')
                create_incident_comment(self.rest_client(), incident_id, note)
            if "Incident attachment" in output_format:
                LOG.info('Writing query results to attachment.')
                note = note.replace('<br>', '\n')
                note = note.replace('<b>', '')
                note = note.replace('</b>', '')
                create_incident_attachment(self.rest_client(), incident_id, note, 'exo-query-results')


            return True

        except Exception as err:
            raise IntegrationError(err)
