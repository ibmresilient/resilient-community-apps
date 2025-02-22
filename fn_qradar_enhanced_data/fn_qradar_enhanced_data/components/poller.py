# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import functools
from traceback import format_exc
from datetime import datetime, timedelta, timezone
from logging import getLogger
from threading import Thread, Event
from resilient_circuits import ResilientComponent
from resilient_lib import IntegrationError, SOARCommon
from fn_qradar_enhanced_data.util.function_utils import (get_qradar_client, get_server_settings,
                                                         get_sync_notes, filter_comments)
from fn_qradar_enhanced_data.util.qradar_constants import (GLOBAL_SETTINGS, PACKAGE_NAME)
from fn_qradar_enhanced_data.util.qradar_utils import AuthInfo, QRadarServers
from fn_qradar_enhanced_data.util.qradar_graphql_queries import GRAPHQL_POLLERQUERY

LOG = getLogger(__name__)
AUTO_ESCALATION_NOTE = "Case created in SOAR"
MANUAL_ESCALATION = "Manual escalation of offense to SOAR"
PLUGIN_ADDED_NOTE = "\nAdded from SOAR"
# The max number of QRadar offenses that can be searched for at once
MAX_OFFENSES_TO_SEARCH = 50

# P O L L E R   L O G I C
def poller(named_poller_interval, named_last_poller_time):
    """
    Decorator for poller, manage poller time, calling the customized method for getting the next entities
    :param named_poller_interval: (str) Name of instance variable containing the poller interval in seconds
    :param named_last_poller_time: (datetime) Name of instance variable containing the lookback value in seconds
    """
    def poller_wrapper(func):
        # Decorator for running a function forever, passing the ms timestamp of
        # when the last poller run to the function it's calling
        @functools.wraps(func)
        def wrapped(self, *args):
            last_poller_time = getattr(self, named_last_poller_time)
            exit_event = Event()

            while not exit_event.is_set():
                LOG.info(f"{PACKAGE_NAME} polling start.")
                poller_start = datetime.now(timezone.utc) # Current UTC time
                try:
                    # Function execution with the last poller time in ms
                    func(self, *args, last_poller_time=int(last_poller_time.timestamp()*1000))

                except Exception as err:
                    LOG.error(str(err))
                    LOG.error(format_exc())
                finally:
                    LOG.info(f"{PACKAGE_NAME} polling complete.")
                    # Set the last poller time for next cycle
                    last_poller_time = poller_start

                    # Sleep before the next poller execution
                    exit_event.wait(getattr(self, named_poller_interval))
            exit_event.set() # Loop complete

        return wrapped
    return poller_wrapper

