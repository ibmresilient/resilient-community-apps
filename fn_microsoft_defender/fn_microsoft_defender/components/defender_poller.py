# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.

"""Function implementation"""

from datetime import datetime, timedelta, timezone
from json import loads, decoder
from logging import getLogger
from traceback import format_exc
from circuits import Event, Timer
from resilient_circuits import ResilientComponent, handler
from resilient_lib import validate_fields
from fn_microsoft_defender.lib.jinja_common import JinjaEnvironment, jinja_resilient_datetimeformat
from fn_microsoft_defender.lib.resilient_common import ResilientCommon, IBM_SOAR_LABEL
from fn_microsoft_defender.lib.defender_common import (DefenderAPI, PACKAGE_NAME,
    DEFAULT_INCIDENT_CREATION_TEMPLATE, DEFAULT_INCIDENT_UPDATE_TEMPLATE,
    DEFAULT_INCIDENT_CLOSE_TEMPLATE, DEFENDER_INCIDENT_SCOPE)

POLLER_CHANNEL = "defender_poller"
TICKET_ID_FIELDNAME = "defender_incident_id"

DEFAULT_POLLER_LOOKBACK_MINUTES = 120

DEFAULT_POLLER_SECONDS = 600
LOG = getLogger(__name__)

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
            LOG.info("Defender poller interval is not configured. Automated escalation is disabled.")
            return

        LOG.info(f"Defender poller initiated, polling interval {self.polling_interval}")
        Timer(self.polling_interval, Poll(), persist=False).register(self)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self._load_options(opts)

    @handler("Poll")
    def _poll(self, event):
        """Handle the timer"""
        LOG.info("Defender start polling.")
        self._escalate()

    @handler("PollCompleted")
    def _poll_completed(self, event):
        """Set up the next timer"""
        LOG.info("Defender poller complete.")
        Timer(self.polling_interval, Poll(), persist=False).register(self)

    def _load_options(self, opts):
        """Read options from config"""
        self.opts = opts
        self.options = opts.get(PACKAGE_NAME, {})

        # Validate required fields in app.config are set
        validate_fields(["api_url", "client_id", "tenant_id", "app_secret"], self.options)

        self.polling_interval = int(self.options.get("polling_interval", 0))
        if not self.polling_interval:
            return

        self.last_poller_time = self._get_last_poller_date(int(self.options.get('polling_lookback', DEFAULT_POLLER_LOOKBACK_MINUTES)))

        self.new_incident_filters = get_profile_filters(self.options.get('new_incident_filters'))
        self.alert_filters = get_profile_filters(self.options.get('alert_filters'))

        # Create api client
        self.defender_client = DefenderAPI(self.options.get('tenant_id', None),
                                           self.options.get('client_id', None),
                                           self.options.get('app_secret', None),
                                           self.opts, self.options,
                                           scope=DEFENDER_INCIDENT_SCOPE)

        self.resilient_common = ResilientCommon(self.rest_client())

    def _escalate(self):
        """ This is the main logic of the poller
            Search for Defender incidents and create associated cases in SOAR
        """
        poller_start = datetime.now(timezone.utc)
        try:
            # Call Defender for recently updated/created incidents
            result, _status, _reason  = self.defender_client.query_incidents(self.last_poller_time)

            self._parse_results(result)

        except Exception as err:
            LOG.error(str(err))
            LOG.error(format_exc())
        finally:
            # Set the last poller time for next cycle
            self.last_poller_time = poller_start
            # We always want to reset the timer to wake up, no matter failure or success
            self.fire(PollCompleted())

    def _get_last_poller_date(self, polling_lookback):
        """Get the last poller datetime based on a lookback time
        Args:
            polling_lookback ([number]): # of minutes to lookback
        Returns:
            [datetime]: [datetime to use for last poller run time]
        """
        return datetime.now(timezone.utc) - timedelta(minutes=polling_lookback)

    def _parse_results(self, result):
        """Create SOAR incidents if the result defender incidents haven't already by been created

        Args:
            result ([dict]): results for getting defender incidents
        """
        for defender_incident in result.get("value", []):
            # Determine if an incident already exists, used to know if create or update
            defender_incident_id = get_defender_incident_id(defender_incident)
            resilient_incident = self.resilient_common.find_incident(defender_incident_id)
            try:
                _result_resilient_incident = self._create_update_incident(defender_incident, resilient_incident,
                    self.new_incident_filters, self.alert_filters)
            except Exception as err:
                if resilient_incident and resilient_incident.get('id', None):
                    LOG.info(f"SOAR incident {resilient_incident.get('id', None)} from Defender incident {defender_incident_id} {str(err)}")
                else:
                    LOG.info(str(err))


    def _create_update_incident(self, defender_incident, resilient_incident, new_incident_filters, alert_filters):
        """Perform the operations on the defender incident: create, update or close

        Args:
            defender_incident ([dict]): Defender to act upon
            resilient_incident ([dict]): Existing resilient or none
            new_incident_filters ([dict]): Filter to apply to new incidents
            alert_filters ([dict]): Filter to apply to alerts

        Returns:
            resilient_incident ([dict])
        """
        defender_incident_id = get_defender_incident_id(defender_incident)
        # SOAR incident found
        updated_resilient_incident = None
        if resilient_incident:
            resilient_incident_id = resilient_incident.get('id', None)
            if resilient_incident.get("plan_status", None) == "C":
                LOG.info(f"Bypassing update to closed incident {resilient_incident_id} from Defender incident {defender_incident_id}")
            elif defender_incident.get('status', None) == "Resolved":
                # Close the incident
                incident_payload = self.jinja_env.make_payload_from_template(
                                                    self.options.get("close_incident_template"),
                                                    DEFAULT_INCIDENT_CLOSE_TEMPLATE,
                                                    defender_incident)
                updated_resilient_incident = self.resilient_common.update_incident(
                                                    resilient_incident_id,
                                                    incident_payload
                                                )
                LOG.info(f"Closed incident {resilient_incident_id} from Defender incident {defender_incident_id}")
            else:
                # Update an defender incident
                incident_payload = self.jinja_env.make_payload_from_template(
                                                    self.options.get("update_incident_template"),
                                                    DEFAULT_INCIDENT_UPDATE_TEMPLATE,
                                                    defender_incident)
                updated_resilient_incident = self.resilient_common.update_incident(
                                                    resilient_incident_id,
                                                    incident_payload
                                                )
                LOG.info(f"Updated incident {resilient_incident_id} from Defender incident {defender_incident_id}")

                # Add any recently added comments
                self.add_comments(resilient_incident_id, defender_incident,
                                  int(self.last_poller_time.timestamp()*1000))
        else:
            # Apply filters to only escalate certain alerts
            if check_incident_filters(defender_incident, new_incident_filters) and \
                check_alert_filters(defender_incident.get("alerts"), alert_filters):
                # Create a new incident
                incident_payload = self.jinja_env.make_payload_from_template(
                                                    self.options.get("create_incident_template"),
                                                    DEFAULT_INCIDENT_CREATION_TEMPLATE,
                                                    defender_incident)
                updated_resilient_incident = self.resilient_common.create_incident(incident_payload)
                LOG.info(f"Created incident {updated_resilient_incident['id']} from Defender incident {defender_incident_id}")
            else:
                LOG.info(f"Defender incident {defender_incident_id} bypassed due to new_incident_filters and alert_filters")
                updated_resilient_incident = None

        return updated_resilient_incident

    def add_comments(self, incident_id, defender_incident, last_poller_time_ms):
        for comment in defender_incident.get("comments", {}):
            comment_create_time = jinja_resilient_datetimeformat(comment.get('createdTime', None))

            if comment_create_time >= last_poller_time_ms and IBM_SOAR_LABEL not in comment.get('comment', None):
                note = f"Defender Incident comment: {comment.get('createdTime', None)}\n{comment.get('comment', None)}"
                self.resilient_common.create_incident_comment(incident_id, note)

