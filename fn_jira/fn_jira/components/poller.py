# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Poller"""

from datetime import datetime, timedelta
from logging import getLogger
from threading import Thread
from resilient_circuits import ResilientComponent
from fn_jira.util import helper, poller_helper
from fn_jira.lib.poller_common import poller
from resilient_lib import validate_fields, SOARCommon
from fn_jira.poller.configure_tab import init_incident_groups_tab
from fn_jira.lib.app_common import AppCommon

LOG = getLogger(__name__)

class PollerComponent(ResilientComponent):
    """Poller to synchronize Jira tickets and SOAR incidents"""

    def __init__(self, opts):
        """Constructor provides access to the configuration options"""
        super(PollerComponent, self).__init__(opts)
        self.opts = opts
        init_incident_groups_tab()

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
        global_settings = self.opts.get(helper.GLOBAL_SETTINGS, {})
        self.polling_interval = int(global_settings.get("polling_interval", 0))
        if not self.polling_interval:
            return False

        LOG.info(f"Poller initiated, polling interval {self.polling_interval}")
        self.last_poller_time = datetime.now() - timedelta(minutes=int(global_settings.get('polling_lookback', 0)))
        LOG.info(f"Poller lookback: {self.last_poller_time}")

        return True

    @poller('polling_interval', 'last_poller_time')
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
        servers_list = helper.JiraServers(self.opts).get_server_name_list()
        # If no servers labeled then add fn_jira to list
        if not servers_list:
            servers_list.append(helper.PACKAGE_NAME)

        # Get global_setting if definied in the app.config
        global_settings = self.opts.get(helper.GLOBAL_SETTINGS, {})

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
            if server.startswith(f"{helper.PACKAGE_NAME}:"):
                server = server[len(helper.PACKAGE_NAME)+1:]

            # Get settings for server from the app.config
            options = helper.get_server_settings(self.opts, server)

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
            jira_issue_list, data_to_get_from_case = AppCommon(self.opts, options).search_jira_issues(
                poller_filters,
                self.last_poller_time,
                max_results,
                data_to_get_from_case
            )

            # Add list of Jira issues to jira_issues_dict under the server the issues where found in
            jira_issues_dict[server] = jira_issue_list

        # Get a list of open SOAR cases that contain the field jira_issue_id.
        soar_cases_list, err_msg = SOARCommon(self.rest_client()).get_soar_cases({"jira_issue_id": True})

        soar_cases_list = self.process_soar_cases(soar_cases_list, data_to_get_from_case)

        # Process Jira issues returned from search
        self.process_jira_issue_dict(jira_issues_dict, soar_cases_list)

    def process_soar_cases(self, cases_list, data_to_get_from_case):
        """
        Process the SOAR cases
        :param cases_list: List of SOAR cases that contain "Jira Issue ID" field
        :param data_to_get_from_case: Dictionary of dicts that say what info to get from each SOAR case
        :return: Dict of processed SOAR cases
        """
        fields_to_remove = ["perms", "creator", "creator_principal", "exposure_type_id", "workspace", "assessment", "pii",
                            "gdpr", "creator_id", "crimestatus_id", "sequence_code", "owner_id", "phase_id", "org_handle", "task_changes"]

        # Remove case keys that are empty and unused keys
        for num in range(len(cases_list)):
            cases_list[num] = dict([(k,v) for k,v in cases_list[num].items() if v])
            for field in fields_to_remove:
                cases_list[num].pop(field)

            # Change the value of the dict key to the one value that is used in that dict
            for key, value in cases_list[num].get("properties").items():
                cases_list[num][key] = value
            cases_list[num].pop("properties")

            # Get the date that needs to be added to the current SOAR case
            data_to_get = data_to_get_from_case.get(cases_list[num].get("jira_issue_id"))
            if data_to_get:

                if data_to_get.get("comments"): # If comments were on the linked Jira ticket
                    # Add comment/notes to case
                    poller_helper.SOAR.add_to_case(self.rest_client(), cases_list, num, "comments")

                if data_to_get.get("attachments"): # If attachments were on the linked Jira ticket
                    # Add attachments to cases
                    poller_helper.SOAR.add_to_case(self.rest_client(), cases_list, num, "attachments")

            tasks = data_to_get_from_case.get("tasks")
            if tasks:
                for task in tasks:
                    if task.get("incident_id") == cases_list[num].get("id"):
                        task_data_to_get = data_to_get_from_case.get(task.get("task_key"))
                        if task_data_to_get:
                            poller_helper.SOAR.add_task_to_case(self.rest_client(),
                                                        cases_list,
                                                        num,
                                                        task.get("task_id"),
                                                        comments=task_data_to_get.get("comments"),
                                                        attachments=task_data_to_get.get("attachments")
                                                       )

        return cases_list

    def process_jira_issue_dict(self, jira_issues_dict, soar_cases_list):
        """
        Process the returned Jira issues
        :param jira_issue_dit: Dictionary of Jira issues based on Jira server
        :param soar_case_list: List of SOAR cases that contain "Jira Issue ID" field
        :return: None
        """

        # List of Jira issues to add as incidents on SOAR
        jira_issues_to_add_to_soar = []

        # A list of lists that contain the SOAR case to update and its corresponding Jira issue
        soar_cases_to_update = []

        # Loop through the Jira servers dict
        for jira_server in jira_issues_dict:

            # List of Jira key for the SOAR cases found that link to the current server
            soar_cases_jira_key = []
            if soar_cases_list:
                # Get the Jira issue keys from the SOAR cases that are linked to the current server
                for soar_case in soar_cases_list:
                    soar_case_jira_server = soar_case.get("jira_server")
                    if soar_case_jira_server == jira_server or (not soar_case_jira_server and jira_server == helper.PACKAGE_NAME):
                        soar_cases_jira_key.append(soar_case.get("jira_issue_id"))

            # List of Jira Issues that have corresponding SOAR cases
            jira_issues_with_soar_case = []

            # Loop through the Jira issues found in the filtered search on the current server
            for jira_issue in jira_issues_dict.get(jira_server):
                # Get the key for the Jira issue
                jira_issue_key = jira_issue.get("key")
                jira_issue["jira_server"] = jira_server # Add jira_server key to jira_issue

                if helper.check_jira_issue_linked_to_task(jira_issue.get("description")):
                    # Add the Jira issue that was found on SOAR to jira_issues_with_soar_case
                    jira_issues_with_soar_case.append(jira_issue)
                elif jira_issue_key in soar_cases_jira_key:
                    # Add the Jira issue that was found on SOAR to jira_issues_with_soar_case
                    jira_issues_with_soar_case.append(jira_issue)
                elif not jira_issue.get("resolutiondate"):
                    # If the Jira issue is not found on SOAR than add to jira_issues_to_add_to_soar list
                    jira_issues_to_add_to_soar.append(jira_issue)

            if soar_cases_list:
                # Check if "SOAR Case Last Updated" time is before Jira issue 'Updated' time
                for soar_case in soar_cases_list:
                    soar_tasks = soar_case.get("tasks") # Get the list of tasks from the SOAR case if they exist
                    for jira_issue in jira_issues_with_soar_case:
                        jira_issue_description = jira_issue.get("description") # Get the description of the Jira issue
                        # Check if the Jira issue is linked to a SOAR task that needs to be updated
                        if soar_tasks and helper.check_jira_issue_linked_to_task(jira_issue_description):
                            task_id = helper.get_id_from_jira_issue_description(jira_issue_description)
                            # Loop through all tasks on the SOAR case
                            for task in soar_tasks:
                                if task.get("id") == task_id:
                                    if jira_issue.get("updated") > task.get("datatable").get("cells").get("last_updated").get("value"):
                                        # Add matching SOAR case and Jira issue to soar_cases_to_update list
                                        soar_cases_to_update.append([jira_issue, soar_case])
                                        break
                        # Check if SOAR incident needs to be updated
                        if jira_issue.get("key") == soar_case.get("jira_issue_id"):
                            if jira_issue.get("updated") > soar_case.get("inc_last_modified_date"):
                                # Add matching SOAR case and Jira issue to soar_cases_to_update list
                                soar_cases_to_update.append([jira_issue, soar_case])
                                break

        # Create new SOAR cases from Jira issues
        for jira_issue in jira_issues_to_add_to_soar:
            helper.create_soar_incident(self.rest_client(), jira_issue)
            LOG.info(f"SOAR incident created: {jira_issue.get('summary')}")

        # Update SOAR cases with data from linked Jira issues
        if soar_cases_to_update:
            helper.update_soar_incident(self.rest_client(), soar_cases_to_update)
