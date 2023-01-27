# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Poller"""

from datetime import datetime, timedelta
from logging import getLogger
from threading import Thread
from resilient_circuits import ResilientComponent
from fn_jira.util.helper import GLOBAL_SETTINGS, PACKAGE_NAME, JiraServers,\
    get_id_from_jira_issue_description, get_server_settings, get_jira_client,\
    create_soar_incident, update_soar_incident, check_jira_issue_linked_to_task
from fn_jira.lib.poller_common import SOARCommon, poller, JiraCommon
from resilient_lib import validate_fields

LOG = getLogger(__name__)

class PollerComponent(ResilientComponent):
    """Poller to synchronize Jira tickets and SOAR incidents"""

    def __init__(self, opts):
        """Constructor provides access to the configuration options"""
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

        # List of the Jira datatable names found in the app.config
        jira_dt_names = []

        # Dictionary of dicts that say what info to get from each SOAR case
        data_to_get_from_case = {"tasks": []}

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

            # Add the datatable name specified in the current app.config
            dt_name = options.get("jira_dt_name")
            if dt_name not in jira_dt_names:
                jira_dt_names.append(dt_name)

            # Get the max_results settings from the global_settings
            max_results = global_settings.get("max_issues_returned")
            if not max_results:
                # Get the max_results settings from the servers settings
                max_results = options.get("max_issues_returned")

            # If poller_filters and or max_results are defnined in the global_settings
            poller_filters = global_settings.get("poller_filters")
            if poller_filters:
                # Validate poller_filter
                validate_fields([poller_filters_validator], global_settings)
            else: # If poller_filters is defnined in individual Jira server settings
                # Validate poller_filter
                validate_fields([poller_filters_validator], options)
                # Get the poller_filters settings from the servers settings
                poller_filters = options.get("poller_filters")

            # Get a list of Jira issues bases on the given search filters
            jira_issue_list, data_to_get_from_case = JiraCommon.search_jira_issues(
                                                                self.opts,
                                                                get_jira_client(self.opts, options),
                                                                poller_filters,
                                                                self.last_poller_time,
                                                                max_results,
                                                                data_to_get_from_case
                                                            )
            # Add list of Jira issues to jira_issues_dict under the server the issues where found in
            jira_issues_dict[server] = jira_issue_list

        # Get a list of open SOAR cases that contain the field jira_issue_id.
        soar_cases_list, err_msg = SOARCommon.get_open_soar_cases(self.opts, {"jira_issue_id": True}, self.rest_client(), data_to_get_from_case)

        # Process Jira issues returned from search
        self.process_jira_issue_dict(jira_issues_dict, soar_cases_list, data_to_get_from_case)

    def process_jira_issue_dict(self, jira_issues_dict, soar_cases_list, data_to_get_from_case):
        """
        Process the returned Jira issues
        :param jira_issue_dit: Dictionary of Jira issues based on Jira server
        :param soar_case_list: List of SOAR cases that contain "Jira Issue ID" field
        :param data_to_get_from_case: Dictionary of dicts that say what info to get from each SOAR case
        :return: None
        """

        # List of Jira issues to add as incidents on SOAR
        jira_issues_to_add_to_soar = []

        # A list of lists that contain the SOAR case to update and its corresponding Jira issue
        soar_cases_to_update = []

        # Loop through the Jira servers dict
        for jira_server in jira_issues_dict:
            # Connect to the Jira server specified in options
            jira_client = get_jira_client(self.opts, get_server_settings(self.opts, jira_server))

            # List of Jira key for the SOAR cases found that link to the current server
            soar_cases_jira_key = []
            if soar_cases_list:
                # Get the Jira issue keys from the SOAR cases that are linked to the current server
                for soar_case in soar_cases_list:
                    soar_case_jira_server = soar_case.get("jira_server")
                    if soar_case_jira_server == jira_server or (not soar_case_jira_server and jira_server == PACKAGE_NAME):
                        soar_cases_jira_key.append(soar_case.get("jira_issue_id"))

            # List of Jira Issues that have corresponding SOAR cases
            jira_issues_with_soar_case = []

            # Loop through the Jira issues found in the filtered search on the current server
            for jira_issue in jira_issues_dict.get(jira_server):
                # Get the key for the Jira issue
                jira_issue_key = jira_issue.get("key")
                jira_issue["jira_server"] = jira_server # Add jira_server key to jira_issue

                if check_jira_issue_linked_to_task(jira_issue.get("description")):
                    # Add the Jira issue that was found on SOAR to jira_issues_with_soar_case
                    jira_issues_with_soar_case.append(jira_issue)
                elif jira_issue_key in soar_cases_jira_key:
                    # Add the Jira issue that was found on SOAR to jira_issues_with_soar_case
                    jira_issues_with_soar_case.append(jira_issue)
                    # Remove jira_issue_key from soar_cases_jira_key list
                    soar_cases_jira_key.pop(soar_cases_jira_key.index(jira_issue_key))
                else:
                    # If the Jira issue is not found on SOAR than add to jira_issues_to_add_to_soar list
                    jira_issues_to_add_to_soar.append(jira_issue)

            # Get the Jira issues that are on SOAR that were not returned from the Jira issue search
            if soar_cases_jira_key:
                cases = str(soar_cases_jira_key).replace("[", "(").replace("]", ")")
                jira_issues, data_to_get_from_case = JiraCommon.search_jira_issues(self.opts, jira_client, f"key in {cases}", data_to_get_from_case=data_to_get_from_case)
                for issue_num in range(len(jira_issues)):
                    jira_issues[issue_num]["jira_server"] = jira_server # Add jira_server key to jira_issue
                    jira_issues_with_soar_case.append(jira_issues[issue_num])
                jira_client.close() # Close connection to Jira server

            if soar_cases_list:
                # Check if "SOAR Case Last Updated" time is before Jira issue 'Updated' time
                for soar_case in soar_cases_list:
                    soar_tasks = soar_case.get("tasks") # Get the list of tasks from the SOAR case if they exist
                    for jira_issue in jira_issues_with_soar_case:
                        jira_issue_description = jira_issue.get("description") # Get the description of the Jira issue
                        # Check if the Jira issue is linked to a SOAR task that needs to be updated
                        if soar_tasks and check_jira_issue_linked_to_task(jira_issue_description):
                            task_id = get_id_from_jira_issue_description(jira_issue_description)
                            # Loop through all tasks on the SOAR case
                            for task in soar_tasks:
                                if task.get("id") == task_id:
                                    if jira_issue.get("updated") > task.get("datatable").get("cells").get("last_updated").get("value"):
                                        # Add matching SOAR case and Jira issue to soar_cases_to_update list
                                        soar_cases_to_update.append([jira_issue, soar_case])
                                        break
                        # Check if SOAR incident needs to be updated
                        if jira_issue.get("key") == soar_case.get("jira_issue_id"):
                            soar_case_last_updated = soar_case.get("soar_case_last_updated")
                            if jira_issue.get("updated") > soar_case_last_updated:
                                # Add matching SOAR case and Jira issue to soar_cases_to_update list
                                soar_cases_to_update.append([jira_issue, soar_case])
                                break

        # Create new SOAR cases from Jira issues
        for jira_issue in jira_issues_to_add_to_soar:
            create_soar_incident(self.rest_client(), jira_issue)
            LOG.info(f"SOAR incident created: {jira_issue.get('summary')}")

        # Update SOAR cases with data from linked Jira issues
        if soar_cases_to_update:
            update_soar_incident(self.rest_client(), soar_cases_to_update)
