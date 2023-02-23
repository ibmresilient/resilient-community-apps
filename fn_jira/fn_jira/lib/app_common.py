# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

from logging import getLogger
from jira import JIRA
from fn_jira.util.helper import str_time_to_int_time, check_jira_issue_linked_to_task, get_id_from_jira_issue_description, GLOBAL_SETTINGS
from resilient_lib import IntegrationError, str_to_bool, validate_fields, RequestsCommon, SOARCommon

LOG = getLogger(__name__)

SUPPORTED_AUTH_METHODS = ("AUTH", "BASIC", "TOKEN", "OAUTH")

class AppCommon():
    def __init__(self, opts, app_configs):
        """
        Initialize the parameters needed to communicate to the endpoint solution

        :param opts: All of the settings from the app.config
        :type opts: dict
        :param app_configs: app.config parameters in order to authenticate and access the endpoint
        :type app_configs: dict
        """

        # Get global_settings if definied in the app.config
        global_settings = opts.get(GLOBAL_SETTINGS, {})

        # Validate the app.config settings for fn_jira
        validate_fields([
            {"name": "url", "placeholder": "https://<jira url>"},
            {"name": "auth_method"},
            {"name": "jira_dt_name"}], app_configs)

        self.rc = RequestsCommon(opts, app_configs)

        # Required configs
        self.endpoint_url = app_configs.get("url")
        self.auth_method = app_configs.get("auth_method")
        self.oauth = self.token_auth = self.basic_auth = self.auth = None

        # Get verify setting from app.config
        self.verify = _get_verify_ssl(app_configs)

        # Get timeout from app.config either from global_settings if present or from individual Jira server settings
        self.timeout = int(global_settings.get("timeout")) if global_settings.get("timeout", None) else int(app_configs.get("timeout", 10))

        # Set proxies variable as a dict
        self.proxies = {}
        # Check if global_settings is definied in the app.config
        if global_settings:
            # Check if proxies are defined in the global_settings
            if global_settings.get("http_proxy"):
                self.proxies["http"] = global_settings.get("http_proxy")
            if global_settings.get("https_proxy"):
                self.proxies["https"] = global_settings.get("https_proxy")
            if not self.proxies:
                self.proxies = None
        else:
            # Call resilient_lib function to find proxies
            self.proxies = self.rc.get_proxies()

        # AUTH and BASIC AUTH
        if self.auth_method.upper() in SUPPORTED_AUTH_METHODS[0:2]:
            validate_fields([{"name": "user", "placeholder": "<jira username or email>"},
                            {"name": "password", "placeholder": "<jira user password or API Key>"}],
                            app_configs)
            if self.auth_method.upper() == SUPPORTED_AUTH_METHODS[0]: # AUTH
                self.auth = (app_configs.get("user"), app_configs.get("password"))
            else: # BASIC
                self.basic_auth = (app_configs.get("user"), app_configs.get("password"))

        # TOKEN
        elif self.auth_method.upper() == SUPPORTED_AUTH_METHODS[2]:
            validate_fields(["auth_token"], app_configs)
            self.token_auth = (app_configs.get("auth_token"))

        # OAUTH
        elif self.auth_method.upper() == SUPPORTED_AUTH_METHODS[3]:
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

            self.oauth = {"access_token": app_configs.get("access_token"),
                    "access_token_secret": app_configs.get("access_token_secret"),
                    "consumer_key": app_configs.get("consumer_key_name"),
                    "key_cert": key_cert_data}

        else:
            raise IntegrationError(f"{self.auth_method} auth_method is not supported. Supported methods: {SUPPORTED_AUTH_METHODS}")

        self.jira_client = self.get_jira_client()

    def get_jira_client(self):
        """ Create Jira client connection"""
        return JIRA(
            auth = self.auth,
            basic_auth = self.basic_auth,
            token_auth = self.token_auth,
            oauth = self.oauth,
            options = {"server": self.endpoint_url,
                    "verify": self.verify,
                    "rest_api_version": "2"},
            proxies = self.proxies,
            timeout = self.timeout
        )

    def search_jira_issues(self, search_filters, last_poller_time=None, max_results=50, data_to_get_from_case=None):
        """
        Search for Jira issues with given filters
        :param jira_client: Client connection to Jira
        :param search_filters: Search filters for Jira
        :param last_poller_time: Last time the poller ran
        :param max_results: Max number of issues that can be returned from Jira issue search
        """

        if last_poller_time:
            search_filters = f"{search_filters} and updated > '{last_poller_time.strftime('%Y/%m/%d %H:%M')}'"

        issues_list = self.jira_client.search_issues(
            search_filters,
            maxResults=max_results,
            json_result=True
        ).get("issues")

        # Format each dictionary
        for issue in issues_list:

            jira_key = issue.get("key")
            internal_url = issue.get("self")
            issue["internal_url"] = internal_url
            issue["url"] = f"<a href='{internal_url[:internal_url.index('/', 8)]}/browse/{jira_key}' target='blank'>{jira_key}</a>"
            issue["fields"]["summary"] = issue.get("fields").get("summary").replace("IBM SOAR: ", "")

            if not data_to_get_from_case.get(issue.get("key")):
                data_to_get_from_case[issue.get("key")] = {}

            data_to_get_from_case[issue.get("key")]["comments"] = False
            data_to_get_from_case[issue.get("key")]["attachments"] = False

            # Create a list of just comment string
            comments = issue.get("fields").get("comment").get("comments")
            if comments:
                data_to_get_from_case[issue.get("key")]["comments"] = True
                for comment_num in range(len(comments)):
                    comments[comment_num] = comments[comment_num].get("body")
            issue["fields"]["comment"] = comments if comments else []

            # Convert the string times to integer epoch time
            issue["fields"]["created"] = str_time_to_int_time(issue.get("fields").get("created"))
            issue["fields"]["updated"] = str_time_to_int_time(issue.get("fields").get("updated"))

            # Create a list of just attachment filenames
            attachments = issue.get("fields").get("attachment")
            if attachments:
                data_to_get_from_case[issue.get("key")]["attachments"] = True
                for attach_num in range(len(attachments)):
                    attachments[attach_num] = {
                        "filename": attachments[attach_num].get("filename"),
                        "content": self.jira_client._session.get(attachments[attach_num].get("content")).content
                    }
            issue["fields"]["attachment"] = attachments if attachments else []

            issue_description = issue.get("fields").get("description")
            if check_jira_issue_linked_to_task(issue_description):
                task_id = get_id_from_jira_issue_description(issue_description)
                data_to_get_from_case["tasks"].append({
                    "incident_id": int(issue_description[issue_description.index("incidents/")+10:issue_description.index("?task_id")]),
                    "task_id": task_id,
                    "task_key": issue.get("key")
                })

        return issues_list, data_to_get_from_case

