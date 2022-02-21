# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""Function implementation"""

import datetime
import logging
from threading import Thread
from resilient_circuits import ResilientComponent
from resilient import get_client
from fn_qradar_enhanced_data.lib.poller_common import SOARCommon, poller
from fn_qradar_enhanced_data.lib.app_common import AppCommon
from fn_qradar_enhanced_data.util.qradar_constants import PACKAGE_NAME, GLOBAL_SETTINGS

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
        cases_list, error_msg = self.soar_common.get_open_soar_cases(["qradar_id", "qradar_destination"])
        print(cases_list)

    def process_entity_list(self, entity_list):
        """Perform all the processing on the entity list, creating, updating and closing SOAR
           cases based on the states of the endpoint entities
        Args:
            entity_list (list): list of endpoint entities to check again SOAR cases
        """

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
