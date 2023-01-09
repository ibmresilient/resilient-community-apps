# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# -*- coding: utf-8 -*-

from jira import JIRA
from resilient_lib import IntegrationError, MarkdownParser, validate_fields, RequestsCommon
from datetime import datetime
from ast import literal_eval

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

def create_soar_incident(res_client, issue):
    """
    Function: Creates a SOAR incident from a Jira ticket
    :param res_client: Client connection to SOAR
    :param issue: Information on the Jira ticket
    :param return: None
    """

    internal_url = issue.get("self")
    jira_key = issue.get("key")

    # Get comments from the Jira ticket
    comments = []
    if issue.get("comment"):
        for comment in issue.get("comment"):
            comments.append({
                "text": {
                    "format": "text",
                    "content": comment
                },
                "type": "incident"
            })

    # Create payload to create incident on SOAR
    payload = {
        "name": issue.get("summary"),
        "description": issue.get("description"),
        "severity_code": issue.get("priority"),
        "create_date": issue.get("created"),
        "discovered_date": issue.get("created"),
        "properties": {
            "jira_internal_url": internal_url,
            "jira_issue_id": jira_key,
            "jira_server": issue.get("jira_server"),
            "jira_url": f"<a href='{internal_url[:internal_url.index('/', 8)]}/browse/{jira_key}' target='blank'>{jira_key}</a>",
            "jira_project_key": issue.get("project"),
            "soar_case_last_updated": issue.get("updated"),
            "jira_issue_status": issue.get("status")
        },
        "comments": comments
    }

    try:
        # Create incident on SOAR
        response = res_client.post("/incidents", payload)
    except Exception as err:
        raise IntegrationError(err)

    if issue.get("attachment"):
        # Get attachments from the Jira ticket
        for attach in issue.get("attachment"):
            try:
                # Add the attachment to the SOAR incident
                res_client.post_attachment(f"/incidents/{response.get('id')}/attachments",
                                               filepath=None,
                                               filename=attach.get("filename"),
                                               bytes_handle=attach.get("content")
                                              )
            except Exception as err:
                raise IntegrationError(err)

def update_soar_incident(res_client, soar_cases_to_update):
    """
    Update the SOAR cases with new data from the corresponding Jira issue
    :param res_client: Client connection to SOAR
    :param soar_cases_to_update: A list of lists that contain the SOAR case to update and its corresponding Jira issue
    :return:
    """

    soar_to_jira_fields = {
        "name": "summary",
        "description": "description",
        "severity_code": "priority",
        "create_date": "created",
        "discovered_date": "created",
        "jira_internal_url": "self",
        "jira_issue_id": "key",
        "jira_server": "jira_server",
        "jira_url": "self",
        "jira_project_key": "project",
        "soar_case_last_updated": "updated",
        "jira_issue_status": "status"
    }

    soar_field_type = {
        "name": "text",
        "description": "textarea",
        "severity_code": "text",
        "create_date": "date",
        "discovered_date": "date",
        "jira_internal_url": "textarea",
        "jira_issue_id": "text",
        "jira_server": "text",
        "jira_url": "textarea",
        "jira_project_key": "text",
        "soar_case_last_updated": "date",
        "jira_issue_status": "text"
    }

    # Payload for updating the field "SOAR Case Last Updated" on SOAR cases to update
    soar_update_payload = {"patches": {}}

    for update in soar_cases_to_update:
        jira = update[0] # Get the Jira issue
        soar = update[1] # Get the SOAR case

        del update # Delete variables that are no longer needed

        # Code to check if new comments added or old comments changed/deleted
        jira_comments = jira.pop("comment") if jira.get("comment") else []
        soar_comments = soar.pop("comments") if soar.get("comments") else []

        if soar_comments:
            for num, soar_comment in enumerate(soar_comments):
                soar_comment_content = soar_comment.get("content")
                # Delete comment on SOAR if comment is not found on Jira issue
                if soar_comment_content not in jira_comments:
                    # Send delete request to SOAR
                    try:
                        res_client.delete(f"/incidents/{soar.get('id')}/comments/{soar_comment.get('id')}")
                    except Exception as e:
                        raise IntegrationError(str(e))
                    # Remove comment from list of SOAR comments
                    soar_comments.pop(num)
                elif soar_comment_content in jira_comments: # If comment on SOAR and Jira then remove it from jira_comments and soar_comments
                    jira_comments.pop(jira_comments.index(soar_comment_content))
                    soar_comments.pop(num)

            # Delete variables that are no longer needed
            del num, soar_comment

        if jira_comments:
            for jira_comment in jira_comments:
                # Send delete request to SOAR
                try:
                    res_client.post(f"/incidents/{soar.get('id')}/comments", {"text": {"content": jira_comment}})
                except Exception as e:
                    raise IntegrationError(str(e))

        # Delete variables that are no longer needed
        del jira_comments, soar_comments

        # Check if new attachments added

        soar_update_payload['patches'][soar.get("id")] = {
                "version": soar.get("vers")+1,
                "changes": []
                }

        for key, value in soar_to_jira_fields.items():
            soar_value = soar.get(key)
            jira_value = jira.get(value)

            if key == "jira_url": # If the key is equal to jira_url
                # Create jira_url
                jira_key = jira.get("key")
                jira_value = f'<a href="{jira_value[:jira_value.index("/", 8)]}/browse/{jira_key}">{jira_key}</a>'
                del jira_key

            if soar_value != jira_value: # Check if the current SOAR value is different fromt the current Jira value
                soar_update_payload['patches'][soar.get("id")]["changes"].append({
                    "old_value": {soar_field_type[key]: soar_value},
                    "new_value": {soar_field_type[key]: jira_value},
                    "field": {"name": key}
                })

        del key, value, soar_value, jira_value # Delete variables that are no longer needed

    # Delete variables that are no longer needed
    del soar_field_type, soar_to_jira_fields, soar_cases_to_update

    # If SOAR payload is not empty then update SOAR fields "soar_case_last_updated" on cases
    if soar_update_payload["patches"]:
        # Send put request to SOAR
        # This will update all cases that need to be updated for the give Jira server
        try:
            res_client.put("/incidents/patch", soar_update_payload)
        except Exception as e:
            raise IntegrationError(str(e))

    del soar_update_payload # Delete variables that are no longer needed

