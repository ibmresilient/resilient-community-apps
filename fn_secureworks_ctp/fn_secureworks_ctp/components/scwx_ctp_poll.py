# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

"""Function implementation"""

import os
from io import BytesIO
import datetime
import logging
import resilient
from circuits import Event, Timer
from pkg_resources import Requirement, resource_filename
from resilient import SimpleHTTPException
from resilient_circuits import ResilientComponent, handler
from resilient_circuits.template_functions import render_json, environment
from resilient_lib import validate_fields, write_file_attachment, IntegrationError
from fn_secureworks_ctp.lib.scwx_ctp_client import SCWXClient


CONFIG_DATA_SECTION = "fn_secureworks_ctp"
SCWX_CTP_POLL_CHANNEL = "scwx_ctp_poll"
TICKET_ID_FIELDNAME = "scwx_ctp_ticket_id"
DEFAULT_POLL_SECONDS = 600
LOG = logging.getLogger(__name__)

class Poll(Event):
    """A Circuits event to trigger polling"""
    channels = (SCWX_CTP_POLL_CHANNEL,)

class PollCompleted(Event):
    """A Circuits event to notify that this poll event is completed"""
    channels = (SCWX_CTP_POLL_CHANNEL,)

def readable_datetime(val):
    """ JINJA filter to convert ms to mm/dd/YYYY:H:M:S """
    dt = datetime.datetime.fromtimestamp(val / 1000.0)
    return dt.strftime("%m/%d/%Y %H:%M:%S")

