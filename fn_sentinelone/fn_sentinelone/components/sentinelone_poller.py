# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

"""Function implementation"""

import datetime
import json
import logging
from circuits import Event, Timer
from resilient_circuits import ResilientComponent, handler
from resilient_lib import validate_fields, RequestsCommon
from fn_sentinelone.lib.function_common import PACKAGE_NAME, SentinelOneProfiles,\
        DEFAULT_INCIDENT_CREATION_TEMPLATE,\
        DEFAULT_INCIDENT_UPDATE_TEMPLATE,\
        DEFAULT_INCIDENT_CLOSE_TEMPLATE
from fn_sentinelone.lib.jinja_common import JinjaEnvironment
from fn_sentinelone.lib.resilient_common import ResilientCommon
from fn_sentinelone.lib.sentinelone_common import SentinelOneClient

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
    Event-driven polling for Sentinel Incidents
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
            LOG.info(u"Sentinel poller interval is not configured.  Automated escalation is disabled.")
            return

        # Set last_poller_time to the specified polling_lookback in minutes to pick up extra threats
        # the first time polling. 
        self.polling_lookback = int(self.options.get("polling_lookback", DEFAULT_POLLER_LOOKBACK_MINUTES))
        self.last_poller_time = datetime.datetime.utcnow() - datetime.timedelta(minutes=self.polling_lookback)

        LOG.info(u"Sentinel poller initiated, polling interval %s", self.polling_interval)
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
        self.rc = RequestsCommon(opts, self.options)
        self.sentinelone_client = SentinelOneClient(self.options, self.rc)

        self.resilient_common = ResilientCommon(self.rest_client())

    def _profileescalate(self):
        """ This is the main logic of the poller
            Search for SentinelOne Threats (incidents) and create associated cases in Resilient SOAR
        """
        try:
            # call Sentinel for each profile to get the incident list
            for profile_name, profile_data in self.sentinelone_profiles.get_profiles().items():
                poller_start = datetime.datetime.utcnow()
                try:
                    LOG.info("polling profile: %s", profile_name)
                    result, status, reason  = self.sentinelone_client.query_incidents(profile_data)
                    threats = result.get("data")
                    while status:
                        self._parse_results(result, profile_name, profile_data)

                        # more results? continue
                        if result.get("nextLink"):
                            LOG.debug("running nextLink")
                            result, status, reason  = self.sentinelone_client.query_next_incidents(profile_data,
                                                                                                result.get("nextLink")
                                                                                               )
                        else:
                            break

                    # filter the incident list returned based on the criteria in a filter
                    if not status:
                        LOG.error("Error querying for incidents: %s, %s", reason, result)

                finally:
                    # set the last poller time for next cycle
                    profile_data['last_poller_time'] = poller_start

        except Exception as err:
            LOG.error(str(err))
        finally:
            # We always want to reset the timer to wake up, no matter failure or success
            self.fire(PollCompleted())

    def _escalate(self):
        """ This is the main logic of the poller
            Search for SentinelOne Threats and create associated cases in Resilient SOAR
        """
        try:
            poller_start = datetime.datetime.utcnow()
 
            # Call SentinelOne to get latest threats since last poller time
            result = self.sentinelone_client.get_threats(self.last_poller_time)

            threats = result.get("data")
            for threat in threats:
                threat_info = threat.get("threatInfo")
                threat_id = threat_info.get("threatId")

                resilient_incident = self.resilient_common.find_incident(threat_id)
                incident_created = False
                if resilient_incident is None:
                    # create a new incident
                    incident_payload = self.jinja_env.make_payload_from_template(
                                                    None,
                                                    DEFAULT_INCIDENT_CREATION_TEMPLATE,
                                                    threat)
                    resilient_incident = self.resilient_common.create_incident(incident_payload)
                    LOG.info("Created incident %s from SentinelOne Threat %s",
                             resilient_incident['id'], threat_id)
                    incident_created = True


                incident_id = resilient_incident['id']
                # get the sentinel comments and add to Resilient.
                # need to ensure not adding the comment more than once
                result_notes = self.sentinelone_client.get_threat_notes(threat_id)
                sentinelone_notes = result_notes.get("data")

                new_comments = self.resilient_common.filter_resilient_comments(
                                                            incident_id,
                                                            sentinelone_notes
                                                        )
                for comment in new_comments:
                    self.resilient_common.create_incident_comment(
                                                            incident_id,
                                                            comment['id'],
                                                            comment['text']
                                                        )

                #for note in sentinelone_notes:
                #    self.resilient_common.add_
            self.last_poller_time = poller_start

        except Exception as err:
            LOG.error(str(err))
        finally:
            # We always want to reset the timer to wake up, no matter failure or success
            self.fire(PollCompleted())


    def _parse_results(self, result, profile_name, profile_data):
        """[create resilient incidents if the result set hasn't already by created]

        Args:
            result ([dict]): [results for getting sentinel incidents]
            profile_name ([str]): [name of profile running]
            profile_data ([dict]): [profile settings]
        """
        for sentinel_incident in result.get("value", []):
            # determine if an incident already exists, used to know if create or update
            sentinel_incident_id, sentinel_incident_number = get_sentinel_incident_ids(sentinel_incident)
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
                                                            comment['name'],
                                                            comment['properties']['message']
                                                        )
                else:
                    LOG.error("Error getting comments: %s", reason)


    def _create_update_incident(self, sentinelone_threat, resilient_incident):
        """[perform the operations on the SentinelOne Threat: create, update or close]

        Args:
            resilient_incident ([dict]): [existing resilient or none]
            new_incident_filters ([dict]): [filter to apply to new incidents]

        Returns:
            resilient_incident ([dict])
        """
        sentinel_incident_id, sentinel_incident_number = get_sentinel_incident_ids(sentinel_incident)
        # resilient incident found
        updated_resilient_incident = None
        if resilient_incident:
            resilient_incident_id = resilient_incident['id']
            if resilient_incident["plan_status"] == "C":
                LOG.info("Bypassing update to closed incident %s from SentinelOne incident %s",
                            resilient_incident_id, sentinel_incident_number)
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
                _ = self.resilient_common.create_incident_comment(resilient_incident_id, None, "Close synchronized from Sentinel")
                LOG.info("Closed incident %s from Sentinel incident %s",
                         resilient_incident_id, sentinel_incident_number)
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
                _ = self.resilient_common.create_incident_comment(resilient_incident_id, None, "Updates synchronized from Sentinel")
                LOG.info("Updated incident %s from Sentinel incident %s",
                         resilient_incident_id, sentinel_incident_number)
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
                         updated_resilient_incident['id'], sentinel_incident_number)
            else:
                LOG.info("Sentinel incident %s bypassed due to new_incident_filters",
                         sentinel_incident_number)
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
        LOG.error('Incorrect format for new_incident_filters, syntax: "field1": "value", "field2": ["value1", "value2"] :%s',
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
    result_list = []
    # flatten the sentinel payload dictionary
    flattened_sentinel_incident = flatten(sentinel_incident)
    for filter_name, filter_value in new_incident_filters.items():
        result = None
        if filter_name in flattened_sentinel_incident:
            if isinstance(filter_value, list):
                result = False
                for value in filter_value:
                    if isinstance(flattened_sentinel_incident[filter_name], list):
                        result = bool(value in flattened_sentinel_incident[filter_name])
                    else:
                        result = bool(value == flattened_sentinel_incident[filter_name])
                    # just need one to match for one pass
                    if result:
                        break
            elif isinstance(flattened_sentinel_incident[filter_name], list):
                result = bool(filter_value in flattened_sentinel_incident[filter_name])
            else:
                result = bool(filter_value == flattened_sentinel_incident[filter_name])

        if result != None:
            result_list.append(result)

    return all(result_list)


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
