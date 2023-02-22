# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Poller implementation"""

from logging import getLogger
from os import path
from threading import Thread
from json import dumps

from resilient_circuits import AppFunctionComponent, is_this_a_selftest
from resilient_lib import (SOARCommon, get_last_poller_date,
                           make_payload_from_template, poller, validate_fields,
                           IntegrationError)

from fn_jira.lib.app_common import AppCommon
from fn_jira.poller.configure_tab import init_incident_groups_tab
from fn_jira.util import helper, poller_helper


PACKAGE_NAME = "fn_jira"
GLOBAL_SETTINGS = f"{PACKAGE_NAME}:global_settings"

LOG = getLogger(__name__)

# Directory of default templates
TEMPLATE_DIR = path.join(path.dirname(__file__), "data")

# Default Templates used to create/update/close SOAR cases.
#   Mostly they will be modified to include custom SOAR fields
CREATE_CASE_TEMPLATE = path.join(TEMPLATE_DIR, "soar_create_case.jinja")
UPDATE_CASE_TEMPLATE = path.join(TEMPLATE_DIR, "soar_update_case.jinja")
CLOSE_CASE_TEMPLATE = path.join(TEMPLATE_DIR, "soar_close_case.jinja")
UPDATE_TASK_TEMPLATE = path.join(TEMPLATE_DIR, "soar_update_task.jinja")

