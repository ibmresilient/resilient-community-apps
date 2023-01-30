# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# -*- coding: utf-8 -*-

from jira import JIRA
from resilient_lib import IntegrationError, MarkdownParser, validate_fields, RequestsCommon
from json import dumps
from re import compile, sub

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

    try:
        rows = res_client.get(f"/incidents/{incident_id}/table_data/{dt_name}?handle_format=names")["rows"]
    except Exception as err:
        raise IntegrationError(f"Failed to get '{dt_name}' Datatable. This is required to send task notes to Jira", err)

    row = [r for r in rows if str(r["cells"].get("task_id").get("value")) == str(task_id)][0]

    if row:
        cells = row.get("cells")
        return str(cells.get("jira_issue_id_col").get("value")), str(cells.get(JIRA_DT_ISSUE_LINK_COL_NAME).get("value"))

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

def get_id_from_jira_issue_description(description):
    """
    Get the SOAR task id from the description of the
    given Jira issue
    :param jira_issue_description: Description of the Jira issue
    """
    task_id = None
    search_end = "]\n\n"

    if "IBM SOAR Link: [" in description and search_end in description:
        task_id = int(description[description.rindex("task_id=")+8:description.index(search_end)])
    else:
        task_id = int(description[description.index("task_id=")+8:description.index("\n\n")])

    return task_id

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

def remove_html_tags(comment):
    """
    Remove html tags from a comment
    :param comment: Comment from Jira issue
    :return: Comment without html tags
    """
    return sub(compile('<.*?>'), '', comment)

def soar_update_comments_attachments(jira, soar, res_client, update_type):
    """
    Add comment\attchment to the SOAR case that are in the Jira issue and
    delete comments\attachments that are in the SOAR case and not in the Jira issue
    :param jira: Dict of Jira issue data
    :param soar: Dict of SOAR case data
    :param res_client: Client connection to SOAR
    :param update_type: Either attachment or comment
    """
    # Get comments\attachments from the Jira issue
    jira_updates = jira.pop(update_type) if jira.get(update_type) else []
    if update_type == "attachment":
        jira_attachments = jira_updates
        jira_updates = [attach.get("filename") for attach in jira_attachments]
    # Get comments\attachments from the SOAR case
    soar_updates = soar.pop(f"{update_type}s") if soar.get(f"{update_type}s") else []
    # Remove the text "\nAdded from Jira" from comments if present
    if update_type == "comment":
        for num in range(len(soar_updates)):
            update_content = soar_updates[num].get("content")
            soar_updates[num]["content"] = remove_html_tags(update_content.replace("\nAdded from Jira", ""))

    if soar_updates:
        for num, soar_update in enumerate(soar_updates):
            soar_update_content = soar_update.get("content")
            if update_type == "attachment":
                soar_update_content = soar_update.get("name")
            # Delete comment\attachment on SOAR if comment\attachment is not found on Jira issue
            if soar_update_content not in jira_updates:
                # Send delete request to SOAR
                try:
                    res_client.delete(f"/incidents/{soar.get('id')}/{update_type}s/{soar_update.get('id')}")
                except Exception as e:
                    raise IntegrationError(str(e))
            elif soar_update_content in jira_updates: # If comment\attachment on SOAR and Jira then remove it from jira_updates
                jira_updates.pop(jira_updates.index(soar_update_content))

        # Delete variables that are no longer needed
        del num, soar_update

    if jira_updates:
        for jira_update in jira_updates:
            # Send post request to SOAR
            try:
                if update_type == "attachment":
                    content = jira_attachments[next((index for (index, attach) in enumerate(jira_attachments) if attach["filename"] == jira_update), None)].get("content")
                    res_client.post_attachment(f"/incidents/{soar.get('id')}/attachments", filepath=None, filename=jira_update, bytes_handle=content)
                else:
                    res_client.post(f"/incidents/{soar.get('id')}/comments", {"text": {"content": f"{jira_update}\nAdded from Jira"}})
            except Exception as e:
                raise IntegrationError(str(e))

