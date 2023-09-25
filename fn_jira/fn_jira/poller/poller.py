# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
"""Poller implementation"""

from logging import getLogger
from os import path
from threading import Thread
from datetime import timezone, timedelta, datetime

from resilient_circuits import AppFunctionComponent, is_this_a_selftest
from resilient_lib import (SOARCommon, get_last_poller_date, clean_html,
                           make_payload_from_template, poller, validate_fields)

from fn_jira.lib.app_common import AppCommon, add_task_to_case, add_to_case
from fn_jira.poller.configure_tab import init_incident_groups_tab
from fn_jira.util.helper import (GLOBAL_SETTINGS, PACKAGE_NAME, JiraServers,
                                 check_jira_issue_linked_to_task,
                                 get_id_from_jira_issue_description,
                                 get_server_settings)

LOG = getLogger(__name__)

# SOAR template names
create_case = "soar_create_case_template"
update_case = "soar_update_case_template"
close_case = "soar_close_case_template"

# Directory of default templates
TEMPLATE_DIR = path.join(path.dirname(__file__), "data")

# Default Templates used to create/update/close SOAR cases.
#  Mostly they will be modified to include custom SOAR fields
CREATE_CASE_TEMPLATE = path.join(TEMPLATE_DIR, f"{create_case}.jinja")
UPDATE_CASE_TEMPLATE = path.join(TEMPLATE_DIR, f"{update_case}.jinja")
CLOSE_CASE_TEMPLATE = path.join(TEMPLATE_DIR, f"{close_case}.jinja")

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
        self.poller_lookback = int(self.global_settings.get("polling_lookback", 0))
        self.last_poller_time = get_last_poller_date(self.poller_lookback).astimezone(timezone.utc)
        LOG.info("Minutes for poller to lookback: %s", self.poller_lookback)

        # Collect the override templates to use when creating, updating and closing cases
        self.soar_create_case_template = self.global_settings.get(f"{create_case}")
        self.soar_update_case_template = self.global_settings.get(f"{update_case}")
        self.soar_close_case_template = self.global_settings.get(f"{close_case}")

        # rest_client is used to make IBM SOAR API calls
        self.res_client = self.rest_client()
        self.soar_common = SOARCommon(self.res_client)

        return True

    def set_time_offset(self, last_poller_time, offset):
        """
        Offset time from UTC time by user given value
        :param last_poller_time: datetime object of last time the poller ran
        :param offset: [str] User given time offset
        :return: Datetime object
        """
        last_poller_time = last_poller_time - timedelta(minutes=self.poller_lookback)

        offset_minutes = 0
        offset_hours = 0

        def make_int(time_offset):
            """
            Make string time offset into int
            :param time_offset: string time offset
            :return: int time offset
            """
            if time_offset.startswith("0"):
                time_offset = time_offset[1:]
            return int(time_offset) if time_offset else 0

        # Get minutes to offset if present
        if ":" in offset:
            offset_minutes = offset[offset.index(":")+1:].strip()
            offset_minutes = make_int(offset_minutes)
            # Remove the minutes offset from offset variable
            offset = offset[0:offset.index(":")]

        if offset.startswith("-"):
            offset_hours = offset[offset.index("-")+1:].strip()
            offset_hours = make_int(offset_hours)
            last_poller_time = last_poller_time - timedelta(hours=offset_hours, minutes=offset_minutes)
        elif offset.startswith("+"):
            offset_hours = offset[offset.index("+")+1:].strip()
            offset_hours = make_int(offset_hours)
            last_poller_time = last_poller_time + timedelta(hours=offset_hours, minutes=offset_minutes)

        return last_poller_time

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
        servers_list = JiraServers(self.opts).get_server_name_list()
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
            options = get_server_settings(self.opts, server)

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

            last_poller_time = datetime.fromtimestamp(kwargs.get("last_poller_time") / 1e3)
            last_poller = last_poller_time
            # Set last_poller_time to correct timezone based off user given offset
            if self.global_settings.get("timezone_offset"):
                # If timezone_offset configured in global_settings
                last_poller = self.set_time_offset(last_poller_time, self.global_settings.get("timezone_offset"))
            elif options.get("timezone_offset"):
                # If timezone_offset configured in individual server settings
                last_poller = self.set_time_offset(last_poller_time, options.get("timezone_offset"))

            # Get a list of Jira issues bases on the given search filters
            jira_issue_list, data_to_get_from_case = AppCommon(self.opts, options).search_jira_issues(
                poller_filters,
                last_poller,
                max_results,
                data_to_get_from_case
            )

            # Add list of Jira issues to jira_issues_dict under the server the issues where found in
            jira_issues_dict[server] = jira_issue_list

        # Query used for getting SOAR incidents that are linked to Jira issues
        query = {
            "filters": [{
                "conditions": [
                    {"field_name": "plan_status", "method": "equals", "value": "A"},
                    {"field_name": "properties.jira_linked_to_incident", "method": "equals", "value": True}
                ]}
            ],
            "sorts": [{"field_name": "create_date", "type": "desc"}]
        }

        # Get a list of open SOAR cases that contain the field jira_issue_id.
        soar_cases_list = self.res_client.post("/incidents/query?return_level=normal&handle_format=names", query)

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
                    add_to_case(self.soar_common, cases_list, num, "comments")

                if data_to_get.get("attachments"): # If attachments were on the linked Jira ticket
                    # Add attachments to cases
                    add_to_case(self.soar_common, cases_list, num, "attachments")

            options = get_server_settings(self.opts, cases_list[num].get("properties").get("jira_server"))

            tasks = data_to_get_from_case.get("tasks")
            if tasks:
                for task in tasks:
                    if task.get("incident_id") == cases_list[num].get("id"):
                        task_data_to_get = data_to_get_from_case.get(task.get("task_key"))
                        if task_data_to_get:
                            add_task_to_case(self.soar_common,
                                options,
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

                if check_jira_issue_linked_to_task(jira_issue.get("fields").get("description")):
                    # Add the Jira issue that was found on SOAR to jira_issues_with_soar_case
                    jira_issues_with_soar_case.append(jira_issue)
                elif jira_issue_key in soar_cases_jira_key:
                    # Add the Jira issue that was found on SOAR to jira_issues_with_soar_case
                    jira_issues_with_soar_case.append(jira_issue)
                elif not jira_issue.get("fields").get("resolutiondate"):
                    # If the Jira issue is not found on SOAR than add to jira_issues_to_add_to_soar list
                    jira_issues_to_add_to_soar.append(jira_issue)

            if soar_cases_list:
                for soar_case in soar_cases_list:
                    soar_tasks = soar_case.get("tasks") # Get the list of tasks from the SOAR case if they exist
                    for jira_issue in jira_issues_with_soar_case:
                        jira_issue_description = jira_issue.get("renderedFields").get("description") # Get the description of the Jira issue
                        # Check if the Jira issue is linked to a SOAR task that needs to be updated
                        if soar_tasks and check_jira_issue_linked_to_task(jira_issue_description):
                            task_id = get_id_from_jira_issue_description(jira_issue_description)
                            # Loop through all tasks on the SOAR case
                            for task in soar_tasks:
                                if task.get("id") == task_id:
                                    # Add matching SOAR case and Jira issue to soar_tasks_to_update list
                                    soar_tasks_to_update.append([jira_issue, task])
                                    break
                        # Check if SOAR incident needs to be updated
                        if jira_issue.get("key") == soar_case.get("properties").get("jira_issue_id"):
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
            self.soar_create_case(jira_issues_to_add_to_soar)

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

    def set_poller_templates(self, server_label, template_name):
        """
        Set the paths to the poller templates
        :param server_label: The label for the Jira server in the app.config
        :return: Poller template
        """
        options = get_server_settings(self.opts, server_label)

        # Collect the override templates to use when creating, updating and closing cases
        # If a path to a poller template is set in the indiviual Jira server configs, then it will ignore
        #  setting in the Global_settings
        if template_name == "create_case":
            return options.get(create_case) if options.get(create_case) else self.soar_create_case_template
        elif template_name == "update_case":
            return options.get(update_case) if options.get(update_case) else self.soar_update_case_template
        elif template_name == "close_case":
            return options.get(close_case) if options.get(close_case) else self.soar_close_case_template

    def soar_create_case(self, jira_issues_to_add_to_soar):
        """
        Create a new SOAR incident from a Jira issue
        :param jira_issues_to_add_to_soar: Dict of Jira issues
        :return: None
        """
        for jira_issue in jira_issues_to_add_to_soar:
            jira_issue["renderedFields"]["description"] = jira_issue.get("renderedFields", {}).get("description").replace('"', "'")
            # Set comments to list of comments
            jira_issue["renderedFields"]["comment"] = [comment.get("body", "").replace('"', "'") for comment in jira_issue.get("renderedFields", {}).get("comment").get("comments")]

            # Create payload for creating SOAR incident from template
            soar_create_payload = make_payload_from_template(
                self.set_poller_templates(jira_issue.get("jira_server"), "create_case"),
                CREATE_CASE_TEMPLATE,
                jira_issue)

            # Make call to SOAR to create incident
            create_soar_case = self.soar_common.create_soar_case(
                soar_create_payload)
            LOG.info(f"SOAR incident created: {jira_issue.get('summary')}")

            attachments = jira_issue.get("fields").get("attachment")
            if attachments:
                # Get attachments from the Jira ticket
                for attach in attachments:
                    # Add the attachment to the SOAR incident
                    self.res_client.post_attachment(f"/incidents/{create_soar_case.get('id')}/attachments",
                        filepath=None,
                        filename=attach.get("filename"),
                        bytes_handle=attach.get("content"))

    def soar_close_cases(self, soar_cases_to_close):
        """
        Close SOAR cases who's linked Jira issue has been closed.
        :param soar_cases_to_close: A list of lists that contain the SOAR cases to close and their corresponding Jira issues.
        :return: None
        """
        soar_close_payload = {"patches": {}}

        for close in soar_cases_to_close:
            soar = close[1]
            jira = close[0]
            LOG.debug(f"Closing SOAR incident: {soar.get('id')} and Jira issue: {jira.get('key')}")

            payload = make_payload_from_template(
                self.set_poller_templates(jira.get("jira_server"), "close_case"),
                CLOSE_CASE_TEMPLATE,
                {"jira": jira, "soar": soar})

            # Create new payload that will only have changes that have different old and new values
            new_payload = filter_out_identical_changes(payload)

            if new_payload.get("changes"):
                soar_close_payload["patches"][soar.get("id")] = new_payload

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
            LOG.debug(f"Updating SOAR incident: {soar.get('id')} with Jira issue: {jira.get('key')}")

            payload = make_payload_from_template(
                self.set_poller_templates(jira.get("jira_server"), "update_case"),
                UPDATE_CASE_TEMPLATE,
                {"jira": jira, "soar": soar})

            # Create new payload that will only have changes that have different old and new values
            new_payload = filter_out_identical_changes(payload)

            if new_payload.get("changes"):
                soar_update_payload["patches"][soar.get("id")] = new_payload

            # Check if new comments added or old comments changed
            self.soar_update_comments(jira, soar)

            # Check if new attachments added
            self.soar_update_attachments(jira, soar)

        # If SOAR soar_update_payload is not empty then update fields on cases
        if soar_update_payload["patches"]:
            try:
                # Send put request to SOAR
                # This will update all cases that need to be updated
                response = self.res_client.put("/incidents/patch", soar_update_payload)
                LOG.debug(str(response))
            except Exception as err:
                LOG.error(str(err))

    def soar_update_comments(self, jira, soar):
        """
        Update SOAR incident with new comments on the linked Jira issue
        :param jira: Dict of Jira issue data
        :param soar: Dict of SOAR case data
        :return: None
        """
        # List of comments from the SOAR incident
        soar_comments = [clean_html(comment.get("content", "").replace("Added from Jira", "")) for comment in soar.get("comments", [])]
        # List of comments from the Jira issue
        jira_comments = [comment.get("body", "").replace("\n", "").replace("Added from Jira", "") for comment in jira.get("renderedFields", {}).get("comment").get("comments", [])]

        if jira_comments:
            for comment in jira_comments:
                if clean_html(comment) not in soar_comments:
                    comment_payload = {
                        "text": {
                            "format": "html",
                            "content": f"{comment}<br/>Added from Jira"
                        }
                    }
                    self.res_client.post(f"/incidents/{soar.get('id')}/comments", comment_payload)

    def soar_update_attachments(self, jira, soar):
        """
        Update SOAR incident with new attachments on the linked Jira issue
        :param jira: Dict of Jira issue data
        :param soar: Dict of SOAR case data
        :return: None
        """
        jira_attachments = jira.get("fields").pop("attachment") if jira.get("fields").get("attachment") else []
        soar_attachments = soar.pop("attachments") if soar.get("attachments") else []

        new_attachments_names = [at.get("filename") for at in jira_attachments\
            if at.get("filename") not in [s_attach.get("name") for s_attach in soar_attachments]]

        for attch_name in new_attachments_names:
            content = jira_attachments[next((index for (index, attach) in enumerate(jira_attachments) if attach["filename"] == attch_name), None)].get("content")
            self.res_client.post_attachment(f"/incidents/{soar.get('id')}/attachments", filepath=None, filename=attch_name, bytes_handle=content)

    # SOAR task functions
    def soar_update_tasks(self, soar_tasks_to_update):
        """
        Update the SOAR tasks with new data from the corresponding Jira issue
        :param soar_tasks_to_update: A list of lists that contain the SOAR tasks to update and its corresponding Jira issue
        :return: None
        """

        def close_task_status(task):
            task["status"] = "C"
            return task

        for update in soar_tasks_to_update:
            jira = update[0]
            task = update[1]

            # Update comments
            self.update_task_comments(task, jira)

            # Update attachments
            self.update_task_attachments(task, jira)

            # Update datatable
            self.update_task_datatable(task, jira)

            # If the Jira issue has a resolutiondate then the issue is closed
            if jira.get("fields", {}).get("resolutiondate") and not task.get("closed_date"):
                try:
                    self.res_client.get_put(f"/tasks/{task.get('id')}", lambda soar_task: close_task_status(soar_task))
                except Exception as err:
                    LOG.error(str(err))

    def update_task_comments(self, task, jira):
        """
        Update the task comments
        :param task: Dictionary of data from the SOAR task
        :param jira: Dictionary of data from the Jira issue
        :return: None
        """
        # SOAR Task comments
        task_comments = [clean_html(note.get("text").replace("Added from Jira", "")) for note in task.get("notes", []) if "Added Jira Issue:" not in note.get("text")]
        # Jira issue comments
        jira_comments = [comment.get("body").replace("\n", "").replace("Added from Jira", "") for comment in jira.get("renderedFields").get("comment").get("comments", [])]

        # Update comments/notes
        if jira_comments:
            for comment in jira_comments:
                if clean_html(comment) not in task_comments:
                    comment_payload = {
                        "text": {
                            "format": "html",
                            "content": f"{comment}<br/>Added from Jira"
                        },
                        "is_deleted": False
                    }
                    self.res_client.post(f"/tasks/{task.get('id')}/comments", comment_payload)

    def update_task_attachments(self, task, jira):
        """
        Update task attachments
        :param task: Dictionary of data from the SOAR task
        :param jira: Dictionary of data from the Jira issue
        :param res_client: Connection to SOAR
        :return: None
        """
        attachments = jira.get("fields").get("attachment")
        if attachments:
            task_attachments = [att.get("name") for att in task.get("attachments")]
            for attach in attachments:
                filename = attach.get("filename")
                if filename not in task_attachments:
                    self.res_client.post_attachment(f"/tasks/{task.get('id')}/attachments", filepath=None, filename=filename, bytes_handle=attach.get("content"))

    def update_task_datatable(self, task, jira):
        """
        Update data table on SOAR with new information from the updated task
        :param task: Dictionary of data from the SOAR task
        :param jira: Dictionary of data from the Jira issue
        :param res_client: Connection to SOAR
        :return: None
        """
        datatable = task.get('datatable')
        datatable_cells = datatable.get("cells")
        # Boolean to define if there is new data to add to the datatable
        datatable_new_data = False

        d_payload = {
            "id": datatable.get("id"),
            "version": datatable.get("version")
        }
        d_payload["cells"] = {cell: { "value": datatable_cells[cell].get("value")} for cell in datatable_cells}

        jira_updated = jira.get("fields").get("updated")
        # If Jira issue updated time is different from the last_updated time in the SOAR datatable
        if d_payload.get("cells").get("last_updated").get("value") < jira_updated:
            datatable_new_data = True
            d_payload["cells"]["last_updated"]["value"] = jira_updated

        jira_status = jira.get("fields").get("status").get("name")
        # If Jira issue status is different from the status in the SOAR datatable
        if d_payload.get("cells").get("status").get("value") != jira_status:
            datatable_new_data = True
            d_payload["cells"]["status"]["value"] = jira_status

        if datatable_new_data: # If equals True
            self.res_client.put(f"/incidents/{task.get('inc_id')}/table_data/{datatable.get('table_id')}/row_data/{datatable.get('id')}", d_payload)

def filter_out_identical_changes(payload):
    """
    Filter out changes in the payload that are identical
    :param payload: SOAR update payload
    :return: Payload with only new fields
    """
    new_payload = payload.copy()
    new_payload["changes"] = []

    for soar_change in payload.get("changes"):
        if soar_change.get("old_value").get("textarea") and soar_change.get("old_value").get("textarea").get("format") == "html":
            old_value = clean_html(soar_change.get("old_value").get("textarea").get("content"))
            new_value = clean_html(soar_change.get("new_value").get("textarea").get("content"))
            if old_value != new_value:
                new_payload["changes"].append(soar_change)
        elif soar_change.get("old_value") != soar_change.get("new_value"):
            new_payload["changes"].append(soar_change)

    return new_payload