# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Poller implementation"""

from json import decoder, loads
from logging import getLogger
from threading import Thread

from resilient_circuits import AppFunctionComponent, is_this_a_selftest
from resilient_lib import (SOARCommon, get_last_poller_date, poller,
                           validate_fields)

from fn_microsoft_sentinel.lib.function_common import (
    DEFAULT_INCIDENT_CLOSE_TEMPLATE, DEFAULT_INCIDENT_CREATION_TEMPLATE,
    DEFAULT_INCIDENT_UPDATE_TEMPLATE, PACKAGE_NAME, SentinelProfiles)
from fn_microsoft_sentinel.lib.jinja_common import JinjaEnvironment
from fn_microsoft_sentinel.lib.resilient_common import ResilientCommon
from fn_microsoft_sentinel.lib.sentinel_common import (
    SentinelAPI, get_sentinel_incident_ids)
from fn_microsoft_sentinel.poller.configure_tab import init_incident_groups_tab

LOG = getLogger(__name__)

class PollerComponent(AppFunctionComponent):
    """
    Poller for escalating SOAR incidents and synchronizing changes
    """

    def __init__(self, opts):
        """
        Constructor provides access to the configuration options
        :param opts: all settings including SOAR settings
        :type opts: dict
        """

        super(PollerComponent, self).__init__(opts, PACKAGE_NAME)
        self.opts = opts
        self.sentinel_profiles = SentinelProfiles(opts, self.options)
        self.jinja_env = JinjaEnvironment()
        init_incident_groups_tab()

        # Collect settings necessary and initialize libraries used by the poller
        if not self._init_env():
            LOG.info("Poller interval is not configured. Automated escalation is disabled.")
            return

        # Create poller thread
        poller_thread = Thread(target=self.run)
        poller_thread.daemon = True
        poller_thread.start()

    def _init_env(self):
        """
        Initialize the environment based on app.config settings
        :return: True if poller is configured
        :rtype: bool
        """
        # Validate required fields in app.config are set
        validate_fields([{"name": "azure_url"},
                         {"name": "client_id", "placeholder": "aaa-bbb-ddd"},
                         {"name": "tenant_id", "placeholder": "aaa-bbb-ccc"},
                         {"name": "app_secret", "placeholder": "aaa-bbb-eee"},
                         {"name": "sentinel_profiles"}],
                         self.options)

        self.polling_interval = int(self.options.get("polling_interval", 0))
        if not self.polling_interval or is_this_a_selftest(self):
            LOG.debug("Exiting poller because polling interval set to 0 or this run is a selftest.")
            return False

        LOG.info("Poller initiated, polling interval %s", self.polling_interval)
        self.last_poller_time = get_last_poller_date(int(self.options.get("polling_lookback", 0)))
        LOG.info("Poller lookback: %s", self.last_poller_time)

        # rest_client is used to make IBM SOAR API calls
        self.res_client = self.rest_client()
        self.soar_common = SOARCommon(self.res_client)
        # Create api client
        self.sentinel_client = SentinelAPI(self.opts, self.options)
        self.resilient_common = ResilientCommon(self.rest_client())

        return True

    @poller("polling_interval", "last_poller_time")
    def run(self, *args, **kwargs):
        """
        Process to query for changes in datasource entities and the cooresponding update SOAR case.
        The steps taken are:
           1) query SOAR for all open entities associated with the datasource
           2) query datasource entities for changes based on these incidents
           3) determine SOAR actions to take: create, update, or close a case
        :param last_poller_time: time in milliseconds when the last poller ran
        :type last_poller_time: int
        """
        for profile_name, profile_data in self.sentinel_profiles.get_profiles().items():
            result, status, reason = self.sentinel_client.query_incidents(profile_data)
            if status:
                self._parse_results(result, profile_name, profile_data)
                if result.get("nextLink"):
                    LOG.debug("running nextLink")
                    result, status, reason = self.sentinel_client.query_next_incidents(
                        profile_data,
                        result.get("nextLink")
                    )

    def _parse_results(self, result, profile_name, profile_data):
        """
        Create SOAR incidents if the result set hasn't already by created
        :param result [dict]: results for getting sentinel incidents
        :param profile_name [str]: name of profile running
        :param profile_data [dict]: profile settings
        """
        for sentinel_incident in result.get("value", []):
            # Determine if an incident already exists, used to know if create or update
            sentinel_incident_id, sentinel_incident_number = get_sentinel_incident_ids(sentinel_incident)
            soar_incident, _ = self.soar_common.get_soar_case({"sentinel_incident_number": sentinel_incident_id})

            new_incident_filters = get_profile_filters(profile_data['new_incident_filters'])
            result_soar_incident = self._create_update_incident(
                profile_name, profile_data,
                sentinel_incident, soar_incident,
                new_incident_filters
            )

            if result_soar_incident:
                incident_id = result_soar_incident['id']
                # Get the sentinel comments and add to SOAR.
                # Need to ensure not adding the comment more than once
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
                        self.soar_common.create_case_comment(
                            incident_id,
                            comment['properties']['message'],
                            entity_comment_header="From Sentinel",
                            entity_comment_id=comment['name']
                        )
                else:
                    LOG.error(f"Error getting comments: {reason}")

    def _create_update_incident(self, profile_name, profile_data, sentinel_incident, soar_incident, new_incident_filters):
        """
        Perform the operations on the sentinel incident: create, update or close
        :param profile_name [str]: [incident profile]
        :param profile_data [dict]: [profile data]
        :param soar_incident [dict]: [existing SOAR or none]
        :param new_incident_filters [dict]: [filter to apply to new incidents]
        :return: soar_incident [dict]
        """
        sentinel_incident_id, sentinel_incident_number = get_sentinel_incident_ids(sentinel_incident)
        # SOAR incident found
        updated_soar_incident = None
        if soar_incident:
            soar_incident_id = soar_incident['id']
            if soar_incident["plan_status"] == "C":
                LOG.info(f"Bypassing update to closed incident {soar_incident_id} from Sentinel incident {sentinel_incident_number}")
            elif sentinel_incident['properties']['status'] == "Closed":
                # Close the incident
                incident_payload = self.jinja_env.make_payload_from_template(
                    profile_data.get("close_incident_template"),
                    DEFAULT_INCIDENT_CLOSE_TEMPLATE,
                    sentinel_incident
                )
                updated_soar_incident = self.soar_common.update_soar_case(soar_incident_id, incident_payload)
                _ = self.soar_common.create_case_comment(soar_incident_id, "Close synchronized from Sentinel")
                LOG.info(f"Closed incident {soar_incident_id} from Sentinel incident {sentinel_incident_number}")
            else:
                # Update an incident incident
                incident_payload = self.jinja_env.make_payload_from_template(
                    profile_data.get("update_incident_template"),
                    DEFAULT_INCIDENT_UPDATE_TEMPLATE,
                    sentinel_incident
                )
                updated_soar_incident = self.soar_common.update_soar_case(soar_incident_id, incident_payload)
                LOG.info(f"Updated incident {soar_incident_id} from Sentinel incident {sentinel_incident_number}")
        else:
            # Apply filters to only escalate certain incidents
            if check_incident_filters(sentinel_incident, new_incident_filters):
                # Add in the profile to track
                sentinel_incident['soar_profile'] = profile_name

                # Create a new incident
                incident_payload = self.jinja_env.make_payload_from_template(
                    profile_data.get("create_incident_template"),
                    DEFAULT_INCIDENT_CREATION_TEMPLATE,
                    sentinel_incident
                )
                updated_soar_incident = self.soar_common.create_soar_case(incident_payload)
                LOG.info(f"Created incident {updated_soar_incident['id']} from Sentinel incident {sentinel_incident_number}")
            else:
                LOG.info(f"Sentinel incident {sentinel_incident_number} bypassed due to new_incident_filters")
                updated_soar_incident = None

        return updated_soar_incident

