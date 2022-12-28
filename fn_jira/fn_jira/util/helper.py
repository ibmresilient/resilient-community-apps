# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-

from jira import JIRA
from resilient_lib import IntegrationError, MarkdownParser, validate_fields, RequestsCommon
from datetime import datetime
from io import BytesIO

PACKAGE_NAME = "fn_jira"
GLOBAL_SETTINGS = f"{PACKAGE_NAME}:global_settings"
SUPPORTED_AUTH_METHODS = ("AUTH", "BASIC", "TOKEN", "OAUTH")

# Jira datatable constants
DEFAULT_JIRA_DT_NAME = "jira_task_references" # can be overridden with app.config jira_dt_name value
JIRA_DT_ISSUE_ID_COL_NAME = "jira_issue_id_col"
JIRA_DT_ISSUE_LINK_COL_NAME = "jira_link"

def get_jira_client(opts, options):
    """
    Function that gets the client for JIRA
    :param opts: All of the settings from the app.config
    :param options: The options for fn_jira from the app.config
    :raise: IntegrationError if auth_method set in app.config is unsupported
    :return: Instance to jira client
    :rtype: JIRA object. See: https://jira.readthedocs.io/en/latest/api.html 
    """

    # Get global_settings if definied in the app.config
    global_settings = opts.get(GLOBAL_SETTINGS, {})

    # Validate the app.config settings for fn_jira
    validate_fields([
        {"name": "url", "placeholder": "https://<jira url>"},
        {"name": "auth_method"},
        {"name": "jira_dt_name"}], options)

    # Set app.config settings to variables
    auth_method = options.get("auth_method")
    oauth = token_auth = basic_auth = auth = None
    url = options.get("url")

    # Get verify setting from app.config
    verify = options.get("verify_cert", False)
    if verify:
        verify = False if verify.lower() == "false" else (True if verify.lower() == "true" else verify)

    # Get timeout from app.config either from global_settings if present or from individual Jira server settings
    timeout = int(global_settings.get("timeout")) if global_settings.get("timeout", None) else int(options.get("timeout", 10))

    # Set proxies variable as a dict
    proxies = {}
    # Check if global_settings is definied in the app.config
    if global_settings:
        # Check if proxies are defined in the global_settings
        if global_settings.get("http_proxy"):
            proxies["http"] = global_settings.get("http_proxy")
        if global_settings.get("https_proxy"):
            proxies["https"] = global_settings.get("https_proxy")
        if not proxies:
            proxies = None
    else:
        # Call resilient_lib function to find proxies
        proxies = RequestsCommon(opts, options).get_proxies()

    # AUTH and BASIC AUTH
    if auth_method.upper() in SUPPORTED_AUTH_METHODS[0:2]:
        validate_fields([{"name": "user", "placeholder": "<jira username or email>"},
                         {"name": "password", "placeholder": "<jira user password or API Key>"}],
                         options)
        if auth_method.upper() == SUPPORTED_AUTH_METHODS[0] and ".atlassian.net" not in url: # AUTH
            auth = (options.get("user"), options.get("password"))
        else: # BASIC
            basic_auth = (options.get("user"), options.get("password"))

    # TOKEN
    elif auth_method.upper() == SUPPORTED_AUTH_METHODS[2] and ".atlassian.net" not in url:
        validate_fields(["auth_token"], options)
        token_auth = (options.get("auth_token"))

    # OAUTH
    elif auth_method.upper() == SUPPORTED_AUTH_METHODS[3]:
        key_cert_data = None

        # Validate required fields
        validate_fields([
            {"name": "access_token", "placeholder": "<oauth access token>"},
            {"name": "access_token_secret", "placeholder": "<oauth access token secret>"},
            {"name": "consumer_key_name", "placeholder": "<oauth consumer key - from Jira incoming link settings>"},
            {"name": "private_rsa_key_file_path", "placeholder": "<private RSA key matched with public key on Jira>"}
            ], options)

        try:
            with open(options.get("private_rsa_key_file_path"), "r") as private_rsa_key:
                key_cert_data = private_rsa_key.read()
        except FileNotFoundError as e:
            raise IntegrationError(f"Private Key file not valid: {str(e)}")

        oauth = {"access_token": options.get("access_token"),
                 "access_token_secret": options.get("access_token_secret"),
                 "consumer_key": options.get("consumer_key_name"),
                 "key_cert": key_cert_data}

    else:
        if ".atlassian.net" in url:
            raise IntegrationError("Only auth_methods BASIC and OAUTH are supported with Jira Cloud platform")
        raise IntegrationError(f"{auth_method} auth_method is not supported. Supported methods: {SUPPORTED_AUTH_METHODS}")

    return JIRA(
        auth = auth,
        basic_auth = basic_auth,
        token_auth = token_auth,
        oauth = oauth,
        options = {"server": url,
                   "verify": verify,
                   "rest_api_version": "2"},
        proxies = RequestsCommon(opts, options).get_proxies(),
        timeout = timeout,
    )

