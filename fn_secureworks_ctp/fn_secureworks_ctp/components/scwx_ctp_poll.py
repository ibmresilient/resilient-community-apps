# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

"""Function implementation"""

import os
from cachetools import cached, LFUCache
import logging
from circuits import Event, Timer, task
from pkg_resources import Requirement, resource_filename
from resilient import SimpleHTTPException
from resilient_circuits import ResilientComponent, handler
from resilient_circuits.template_functions import render_json, environment
from resilient_lib import validate_fields
from fn_secureworks_ctp.lib.scwx_ctp_client import SCWXClient


CONFIG_DATA_SECTION = "fn_secureworks_ctp"
SCWX_CTP_POLL_CHANNEL = "scwx_ctp_poll"
TICKET_ID_FIELDNAME = "scwx_ctp_ticket_id"
DEFAULT_POLL_SECONDS=600
LOG = logging.getLogger(__name__)

class Poll(Event):
    """A Circuits event to trigger polling"""
    channels = (SCWX_CTP_POLL_CHANNEL,)

class PollCompleted(Event):
    """A Circuits event to notify that this poll event is completed"""
    channels = (SCWX_CTP_POLL_CHANNEL,)

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
        required_fields = ["base_url", "username", "password", "query_limit", "query_ticket_types",
                           "query_grouping_types", "polling_interval"]
        validate_fields(required_fields, self.options)

        self.polling_interval = int(self.options.get("polling_interval", DEFAULT_POLL_SECONDS))

        # Create Secureworks client
        self.scwx_client = SCWXClient(self.opts, self.options)

    def _escalate(self):
        """ Search for Secureworks CTP tickets and create incidents in Resilient for them
        :return:
        """
        LOG.info(u"Secureworks CTP escalate.")
        try:
            # Get list of tickets needing updating
            response = self.scwx_client.post_tickets_updates()

            tickets = response.get('tickets')

            for ticket in tickets:
                # Acknowledge Secureworks that we have received the tickets.
                response_ack = self.scwx_client.post_tickets_acknowledge(ticket)

                if response_ack.get('code') is not "SUCCESS":
                    LOG.info(u"Secureworks CTP could not acknowledge ticket: %s code: %s", ticket_id, code)
                    continue

                ticket_id = response_ack.get('ticketId')
                LOG.info(u"Secureworks CTP ticket acknowledged: %s.", ticket_id)

                # Check if there is already a Resilient incident for this Secureworks ticket.
                resilient_incident = self._find_resilient_incident_for_req(ticket_id)
                if not resilient_incident:
                    # Create a new incident for this Secureworks CTP ticket.
                    resilient_incident = self._create_incident(ticket)

                # Add worklogs here

        except Exception as err:
            raise err
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
        if len(r_incidents) > 0:
            return r_incidents[0]
        return None

    def _create_incident(self, ticket):
        """
        :param ticket: Secureworks CTP ticket (json object)
        :return:
        """
        ticket_id = ticket.get('ticketId')
        LOG.info(u"Processing Secureworks CTP ticket %s", ticket_id)
        try:
            # Create a new Resilient incident from this ticket
            # using a JSON (JINJA2) template file
            template_file_path = self.options.get('template_file')
            if template_file_path and not os.path.exists(template_file_path):
                LOG.warn(u"Template file '%s' not found.", template_file_path)
                template_file_path = None
            if not template_file_path:
                # Use the template file installed by this package
                template_file_path = resource_filename(Requirement("fn-secureworks-ctp"),
                                                       "fn_secureworks_ctp/data/scwx_ctp_template.jinja")
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
            raise err

