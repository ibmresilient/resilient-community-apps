# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Poller"""

from datetime import datetime, timedelta
from logging import getLogger
from threading import Thread
from resilient_circuits import ResilientComponent
from fn_jira.util.helper import GLOBAL_SETTINGS, PACKAGE_NAME, JiraServers, get_server_settings, get_jira_client
from fn_jira.lib.poller_common import SOARCommon, poller, JiraCommon
from resilient_lib import validate_fields

LOG = getLogger(__name__)

class PollerComponent(ResilientComponent):
    """Poller to synchronize Jira tickets and SOAR incidents"""

    def __init__(self, opts):
        """Constructor provides access to the configuration options"""
        super(PollerComponent, self).__init__(opts)
        self.opts = opts

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

        LOG.info(f"Poller initiated, polling interval {self.polling_interval}")
        self.last_poller_time = datetime.now() - timedelta(minutes=int(global_settings.get('polling_lookback', 0)))
        LOG.info(f"Poller lookback: {self.last_poller_time}")

        return True

    @poller('polling_interval', 'last_poller_time', PACKAGE_NAME)
    def run(self, last_poller_time=None):
        """
        Get a list of open SOAR cases that contain the field jira_issue_id.
        Get a list of Jira issues bases on the given search filters.
        :param last_poller_time: (int) Time in milliseconds when the last poller ran
        :return: None
        """

        # Get a list of open SOAR cases that contain the field jira_issue_id.
        soar_case_list, err_msg = SOARCommon.get_open_soar_cases({"jira_issue_id": True}, self.rest_client())

        # Get list of Jira servers configured in the app.config
        servers_list = JiraServers(self.opts).get_server_name_list()
        # If no servers labeled then add fn_jira to list
        if not servers_list:
            servers_list.append(PACKAGE_NAME)

        # Get global_setting if definied in the app.config
        global_settings = self.opts.get(GLOBAL_SETTINGS, {})

        # Validation dictionary for the "poller_filters" app.config setting
        poller_filters_validator = {"name": "poller_filters",
                                   "placeholder": "priority in (high, medium, low) and "\
                                   "status in ('to do', 'in progress', done) and project in "\
                                   "(project_name1, project_name2)"}

        # Dictionary for Jira Issues
        jira_issues_dict = {}

        # Loop through all the Jira servers in the app.config
        for server in servers_list:

            # If multiple servers are define get just the servers label
            if server.startswith(f"{PACKAGE_NAME}:"):
                server = server[len(PACKAGE_NAME)+1:]

            # Get settings for server from the app.config
            options = get_server_settings(self.opts, server)
            # Connect to the Jira server specified in options
            jira_client = get_jira_client(self.opts, options)
            # Get the max_results settings from the servers settings
            max_results = options.get("max_issues_returned")

            # If poller_filters and or max_results are defnined in the global_settings
            if global_settings:
                poller_filters = global_settings.get("poller_filters")
                if poller_filters:
                    # Validate poller_filter
                    validate_fields([poller_filters_validator], global_settings)
                # Get the max_results settings from the global_settings
                max_results = global_settings.get("max_issues_returned")
            else: # If poller_filters is defnined in individual Jira server settings
                # Validate poller_filter
                validate_fields([poller_filters_validator], options)
                # Get the poller_filters settings from the servers settings
                poller_filters = options.get("poller_filters")

            # Get a list of Jira issues bases on the given search filters
            jira_issue_list = JiraCommon.search_jira_issues(jira_client, poller_filters, max_results)
            # Add list of Jira issues to jira_issues_dict under the server the issues where found in
            jira_issues_dict[server] = jira_issue_list

        # Process Jira issues returned from search
        self.process_jira_issue_dict(jira_issues_dict, soar_case_list)

    def process_jira_issue_dict(self, jira_issue_dict, soar_case_list):
        """
        Process the returned Jira issues
        :param case_list: List of Jira issues
        :return: None
        """

        print("f")

