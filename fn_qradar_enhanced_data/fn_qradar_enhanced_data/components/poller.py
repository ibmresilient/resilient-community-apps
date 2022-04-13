# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""Function implementation"""

from ast import literal_eval
from threading import Thread
from logging import getLogger
from datetime import datetime, timedelta
from resilient_lib import IntegrationError
from resilient_circuits import ResilientComponent
from fn_qradar_enhanced_data.util.qradar_utils import AuthInfo
from fn_qradar_enhanced_data.lib.poller_common import SOARCommon, poller
from fn_qradar_enhanced_data.util.qradar_constants import PACKAGE_NAME, GLOBAL_SETTINGS
from fn_qradar_enhanced_data.util.function_utils import get_server_settings, get_qradar_client

LOG = getLogger(__name__)

class PollerComponent(ResilientComponent):
    """
    Poller to synchronize Offense and Case data
    """

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(PollerComponent, self).__init__(opts)
        self.opts = opts
        self.rest_client()

        # Collect settings necessary and initialize libraries used by the poller
        if not self._init_env():
            LOG.info(u"Poller interval is not configured, so poller will not run.")
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
        global_settings = self.opts.get(GLOBAL_SETTINGS, {})
        self.polling_interval = int(global_settings.get("polling_interval", 0))
        if not self.polling_interval:
            return False

        LOG.info(u"Poller initiated, polling interval %s", self.polling_interval)
        self.last_poller_time = datetime.now() - timedelta(minutes=int(global_settings.get('polling_lookback', 0)))
        LOG.info("Poller lookback: %s", self.last_poller_time)

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
        case_list, error_msg = SOARCommon.get_open_soar_cases({"qradar_id": True, "qradar_destination": True}, self.rest_client())

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
            qradar_id = case["properties"]["qradar_id"]
            qradar_destination = case["properties"]["qradar_destination"]
            if qradar_destination not in case_server_dict:
                case_server_dict[qradar_destination] = {}
            case_server = case_server_dict[qradar_destination]
            # Add the case_id and case_lastPersistedTime fields to the qradar_id dictionary
            # that is inside of the QRadar servers dictionary
            if qradar_id not in case_server:
                case_server[qradar_id] = {"case_id": case['id'], "case_lastPersistedTime": case["properties"]["qr_last_updated_time"], "case_ver": case['vers']}
        # :End: QRadar servers dictionary

        for server in case_server_dict:
            # Create filter string which contains the filters for the api call
            filters = ""
            id_list = list(case_server_dict[server].keys())
            for id in id_list:
                filters = "{}id={}".format(filters, str(id))
                if id_list.index(id) != len(id_list)-1:
                    filters = "{} or ".format(filters)

            # Get configuration for QRadar server specified
            options = get_server_settings(self.opts, server)
            # Create connection to QRadar server
            qradar_client = get_qradar_client(self.opts, options)

            auth_info = AuthInfo.get_authInfo()
            # Create url to get all offenses in SOAR from the given QRadar server
            url = auth_info.api_url + "siem/offenses?fields={}&filter={}".format("id, last_persisted_time", filters)
            # Makes GET call to QRadar server using api
            response = auth_info.make_call("GET", url)
            offenses_update_list = response.json()

            payload = { "patches": {} }
            updated_cases = []

            if offenses_update_list:
                # Iterate through list of offenses recieved from QRadar query
                for offense in offenses_update_list:
                    offense_lastPersistedTime = int(offense['last_persisted_time'])
                    case_dict = case_server_dict[server][str(offense['id'])]
                    case_id = case_dict['case_id']
                    case_lastPersistedTime = case_dict['case_lastPersistedTime']
                    LOG.debug("QRadar last persisted time: {}".format(
                        datetime.fromtimestamp(offense_lastPersistedTime).strftime('%m-%d-%Y %H:%M"%S')))
                    LOG.debug("SOAR Incident last updated time: {}".format(
                        datetime.fromtimestamp(case_lastPersistedTime).strftime('%m-%d-%Y %H:%M"%S')))
                    if offense_lastPersistedTime > case_lastPersistedTime:
                        # If time is different then update the case
                        updated_cases.append(case_id)
                        # Create payload to update cases
                        payload['patches'][case_id] = {
                                                "version": case_dict['case_ver']+1,
                                                "changes": [ {
                                                    "old_value": { "date": case_lastPersistedTime },
                                                    "new_value": { "date": offense_lastPersistedTime },
                                                    "field": { "name": "qr_last_updated_time" }
                                                } ]
                                            },
            # If there are changes then fix payload and send put request to SOAR
            if updated_cases:
                # Removes characters added by python that are not needed
                payload_str = str(payload).replace('(','').replace(')','').replace(',,',',')
                payload_str = payload_str[0:payload_str.rfind(",")]+payload_str[payload_str.rfind(",")+1:]
                payload = literal_eval(payload_str)

                # Send put request to SOAR
                # This will update all cases that need to be updated for the give QRadar server
                response = self.rest_client().put("/incidents/patch", payload)
                # If failures dictionary is not empty then raise error
                if response['failures']:
                    raise IntegrationError(str(response))

                LOG.info("Incident: {} updated field: qr_last_updated_time".format(str(updated_cases)))
