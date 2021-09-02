# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

"""Function implementation"""

import datetime
import json
import logging
import traceback
from circuits import Event, Timer
from resilient_circuits import ResilientComponent, handler
from resilient_lib import validate_fields, IntegrationError
from fn_microsoft_defender.lib.jinja_common import JinjaEnvironment
from fn_microsoft_defender.lib.resilient_common import ResilientCommon
from fn_microsoft_defender.lib.defender_common import DefenderAPI, PACKAGE_NAME, \
    DEFAULT_INCIDENT_CREATION_TEMPLATE,\
    DEFAULT_INCIDENT_UPDATE_TEMPLATE,\
    DEFAULT_INCIDENT_CLOSE_TEMPLATE

POLLER_CHANNEL = "defender_poller"
TICKET_ID_FIELDNAME = "defender_alert_id"

DEFAULT_POLLER_LOOBACK_MINUTES = 120

DEFAULT_POLLER_SECONDS = 600
LOG = logging.getLogger(__name__)

class Poll(Event):
    """A Circuits event to trigger polling"""
    channels = (POLLER_CHANNEL,)

class PollCompleted(Event):
    """A Circuits event to notify that this poll event is completed"""
    channels = (POLLER_CHANNEL,)


class DefenderPollerComponent(ResilientComponent):
    """
    Event-driven polling for Defender Incidents
    """

    # This doesn't listen to Action Module, only its internal channel for timer events
    # But we still inherit from ResilientComponent so we get a REST client etc
    channel = POLLER_CHANNEL

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(DefenderPollerComponent, self).__init__(opts)
        self.jinja_env = JinjaEnvironment()
        self.options = opts.get(PACKAGE_NAME, {})

        self._load_options(opts)
        if self.polling_interval == 0:
            LOG.info(u"Defender poller interval is not configured.  Automated escalation is disabled.")
            return

        LOG.info(u"Defender poller initiated, polling interval %s", self.polling_interval)
        Timer(self.polling_interval, Poll(), persist=False).register(self)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self._load_options(opts)

    @handler("Poll")
    def _poll(self, event):
        """Handle the timer"""
        LOG.info(u"Defender start polling.")
        self._escalate()

    @handler("PollCompleted")
    def _poll_completed(self, event):
        """Set up the next timer"""
        LOG.info(u"Defender poller complete.")
        Timer(self.polling_interval, Poll(), persist=False).register(self)

    def _load_options(self, opts):
        """Read options from config"""
        self.opts = opts
        self.options = opts.get(PACKAGE_NAME, {})

        # Validate required fields in app.config are set
        required_fields = ["api_url", "client_id", "tenant_id", "app_secret"]
        validate_fields(required_fields, self.options)

        self.polling_interval = int(self.options.get("polling_interval", 0))
        if not self.polling_interval:
            return

        self.last_poller_time = self._get_last_poller_date(int(self.options.get('polling_lookback', DEFAULT_POLLER_LOOBACK_MINUTES)))

        self.new_incident_filters = get_profile_filters(self.options.get('new_incident_filters'))

        # Create api client
        self.defender_client = DefenderAPI(self.options['tenant_id'],
                                           self.options['client_id'],
                                           self.options['app_secret'],
                                           self.opts, self.options)

        self.resilient_common = ResilientCommon(self.rest_client())

    def _escalate(self):
        """ This is the main logic of the poller
            Search for Defender alerts and create associated cases in Resilient SOAR
        """
        try:
            # call Defender for recently updated/created alerts
            result, status, reason  = self.defender_client.query_alerts(self.last_poller_time)

            self._parse_results(result)

        except Exception as err:
            LOG.error(str(err))
            LOG.error(traceback.format_exc())
        finally:
            # set the last poller time for next cycle
            self.last_poller_time = datetime.datetime.utcnow()
            # We always want to reset the timer to wake up, no matter failure or success
            self.fire(PollCompleted())

    def _get_last_poller_date(self, polling_lookback):
        """get the last poller datetime based on a lookback time
        Args:
            polling_lookback ([number]): # of minutes to lookback
        Returns:
            [datetime]: [datetime to use for last poller run time]
        """
        return datetime.datetime.utcnow() - datetime.timedelta(minutes=polling_lookback)

    def _parse_results(self, result):
        """[create resilient incidents if the result alerts haven't already by been created]

        Args:
            result ([dict]): [results for getting defender alerts]
        """
        for defender_alert in result.get("value", []):
            # determine if an incident already exists, used to know if create or update
            defender_alert_id = get_defender_alert_id(defender_alert)
            resilient_incident = self.resilient_common.find_incident(defender_alert_id)

            result_resilient_incident = self._create_update_incident(defender_alert, resilient_incident,
                                                                     self.new_incident_filters)

            #TODO template to include loop for comments and artfiacts


    def _create_update_incident(self, defender_alert, resilient_incident, new_incident_filters):
        """[perform the operations on the defender alert: create, update or close]

        Args:
            defender_alert ([dict]): [defender to act upon]
            resilient_incident ([dict]): [existing resilient or none]
            new_incident_filters ([dict]): [filter to apply to new incidents]

        Returns:
            resilient_incident ([dict])
        """
        defender_alert_id = get_defender_alert_id(defender_alert)
        # resilient incident found
        updated_resilient_incident = None
        if resilient_incident:
            resilient_incident_id = resilient_incident['id']
            if resilient_incident["plan_status"] == "C":
                LOG.info("Bypassing update to closed incident %s from Defender alert %s",
                            resilient_incident_id, defender_alert_id)
            elif defender_alert['status'] == "Resolved":
                # close the incident
                incident_payload = self.jinja_env.make_payload_from_template(
                                                    self.options.get("close_incident_template"),
                                                    DEFAULT_INCIDENT_CLOSE_TEMPLATE,
                                                    defender_alert)
                updated_resilient_incident = self.resilient_common.close_incident(
                                                    resilient_incident_id,
                                                    incident_payload
                                                )
                LOG.info("Closed incident %s from Defender alert %s",
                         resilient_incident_id, defender_alert_id)
            else:
                # update an defender incident
                incident_payload = self.jinja_env.make_payload_from_template(
                                                    self.options.get("update_incident_template"),
                                                    DEFAULT_INCIDENT_UPDATE_TEMPLATE,
                                                    defender_alert)
                updated_resilient_incident = self.resilient_common.update_incident(
                                                    resilient_incident_id,
                                                    incident_payload
                                                )
                LOG.info("Updated incident %s from Defender alert %s",
                         resilient_incident_id, defender_alert_id)
        else:
            # apply filters to only escalate certain alerts
            if check_incident_filters(defender_alert, new_incident_filters):
                # create a new incident
                incident_payload = self.jinja_env.make_payload_from_template(
                                                    self.options.get("create_incident_template"),
                                                    DEFAULT_INCIDENT_CREATION_TEMPLATE,
                                                    defender_alert)
                updated_resilient_incident = self.resilient_common.create_incident(incident_payload)
                LOG.info("Created incident %s from Defender alert %s",
                         updated_resilient_incident['id'], defender_alert_id)
            else:
                LOG.info("Defender alert %s bypassed due to new_incident_filters",
                         defender_alert_id)
                updated_resilient_incident = None

        return updated_resilient_incident


