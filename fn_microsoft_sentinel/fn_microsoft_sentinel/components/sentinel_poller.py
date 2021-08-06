# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

"""Function implementation"""

import datetime
import json
import logging
from circuits import Event, Timer
from resilient_circuits import ResilientComponent, handler
from resilient_lib import validate_fields, IntegrationError
from fn_microsoft_sentinel.lib.function_common import PACKAGE_NAME, SentinelProfiles,\
        DEFAULT_INCIDENT_CREATION_TEMPLATE,\
        DEFAULT_INCIDENT_UPDATE_TEMPLATE,\
        DEFAULT_INCIDENT_CLOSE_TEMPLATE
from fn_microsoft_sentinel.lib.jinja_common import JinjaEnvironment
from fn_microsoft_sentinel.lib.resilient_common import ResilientCommon
from fn_microsoft_sentinel.lib.sentinel_common import SentinelAPI, get_sentinel_incident_id

POLLER_CHANNEL = "sentinel_poller"
TICKET_ID_FIELDNAME = "sentinel_incident_id"

DEFAULT_POLLER_SECONDS = 600
LOG = logging.getLogger(__name__)

class Poll(Event):
    """A Circuits event to trigger polling"""
    channels = (POLLER_CHANNEL,)

class PollCompleted(Event):
    """A Circuits event to notify that this poll event is completed"""
    channels = (POLLER_CHANNEL,)


class SentinelPollerComponent(ResilientComponent):
    """
    Event-driven polling for Sentinel Incidents
    """

    # This doesn't listen to Action Module, only its internal channel for timer events
    # But we still inherit from ResilientComponent so we get a REST client etc
    channel = POLLER_CHANNEL

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(SentinelPollerComponent, self).__init__(opts)
        self.jinja_env = JinjaEnvironment()
        self.options = opts.get(PACKAGE_NAME, {})
        self.sentinel_profiles = SentinelProfiles(opts, self.options)

        self._load_options(opts)
        if self.polling_interval == 0:
            LOG.info(u"Sentinel poller interval is not configured.  Automated escalation is disabled.")
            return

        LOG.info(u"Sentinel poller initiated, polling interval %s", self.polling_interval)
        Timer(self.polling_interval, Poll(), persist=False).register(self)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.sentinel_profiles = SentinelProfiles(opts, self.options)
        self._load_options(opts)

    @handler("Poll")
    def _poll(self, event):
        """Handle the timer"""
        LOG.info(u"Sentinel start polling.")
        self._escalate()

    @handler("PollCompleted")
    def _poll_completed(self, event):
        """Set up the next timer"""
        LOG.info(u"Sentinel poller complete.")
        Timer(self.polling_interval, Poll(), persist=False).register(self)

    def _load_options(self, opts):
        """Read options from config"""
        self.opts = opts
        self.options = opts.get(PACKAGE_NAME, {})

        # Validate required fields in app.config are set
        required_fields = ["azure_url", "client_id", "tenant_id", "app_secret", "sentinel_profiles"]
        validate_fields(required_fields, self.options)

        self.polling_interval = int(self.options.get("polling_interval", 0))
        if not self.polling_interval:
            return

        # Create api client
        self.sentinel_client = SentinelAPI(self.options['tenant_id'],
                                           self.options['client_id'],
                                           self.options['app_secret'],
                                           self.opts, self.options)

        self.resilient_common = ResilientCommon(self.rest_client())

    def _escalate(self):
        """ This is the main logic of the poller
            Search for Sentinel Incidents and create associated cases in Resilient SOAR
        """
        try:
            # call Sentinel for each profile to get the incident list
            for profile_name, profile_data in self.sentinel_profiles.get_profiles().items():
                try:
                    LOG.info("polling profile: %s", profile_name)
                    result, status, reason  = self.sentinel_client.query_incidents(profile_data)

                    # filter the incident list returned based on the criteria in a filter
                    if not status:
                        LOG.error("Error querying for incidents: %s, %s", reason, result)
                    else:
                        for sentinel_incident in result.get("value", []):
                            # determine if an incident already exists, used to know if create or update
                            sentinel_incident_id = get_sentinel_incident_id(sentinel_incident)
                            resilient_incident = self.resilient_common.find_incident(sentinel_incident_id)

                            new_incident_filters = get_profile_filters(profile_data['new_incident_filters'])
                            result_resilient_incident = self._create_update_incident(profile_name, profile_data,
                                                                        sentinel_incident, resilient_incident,
                                                                        new_incident_filters)

                            if result_resilient_incident:
                                incident_id = result_resilient_incident['id']
                                # get the sentinel comments and add to Resilient.
                                # need to ensure not adding the comment more than once
                                result, status, reason = self.sentinel_client.get_comments(
                                                                                profile_data,
                                                                                sentinel_incident_id
                                                                            )
                                new_comments = []
                                if status:
                                    new_comments = self.resilient_common.filter_resilient_comments(
                                                                            incident_id,
                                                                            result['value']
                                                                        )
                                    for comment in new_comments:
                                        self.resilient_common.create_incident_comment(
                                                                            incident_id,
                                                                            sentinel_incident_id,
                                                                            comment['properties']['message']
                                                            )

                finally:
                    # set the last poller time for next cycle
                    profile_data['last_poller_time'] = datetime.datetime.utcnow()

        except Exception as err:
            LOG.error(str(err))
        finally:
            # We always want to reset the timer to wake up, no matter failure or success
            self.fire(PollCompleted())

    def _create_update_incident(self, profile_name, profile_data,\
                                sentinel_incident, resilient_incident, new_incident_filters):
        """[perform the operations on the sentinel incident: create, update or close]

        Args:
            profile_name ([str]): [incident profile]
            profile_data ([dict]): [profile data]
            resilient_incident ([dict]): [existing resilient or none]
            new_incident_filters ([dict]): [filter to apply to new incidents]

        Returns:
            resilient_incident ([dict])
        """
        sentinel_incident_id = get_sentinel_incident_id(sentinel_incident)
        # resilient incident found
        updated_resilient_incident = None
        if resilient_incident:
            resilient_incident_id = resilient_incident['id']
            if resilient_incident["plan_status"] == "C":
                LOG.info("Bypassing update to closed incident %s from Sentinel incident %s",
                            resilient_incident_id, sentinel_incident_id)
            elif sentinel_incident['properties']['status'] == "Closed":
                # close the incident
                incident_payload = self.jinja_env.make_payload_from_template(
                                                    profile_data.get("close_incident_template"),
                                                    DEFAULT_INCIDENT_CLOSE_TEMPLATE,
                                                    sentinel_incident)
                updated_resilient_incident = self.resilient_common.close_incident(
                                                                resilient_incident_id,
                                                                incident_payload
                                                            )
                LOG.info("Closed incident %s from Sentinel incident %s",
                         resilient_incident_id, sentinel_incident_id)
            else:
                # update an incident incident
                incident_payload = self.jinja_env.make_payload_from_template(
                                                    profile_data.get("update_incident_template"),
                                                    DEFAULT_INCIDENT_UPDATE_TEMPLATE,
                                                    sentinel_incident)
                updated_resilient_incident = self.resilient_common.update_incident(
                                                    resilient_incident_id,
                                                    incident_payload
                                                )
                LOG.info("Updated incident %s from Sentinel incident %s",
                         resilient_incident_id, sentinel_incident_id)
        else:
            # apply filters to only escalate certain incidents
            if check_incident_filters(sentinel_incident, new_incident_filters):
                # add in the profile to track
                sentinel_incident['resilient_profile'] = profile_name

                # create a new incident
                incident_payload = self.jinja_env.make_payload_from_template(
                                                    profile_data.get("create_incident_template"),
                                                    DEFAULT_INCIDENT_CREATION_TEMPLATE,
                                                    sentinel_incident)
                updated_resilient_incident = self.resilient_common.create_incident(incident_payload)
                LOG.info("Created incident %s from Sentinel incident %s",
                         updated_resilient_incident['id'], sentinel_incident_id)
            else:
                LOG.info("Sentinel incident %s bypassed due to new_incident_filters",
                         sentinel_incident_id)
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

