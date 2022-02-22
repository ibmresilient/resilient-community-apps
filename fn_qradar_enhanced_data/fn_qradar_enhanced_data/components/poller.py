# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""Function implementation"""

import datetime
import logging
from threading import Thread
import fn_qradar_enhanced_data.util.qradar_graphql_queries as qradar_graphql_queries
from resilient_circuits import ResilientComponent
from resilient import get_client
from resilient_lib import IntegrationError
from fn_qradar_enhanced_data.lib.poller_common import SOARCommon, poller
from fn_qradar_enhanced_data.lib.app_common import AppCommon
from fn_qradar_enhanced_data.util.qradar_constants import PACKAGE_NAME, GLOBAL_SETTINGS
from fn_qradar_enhanced_data.util.function_utils import get_servers_list
from fn_qradar_enhanced_data.util.qradar_utils import QRadarServers, QRadarClient

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

        #Figure out how to sort to case_list by qradar_server, so that qradar is called as little as possible

        # Connect to the qradar server for the given case
        # qradar_client = QRadarServers.get_qradar_client(self.opts, qradar_destination)

        # open_offenses_last_updated_times = qradar_client.graphql_query(variables, qradar_graphql_queries.GRAPHQL_OPENOFFENSESLASTUPDATE)

        # for case in case_list:
        #     for offense in open_offenses_last_updated_times["content"]:
        #         if case["properties"]["qradar_id"] == offense[""]:
        #             pass

        for case in case_list:
            # Get variables from the case
            qradar_id = case["properties"]["qradar_id"]
            qradar_destination = case["properties"]["qradar_destination"]
            case_lastUpdatedTime = case["properties"]["qr_offense_last_updated_time"]
            case_id = case['id']

            # Connect to the qradar server for the given case
            qradar_client = QRadarServers.get_qradar_client(self.opts, qradar_destination)

            variables = {"limit": 0,"offset": 0,"orderBy": "LAST_UPDATED_TIME_ASC","filter": "status=OPEN"}
            offenses_update = qradar_client.graphql_query(variables, qradar_graphql_queries.GRAPHQL_OPENOFFENSESLASTUPDATE)

            # Query the offense for the last updated time
            offense_update = qradar_client.get_offense_last_updated_time(qradar_id)
            offense_lastUpdatedTime = int(offense_update['content']['lastUpdatedTime'])
            # Compare last updated time of the offense to the case 
            if offense_lastUpdatedTime != case_lastUpdatedTime:
                # If time is different then update the case
                payload = { "properties": 
                            { "qr_offense_last_updated_time": offense_lastUpdatedTime }
                          }
                self.soar_common.update_soar_case(case_id, payload)
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