def to_markdown(html):
    """Takes a string of html converts it to Markdown
    and returns it"""
    return MarkdownParser(strikeout="-", bold="*", underline="+", italic="_").convert(html)

def get_jira_issue_id(res_client, dt_name, incident_id, task_id):
    """Returns the jira_issue_id and jira_url that relates to the task_id"""
    cell_name = "task_id"

    try:
        data = res_client.get(f"/incidents/{incident_id}/table_data/{dt_name}?handle_format=names")
        rows = data["rows"]
    except Exception as err:
        raise IntegrationError(f"Failed to get '{dt_name}' Datatable. This is required to send task notes to Jira", err)

    found = False
    for row in rows:
        cells = row["cells"]
        if cells.get(cell_name) and cells[cell_name].get("value") and str(cells[cell_name].get("value")) == str(task_id):
            found = True
            break

    if row and found:
        cells = row.get("cells")
        return str(cells["jira_issue_id"]["value"]), str(cells[JIRA_DT_ISSUE_LINK_COL_NAME]["value"])

class JiraServers():
    def __init__(self, opts):
        self.servers, self.server_name_list = self._load_servers(opts)

    def _load_servers(self, opts):
        """
        Create list of label names and a dictionary of the servers and their configs
        :param opts: Dict of options
        :return servers: Dictonary of all the Jira servers from the app.config that contains each servers configurations
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

    def jira_label_test(jira_label, servers_list):
        """
        Check if the given jira_label is in the app.config
        :param jira_label: User selected server
        :param servers_list: List of jira servers
        :return: Dictionary of options for choosen server
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
            raise IntegrationError("{} did not match labels given in the app.config".format(jira_label))

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

def get_server_settings(opts, jira_label):
    """
    Used for initilizing or reloading the options variable
    :param opts: List of options
    :param jira_label: Label of the server in the app.config to use
    :return: Jira server settings for specified server
    """
    server_list = {PACKAGE_NAME} if opts.get(PACKAGE_NAME, {}) else JiraServers(opts).get_server_name_list()

    # Creates a dictionary that is filled with the jira servers
    # and there configurations
    servers_list = {server_name:opts.get(server_name, {}) for server_name in server_list}

    # Get configuration for jira server specified
    return JiraServers.jira_label_test(jira_label, servers_list)

def str_time_to_int_time(str_time):
    """
    Convert time string to integer epoch time
    :param str_time: Time in string
    :return: Epoch time as integrer
    """
    str_time = str_time[:str_time.rindex(".")]
    return int(datetime.strptime(str_time, "%Y-%m-%dT%H:%M:%S").timestamp() * 1e3)

def create_soar_incident(res_client, issue):
    """
    Function: Creates a SOAR incident from a Jira ticket
    :param res_client: Client connection to SOAR
    :param issue: Information on the Jira ticket
    """

    issue_fields = issue.get("fields")
    internal_url = issue.get("self")
    jira_key = issue.get("key")

    # Get comments from the Jira ticket
    comments = []
    if issue_fields.get("comment"):
        for comment in issue_fields.get("comment").get("comments"):
            comments.append({
                "text": {
                    "format": "text",
                    "content": comment.get("body")
                },
                "type": "incident"
            })

    payload = {
        "name": issue_fields.get("summary"),
        "description": issue_fields.get("description"),
        "severity_code": issue_fields.get("priority").get("name"),
        "create_date": str_time_to_int_time(issue_fields.get("created")),
        "discovered_date": str_time_to_int_time(issue_fields.get("created")),
        "properties": {
            "jira_internal_url": internal_url,
            "jira_issue_id": jira_key,
            "jira_server": issue.get("jira_server"),
            "jira_url": f"<a href='{internal_url[:internal_url.index('/', 8)]}/browse/{jira_key}' target='blank'>{jira_key}</a>",
            "jira_project_key": issue_fields.get("project").get("key"),
            "soar_case_last_updated": str_time_to_int_time(issue_fields.get("updated"))
        },
        "comments": comments
    }

    response = res_client.post("/incidents", payload)

    if issue_fields.get("attachment"):
        # Get attachments from the Jira ticket
        for attach in issue_fields.get("attachment"):
            r = res_client.post_attachment(f"/incidents/{response.get('id')}/attachments", filepath=None, filename=attach.get("filename"), bytes_handle=attach.get("content"))

