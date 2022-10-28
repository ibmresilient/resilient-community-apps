# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""Function implementation"""

import datetime
import logging
from circuits import Event, Timer
from resilient_circuits import ResilientComponent, handler
from resilient_lib import validate_fields, build_incident_url, build_resilient_url, IntegrationError
from fn_sentinelone.lib.jinja_common import JinjaEnvironment
from fn_sentinelone.lib.resilient_common import ResilientCommon
from fn_sentinelone.lib.sentinelone_common import SentinelOneClient

PACKAGE_NAME = "fn_sentinelone"

DEFAULT_INCIDENT_CREATION_TEMPLATE = "data/incident_creation_template.jinja"
DEFAULT_INCIDENT_UPDATE_TEMPLATE = "data/incident_update_template.jinja"
DEFAULT_INCIDENT_CLOSE_TEMPLATE = "data/incident_close_template.jinja"

POLLER_CHANNEL = "sentinelone_poller"

DEFAULT_POLLER_LOOKBACK_MINUTES = 120
DEFAULT_POLLER_SECONDS = 600
LOG = logging.getLogger(__name__)

class Poll(Event):
    """A Circuits event to trigger polling"""
    channels = (POLLER_CHANNEL,)

class PollCompleted(Event):
    """A Circuits event to notify that this poll event is completed"""
    channels = (POLLER_CHANNEL,)


