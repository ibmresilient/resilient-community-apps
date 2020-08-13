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
            response = self._init_close_codes(self.close_codes)

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
                           "polling_interval"]
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
                response = self.scwx_client.post_tickets_updates(ticket_type, grouping_type)

                tickets = response.get('tickets')
                ticket_id_list = [ticket.get('ticketId') for ticket in tickets]
                message = u"Secureworks CTP tickets to be processed this poll:\nticketType: {0} groupingType: {1}".format(ticket_type, grouping_type)
                LOG.info(message)
                LOG.info(u"ticket list: %s", ticket_id_list)

                for ticket in tickets:
                    code = self.process_ticket(ticket)

        except Exception as err:
            raise IntegrationError(err)
        finally:
            # We always want to reset the timer to wake up, no matter failure or success
            self.fire(PollCompleted())

    def process_ticket(self, ticket):
        """
        process_ticket process a Secureworks ticket and create a Resilient incident if one does not already exist.
        Add new worklogs and attachments if any and close a ticket if the status is Closed or Resolved.
        :param ticket:
        :return:
        """
        code = "NOT SUCCESS"
        incident_created = False
        try:
            ticket_id = ticket.get('ticketId')
            status = ticket.get('status')

            LOG.info(u"Processing ticket: %s status: %s", ticket_id, status)

            # Check if there is already a Resilient incident for this Secureworks ticket.
            resilient_incident = self._find_resilient_incident_for_req(ticket_id)

            if not resilient_incident and status not in ('Closed', 'Resolved'):
                # Create a new incident for this Secureworks CTP ticket.
                resilient_incident = self._create_incident(ticket)
                incident_created = True

            if not resilient_incident:
                LOG.info(u"No Resilient incident for Secureworks Ticket: %s, status: %s", ticket_id, status)

                # Acknowledge Secureworks that we have received and processed the ticket.
                code = self.scwx_client.post_tickets_acknowledge(ticket)
            else:

                # Add ticket worklogs to the incident as notes
                self._add_worklog_notes(resilient_incident, ticket)

                # Add ticket attachments to the incident as attachments
                self._add_ticket_attachments(resilient_incident, ticket)

                # Update custom fields, but only if incident was not just created (to reduce API calls).
                if not incident_created:
                    self._update_custom_fields(resilient_incident, ticket)

                # Acknowledge Secureworks that we have received and processed the ticket.
                # The ticket must be acknowledged before call POST to close the ticket.
                code = self.scwx_client.post_tickets_acknowledge(ticket)

                if status in ('Closed', 'Resolved'):
                    # Ticket was closed in Secureworks, so close the Resilient incident now.
                    LOG.info(u"Secureworks ticket %s is %s: Closing incident %s.", ticket_id, status,
                             resilient_incident)
                    result = self._close_incident(resilient_incident, ticket)

        except Exception as err:
            LOG.error(err)

        return code

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
                        'field_name': 'properties.{0}'.format(TICKET_ID_FIELDNAME),
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
            query_uri = u"/incidents/query?return_level=normal&field_handle={0}".format(TICKET_ID_FIELDNAME)
            query = {
                'filters': [{
                    'conditions': [
                        {
                            'field_name': 'properties.{0}'.format(TICKET_ID_FIELDNAME),
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
                    raise Exception(u"Template file '{0}' not found".format(template_file_path))

            LOG.info(u"Secureworks CTP Template file: %s", template_file_path)
            with open(template_file_path, "r") as definition:
                escalate_template = definition.read()

            # Render the template.
            new_incident_payload = render_json(escalate_template, ticket)

            # The detailedDescription field from Secureworks may be a very long escaped string,
            # which can present problems with jinja template rendering and creating a validate
            # json payload. Instead of rendering the detailedDescription field to the Resilient
            # desription field, put it in the payload now if it's not already there.
            if "description" not in new_incident_payload:
                new_incident_payload = self._add_description_to_payload(new_incident_payload, ticket)

            LOG.debug(new_incident_payload)

            # Post incident to Resilient
            incident = self.rest_client().post("/incidents", new_incident_payload)
            incident_id = incident.get('id')
            message = u"Created incident {0} for Secureworks CTP ticket {1}".format(incident_id, ticket_id)
            LOG.info(message)
            return incident

        except Exception as err:
            raise IntegrationError(err)

    def _add_description_to_payload(self, payload, ticket):
        """
        Add the Resilient "description" field to the create incident payload using the Secureworks ticket
        field: detailedDescription
        :param payload: create incident payload to add the "description" to
        :param ticket:  Secureworks ticket containing detailedDescription field
        :return: payload updated with the description field
        """
        try:
            detailed_description = ticket.get('detailedDescription')
            if detailed_description:
                html_description = "<div><p>{0}</p></div>".format(detailed_description)
            else:
                html_description = "<div><p>No detailedDescription</p></div>"
            html_description = html_description.replace('\n', '<br>').replace('\\n', '<br>')
            description_json = {"format": "html",
                                "content": html_description}
            payload["description"] = description_json
            return payload
        except Exception as err:
            raise IntegrationError(err)

    def _close_incident(self, incident, ticket):
        """
        Close a Resilient incident by rendering a jinja2 template
        :param ticket: Secureworks CTP ticket (json object)
        :return: Resilient incident
        """

        try:
            # Close a Resilient incident from this ticket
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
                    raise Exception(u"Template file for close'{0}' not found".format(template_file_path))

            LOG.info(u"Secureworks CTP jinja template file for closing incident: %s", template_file_path)
            with open(template_file_path, "r") as definition:
                close_template = definition.read()

            incident_payload = render_json(close_template, ticket)
            # Set the scwx_ctp_status incident field to the ticket status (Closed or Resolved) so that the
            # automatic rule to close the Securework ticket is not triggered as the ticket is already closed in SCWX.
            incident_payload['properties']['scwx_ctp_status'] = ticket.get("status")

            # Render the template.
            incident_id = incident.get('id')
            result = self._update_incident(incident_id, incident_payload)
            LOG.debug(incident_payload)

            ticket_id = ticket.get('ticketId')
            if result and result.get('success'):
                message = u"Closed incident {0} for Secureworks CTP ticket {1}".format(incident_id, ticket_id)
                LOG.info(message)
            else:
                message = u"Unable to update incident {0} for closing. Secureworks CTP ticket {1}".format(incident_id,
                                                                                                          ticket_id)
                LOG.error(message)
            return result

        except Exception as err:
            raise IntegrationError(err)

    def _update_custom_fields(self, incident, ticket):
        """
        Update a Resilient incident by rendering a jinja2 template
        :param ticket: Secureworks CTP ticket (json object)
        :return: Resilient incident
        """

        try:
            # Update Resilient custom incident fields from this ticket
            # using a JSON (JINJA2) template file
            template_file_path = self.options.get('template_file_update')
            if template_file_path and not os.path.exists(template_file_path):
                LOG.warning(u"Template file '%s' not found.", template_file_path)
                template_file_path = None
            if not template_file_path:
                # Use the template file installed by this package
                template_file_path = resource_filename(Requirement("fn-secureworks-ctp"),
                                                       "fn_secureworks_ctp/data/scwx_ctp_template_update.jinja")
                if not os.path.exists(template_file_path):
                    raise Exception(u"Template file for updating incident'{0}' not found".format(template_file_path))

            LOG.info(u"Secureworks CTP jinja template file for updating incident: %s", template_file_path)
            with open(template_file_path, "r") as definition:
                update_template = definition.read()

            incident_payload = render_json(update_template, ticket)

            # Render the template.
            incident_id = incident.get('id')
            result = self._update_incident(incident_id, incident_payload)
            LOG.debug(incident_payload)

            ticket_id = ticket.get('ticketId')
            if result and result.get('success'):
                message = u"Updated incident {0} for Secureworks CTP ticket {1}".format(incident_id, ticket_id)
                LOG.info(message)
            else:
                message = u"Unable to update incident {0} for Secureworks CTP ticket {1}".format(incident_id, ticket_id)
                LOG.error(message)
            return result

        except Exception as err:
            raise IntegrationError(err)

    def _update_incident(self, incident_id, incident_payload):
        """ _update_incident will update an incident with the specified json payload.
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

    def _create_incident_comment(self, incident_id, note):
        """
        Add a comment to the specified Resilient Incident by ID
        :param incident_id:  Resilient Incident ID
        :param note: Content to be added as note
        :return: Response from Resilient for debug
        """
        try:
            uri = u'/incidents/{0}/comments'.format(incident_id)
            resilient_client = self.rest_client()
            note_json = {
                'format': 'html',
                'content': note
            }
            payload = {'text': note_json}
            comment_response = resilient_client.post(uri=uri, payload=payload)
            return comment_response

        except Exception as err:
            raise IntegrationError(err)

    def _get_field_from_note(self, note, field):
        """
        Given note text string, get the Secureworksl worklog field from the note.
        :param note: text string containing Secureworks worklog that is a note in Resilient
        :param field: Secureworks worklog field that is contained in the note:
        "Type:" , "Date Created:", "Secureworks CTP Worklog:"
        :return: return the string field or None if not found
        """

        if field in note:
            split_note = note.split(field)
            res_field_temp = split_note[1].lstrip(" </b>")
            if res_field_temp:
                res_field = res_field_temp.split("<br />")
                if res_field:
                    return res_field[0]
        return None

    def _find_note_in_incident(self, incident_id, worklog_timestamp, worklog_type):
        """
        Get the notes of the incident and determine if the note is already contained in the incident by
        comparing the worklog "dateCreated" timestamp to the timestamp stored in the first line of the
        Resilient note.  Also compare the worklog type to the type stored in the note.
        :param incident_id: id of the incident to be searched
        :param worklog_timestamp: worklog "dateCreated" timestamp that appears in the first line of the
        corresponding Resilient note.
        :param worklog_type: worklog "type" that is a field of the Secureworks worklog and tappears in
        the second line of the Resilient note.
        :return: return True if the note is already contained in the incident and False if it is not.
        """
        try:
            uri = u'/incidents/{0}/comments'.format(incident_id)
            res_notes = self.rest_client().get(uri)

            # Loop through the notes of the incident to see if note is already in the incident by comparing
            # the timestamp stored in the first line of the Resilient note to the "dateCreated" field of
            # the worklog.  If the 2 timestamps match, the worklogs are probably the same.
            for note in res_notes:
                res_note_text = note.get('text')

                # Only consider the Securworks worklog notes: get the createdDate timestamp and worklog type
                # to compare and determine if this note is already in Resilient.
                res_timestamp_string = self._get_field_from_note(res_note_text, "Secureworks CTP Worklog:")
                res_note_type = self._get_field_from_note(res_note_text, "Type:")
                if res_timestamp_string and res_note_type:
                    res_timestamp = int(res_timestamp_string)
                    if res_timestamp == worklog_timestamp:
                        if res_note_type == worklog_type:
                            return True
            return False
        except Exception as err:
            raise IntegrationError(err)

    def _add_worklog_notes(self, incident, ticket):
        """
        For each worklog of a Secureworks CTP ticket, post a note in the corresponding Resilient incident.
        Only post the worklog note if it has not been posted already.  Check the "dateCreated" timestamp
        of the worklog and compare to the timestamp stored in the first line of the resilient note to
        determine of the worklog is already in Resilient.  Seems like Secureworks should only send worklogs
        that are updated and not ALL as it does.  There is a conflict with calling worklogs=UPDATED as
        newly created tickets will not be sent to Resilient if we use this parameter.
        :param incident: Resilient incident
        :param ticket: Secureworks ticket
        :return:
        """
        try:
            incident_id = incident.get('id')

            # Get worklogs list and reverse the order so that older notes are added first.
            worklogs = ticket.get('worklogs')
            worklogs.reverse()

            # Loop through the list of worklogs for the ticket and add a Resilient incident note.
            for worklog in worklogs:
                date_timestamp = worklog.get('dateCreated')
                worklog_type = worklog.get('type')
                # Determine if the note for this worklog is already in Resilent.
                found = self._find_note_in_incident(incident_id, date_timestamp, worklog_type)
                if found:
                    continue

                # Continue on to build the note string and post to Resilient
                description = worklog.get('description')
                worklog_type = worklog.get('type')
                created_by = worklog.get('createdBy')
                note = u"<b>Secureworks CTP Worklog:</b> {0}<br />".format(date_timestamp)
                if worklog_type:
                    note = u"{0}    <b>Type:</b> {1}<br />".format(note, worklog_type)
                if date_timestamp:
                    created = readable_datetime(date_timestamp)
                    note = u"{0}    <b>Date Created:</b> {1}<br />".format(note, created)
                if created_by:
                    note = u"{0}    <b>Created by:</b> {1}<br />".format(note, created_by)
                if description:
                    description = description.replace("\n", "<br />")
                    note = u"{0}    <b>Description:</b><br /> {1}".format(note, description)

                LOG.info(u"Writing note to incident %d: %s", incident_id, note)
                response = self._create_incident_comment(incident_id, note)
                LOG.debug(response)

        except Exception as err:
            raise IntegrationError(err)

    def _add_ticket_attachments(self, incident, ticket):
        """
        Add the list of Secureworks ticket attachments to the Resilient incident.  Only add attachments that
        are not already in Resilient.  To make sure this is the case, add the Secureworks attachmentInfo id
        to the attachment name in Resilient and then check whether this attachment name is already in Resilient.
        :param incident: Resilient incident
        :param ticket:  Secureworks ticket
        :return:
        """
        try:
            attachment_info_list = ticket.get('attachmentInfo')
            incident_id = incident.get('id')
            ticket_id = ticket.get('ticketId')

            # Get the list of attachments in this incident.
            uri = u'/incidents/{0}/attachments'.format(incident_id)
            res_attachments = self.rest_client().get(uri)

            for attachment in attachment_info_list:
                attachment_id = attachment.get('id')

                # Get ticket attachment and name
                response = self.scwx_client.get_tickets_attachment(ticket_id, attachment_id)
                attachment_name = attachment.get('name')

                # Use the Secureworks attachmentInfo id in the name to uniquely identify it.
                if not attachment_name:
                    res_attachment_name = u"attachmentInfo-id-{0}".format(attachment_id)
                else:
                    res_attachment_name = u"{0}-attachmentInfo-id-{1}".format(attachment_name, attachment_id)

                attachment_in_incident = False
                for r_attachment in res_attachments:
                    if r_attachment.get("name") == res_attachment_name:
                        attachment_in_incident = True

                if attachment_in_incident:
                    # Don't create attachment as it is already in Resilient
                    continue

                content = response.get('content')
                datastream = BytesIO(content)
                # Write the file as attachement: failures will raise an exception
                message = u"Writing {0} for Secureworks CTP ticket {1} to Resilient incident {2}".format(attachment_name,
                                                                                                         ticket_id,
                                                                                                         incident_id)
                LOG.info(message)
                new_attachment = write_file_attachment(self.rest_client(), res_attachment_name, datastream,
                                                       incident_id, None)
                LOG.debug(new_attachment)
        except Exception as err:
            raise IntegrationError(err)

    def _init_close_codes(self, close_codes):
        """
        _init_close_codes takes a list of string close-codes for Secureworks CTP and places them in the
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
                    raise IntegrationError(u"status code failure: {0}".format(resp.status_code))
            elif resp.status_code != rc:
                raise IntegrationError(u"status code failure: {0}".format(resp.status_code))

            return resp.json()

        return {}
