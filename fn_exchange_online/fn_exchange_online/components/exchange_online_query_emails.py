# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import sys
from io import BytesIO
from datetime import datetime
import json
import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, RequestsCommon, ResultPayload, write_file_attachment, IntegrationError
from fn_exchange_online.lib.ms_graph_helper import MSGraphHelper, MAX_RETRIES_TOTAL, MAX_RETRIES_BACKOFF_FACTOR

CONFIG_DATA_SECTION = 'fn_exchange_online'
LOG = logging.getLogger(__name__)
TIME_FORMAT = '%Y-%m-%dT%H:%M:%S'

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
            validate_fields(['exo_email_address', 'exo_query_output'], kwargs)

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
            query_output = self.get_select_param(kwargs.get('exo_query_output'))  # select values: "Exchange Online data table", "Incident attachment", "Incident note"

            LOG.info(u"incident_id: %s", str(incident_id))
            LOG.info(u"exo_email_address: %s", email_address)
            LOG.info(u"exo_mailfolders: %s", mail_folders)
            LOG.info(u"exo_email_address_sender: %s", sender)
            LOG.info(u"exo_start_date: %s", start_date)
            LOG.info(u"exo_end_date: %s", end_date)
            LOG.info(u"exo_email_has_attachments: %s", has_attachments)
            LOG.info(u"exo_message_subject: %s", message_subject)
            LOG.info(u"exo_message_body: %s", message_body)
            LOG.info(u"exo_query_output: %s", query_output)

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
                                            RequestsCommon(self.opts, self.options).get_proxies())

            email_results = MS_graph_helper.query_messages(email_address, mail_folders, sender, start_date, end_date,
                                                           has_attachments, message_subject, message_body)

            query_results = {"exo_query_output_format": query_output,
                             "email_results": email_results}

            # Put query results in the results payload.
            results = rp.done(True, query_results)

            # Write the requests to attachment or note if the user requests it.
            if "Incident attachment" in query_output or "Incident note" in query_output:

                note = u"Message Query Criteria:\n\n"
                note = u"{0}    email address:   {1}\n".format(note, email_address)
                note = u"{0}    mail folder:     {1}\n".format(note, mail_folders)
                note = u"{0}    email sender:    {1}\n".format(note, sender)
                note = u"{0}    start date:      {1}\n".format(note, start_date)
                note = u"{0}    end date:        {1}\n".format(note, end_date)
                note = u"{0}    has attachments: {1}\n".format(note, has_attachments)
                note = u"{0}    message subject: {1}\n".format(note, message_subject)
                note = u"{0}    message body:    {1}\n\nResults:\n\n".format(note, message_body)

                total_emails = 0
                email_note = u""
                for email in email_results:
                    num_emails_found = len(email.get('email_list'))
                    email_note = u"{0} {1} {2} matching messages found.\n".format(email_note, email.get('email_address'),
                                                                               num_emails_found)
                    total_emails = total_emails + num_emails_found

                note = "{0}Total messages matching search criteria: {1}\n\n{2}".format(note, total_emails, email_note)

                if "Incident attachment" in query_output:
                    self.create_incident_attachment(incident_id, note)
                if "Incident note" in query_output:
                    note = note.replace('\n', '<br>')
                    self.create_incident_comment(incident_id, note)

            yield StatusMessage(u"Returning results from query.")

            LOG.debug(json.dumps(results['content']))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

        except Exception as err:
            LOG.error(err)
            yield FunctionError(err)

    def create_incident_attachment(self, incident_id, note):
        """
        Add an attachment to the specified Resilient Incident by ID
        :param incident_id:  Resilient Incident ID
        :param note: Content to be added as attachment
        :return: Response from Resilient for debug
        """
        try:
            dt = datetime.now()
            attachment_name = "exo-query-output-{0}.txt".format(dt.strftime(TIME_FORMAT))
            if sys.version_info.major < 3:
                datastream = BytesIO(note)
            else:
                datastream = BytesIO(note.encode("utf-8"))
            rest_client = self.rest_client()
            attachment = write_file_attachment(rest_client, attachment_name, datastream, incident_id, None)
            return attachment

        except Exception as err:
            raise IntegrationError(err)

    def create_incident_comment(self, incident_id, note):
        """
        Add a comment to the specified Resilient Incident by ID
        :param incident_id:  Resilient Incident ID
        :param note: Content to be added as note
        :return: Response from Resilient for debug
        """
        try:
            uri = '/incidents/{}/comments'.format(incident_id)
            rest_client = self.rest_client()
            note_json = {
                'format': 'html',
                'content': note
            }
            payload = {'text': note_json}
            comment_response = rest_client.post(uri=uri, payload=payload)
            return comment_response

        except Exception as err:
            raise IntegrationError(err)