def get_profile_filters(str_filters):
    """convert str representation of filters into a dictionary

    Args:
        str_filters ([str]): ["filter1": "value", "filter2": ["value-a", "value-b"]]

    Returns:
        [dict]: [dictionary representation of filters]
    """
    if not str_filters:
        return None

    try:
        return json.loads(u"{{ {0} }}".format(str_filters))
    except json.decoder.JSONDecodeError as err:
        LOG.error('Incorrect format for new_incident_filters, syntax: "field1": "value, "field2": ["value1", "value2"] :%s',
                  err)

def check_incident_filters(defender_alert, new_incident_filters):
    """apply the app.config profile filters to determine which incidents to escalate

    Args:
        defender_alert ([dict]): [sentinel incident fields]
        new_incident_filters ([dict]): [filters to apply]

    Returns:
        [bool]: [True if sentinel incident should be escalated]
    """
    if not new_incident_filters:
        return True

    result = False
    result_list = []

    for filter_name, filter_value in new_incident_filters.items():
        result = None
        if filter_name in defender_alert:
            if isinstance(filter_value, list):
                result = False
                for value in filter_value:
                    if isinstance(defender_alert[filter_name], list):
                        result = bool(value in defender_alert[filter_name])
                    else:
                        result = bool(value == defender_alert[filter_name])
                    # just need one to match for one pass
                    if result:
                        break
            elif isinstance(defender_alert[filter_name], list):
                result = bool(filter_value in defender_alert[filter_name])
            else:
                result = bool(filter_value == defender_alert[filter_name])

        if result != None:
            result_list.append(result)

    return all(result_list)

def get_defender_alert_id(defender_alert):
    """
    Returns:
        [str]: [defender_alert_id or None if not found]
    """
    if not defender_alert:
        return None

    return defender_alert['id']