def check_incident_filters(sentinel_incident, new_incident_filters):
    """apply the app.config profile filters to determine which incidents to escalate

    Args:
        sentinel_incident ([dict]): [sentinel incident fields]
        new_incident_filters ([dict]): [filters to apply]

    Returns:
        [bool]: [True if sentinel incident should be escalated]
    """
    if not new_incident_filters:
        return True
    result = False
    # flatten the sentinel payload dictionary
    flattened_sentinel_incident = flatten(sentinel_incident)
    for filter_name, filter_value in new_incident_filters.items():
        if filter_name in flattened_sentinel_incident:
            if isinstance(filter_value, list):
                for value in filter_value:
                    if isinstance(flattened_sentinel_incident[filter_name], list):
                        result = bool(value in flattened_sentinel_incident[filter_name])
                    else:
                        result = bool(value == flattened_sentinel_incident[filter_name])
                    # just need one to match for one pass
                    if result:
                        break
            else:
                result = (filter_value == flattened_sentinel_incident[filter_name])
    return result


def flatten(json_payload):
    """take a dictionary with embedded dictionaries and convert to a single depth dictionary

    Args:
        json_payload ([dict]): [dictionary to flatten]

    Returns:
        [dict]: [flattened dictionary]
    """
    result = {}
    for item, item_value in json_payload.items():
        if isinstance(item_value, dict):
            flatten_result = flatten(item_value)
            # append the dictionary flattended to the existing dictionary
            result = {**result, **flatten_result}
        else:
            result[item] = item_value
    return result