class SecureworksCTPPollComponent(ResilientComponent):
    """
    Event-driven polling for Secureworks CTP tickets
    """

    # This doesn't listen to Action Module, only its internal channel for timer events
    # But we still inherit from ResilientComponent so we get a REST client etc
    channel = SCWX_CTP_POLL_CHANNEL

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(SecureworksCTPPollComponent, self).__init__(opts)

        self._load_options(opts)

        if not self.polling_interval:
            LOG.info(u"Secureworks CTP escalation interval is not configured.  Automated escalation is disabled.")
            return

        # Add the timestamp-parse function to the global JINJA environment
        env = environment()
        env.globals.update({"readable_datetime": readable_datetime})
        env.filters.update({"readable_datetime": readable_datetime})

        # If close_codes are defined in the app.config, then load them into the select input list.
        if self.close_codes:
            response = self.init_close_codes(self.close_codes)

        LOG.info(u"Secureworks CTP escalation initiated, polling interval %s", self.polling_interval)
        Timer(self.polling_interval, Poll(), persist=False).register(self)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self._load_options(opts)

    @handler("Poll")
    def _poll(self, event):
        """Handle the timer"""
        LOG.info(u"Secureworks CTP start polling.")
        self._escalate()

    @handler("PollCompleted")
    def _poll_completed(self, event):
        """Set up the next timer"""
        LOG.info(u"Secureworks CTP poll complete.")
        Timer(self.polling_interval, Poll(), persist=False).register(self)

    def _load_options(self, opts):
        """Read options from config"""
        self.opts = opts
        self.options = opts.get(CONFIG_DATA_SECTION, {})

        # Validate required fields in app.config are set
        required_fields = ["base_url", "username", "password", "query_limit", "query_ticket_grouping_types",
                           "assigned_to_customer", "polling_interval"]
        validate_fields(required_fields, self.options)

        self.polling_interval = int(self.options.get("polling_interval", DEFAULT_POLL_SECONDS))

        # If close_codes are defined in the app.config, then turn them into a list of string
        close_codes = self.options.get("close_codes", None)
        if close_codes:
            self.close_codes = [code.strip() for code in close_codes.split(',')]
        else:
            self.close_codes = None

        # Create Secureworks client
        self.scwx_client = SCWXClient(self.opts, self.options)

    def _escalate(self):
        """ Search for Secureworks CTP tickets and create incidents in Resilient for them
        :return:
        """
        LOG.info(u"Secureworks CTP escalate.")
        try:
            # Call Secureworks endpoint for each ticketType groupingType combination the user has
            # specified in the app.config
            for query in self.scwx_client.query_types:

                # Get list of tickets needing updating
                ticket_type = query.get('ticketType')
                grouping_type = query.get('groupingType')
                #response = self.scwx_client.post_tickets_updates(ticket_type, grouping_type)
                response = self.scwx_client.mock_post_tickets_updates()

                tickets = response.get('tickets')
                ticket_id_list = [ticket.get('ticketId') for ticket in tickets]
                message = u"Secureworks CTP tickets to be processed this poll:\nticketType: {0} groupingType: {1}".format(ticket_type, grouping_type)
                LOG.info(message)
                LOG.info(u"%s", ticket_id_list)

                for ticket in tickets:

                    ticket_id = ticket.get('ticketId')
                    status = ticket.get('status')

                    LOG.info(u"Processing ticket: %s status: %s", ticket_id, status)

                    # Check if there is already a Resilient incident for this Secureworks ticket.
                    resilient_incident = self._find_resilient_incident_for_req(ticket_id)

                    if status in ('Closed', 'Resolved'):
                        # Ticket was closed in Secureworks, so closed the Resilient incident now.
                        if resilient_incident:
                            result = self._close_incident(resilient_incident, ticket_id, status)
                    else:
                        if not resilient_incident:
                            # Create a new incident for this Secureworks CTP ticket.
                            resilient_incident = self._create_incident(ticket)

                        # Add ticket worklogs to the incident as notes
                        self.add_worklog_notes(resilient_incident, ticket)

                        # Add ticket attachments to the incident as attachments
                        self.add_ticket_attachments(resilient_incident, ticket)

                    # Acknowledge Secureworks that we have received and processed the ticket.
                    #response_ack = self.scwx_client.post_tickets_acknowledge(ticket)
                    response_ack = [{'code': "SUCCESS", 'ticketId': ticket.get('ticketId')}]

                    code = response_ack[0].get('code')
                    if code != "SUCCESS":
                        LOG.warning(u"Secureworks CTP could NOT acknowledge ticket: %s code: %s", ticket_id, code)
                    else:
                        LOG.info(u"Secureworks CTP acknowledged ticket: %s code: %s", ticket_id, code)

        except Exception as err:
            raise IntegrationError(err)
        finally:
            # We always want to reset the timer to wake up, no matter failure or success
            self.fire(PollCompleted())

    def _find_resilient_incident_for_req(self, ticket_id):
        """
         Query resilient for to see if an incident has already been created for the Secureworks ticket.
         """
        r_incidents = []
        query_uri = "/incidents/query?return_level=partial"
        query = {
            'filters': [{
                'conditions': [
                    {
                        'field_name': 'properties.{}'.format(TICKET_ID_FIELDNAME),
                        'method': 'equals',
                        'value': ticket_id
                    },
                    {
                        'field_name': 'plan_status',
                        'method': 'equals',
                        'value': 'A'
                    }
                ]
            }],
            "sorts": [{
                "field_name": "create_date",
                "type": "desc"
            }]
        }
        try:
            r_incidents = self.rest_client().post(query_uri, query)
        except SimpleHTTPException:
            # Some versions of Resilient 30.2 onward have a bug that prevents query for numeric fields.
            # To work around this issue, let's try a different query, and filter the results. (Expensive!)
            query_uri = u"/incidents/query?return_level=normal&field_handle={}".format(TICKET_ID_FIELDNAME)
            query = {
                'filters': [{
                    'conditions': [
                        {
                            'field_name': 'properties.{}'.format(TICKET_ID_FIELDNAME),
                            'method': 'has_a_value'
                        },
                        {
                            'field_name': 'plan_status',
                            'method': 'equals',
                            'value': 'A'
                        }
                    ]
                }]
            }
            LOG.debug(query)
            r_incidents_tmp = self.rest_client().post(query_uri, query)
            r_incidents = [r_inc for r_inc in r_incidents_tmp
                           if r_inc["properties"].get(TICKET_ID_FIELDNAME) == ticket_id]
        if r_incidents:
            return r_incidents[0]
        return None

    def _create_incident(self, ticket):
        """
        Create a new Resilient incident by rendering a jinja2 template
        :param ticket: Secureworks CTP ticket (json object)
        :return: Resilient incident
        """
        ticket_id = ticket.get('ticketId')
        try:
            # Create a new Resilient incident from this ticket
            # using a JSON (JINJA2) template file
            template_file_path = self.options.get('template_file_escalate')
            if template_file_path and not os.path.exists(template_file_path):
                LOG.warning(u"Template file '%s' not found.", template_file_path)
                template_file_path = None
            if not template_file_path:
                # Use the template file installed by this package
                template_file_path = resource_filename(Requirement("fn-secureworks-ctp"),
                                                       "fn_secureworks_ctp/data/scwx_ctp_template_escalate.jinja")
                if not os.path.exists(template_file_path):
                    raise Exception(u"Template file '{}' not found".format(template_file_path))

            LOG.info(u"Secureworks CTP Template file: %s", template_file_path)
            with open(template_file_path, "r") as definition:
                escalate_template = definition.read()

            # Render the template.
            new_incident_payload = render_json(escalate_template, ticket)
            LOG.debug(new_incident_payload)

            # Post incident to Resilient
            incident = self.rest_client().post("/incidents", new_incident_payload)
            incident_id = incident.get('id')
            message = u"Created incident {} for Secureworks CTP ticket {}".format(incident_id, ticket_id)
            LOG.info(message)
            return incident

        except Exception as err:
            raise IntegrationError(err)

    def _close_incident(self, incident, ticket_id, status):
        """
        Create a new Resilient incident by rendering a jinja2 template
        :param ticket: Secureworks CTP ticket (json object)
        :return: Resilient incident
        """

        try:
            # Create a new Resilient incident from this ticket
            # using a JSON (JINJA2) template file
            template_file_path = self.options.get('template_file_close')
            if template_file_path and not os.path.exists(template_file_path):
                LOG.warning(u"Template file '%s' not found.", template_file_path)
                template_file_path = None
            if not template_file_path:
                # Use the template file installed by this package
                template_file_path = resource_filename(Requirement("fn-secureworks-ctp"),
                                                       "fn_secureworks_ctp/data/scwx_ctp_template_close.jinja")
                if not os.path.exists(template_file_path):
                    raise Exception(u"Template file for close'{}' not found".format(template_file_path))

            LOG.info(u"Secureworks CTP Template Close file: %s", template_file_path)
            with open(template_file_path, "r") as definition:
                close_template = definition.read()

            incident_payload = render_json(close_template, incident)
            # Set the scwx_ctp_status incident field to the ticket status (Closed or Resolved) so that the
            # automatic rule to close the Securework ticket is not triggered as the ticket is already closed in SCWX.
            incident_payload['properties']['scwx_ctp_status'] = status

            # Render the template.
            incident_id = incident.get('id')

            result = self._update_incident(incident_id, incident_payload)

            if result and result.get('success'):
                message = u"Closed incident {} for Secureworks CTP ticket {}".format(incident_id, ticket_id)
                LOG.info(message)
            else:
                message = u"Unable to update incident {} for closing. Secureworks CTP ticket {}".format(incident_id, ticket_id)
                LOG.error(message)
            return result

        except Exception as err:
            raise IntegrationError(err)

    def _update_incident(self, incident_id, incident_payload):
        """ _update incident will
        :param incident_id: incident ID of incident to be updated.
        ;param incident_payload: incident fields to be updated.
        :return:
        """
        try:
            # Update incident
            incident_url = "/incidents/{0}".format(incident_id)
            incident = self.rest_client().get(incident_url)
            patch = resilient.Patch(incident)

            # Iterate over payload dict.
            for name, value in incident_payload.items():
                if name == 'properties':
                    for field_name, field_value in incident_payload['properties'].items():
                        patch.add_value(field_name, field_value)
                else:
                    payload_value = incident_payload.get(name)
                    patch.add_value(name, payload_value)

            patch_result = self.rest_client().patch(incident_url, patch)
            result = self._chk_status(patch_result)
            return result if result else {}

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
            resilient_client = self.rest_client()
            note_json = {
                'format': 'html',
                'content': note
            }
            payload = {'text': note_json}
            comment_response = resilient_client.post(uri=uri, payload=payload)
            return comment_response

        except SimpleHTTPException as ex:
            LOG.error("Failed to add note for incident %d: %s", incident_id, ex)


    def add_worklog_notes(self, incident, ticket):
        """
        For each worklog of a Secureworks CTP ticket, post a note in the corresponding Resilient incident
        :param incident: Resilient incident
        :param ticket: Secureworks ticket
        :return:
        """
        try:
            worklogs = ticket.get('worklogs')
            incident_id = incident.get('id')
            # Loop through the list of worklogs  for the ticket and add a Resilient incident.
            for worklog in worklogs:
                # Build the note string
                note = u"<b>Secureworks CTP Worklog:</b><br>"
                date = worklog.get('dateCreated')
                description = worklog.get('description')
                worklog_type = worklog.get('type')
                created_by = worklog.get('createdBy')
                if created_by:
                    note = u"{}    <b>Created by:</b> {}<br>".format(note, created_by)
                if date:
                    created = readable_datetime(date)
                    note = u"{}    <b>Date Created:</b> {}<br>".format(note, created)
                if worklog_type:
                    note = u"{}    <b>Type:</b> {}<br>".format(note, worklog_type)
                if description:
                    description = description.replace("\n", "<br>")
                    note = u"{}    <b>Description:</b><br> {}".format(note, description)

                LOG.info(u"Writing note to incident %d: %s", incident_id, note)
                response = self.create_incident_comment(incident_id, note)

                LOG.debug(response)
        except Exception as err:
            raise IntegrationError(err)

    def add_ticket_attachments(self, incident, ticket):
        """
        Add the list of Secureworks ticket attachments to the Resilient incident
        :param incident: Resilient incident
        :param ticket:  Secureworks ticket
        :return:
        """
        try:
            attachment_info_list = ticket.get('attachmentInfo')
            incident_id = incident.get('id')
            ticket_id = ticket.get('ticketId')
            for attachment in attachment_info_list:
                attachment_id = attachment.get('id')

                # Get ticket attachment
                #response = self.scwx_client.get_tickets_attachment(ticket_id, attachment_id)
                response = {'content': b'Mock text'}

                content = response.get('content')
                datastream = BytesIO(content)
                attachment_name = attachment.get('name')
                if not attachment_name:
                    attachment_name = u"TicketId-{0}-AttachmentID-{1}".format(ticket_id, attachment_id)

                # Write the file as attachement: failures will raise an exception
                message = u"Writing {0} for Secureworks CTP ticket {1} to Resilient incident {2}".format(attachment_name,
                                                                                                         ticket_id,
                                                                                                         incident_id)
                LOG.info(message)
                new_attachment = write_file_attachment(self.rest_client(), attachment_name, datastream,
                                                       incident_id, None)
                LOG.debug(new_attachment)
        except Exception as err:
            raise IntegrationError(err)

    def init_close_codes(self, close_codes):
        """
        init_close_codes takes a list of string close-codes for Secureworks CTP and places them in the
        select (swcx_ctp_close_code custom incident field) input type.  There are default codes defined in
        the Resilient UI but users can override the select list via app.config 'close_codes' parameter.
        The close codes are similar to Resilient resolution_id. The select list will appear in the
        Resilient Close Incident popup when the user closes an incident.
        :param close_codes: list of strings (each string will be an entry in the select list) which will appear
        in the Resilient Close Incident popup
        :return: response from the 'put' operation
        """
        # Get the current close_code select list.
        uri = '/types/incident/fields/scwx_ctp_close_code'
        get_response = self.rest_client().get(uri)
        values = []

        # Add each close_code as a select list entry.
        for code in close_codes:
            entry = {'label': code,
                     'enabled': True,
                     'hidden': False}
            values.append(entry)

        # Put the new values into the select list to replace the currently values there.
        get_response['values'] = values
        put_response = self.rest_client().put(uri, payload=get_response)

        return put_response

    def _chk_status(self, resp, rc=200):
        """
        check the return status. If return code is not met, raise IntegrationError,
        if success, return the json payload
        :param resp:
        :param rc:
        :return:
        """
        if hasattr(resp, "status_code"):
            if isinstance(rc, list):
                if resp.status_code < rc[0] or resp.status_code > rc[1]:
                    raise IntegrationError("status code failure: {}".format(resp.status_code))
            elif resp.status_code != rc:
                raise IntegrationError("status code failure: {}".format(resp.status_code))

            return resp.json()
        else:
            return {}