def _get_verify_ssl(app_configs):
    """
    Get ``verify`` parameter from app config.
    Value can be set in the [fn_my_app] section

    :param opts: All of the app.config file as a dict
    :type opts: dict
    :param app_options: App specific configs
    :type app_options: dict
    :return: Value to set ``requests.request.verify`` to. Either a path or a boolean. Defaults to ``True``
    :rtype: bool|str(path)
    """
    # start checking the app specific settings
    verify = app_configs.get("verify")

    # because verify can be either a boolean or a path,
    # we need to check if it is a string with a boolean 
    # value first then, and only then, we convert it to a bool
    # NOTE: that this will then only support "true" or "false"
    # (case-insensitive) rather than the normal "true", "yes", etc...
    if isinstance(verify, str) and verify.lower() in ["false", "true"]:
        verify = str_to_bool(verify)

    return verify

class SOAR():

    def add_task_to_case(rest_client, cases_list, num, id, comments=False, attachments=False):
        """
        Adds task data to the SOAR case
        :param rest_client: Client connection to SOAR
        :param cases_list: List of SOAR cases
        :param num: The index of the case in case_list
        :param id: Task ID
        :param comments: Boolean if to add comments
        :param attachments: Boolean if to add attachments
        :return: None
        """
        case_id = cases_list[num].get('id')

        # Add Tasks to cases
        case_tasks = SOARCommon(rest_client)._get_case_info(case_id, "tasks?want_notes=true")
        if case_tasks:
            # Add tasks field to the case if the field does not exist
            task = cases_list[num].get("tasks")
            cases_list[num]["tasks"] = task if task else []
            del task # Delete variable that is no longer needed

            for task_num in range(len(case_tasks)):
                task_id = case_tasks[task_num].get("id")
                if id == task_id:
                    cases_list[num]["tasks"].append(
                        {k: v for k, v in case_tasks[task_num].items()\
                            if v is not None and \
                                k not in ["perms", "actions", "playbooks", "creator_principal", "regs", "notes_count", "attachments_count", "inc_owner_id", "user_notes", "auto_deactivate", "phase_id"]}
                    )
                    case_task_num = len(cases_list[num]["tasks"])-1

                    # Get notes
                    if comments:
                        task_notes = case_tasks[task_num].get("notes")
                        cases_list[num]["tasks"][case_task_num]["notes"] = []
                        for note_num in range(len(task_notes)):
                            cases_list[num]["tasks"][case_task_num]["notes"].append(
                                task_notes[note_num].get("text")
                            )
                    else:
                        cases_list[num]["tasks"][case_task_num]["notes"] = []

                    del comments

                    # Get attachments
                    if attachments:
                        task_attachments = rest_client.get(f"/tasks/{task_id}/attachments")
                        cases_list[num]["tasks"][case_task_num]["attachments"] = []
                        for attach_num in range(len(task_attachments)):
                            cases_list[num]["tasks"][case_task_num]["attachments"].append({
                                "id": task_attachments[attach_num].get("id"),
                                "name": task_attachments[attach_num].get("name")
                            })
                    else:
                        cases_list[num]["tasks"][case_task_num]["attachments"] = []

                    # Add the data table that contains the task info to the task
                    case_datatables = SOARCommon(rest_client)._get_case_info(case_id, "table_data?handle_format=names")
                    if case_datatables:
                        found = False
                        for datatable in case_datatables:
                            if found:
                                break
                            for row in case_datatables[datatable].get("rows"):
                                if str(id) == row["cells"].get("task_id").get("value"):
                                    found = True
                                    for field in ["actions", "playbooks", "inc_owner", "inc_name"]:
                                        row.pop(field)
                                    cases_list[num]["tasks"][case_task_num]["datatable"] = row
                                    cases_list[num]["tasks"][case_task_num]["datatable"]["table_id"] = case_datatables[datatable].get("id")
                                    break
                    break

    def add_to_case(rest_client, cases_list, num, field_name):
        """
        Function adds comments and attachments on the SOAR incident to the case in the list
        :param rest_client: Client connection to SOAR
        :param cases_list: List of SOAR cases
        :param num: The index of the case in case_list
        :param field_name: Name of the field to add. Either 'attachments' or 'comments'
        :return: None
        """
        url_end = '?want_notes=true' if field_name == 'tasks' else ''
        case_field = SOARCommon(rest_client)._get_case_info(cases_list[num].get('id'), f"{field_name}{url_end}")
        if case_field:
            cases_list[num][field_name] = []
            for field_num in range(len(case_field)):
                field_dict = {"id": case_field[field_num].get("id")}
                if field_name == "comments":
                    field_dict["content"] = case_field[field_num].get("text").replace("<div>","").replace("</div>","")
                if field_name == "attachments":
                    field_dict["name"] = case_field[field_num].get("name")
                cases_list[num][field_name].append(field_dict)