class PollerComponent(AppFunctionComponent):
    """
    poller for escalating SOAR incidents and synchronizing changes
    """

    def __init__(self, opts):
        """
        Constructor provides access to the configuration options

        :param opts: all settings including SOAR settings
        :type opts: dict
        """

        super(PollerComponent, self).__init__(opts, PACKAGE_NAME)
        self.opts = opts
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
        self.global_settings = self.opts.get(GLOBAL_SETTINGS, {})
        self.polling_interval = int(self.global_settings.get("polling_interval", 0))
        if not self.polling_interval or is_this_a_selftest(self):
            LOG.debug("Exiting poller because polling interval set to 0 or this run is a selftest.")
            return False

        LOG.info("Poller initiated, polling interval %s", self.polling_interval)
        self.last_poller_time = get_last_poller_date(int(self.global_settings.get("polling_lookback", 0)))
        LOG.info("Poller lookback: %s", self.last_poller_time)

        # Collect the override templates to use when creating, updating and closing cases
        self.soar_create_case_template = self.global_settings.get("soar_create_case_template")
        self.soar_update_case_template = self.global_settings.get("soar_update_case_template")
        self.soar_close_case_template = self.global_settings.get("soar_close_case_template")
        self.soar_update_task_template = self.global_settings.get("soar_update_task_template")

        # rest_client is used to make IBM SOAR API calls
        self.res_client = self.rest_client()
        self.soar_common = SOARCommon(self.res_client)

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

        # List of the Jira datatable names found in the app.config
        jira_dt_names = []

        # Dictionary of dicts that say what info to get from each SOAR case
        data_to_get_from_case = {"tasks": []}

        # Get list of Jira servers configured in the app.config
        servers_list = helper.JiraServers(self.opts).get_server_name_list()
        # If no servers labeled then add fn_jira to list
        if not servers_list:
            servers_list.append(PACKAGE_NAME)

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
            options = helper.get_server_settings(self.opts, server)

            # Add the datatable name specified in the current app.config
            dt_name = options.get("jira_dt_name")
            if dt_name not in jira_dt_names:
                jira_dt_names.append(dt_name)

            # Get the max_results settings from the global_settings
            max_results = self.global_settings.get("max_issues_returned")
            if not max_results:
                # Get the max_results settings from the servers settings
                max_results = options.get("max_issues_returned")

            # If poller_filters and or max_results are defnined in the global_settings
            poller_filters = self.global_settings.get("poller_filters")
            if poller_filters:
                # Validate poller_filter
                validate_fields([poller_filters_validator], self.global_settings)
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
        soar_cases_list = self.res_client.post(
            "/incidents/query?return_level=normal&handle_format=names",
            self.soar_common._build_search_query({"jira_issue_id": True}, open_cases=True)
        )

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

        for num in range(len(cases_list)):
            # Get the date that needs to be added to the current SOAR case
            data_to_get = data_to_get_from_case.get(cases_list[num].get("properties").get("jira_issue_id"))
            if data_to_get:

                if data_to_get.get("comments"): # If comments were on the linked Jira ticket
                    # Add comment/notes to case
                    poller_helper.SOAR.add_to_case(self.res_client, cases_list, num, "comments")

                if data_to_get.get("attachments"): # If attachments were on the linked Jira ticket
                    # Add attachments to cases
                    poller_helper.SOAR.add_to_case(self.res_client, cases_list, num, "attachments")

            tasks = data_to_get_from_case.get("tasks")
            if tasks:
                for task in tasks:
                    if task.get("incident_id") == cases_list[num].get("id"):
                        task_data_to_get = data_to_get_from_case.get(task.get("task_key"))
                        if task_data_to_get:
                            poller_helper.SOAR.add_task_to_case(self.res_client,
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
        # A list of lists that contain the SOAR case and its corresponding Jira issue
        soar_cases_to_update = []
        soar_cases_to_close = []
        soar_tasks_to_update = []

        # Loop through the Jira servers dict
        for jira_server in jira_issues_dict:

            # List of Jira key for the SOAR cases found that link to the current server
            soar_cases_jira_key = []
            if soar_cases_list:
                # Get the Jira issue keys from the SOAR cases that are linked to the current server
                for soar_case in soar_cases_list:
                    soar_case_jira_server = soar_case.get("properties").get("jira_server")
                    if soar_case_jira_server == jira_server or (not soar_case_jira_server and jira_server == PACKAGE_NAME):
                        soar_cases_jira_key.append(soar_case.get("properties").get("jira_issue_id"))

            # List of Jira Issues that have corresponding SOAR cases
            jira_issues_with_soar_case = []

            # Loop through the Jira issues found in the filtered search on the current server
            for jira_issue in jira_issues_dict.get(jira_server):
                # Get the key for the Jira issue
                jira_issue_key = jira_issue.get("key")
                jira_issue["jira_server"] = jira_server # Add jira_server key to jira_issue

                if helper.check_jira_issue_linked_to_task(jira_issue.get("fields").get("description")):
                    # Add the Jira issue that was found on SOAR to jira_issues_with_soar_case
                    jira_issues_with_soar_case.append(jira_issue)
                elif jira_issue_key in soar_cases_jira_key:
                    # Add the Jira issue that was found on SOAR to jira_issues_with_soar_case
                    jira_issues_with_soar_case.append(jira_issue)
                elif not jira_issue.get("fields").get("resolutiondate"):
                    # If the Jira issue is not found on SOAR than add to jira_issues_to_add_to_soar list
                    jira_issues_to_add_to_soar.append(jira_issue)

            if soar_cases_list:
                # Check if "SOAR Case Last Updated" time is before Jira issue 'Updated' time
                for soar_case in soar_cases_list:
                    soar_tasks = soar_case.get("tasks") # Get the list of tasks from the SOAR case if they exist
                    for jira_issue in jira_issues_with_soar_case:
                        jira_issue_updated = jira_issue.get("fields").get("updated")
                        jira_issue_description = jira_issue.get("fields").get("description") # Get the description of the Jira issue
                        # Check if the Jira issue is linked to a SOAR task that needs to be updated
                        if soar_tasks and helper.check_jira_issue_linked_to_task(jira_issue_description):
                            task_id = helper.get_id_from_jira_issue_description(jira_issue_description)
                            # Loop through all tasks on the SOAR case
                            for task in soar_tasks:
                                if task.get("id") == task_id:
                                    if jira_issue_updated > task.get("datatable").get("cells").get("last_updated").get("value"):
                                        # Add matching SOAR case and Jira issue to soar_tasks_to_update list
                                        soar_tasks_to_update.append([jira_issue, soar_case])
                                        break
                        # Check if SOAR incident needs to be updated
                        if jira_issue.get("key") == soar_case.get("properties").get("jira_issue_id") and\
                        jira_issue_updated > soar_case.get("inc_last_modified_date"):
                            # Check if the Jira issue has been closed
                            if jira_issue.get("fields").get("resolutiondate"):
                                # Add matching SOAR case and Jira issue to soar_cases_to_close list
                                soar_cases_to_close.append([jira_issue, soar_case])
                                break
                            # Add matching SOAR case and Jira issue to soar_cases_to_update list
                            soar_cases_to_update.append([jira_issue, soar_case])
                            break

        # Create new SOAR cases from Jira issues
        if jira_issues_to_add_to_soar:
            for jira_issue in jira_issues_to_add_to_soar:
                self.soar_create_case(jira_issue)
                LOG.info(f"SOAR incident created: {jira_issue.get('summary')}")

        # Close SOAR cases that's linked Jira issue is closed
        if soar_cases_to_close:
            self.soar_close_cases(soar_cases_to_close)

        # Update SOAR tasks with data from linked Jira issues
        if soar_tasks_to_update:
            self.soar_update_tasks(soar_tasks_to_update)

        # Update SOAR cases with data from linked Jira issues
        if soar_cases_to_update:
            # helper.update_soar_incident(self.rest_client(), soar_cases_to_update)
            self.soar_update_cases(soar_cases_to_update)

    def soar_create_case(self, jira_issue):
        """
        Create a new SOAR incident from a Jira issue
        :param jira_issue: Dict of Jira issue data
        :return: None
        """
        soar_create_payload = make_payload_from_template(
            self.soar_create_case_template,
            CREATE_CASE_TEMPLATE,
            jira_issue)
        create_soar_case = self.soar_common.create_soar_case(
            soar_create_payload)

        attachments = jira_issue.get("fields").get("attachment")
        if attachments:
            # Get attachments from the Jira ticket
            for attach in attachments:
                try:
                    # Add the attachment to the SOAR incident
                    self.res_client.post_attachment(f"/incidents/{create_soar_case.get('id')}/attachments",
                                            filepath=None,
                                            filename=attach.get("filename"),
                                            bytes_handle=attach.get("content")
                                            )
                except Exception as err:
                    raise IntegrationError(err)

    def soar_close_cases(self, soar_cases_to_close):
        """
        Close SOAR cases who's linked Jira issue has been closed.
        :param soar_cases_to_close: A list of lists that contain the SOAR cases to close and their corresponding Jira issues.
        :return: None
        """
        soar_close_payload = {"patches": {}}

        for close in soar_cases_to_close:
            soar = close[1]

            payload = make_payload_from_template(
                self.soar_close_case_template,
                CLOSE_CASE_TEMPLATE,
                {"jira": close[0], "soar": soar})

            soar_close_payload["patches"][soar.get("id")] = payload

        # If SOAR soar_close_payload is not empty then close cases
        if soar_close_payload["patches"]:
            # Send put request to SOAR
            # This will close all cases that need to be closed
            self.res_client.put("/incidents/patch", soar_close_payload)

    def soar_update_cases(self, soar_cases_to_update):
        """
        Update the SOAR cases with new data from the corresponding Jira issue
        :param soar_cases_to_update: A list of lists that contain the SOAR case to update and its corresponding Jira issue
        :return: None
        """
        soar_update_payload = {"patches": {}}

        for update in soar_cases_to_update:
            jira = update[0]
            soar = update[1]

            payload = make_payload_from_template(
                self.soar_update_case_template,
                UPDATE_CASE_TEMPLATE,
                {"jira": jira, "soar": soar})

            if payload.get("changes"):
                soar_update_payload["patches"][soar.get("id")] = payload

            # Check if new comments added or old comments changed/deleted
            self.soar_update_comments_attachments(jira, soar, "comment")

            # Check if new attachments added or old attachments deleted
            self.soar_update_comments_attachments(jira, soar, "attachment")

        # If SOAR soar_update_payload is not empty then update fields on cases
        if soar_update_payload["patches"]:
            # Send put request to SOAR
            # This will update all cases that need to be updated
            self.res_client.put("/incidents/patch", soar_update_payload)

    def soar_update_tasks(self, soar_tasks_to_update):
        """
        Update the SOAR tasks with new data from the corresponding Jira issue
        :param soar_tasks_to_update: A list of lists that contain the SOAR tasks to update and its corresponding Jira issue
        :return: None
        """
        soar_task_update_payload = {"patches": {}}

        for update in soar_tasks_to_update:
            jira = update[0]
            soar = update[1]

            payload = make_payload_from_template(
                self.soar_update_task_template,
                UPDATE_TASK_TEMPLATE,
                {"jira": jira, "soar": soar})

            soar_task_update_payload["patches"][soar.get("id")] = payload

    def soar_update_comments_attachments(self, jira, soar, update_type):
        """
        Add comment\attchment to the SOAR case that are in the Jira issue and
        delete comments\attachments that are in the SOAR case and not in the Jira issue
        :param jira: Dict of Jira issue data
        :param soar: Dict of SOAR case data
        :param update_type: Either attachment or comment
        :return: None
        """
        # Get comments\attachments from the Jira issue
        jira_updates = jira.get("fields").pop(update_type) if jira.get("fields").get(update_type) else []
        if update_type == "attachment":
            jira_attachments = jira_updates
            jira_updates = [attach.get("filename") for attach in jira_attachments]
        # Get comments\attachments from the SOAR case
        soar_updates = soar.pop(f"{update_type}s") if soar.get(f"{update_type}s") else []
        # Remove the text "\nAdded from Jira" from comments if present
        if update_type == "comment":
            for num in range(len(soar_updates)):
                update_content = soar_updates[num].get("content")
                soar_updates[num]["content"] = helper.remove_html_tags(update_content.replace("\nAdded from Jira", ""))

        if soar_updates:
            for num, soar_update in enumerate(soar_updates):
                soar_update_content = soar_update.get("content")
                if update_type == "attachment":
                    soar_update_content = soar_update.get("name")
                if soar_update_content in jira_updates: # If comment\attachment on SOAR and Jira then remove it from jira_updates
                    jira_updates.pop(jira_updates.index(soar_update_content))

            # Delete variables that are no longer needed
            del num, soar_update

        if jira_updates:
            for jira_update in jira_updates:
                # Send post request to SOAR
                try:
                    if update_type == "attachment":
                        content = jira_attachments[next((index for (index, attach) in enumerate(jira_attachments) if attach["filename"] == jira_update), None)].get("content")
                        self.res_client.post_attachment(f"/incidents/{soar.get('id')}/attachments", filepath=None, filename=jira_update, bytes_handle=content)
                    else:
                        SOARCommon(self.res_client).create_case_comment(soar.get('id'), f"{jira_update}\nAdded from Jira")
                except Exception as e:
                    raise IntegrationError(str(e))