def get_profile_filters(str_filters):
    """
    Convert str representation of filters into a dictionary
    :param str_filters [str]: "filter1": "value", "filter2": ["value-a", "value-b"]
    :return [dict]: dictionary representation of filters
    """
    if not str_filters:
        return None

    try:
        return loads(f"{{ {str_filters} }}")
    except decoder.JSONDecodeError as err:
        LOG.error(f'Incorrect format for new_incident_filters, syntax: "field1": "value", "field2": ["value1", "value2"] :{err}')

def check_incident_filters(sentinel_incident, new_incident_filters):
    """
    Apply the app.config profile filters to determine which incidents to escalate
    :param sentinel_incident [dict]: sentinel incident fields
    :param new_incident_filters [dict]: filters to apply
    :return [bool]: True if sentinel incident should be escalated
    """
    if not new_incident_filters:
        return True

    result = False
    result_list = []
    # Flatten the sentinel payload dictionary
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
                    # Just need one to match for one pass
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
    """
    Take a dictionary with embedded dictionaries and convert to a single depth dictionary
    :param json_payload [dict]: dictionary to flatten
    :return [dict]: flattened dictionary
    """
    result = {}
    for item, item_value in json_payload.items():
        if isinstance(item_value, dict):
            flatten_result = flatten(item_value)
            # Append the dictionary flattended to the existing dictionary
            result = {**result, **flatten_result}
        else:
            result[item] = item_value
    return result