def get_profile_filters(str_filters):
    """Convert str representation of filters into a dictionary

    Args:
        str_filters ([str]): "filter1": "value", "filter2": ["value-a", "value-b"]

    Returns:
        [dict]: Dictionary representation of filters
    """
    if not str_filters:
        return

    try:
        return loads(f"{{ {str_filters} }}")
    except decoder.JSONDecodeError as err:
        LOG.error(f'Incorrect format for new_incident_filters, syntax: "field1": "value, "field2": ["value1", "value2"] :{err}')

def check_incident_filters(defender_incident, new_incident_filters):
    """Apply the app.config profile filters to determine which incidents to escalate

    Args:
        defender_incident ([dict]): Defender incident fields
        new_incident_filters ([dict]): Filters to apply

    Returns:
        [bool]: True if defender incident should be escalated
    """
    if not new_incident_filters:
        return True

    result = False
    result_list = []

    for filter_name, filter_value in new_incident_filters.items():
        result = None
        if filter_name in defender_incident:
            if isinstance(filter_value, list):
                result = False
                for value in filter_value:
                    if isinstance(defender_incident.get(filter_name, None), list):
                        result = bool(value in defender_incident.get(filter_name, None))
                    else:
                        result = bool(value == defender_incident.get(filter_name, None))
                    # Just need one to match for one pass
                    if result:
                        break
            elif isinstance(defender_incident.get(filter_name, None), list):
                result = bool(filter_value in defender_incident.get(filter_name, None))
            else:
                result = bool(filter_value == defender_incident.get(filter_name, None))

        if result is not None:
            result_list.append(result)

    return all(result_list)

def check_alert_filters(alert_list, alert_filters):
    """Apply the app.config profile filters to determine which incidents to escalate
       based on the alerts which make up the defender incident

    Args:
        alert_list ([list]): incident alert list
        alert_filters ([dict]): filters to apply

    Returns:
        [bool]: True if defender incident should be escalated
    """
    if not alert_filters:
        return True

    # For all alerts, only one alert needs to match the filter criteria to accept the defender incident
    for alert in alert_list:
        alert_result = []
        # Iterate over all alert_filters
        for filter_name, filter_value in alert_filters.items():
            if filter_name not in alert:
                LOG.warning(f"Alert filter: {filter_name} not found in alert. Continuing")
            else:
                # Compare the filter against the alert value. Different combinations exist:
                #  alert: list, alert_filter: list
                #  alert: single value, alert_filter: list
                #  alert: list, alert_filter: single_value
                #  alert: single value, alert_filter: single_value
                if isinstance(filter_value, list):
                    filter_result = None
                    for value in filter_value:
                        if isinstance(alert.get(filter_name, None), list):
                            filter_result = bool(value in alert.get(filter_name, None))
                        else:
                            filter_result = bool(value == alert.get(filter_name, None))
                        # Just need one to match for one pass
                        if filter_result:
                            break
                elif isinstance(alert.get(filter_name, None), list):
                    filter_result = bool(filter_value in alert.get(filter_name, None))
                else:
                    filter_result = bool(filter_value == alert.get(filter_name, None))

                # When a test is done, save the value to compare with all other tests
                if filter_result is not None:
                    alert_result.append(filter_result)

        # If one alert passes all criteria, return with success. Otherwise continue to next alert
        if alert_result and all(alert_result):
            return True

    return False

def get_defender_incident_id(defender_incident):
    """
    Returns:
        [str]: defender_incident_id or None if not found
    """
    return None if not defender_incident else defender_incident.get('incidentId', None)