class SentinelOnePollerComponent(ResilientComponent):
    """
    Event-driven polling for SentinelOne Threats
    """

    # This doesn't listen to Action Module, only its internal channel for timer events
    # But we still inherit from ResilientComponent so we get a REST client etc
    channel = POLLER_CHANNEL

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(SentinelOnePollerComponent, self).__init__(opts)
        self.jinja_env = JinjaEnvironment()
        self.options = opts.get(PACKAGE_NAME, {})

        self._load_options(opts)
        if self.polling_interval == 0:
            LOG.info(u"SentinelOne poller interval is not configured.  Automated escalation is disabled.")
            return

        # Set last_poller_time to the specified polling_lookback in minutes to pick up extra threats
        # the first time polling. 
        self.polling_lookback = int(self.options.get("polling_lookback", DEFAULT_POLLER_LOOKBACK_MINUTES))
        self.last_poller_time = datetime.datetime.utcnow() - datetime.timedelta(minutes=self.polling_lookback)

        LOG.info(u"SentinelOne poller initiated, polling interval %s", self.polling_interval)
        Timer(self.polling_interval, Poll(), persist=False).register(self)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self._load_options(opts)

    @handler("Poll")
    def _poll(self, event):
        """Handle the timer"""
        LOG.info(u"SentinelOne start polling.")
        self._escalate()

    @handler("PollCompleted")
    def _poll_completed(self, event):
        """Set up the next timer"""
        LOG.info(u"SentinelOne poller complete.")
        Timer(self.polling_interval, Poll(), persist=False).register(self)

    def _load_options(self, opts):
        """Read options from config"""
        self.opts = opts
        self.options = opts.get(PACKAGE_NAME, {})

        # Validate required fields in app.config are set
        required_fields = ["sentinelone_server", "api_version", "api_token"]
        validate_fields(required_fields, self.options)

        self.polling_interval = int(self.options.get("polling_interval", 0))
        if not self.polling_interval:
            return

        # Create api client
        self.sentinelone_client = SentinelOneClient(self.opts, self.options)

        self.resilient_common = ResilientCommon(self.rest_client())

    def _escalate(self):
        """ This is the main logic of the poller
            Search for SentinelOne Threats and create associated cases in Resilient SOAR
        """
        try:
            poller_start = datetime.datetime.utcnow()
            LOG.debug("Poll start = %s ", poller_start)

            # Call SentinelOne to get latest threats since last poller time
            threats = self.sentinelone_client.get_threats_by_time(self.last_poller_time)
            try:
                for threat in threats:
                    self._process_threat(threat)

            finally:
                self.last_poller_time = poller_start

        except Exception as err:
            LOG.error(str(err))
        finally:
            # We always want to reset the timer to wake up, no matter failure or success
            self.fire(PollCompleted())

    def _process_threat(self, threat):
        """Process the threat found in SentinelOne.  Use jinja templates to create, update
           or close the incident in SOAR.

        Args:
            threat ([type]): [SentinelOne Threat object]
        """
        try:
            threat_info = threat.get("threatInfo")
            threat_id = threat_info.get("threatId")
        
            resilient_incident = self.resilient_common.find_incident(threat_id)
            if resilient_incident is None:         
                # create a new incident
                incident_payload = self.jinja_env.make_payload_from_template(
                                                    self.options.get("create_incident_template"),
                                                    DEFAULT_INCIDENT_CREATION_TEMPLATE,
                                                    threat)
                incident_payload = self._add_threat_url_to_payload(threat_id, incident_payload)
                resilient_incident = self.resilient_common.create_incident(incident_payload)
                LOG.info("Created incident %s from SentinelOne Threat %s",
                             resilient_incident.get('id'), threat_id)
                resilient_incident_url = self._send_incident_url_to_sentinelone(resilient_incident, threat_id)
            else:
                resilient_incident_id = resilient_incident.get('id')
                if resilient_incident.get("plan_status") == "C":
                    LOG.info("Bypassing update to closed incident %s from SentinelOne threat %s",
                            resilient_incident_id, threat_id)
                elif threat_info.get("incidentStatus") == "resolved":
                    # close the incident
                    incident_payload = self.jinja_env.make_payload_from_template(
                                                    self.options.get("close_incident_template"),
                                                    DEFAULT_INCIDENT_CLOSE_TEMPLATE,
                                                    threat)
                    updated_resilient_incident = self.resilient_common.close_incident(
                                                                resilient_incident_id,
                                                                incident_payload)
                    _ = self.resilient_common.create_incident_comment(resilient_incident_id, None, 
                                                                      "Close synchronized from SentinelOne")
                    LOG.info("Closed incident %s from SentinelOne threat %s", resilient_incident_id, threat_id)
                else:
                    # update an incident
                    incident_payload = self.jinja_env.make_payload_from_template(
                                                    self.options.get("update_incident_template"),
                                                    DEFAULT_INCIDENT_UPDATE_TEMPLATE,
                                                    threat)
                    updated_resilient_incident = self.resilient_common.update_incident(
                                                    resilient_incident_id,
                                                    incident_payload)
                    _ = self.resilient_common.create_incident_comment(resilient_incident_id, None, 
                                                                      "Updates synchronized from SentinelOne")
                    LOG.info("Updated incident %s from SentinelOne threat %s", resilient_incident_id, threat_id)

            incident_id = resilient_incident.get('id')
            self._update_notes(incident_id, threat_id)
        except Exception as err:
            LOG.error(str(err))

    def _update_notes(self, incident_id, threat_id):
        """Update the SOAR incident with any threat notes from SentinelOne.
        """
        # get the SentinelOne threat notes and add to Resilient.
        # need to ensure not adding the comment more than once
        sentinelone_notes  = self.sentinelone_client.get_threat_notes(threat_id)

        new_comments = self.resilient_common.filter_resilient_comments(
                                                            incident_id,
                                                            sentinelone_notes)
        for comment in new_comments:
            self.resilient_common.create_incident_comment(incident_id,
                                                          comment['id'],
                                                          comment['text'])
        return len(new_comments)

    def _add_threat_url_to_payload (self, threat_id, payload):
        """Create a link link back to the SentinelOne threat in a custom incident field

        Args:
            threat_id ([type]): [SentinelOne Threat Id]
            payload (dict): [Resilient new incident payload]

        Returns:
            [dict]: [incident payload]
        """
        threat_url = 'https://{0}/incidents/threats/{1}/overview'.format(
                                          self.options.get('sentinelone_server'), 
                                          threat_id)
        threat_url_link = "<a target='blank' href='{0}'>SentinelOne Threat</a>".format(threat_url)
        payload["properties"]["sentinelone_threat_overview_url"] = threat_url_link
        return payload

    def _send_incident_url_to_sentinelone(self, incident, threat_id):
        """[summary]

        Args:
            incident (dict): [Resilient incident payload]
            threat_id (string): [SentinelOne threat Id]

        Returns:
            [string]: [URLto Resilient incident corresponding to the the SentinelOne threat Id]
        """
        try: 
            # If app.config setting says don't sent threat note to SentinelOne then return None
            if not self.options.get("send_soar_link_to_sentinelone"):
                return None

            # Build the Resilient incident URL
            host = self.opts.get('host')
            port = self.opts.get('port')
            incident_id = incident.get("id")
            resilient_incident_url = build_incident_url(build_resilient_url(host, port), incident_id)

            # Send a threat note containing the incident URL to SentinelOne 
            resilient_url_link = "IBM SOAR created incident {0}: {1}".format(incident_id, resilient_incident_url)
            self.sentinelone_client.add_threat_note(threat_id, resilient_url_link)

            return resilient_incident_url

        except Exception as err:
            raise IntegrationError(str(err))