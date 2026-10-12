# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, line-too-long, too-many-locals, too-many-arguments, too-many-positional-arguments, too-many-branches
"""Function implementation"""

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
        super().__init__(opts)
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

            LOG.info("incident_id: %s", str(incident_id))
            LOG.info("exo_email_address: %s", email_address)
            LOG.info("exo_mailfolders: %s", mail_folders)
            LOG.info("exo_email_address_sender: %s", sender)
            LOG.info("exo_start_date: %s", start_date)
            LOG.info("exo_end_date: %s", end_date)
            LOG.info("exo_email_has_attachments: %s", has_attachments)
            LOG.info("exo_message_subject: %s", message_subject)
            LOG.info("exo_message_body: %s", message_body)
            LOG.info("exo_query_output_format: %s", query_output_format)

            yield StatusMessage("Starting message query.")

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

            note = []
            note.append("<b>Exchange Online Message Query Criteria:</b><br><br>")
            if email_address:
                note.append(f"    <b>email address:</b>   {email_address}<br>")
            if mail_folders:
                note.append(f"    <b>mail folder:</b>     {mail_folders}<br>")
            if sender:
                note.append(f"    <b>email sender:</b>    {sender}<br>")
            if start_date:
                utc_time = datetime.datetime.fromtimestamp(start_date / 1000).strftime('%Y-%m-%dT%H:%M:%SZ')
                note.append(f"    <b>start date:</b>      {utc_time}<br>")
            if end_date:
                utc_time = datetime.datetime.fromtimestamp(end_date / 1000).strftime('%Y-%m-%dT%H:%M:%SZ')
                note.append(f"    <b>end date:</b>        {utc_time}<br>")
            if has_attachments:
                note.append(f"    <b>has attachments:</b> {has_attachments}<br>")
            if message_subject:
                note.append(f"    <b>message subject:</b> {message_subject}<br>")
            if message_body:
                note.append(f"    <b>message body:</b>    {message_body}<br>")

            total_emails = 0
            email_note = []
            for email in email_results:
                num_emails_found = len(email.get('email_list'))
                if num_emails_found > 0:
                    email_note.append(f"    {email.get('email_address')}:  {num_emails_found}<br>")
                    total_emails = total_emails + num_emails_found

            # Add line with total emails found
            note.append(f"<br><b>Total messages matching search criteria:</b>  {total_emails}<br>")

            # Add one line for each mailbox in which a matching message was found and total matching messages.
            for line in email_note:
                note.append(line)

            # Add the query execution time
            note.append(f"<b>Query execution time:</b>  {query_time_ms/1000} seconds.")

            # Join all of the note lines together
            complete_note = ''.join(note)

            if "Incident note" in output_format:
                LOG.info('Writing query results to incident note.')
                create_incident_comment(self.rest_client(), incident_id, complete_note)
            if "Incident attachment" in output_format:
                LOG.info('Writing query results to attachment.')
                complete_note = complete_note.replace('<br>', '\n')
                complete_note = complete_note.replace('<b>', '')
                complete_note = complete_note.replace('</b>', '')
                create_incident_attachment(self.rest_client(), incident_id, complete_note, 'exo-query-results')

            return True

        except Exception as err:
            raise IntegrationError(err) from err
