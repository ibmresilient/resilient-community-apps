# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""Function implementation"""

import datetime
import logging
import json
import ast
from threading import Thread
import fn_qradar_enhanced_data.util.qradar_graphql_queries as qradar_graphql_queries
from resilient_circuits import ResilientComponent
from resilient import get_client
from resilient_lib import IntegrationError
from fn_qradar_enhanced_data.lib.poller_common import SOARCommon, poller
from fn_qradar_enhanced_data.lib.app_common import AppCommon
from fn_qradar_enhanced_data.util.qradar_constants import PACKAGE_NAME, GLOBAL_SETTINGS
from fn_qradar_enhanced_data.util.qradar_utils import QRadarServers

LOG = logging.getLogger(__name__)

def init_app(rc, options):
    """ intialize settings used for your app
    Args:
        rc (obj): RequestsCommon class for making API calls
        options (dict): app.config settings for the app
    Returns:
        obj: class to app class for ongoing API calls
    """
    # initialize the class for making API calls to your endpoint
    endpoint_class = AppCommon(rc, options)

    return endpoint_class

class PollerComponent(ResilientComponent):
    """
    poller for escalating SOAR incidents and synchronizing changes
    """

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(PollerComponent, self).__init__(opts)
        self.global_settings = opts.get(GLOBAL_SETTINGS, {})
        self.opts = opts

        # collect settings necessary and initialize libraries used by the poller
        if not self._init_env(opts):
            LOG.info(u"Poller interval is not configured.  Automated escalation is disabled.")
            return

        poller_thread = Thread(target=self.run)
        poller_thread.daemon = True
        poller_thread.start()

    def _init_env(self, opts):
        """[initialize the environment based on app.config settings]
        Args:
            opts ([dict]): [all settings including SOAR settings]
        Returns:
            [bool]: [True if poller is configured]
        """
        self.polling_interval = int(self.global_settings.get("polling_interval", 0))
        if not self.polling_interval:
            return False

        LOG.info(u"Poller initiated, polling interval %s", self.polling_interval)
        self.last_poller_time = self._get_last_poller_date(int(self.global_settings.get('polling_lookback', 0)))
        LOG.info("Poller lookback: %s", self.last_poller_time)

        # rest_client is used to make IBM SOAR API calls
        self.rest_client = get_client(opts)
        self.soar_common = SOARCommon(self.rest_client)

        return True

    @poller('polling_interval', 'last_poller_time', PACKAGE_NAME)
    def run(self, last_poller_time=None):
        """[Process to query for changes in datasource entities and the cooresponding update SOAR case]
           The steps taken are to
           1) query SOAR for all open entities associated with the datasource
           2) query datasource entities for changes based on these incidents
           3) determine SOAR actions to take: create, update case or close
        Args:
            last_poller_time ([int]): [time in milliseconds when the last poller ran]
        """
        case_list, error_msg = self.soar_common.get_open_soar_cases(["qradar_id", "qradar_destination"])

        if error_msg:
            raise IntegrationError(error_msg)

        self.process_case_list(case_list)

    def process_case_list(self, case_list):
        """
        Process the open cases
        :param case_list: list of open cases
        :return:
        """

        # :Start: Create dictionary of the QRadar servers to query
        # This is created, so that each QRadar server is only queried once
        case_server_dict = {}
        for case in case_list:
            qradar_id = case["properties"]["qradar_id"]
            qradar_destination = case["properties"]["qradar_destination"]
            case_lastUpdatedTime = case["properties"]["qr_offense_last_updated_time"]
            case_id = case['id']
            case_ver = case['vers']
            if qradar_destination not in case_server_dict:
                case_server_dict[qradar_destination] = {}
            case_server = case_server_dict[qradar_destination]
            # Add the case_id and case_lastUpdatedTime fields to the qradar_id dictionary
            # that is inside of the QRadar servers dictionary
            if qradar_id not in case_server:
                case_server[qradar_id] = {"case_id": case_id, "case_lastUpdatedTime": case_lastUpdatedTime, "case_ver": case_ver}
        # :End: QRadar servers dictionary

        for server in case_server_dict:
            qradar_client = QRadarServers.get_qradar_client(self.opts, server)
            # :Start: Create the filter string to filter for cases in SOAR
            filter_var = ""
            id_list = list(case_server_dict[server].keys())
            for id in id_list:
                filter_var = "{} id={}".format(filter_var, str(id))
                if id_list.index(id) != len(id_list)-1:
                    filter_var = "{} OR".format(filter_var)
            # :End: Filter string creation

            # Set variables that will be in the QRadar query
            variables = {"limit": 0, "offset": 0, "orderBy": "LAST_UPDATED_TIME_ASC", "filter": filter_var}
            # Run the QRadar Query and recieve the returned dictionary
            offenses = qradar_client.graphql_query(variables, qradar_graphql_queries.GRAPHQL_OPENOFFENSESLASTUPDATE)
            offenses_update_list = offenses["content"]

            payload = { "patches": {} }

            # Iterate through list of offenses recieved from QRadar query
            for offense in offenses_update_list:
                offense_lastUpdatedTime = int(offense['lastUpdatedTime'])
                case_dict = case_server_dict[server][offense['id']]
                case_id = case_dict['case_id']
                case_lastUpdatedTime = case_dict['case_lastUpdatedTime']
                case_ver = case['vers']
                if offense_lastUpdatedTime != case_lastUpdatedTime:
                    # If time is different then update the case
                    patches = payload['patches']
                    patches[case_id] = {
                                            "version": case_ver+1,
                                            "changes": [ {
                                                "old_value": { "date": case_lastUpdatedTime },
                                                "new_value": { "date": offense_lastUpdatedTime },
                                                "field": { "name": "qr_offense_last_updated_time" }
                                            } ]
                                        },
            payload_str = str(payload).replace('(','').replace(')','').replace(',,',',')
            payload_str = payload_str[0:payload_str.rfind(",")]+payload_str[payload_str.rfind(",")+1:]
            payload = ast.literal_eval(payload_str)

            response = self.rest_client.put("/incidents/patch", payload)
            if response['failures']:
                raise IntegrationError(str(response))

            LOG.info("Incident: {} updated field: qr_offense_last_updated_time with value: {}".format(case_id, offense_lastUpdatedTime))

    def _get_last_poller_date(self, polling_lookback):
        """get the last poller datetime based on a lookback value
        Args:
            polling_lookback ([number]): # of minutes to lookback
        Returns:
            [datetime]: [datetime to use for last poller run time]
        """
        return self._get_timestamp() - datetime.timedelta(minutes=polling_lookback)

    def _get_timestamp(self):
        """get the existing timestamp
        Returns:
            datetime: current datetime
        """
        return datetime.datetime.now()