class PollerComponent(ResilientComponent):
    """Poller to synchronize Offense and Case data"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(PollerComponent, self).__init__(opts)
        self.opts = opts

        # Collect settings necessary and initialize libraries used by the poller
        if not self._init_env():
            LOG.info("Poller interval is not configured, so the poller will not run.")
            return

        # Create poller thread
        poller_thread = Thread(target=self.run)
        poller_thread.daemon = True
        poller_thread.start()

    def _init_env(self):
        """
        Initialize the environment based on app.config settings
        :param opts: (dict) All settings including SOAR settings
        :return: (bool) True if poller is configured
        """
        self.global_settings = self.opts.get(GLOBAL_SETTINGS, {})
        self.polling_interval = int(self.global_settings.get("polling_interval", 0))
        if not self.polling_interval:
            return False

        LOG.info(f"Poller initiated, polling interval {self.polling_interval}")
        poller_lookback = int(self.global_settings.get('polling_lookback', 0))
        # Get the current UTC time.
        self.last_poller_time = datetime.now(timezone.utc) - timedelta(minutes=poller_lookback)
        LOG.info(f"Minutes for poller to lookback: {poller_lookback}")

        # Look for the setting `timezone_offset` in the app.config and add a warning log that it is deprecated.
        qradar_servers = QRadarServers(self.opts).get_servers_dict() # Dictionary of all configured QRadar servers and there settings.
        for qradar_server in qradar_servers.values(): # Loop through the configured QRadar servers
            if "timezone_offset" in qradar_server:
                LOG.warning("The setting 'timezone_offset' is deprecated.")
                break

        self.rest_client()
        self.soar_common = SOARCommon(self.rest_client())

        return True

    @poller('polling_interval', 'last_poller_time')
    def run(self, last_poller_time=None):
        """
        Process to query for changes in datasource entities and the corresponding update SOAR case
           The steps taken are to
            1) Query SOAR for all open cases with qradar_id and qradar_destination fields
            2) Create dictionary of QRadar servers that have incidents on SOAR, each QRadar server equals a list of the offense ID's to query
            3) Query each QRadar server in the dictionary for each offense's, in the servers list, last_persisted_time
            4) Check if the last_persisted_time value received from the QRadar offense is different than the last_persisted_time value in the corresponding SOAR incident
            5) If the last_persistent_time is different between the offense on QRadar and the corresponding incident on SOAR then the last_persistent_time value on the SOAR incident is update
            6) When the last_persistent_time value on SOAR is changed it triggers the QRadar Enhanced Data automatic rule on SOAR
        :param last_poller_time: (int) Time in milliseconds when the last poller ran
        :return: None
        """
        # last_poller_time minus minutes set in poller_lookback
        self.last_poller_time = datetime.fromtimestamp(int(last_poller_time / 1000), timezone.utc)
        case_list, error_msg = self.soar_common.get_soar_cases({"qradar_id": True, "qradar_destination": True})

        if error_msg:
            raise IntegrationError(error_msg)

        def split(cases_list: list):
            """ Split up case_list into lists of the max size """
            for c in range(0, len(cases_list), MAX_OFFENSES_TO_SEARCH):
                yield cases_list[c:c + MAX_OFFENSES_TO_SEARCH]

        case_lists = list(split(case_list))
        # Loop through list of lists. This will help keep the calls to QRadar from erroring because of to many filters.
        for list_cases in case_lists:
            self.process_case_list(list_cases)

    def process_case_list(self, case_list):
        """
        Process the open cases
        :param case_list: List of open cases
        :return: None
        """
        # :Start: Create dictionary of the QRadar servers to query
        # This is created, so that each QRadar server is only queried once
        case_server_dict = {}
        for case in case_list:
            qradar_destination = case.get("properties", {}).get("qradar_destination")
            if qradar_destination not in case_server_dict:
                case_server_dict[qradar_destination] = {}
            # Add the case to the dictionary of the server it is from
            case_server_dict[qradar_destination][case.get("properties", {}).get("qradar_id")] = case
        # :End: QRadar servers dictionary
        LOG.debug(f"Dictionary of configured QRadar servers and the cases that returned from each: {case_server_dict}")

        for server in case_server_dict:
            # Create filter string which contains the filters for the api call
            filter_note = []
            filter = []
            id_list = list(case_server_dict[server].keys())
            for id in id_list:
                filter_note.append(f"id={str(id)} and status!=CLOSED")
                qr_last_updated = case_server_dict[server][id].get('properties', {}).get('qr_last_updated_time', 0)
                # If not in SOAR case then set time to 0
                if not qr_last_updated:
                    qr_last_updated = 0
                filter.append(f"id={str(id)} and last_persisted_time > {int(qr_last_updated)} and status!=CLOSED")

            filters = " or ".join(list(set(filter))) # Using set will remove any duplicate IDs in the list
            filter_notes = " or ".join(list(set(filter_note)))
            LOG.debug(f"The filters for the query to QRadar to return the required cases: {filters}")
            LOG.debug(f"The filters for the query to QRadar to return the required cases notes: {filter_note}")

            # Create connection to QRadar server
            qradar_client = get_qradar_client(self.opts, get_server_settings(self.opts, server))

            auth_info = AuthInfo.get_authInfo()
            # Makes a call to the QRadar server to get all the QRadar offense that have a last_persisted_time that is greater than its
            # corresponding SOAR incidents last_persisted_time.
            offenses_update_list = auth_info.make_call("GET",
                                                       f"{auth_info.api_url}siem/offenses?fields=id,last_persisted_time,assigned_to&filter={filters}"
                                                      ).json()

            LOG.debug(f"QRadar returned matching offenses: {str(offenses_update_list)}")

            payload = { "patches": {} }
            updated_cases = []

            # Add to payload to update SOAR cases field qr_last_updated_time
            if offenses_update_list:
                updated_cases = [case_server_dict.get(server, {}).get(str(offense.get('id')), {}).get("id") for offense in offenses_update_list]
                # Iterate through list of offenses received from QRadar query
                for offense in offenses_update_list:
                    offense_lastPersistedTime = int(offense.get("last_persisted_time"))
                    offense_id = str(offense.get('id'))
                    case_dict = case_server_dict[server][offense_id]
                    case_id = case_dict.get('id')
                    case_lastPersistedTime = case_dict.get("properties", {}).get("qr_last_updated_time")
                    if not case_lastPersistedTime or offense_lastPersistedTime > case_lastPersistedTime:
                        # If time is different then update the case
                        updated_cases.append(case_id)
                        # Create payload to update cases
                        payload['patches'][case_id] = {
                                                "version": case_dict.get("vers")+1,
                                                "changes": [{
                                                    "old_value": {"date": case_lastPersistedTime},
                                                    "new_value": {"date": offense_lastPersistedTime},
                                                    "field": {"name": "qr_last_updated_time"}
                                                }]
                                            }

            self.sync_notes(qradar_client, server, filter_notes, case_server_dict)

            # If there are changes then fix payload and send put request to SOAR
            if updated_cases:
                # Send put request to SOAR
                # This will update all cases that need to be updated for the give QRadar server
                response = self.rest_client().put("/incidents/patch", payload)
                # If failures dictionary is not empty then raise error
                if response.get('failures'):
                    raise IntegrationError(str(response))

                LOG.info(f"Case: {str(updated_cases)} updated field: qr_last_updated_time")

    def sync_notes(self, qradar_client, server, filter_notes, case_server_dict):
        """
        Sync QRadar offense notes with SOAR incident
        :param qradar_client: Client connection to QRadar server
        :param server: Label of the current server
        :param filter_notes: Filter to get QRadar offense notes
        :param case_server_dict: Dictionary of SOAR incidents
        :return: None
        """
        options = self.opts.get(f"{PACKAGE_NAME}:{server}", {})

        if get_sync_notes(self.global_settings, options): # Check if the 'sync_notes' setting in the app.config equals True
            # Get notes from all QRadar offenses in filter
            offenses_notes = qradar_client.graphql_query({"filter": filter_notes}, GRAPHQL_POLLERQUERY).get("content") # QRadar offense notes
            # Initialize list that will be filled with notes from the QRadar offense that will be added to the SOAR incident.
            notes_to_add = []

            # Update offense notes
            if offenses_notes:
                for notes in offenses_notes:
                    if notes.get("notes", []): # Check if notes list is empty or not
                        incident_id = case_server_dict.get(server, {}).get(notes.get('id'), {}).get('id') # ID of the SOAR incident
                        # Create a list of notes on the QRadar offense if they where created after the last time the poller ran
                        # and if the following are not present in the notes text: AUTO_ESCALATION_NOTE, MANUAL_ESCALATION,
                        # \x03, PLUGIN_ADDED_NOTE
                        qradar_notes = [note.get("noteText").replace("\r", "") for note in notes.get("notes", {})
                                        if datetime.fromtimestamp(int(note.get("createTime"))/1000).astimezone(timezone.utc) > self.last_poller_time # Convert createTime to UTC and check if it is greater than last_poller_time
                                        and not any(ele in note.get("noteText") for ele in [AUTO_ESCALATION_NOTE, MANUAL_ESCALATION, "\x03", PLUGIN_ADDED_NOTE, PLUGIN_ADDED_NOTE[2:]])]
                        if qradar_notes: # Check that the list is not empty
                            notes_to_add = filter_comments(self.soar_common, incident_id, qradar_notes, soar_str_to_remove="\nAdded from QRadar")
                        if notes_to_add: # Check that the list is not empty
                            for note in notes_to_add:
                                self.soar_common.create_case_comment(incident_id, f"{note}\nAdded from QRadar")
