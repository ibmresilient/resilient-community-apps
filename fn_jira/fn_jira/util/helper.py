# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# -*- coding: utf-8 -*-

from resilient_lib import IntegrationError, MarkdownParser, SOARCommon
from re import compile
from datetime import datetime

PACKAGE_NAME = "fn_jira"
GLOBAL_SETTINGS = f"{PACKAGE_NAME}:global_settings"

# Jira datatable constants
DEFAULT_JIRA_DT_NAME = "jira_task_references" # Can be overridden with app.config jira_dt_name value
JIRA_DT_ISSUE_LINK_COL_NAME = "jira_link"
IBM_SOAR_LINK = "IBM SOAR Link:"
html_tags = compile('<.*?>')

class JiraServers():
    def __init__(self, opts):
        self.servers, self.server_name_list = self._load_servers(opts)

    def _load_servers(self, opts):
        """
        Create list of label names and a dictionary of the servers and their configs
        :param opts: Dict of options
        :return servers: Dictionary of all the Jira servers from the app.config that contains each servers configurations
        :return server_name_list: List filled with all of the labels for the servers from the app.config
        """
        servers = {}
        server_name_list = self._get_server_name_list(opts)
        for server in server_name_list:
            server_data = opts.get(server)
            if not server_data:
                raise KeyError(f"Unable to find Jira server: {server}")

            servers[server] = server_data

        return servers, server_name_list

    def jira_label_test(self, jira_label, servers_list):
        """
        Check if the given jira_label is in the app.config
        :param jira_label: User selected server
        :param servers_list: List of jira servers
        :return: Dictionary of options for the selected server
        """
        # If label not given and using previous versions app.config [fn_jira]
        if not jira_label and servers_list.get(PACKAGE_NAME):
            return servers_list[PACKAGE_NAME]
        elif not jira_label:
            raise IntegrationError("No label was given and is required if servers are labeled in the app.config")

        label = f"{PACKAGE_NAME}:{jira_label}"
        if jira_label and label in servers_list:
            options = servers_list[label]
        elif len(servers_list) == 1:
            options = servers_list[list(servers_list.keys())[0]]
        else:
            raise IntegrationError(f"{jira_label} did not match labels given in the app.config")

        return options

    def _get_server_name_list(self, opts):
        """
        Return the list of jira server names defined in the app.config in fn_jira.
        :param opts: List of options
        :return: List of servers
        """
        return [key for key in opts.keys() if key.startswith(f"{PACKAGE_NAME}:") and key != GLOBAL_SETTINGS]

    def get_server_name_list(self):
        """
        Return list of all server names
        """
        return self.server_name_list

def str_time_to_int_time(str_time):
    """
    Convert time string to integer epoch time
    :param str_time: Time in string
    :return: Epoch time as integer
    """
    str_time = str_time[:str_time.rindex(".")]
    return int(datetime.strptime(str_time, "%Y-%m-%dT%H:%M:%S").timestamp() * 1000)

def to_markdown(html):
    """ Takes a string of html converts it to Markdown and returns it """
    return MarkdownParser(strikeout="-", bold="*", underline="+", italic="_").convert(html)

def get_jira_issue_id(res_client, dt_name, incident_id, task_id):
    """ Returns the jira_issue_id and jira_url that relates to the task_id """
    try:
        rows = SOARCommon(res_client)._get_case_info(incident_id, f"table_data/{dt_name}?handle_format=names")["rows"]
    except Exception as err:
        raise IntegrationError(f"Failed to get '{dt_name}' Datatable. This is required to send task notes to Jira", err)

    row = [r for r in rows if str(r["cells"].get("task_id").get("value")) == str(task_id)][0]

    if row:
        cells = row.get("cells")
        return str(cells.get("jira_issue_id_col").get("value")), str(cells.get(JIRA_DT_ISSUE_LINK_COL_NAME).get("value"))

def get_id_from_jira_issue_description(description):
    """
    Get the SOAR task id from the description of the given Jira issue
    :param jira_issue_description: Description of the Jira issue
    """
    return int(description[description.rindex("task_id=")+8:description.index('</a>')])

def get_server_settings(opts, jira_label):
    """
    Used for initializing or reloading the options variable
    :param opts: List of options
    :param jira_label: Label of the server in the app.config to use
    :return: Jira server settings for specified server
    """
    jiraServers = JiraServers(opts)
    server_list = {PACKAGE_NAME} if opts.get(PACKAGE_NAME, {}) else jiraServers.get_server_name_list()

    # Creates a dictionary that is filled with the jira servers
    # and there configurations
    servers_list = {server_name:opts.get(server_name, {}) for server_name in server_list}

    # Get configuration for jira server specified
    return jiraServers.jira_label_test(jira_label, servers_list)

def check_jira_issue_linked_to_task(jira_issue_description):
    """
    Check if the given Jira issue is linked to a SOAR task
    :param jira_issue_description: String description of Jira issue
    :return: Boolean
    """
    # Check if the Jira issue is linked to a SOAR task
    if jira_issue_description and IBM_SOAR_LINK in jira_issue_description and "?task_id=" in jira_issue_description:
        return True