def soar_update_task(jira, res_client, task):
    """
    Update soar tasks
    :param jira: Dict of Jira issue data
    :param res_client: Client connection to SOAR
    :param task: SOAR task dictionry
    """
    jira_issue_description = jira.get("description")

    # Add data to task update payload
    t_payload = task.copy()
    t_payload["notes"] = []
    del t_payload["attachments"], t_payload["datatable"]

    link_end_index = jira_issue_description.index("\n\n")+2
    # Check if link to SOAR task is in the Jira issue description
    if check_jira_issue_linked_to_task(jira_issue_description) and link_end_index < len(jira_issue_description):
        # Remove link to SOAR task from the description
        instructions = jira_issue_description[link_end_index:].replace("Created in IBM SOAR", "")
    else:
        instructions = jira_issue_description

    if instructions:
        # Update the SOAR task instructions and instr_text to be the rest of the Jira issue description
        t_payload["instructions"] = f'<div class="rte"><div>{instructions}</div></div>'
        t_payload["instr_text"] = f'<div class="rte"><div>{instructions}</div></div>'

    # Removed no longer needed variables
    del link_end_index, instructions

    # Check if Jira issue has been closed
    # If the Jira issue has a resolutiondate then it has been closed
    if jira.get("resolutiondate"):
        t_payload["status"] = "C"

    # Remove all html tags from the task notes
    for num in range(len(task.get("notes"))):
        task["notes"][num] = remove_html_tags(task["notes"][num].replace("<br/>Added from Jira", ""))

    # Update comments/notes
    comments = jira.get("comment")
    if comments:
        for comment in comments:
            if comment not in task.get("notes"):
                comment_payload = {
                    "text": {
                        "format": "text",
                        "content": f"{comment}\nAdded from Jira"
                    },
                    "is_deleted": False
                }
                res_client.post(f"/tasks/{task.get('id')}/comments", comment_payload)

    # Update attachments
    attachments = jira.get("attachment")
    if attachments:
        task_attachments = [att.get("name") for att in task.get("attachments")]
        for attach in attachments:
            filename = attach.get("filename")
            if filename not in task_attachments:
                res_client.post_attachment(f"/tasks/{task.get('id')}/attachments", filepath=None, filename=filename, bytes_handle=attach.get("content"))

    # Update data table on SOAR with new information from the updated task
    datatable = task.get('datatable')
    datatable_cells = datatable.get("cells")

    d_payload = {
        "id": datatable.get("id"),
        "version": datatable.get("version")
    }
    d_payload["cells"] = {cell: { "value": datatable_cells[cell].get("value")} for cell in datatable_cells}
    d_payload["cells"]["last_updated"]["value"] = jira.get("updated")
    d_payload["cells"]["status"]["value"] = jira.get("status")

    res_client.put(f"/incidents/{task.get('inc_id')}/table_data/{datatable.get('table_id')}/row_data/{datatable.get('id')}", d_payload)

    return t_payload

def check_jira_issue_linked_to_task(jira_issue_description):
    """
    Check if the given Jira issue is linked to a SOAR task
    :param jira_issue_description: String description of Jira issue
    :return: Boolean
    """

    # Check if the Jira issue is linked to a SOAR task
    if jira_issue_description and "IBM SOAR Link:" in jira_issue_description and "?task_id=" in jira_issue_description:
            return True

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

    # Payload for updating SOAR tasks
    task_update_payload = []

    for update in soar_cases_to_update:
        jira = update[0] # Get the Jira issue
        soar = update[1] # Get the SOAR case
        # Get the description of the Jira issue
        jira_issue_description = jira.get("description")

        # Check if the Jira issue is linked to a SOAR task
        if check_jira_issue_linked_to_task(jira_issue_description):
            task_id = get_id_from_jira_issue_description(jira_issue_description)
            for task in soar.get("tasks"):
                if task.get("id") == task_id:
                    # Update SOAR task with Jira data
                    task_update_payload.append(soar_update_task(jira, res_client, task))
                    break
            continue

        # If Jira issue is linked to SOAR incident and not a SOAR task
        # Check if new comments added or old comments changed/deleted
        soar_update_comments_attachments(jira, soar, res_client, "comment")

        # Check if new attachments added or old attachments deleted
        soar_update_comments_attachments(jira, soar, res_client, "attachment")

        soar_update_payload['patches'][soar.get("id")] = {
                "version": soar.get("vers")+1,
                "changes": []
                }

        # Close SOAR incident if linked Jira issue is closed
        # If the Jira issue has a resolutiondate then it has been closed
        if jira.get("resolutiondate"):
            soar_update_payload['patches'][soar.get("id")]["changes"].append({
                "old_value": {"text": "A"},
                "new_value": {"text": "C"},
                "field": {"name": "plan_status"}
            })
            soar_update_payload['patches'][soar.get("id")]["changes"].append({
                "old_value": {"text": None},
                "new_value": {"text": "Closed on Jira"},
                "field": {"name": "resolution_summary"}
            })
            soar_update_payload['patches'][soar.get("id")]["changes"].append({
                "old_value": {"text": None},
                "new_value": {"text": "Resolved"},
                "field": {"name": "resolution_id"}
            })

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

    # If SOAR payload is not empty then update fields on cases
    if soar_update_payload["patches"]:
        # Send put request to SOAR
        # This will update all cases that need to be updated
        try:
            re = res_client.put("/incidents/patch", soar_update_payload)
        except Exception as e:
            raise IntegrationError(str(e))

    # If task update payload is not empty then update fields on tasks
    if task_update_payload:
        # Send put request to SOAR
        # This will update all tasks that need to be updated
        try:
            res_client.put("/tasks", task_update_payload)
        except Exception as e:
            raise IntegrationError(str(e))
