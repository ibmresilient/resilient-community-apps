# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from datetime import datetime, timedelta
from logging import getLogger
from threading import Thread
from resilient_circuits import ResilientComponent
from resilient_lib import IntegrationError, SOARCommon, clean_html
from fn_qradar_enhanced_data.lib.poller_common import poller
from fn_qradar_enhanced_data.util.function_utils import (get_qradar_client, get_server_settings, get_sync_notes)
from fn_qradar_enhanced_data.util.qradar_constants import (GLOBAL_SETTINGS, PACKAGE_NAME)
from fn_qradar_enhanced_data.util.qradar_utils import AuthInfo
from fn_qradar_enhanced_data.util.qradar_graphql_queries import GRAPHQL_POLLERQUERY

LOG = getLogger(__name__)

class PollerComponent(ResilientComponent):
    """Poller to synchronize Offense and Case data"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(PollerComponent, self).__init__(opts)
        self.opts = opts
        self.rest_client()

        # Collect settings necessary and initialize libraries used by the poller
        if not self._init_env():
            LOG.info(u"Poller interval is not configured, so the poller will not run.")
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
        self.last_poller_time = datetime.now() - timedelta(minutes=int(self.global_settings.get('polling_lookback', 0)))
        LOG.info(f"Poller lookback: {self.last_poller_time}")

        return True

    @poller('polling_interval', 'last_poller_time', PACKAGE_NAME)
    def run(self, last_poller_time=None):
        """
        Process to query for changes in datasource entities and the cooresponding update SOAR case
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
        case_list, error_msg = SOARCommon(self.rest_client()).get_soar_cases({"qradar_id": True, "qradar_destination": True})

        if error_msg:
            raise IntegrationError(error_msg)

        self.process_case_list(case_list)

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

        for server in case_server_dict:
            # Create filter string which contains the filters for the api call
            filter_note = []
            filter = []
            id_list = list(case_server_dict[server].keys())
            for id in id_list:
                filter_note.append(f"id={str(id)}")
                filter.append(f"id={str(id)} and last_persisted_time > {int(case_server_dict[server][id].get('properties').get('qr_last_updated_time'))}")

            filters = " or ".join(filter)
            filter_notes = " or ".join(filter_note)

            # Create connection to QRadar server
            qradar_client = get_qradar_client(self.opts, get_server_settings(self.opts, server))

            auth_info = AuthInfo.get_authInfo()
            # Makes GET call to QRadar server using api
            offenses_update_list = auth_info.make_call("GET",
                                                       f"{auth_info.api_url}siem/offenses?fields=id, last_persisted_time, assigned_to&filter={filters}"
                                                      ).json()

            LOG.debug(f"QRadar returned macthing offenses: {str(offenses_update_list)}")

            payload = { "patches": {} }
            updated_cases = []

            # Add to payload to update SOAR cases field qr_last_updated_time
            if offenses_update_list:
                updated_cases = [case_server_dict.get(server, {}).get(str(offense.get('id')), {}).get("id") for offense in offenses_update_list]
                # Iterate through list of offenses recieved from QRadar query
                for offense in offenses_update_list:
                    offense_lastPersistedTime = int(offense.get("last_persisted_time"))
                    offense_id = str(offense.get('id'))
                    case_dict = case_server_dict[server][offense_id]
                    case_id = case_dict.get('id')
                    case_lastPersistedTime = case_dict.get("properties", {}).get("qr_last_updated_time")
                    LOG.debug(f"QRadar last persisted time: {datetime.fromtimestamp(offense_lastPersistedTime / 1e3).strftime('%m-%d-%Y %H:%M:%S')}")
                    LOG.debug(f"SOAR Incident last updated time: {datetime.fromtimestamp(case_lastPersistedTime / 1e3).strftime('%m-%d-%Y %H:%M:%S')}")
                    if offense_lastPersistedTime > case_lastPersistedTime:
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

        if get_sync_notes(self.global_settings, self.opts.get(f"{PACKAGE_NAME}:{server}", {})):
            # Get notes from all QRadar offenses in filter
            offenses_notes = qradar_client.graphql_query({"filter": filter_notes}, GRAPHQL_POLLERQUERY).get("content")

            # Update offense notes
            if offenses_notes:
                poller_time = int(self.last_poller_time.strftime("%s")) * 1e3
                for notes in offenses_notes:
                    incident_id = case_server_dict.get(server, {}).get(notes.get('id'), {}).get('id') # ID of the SOAR incident
                    incident_notes = self.rest_client().get(f"/incidents/{incident_id}/comments")
                    for note in notes.get("notes"):
                        # Check if the QRadar note was created after the last_poller_time
                        if int(note.get("createTime")) > poller_time:
                            # Create a list of notes that are on the SOAR incident
                            inc_notes = [clean_html(n.get("text")) for n in incident_notes if "Added from QRadar" not in n.get("text")]
                            if note.get("noteText") not in inc_notes:
                                # Create the comment payload
                                comment_payload = {
                                    "text": {
                                        "format": "text",
                                        "content": f"{note.get('noteText')}\nAdded from QRadar"
                                    },
                                    "create_date": int(note.get("createTime"))
                                }
                                # Send POST request to SOAR server to add the comment
                                self.rest_client().post(f"/incidents/{incident_id}/comments", comment_payload)
