# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-

from jira import JIRA
from resilient_lib import IntegrationError, MarkdownParser, str_to_bool, validate_fields

PACKAGE_NAME = "fn_jira"
SUPPORTED_AUTH_METHODS = ("AUTH", "BASIC", "TOKEN", "OAUTH")

# Jira datatable constants
DEFAULT_JIRA_DT_NAME = "jira_task_references" # can be overridden with app.config jira_dt_name value
JIRA_DT_ISSUE_ID_COL_NAME = "jira_issue_id_col"
JIRA_DT_ISSUE_LINK_COL_NAME = "jira_link"

# Other Jira SOAR variable constants
JIRA_ISSUE_ID_FUNCT_INPUT_NAME = "jira_issue_id"
JIRA_COMMENT_FUNCT_INPUT_NAME = "jira_comment"
JIRA_ISSUE_LINK = "jira_url"
INCIDENT_ID_FUNCT_INPUT_NAME = "incident_id"
TASK_ID_FUNCT_INPUT_NAME = "task_id"

def validate_app_configs(app_configs):
    """
    Validates the app configs for fn_jira. Raises an error
    if the required configs are not set

    :param app_configs: The app_configs for fn_jira
    :return: All the app configs
    :rtype: dict
    """
    valid_app_configs = validate_fields([
        {"name": "url", "placeholder": "https://<jira url>"},
        {"name": "auth_method"},
        {"name": "verify_cert"}
    ], app_configs)

    valid_app_configs["verify_cert"] = str_to_bool(valid_app_configs.get("verify_cert"))

    return valid_app_configs

def get_jira_client(app_configs, rc):
    """
    Function that gets the client for JIRA

    :param app_configs: The app_configs for fn_jira
    :param rc: resilient_lib.RequestsCommon object used to get proxies
    :raise: IntegrationError if auth_method set in app.config is unsupported
    :return: Instance to jira client
    :rtype: JIRA object. See: https://jira.readthedocs.io/en/latest/api.html 
    """
    # set default to "BASIC" as that is what most users should be using
    auth_method = app_configs.get("auth_method", SUPPORTED_AUTH_METHODS[1])
    oauth = token_auth = basic_auth = auth = None

    try:
        timeout = int(app_configs.get("timeout", 10))
    except ValueError:
        raise IntegrationError("Ensure 'timeout' is an integer in your config file")

    # AUTH and BASIC AUTH
    if auth_method.upper() in SUPPORTED_AUTH_METHODS[0:2]:
        validate_fields([{"name": "user", "placeholder": "<jira username or email>"},
                         {"name": "password", "placeholder": "<jira user password or API Key>"}],
                         app_configs)
        if auth_method.upper() == SUPPORTED_AUTH_METHODS[0]: # AUTH
            auth = (app_configs.get("user"), app_configs.get("password"))
        else: # BASIC
            basic_auth = (app_configs.get("user"), app_configs.get("password"))

    # TOKEN
    elif auth_method.upper() == SUPPORTED_AUTH_METHODS[2]:
        validate_fields(["auth_token"], app_configs)
        token_auth = (app_configs.get("auth_token"))

    # OAUTH
    elif auth_method.upper() == SUPPORTED_AUTH_METHODS[3]:
        key_cert_data = None

        # Validate required fields
        validate_fields([
            {"name": "access_token", "placeholder": "<oauth access token>"},
            {"name": "access_token_secret", "placeholder": "<oauth access token secret>"},
            {"name": "consumer_key_name", "placeholder": "<oauth consumer key - from Jira incoming link settings>"},
            {"name": "private_rsa_key_file_path", "placeholder": "<private RSA key matched with public key on Jira>"}
            ], app_configs)

        try:
            with open(app_configs.get("private_rsa_key_file_path"), "r") as private_rsa_key:
                key_cert_data = private_rsa_key.read()
        except FileNotFoundError as e:
            raise IntegrationError(f"Private Key file not valid: {str(e)}")

        oauth = {"access_token": app_configs.get("access_token"),
                 "access_token_secret": app_configs.get("access_token_secret"),
                 "consumer_key": app_configs.get("consumer_key_name"),
                 "key_cert": key_cert_data
                }

    else:
        raise IntegrationError(f"{auth_method} auth_method is not supported. Supported methods: {SUPPORTED_AUTH_METHODS}")

    return JIRA(
        auth = auth,
        basic_auth = basic_auth,
        token_auth = token_auth,
        oauth = oauth,
        options = {"server": app_configs.get("url"),
                   "verify": app_configs.get("verify_cert")},
        proxies = rc.get_proxies(),
        timeout = timeout,
    )

def to_markdown(html):
    """Takes a string of html converts it to Markdown
    and returns it"""
    return MarkdownParser(strikeout="-", bold="*", underline="+", italic="_").convert(html)

def get_jira_issue_id(res_client, dt_name, incident_id, task_id):
    """Returns the jira_issue_id and jira_url that relates to the task_id"""
    row = _get_row(res_client, dt_name, incident_id, "task_id", task_id)

    if row:
        cells = row.get("cells")
        return str(cells[JIRA_DT_ISSUE_ID_COL_NAME]["value"]), str(cells[JIRA_DT_ISSUE_LINK_COL_NAME]["value"])

def _get_row(res_client, dt_name, incident_id, cell_name, cell_value):
    """Returns the row with a matching value to cell_name and cell_value if found. Returns None if no matching row found"""
    try:
        data = res_client.get(f"/incidents/{incident_id}/table_data/{dt_name}?handle_format=names")
        rows = data["rows"]
    except Exception as err:
        raise IntegrationError(f"Failed to get '{dt_name}' Datatable. This is required to send task notes to Jira", err)

    for row in rows:
        cells = row["cells"]
        if cells.get(cell_name) and cells[cell_name].get("value") and str(cells[cell_name].get("value")) == str(cell_value):
            return row

class JiraServers():
    def __init__(self, opts):
        self.servers, self.server_name_list = self._load_servers(opts)

    def _load_servers(self, opts):
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
        return [key for key in opts.keys() if key.startswith(f"{PACKAGE_NAME}:")]

    def get_server_name_list(self):
        """
        Return list of all server names
        """
        return self.server_name_list

def get_server_settings(opts, jira_label):
    """
    Used for initilizing or reloading the options variable
    :param opts: List of options
    :return: jira server settings for specified server
    """
    server_list = {PACKAGE_NAME} if opts.get(PACKAGE_NAME, {}) else JiraServers(opts).get_server_name_list()

    # Creates a dictionary that is filled with the jira servers
    # and there configurations
    servers_list = {server_name:opts.get(server_name, {}) for server_name in server_list}

    # Get configuration for jira server specified
    return JiraServers.jira_label_test(jira_label, servers_list)
