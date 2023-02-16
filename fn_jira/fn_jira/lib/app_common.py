# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

from logging import getLogger
from jira import JIRA
from fn_jira.util.helper import str_time_to_int_time, check_jira_issue_linked_to_task, get_id_from_jira_issue_description
from resilient_lib import IntegrationError, str_to_bool, validate_fields, RequestsCommon
from datetime import datetime

LOG = getLogger(__name__)

PACKAGE_NAME = "fn_jira"
GLOBAL_SETTINGS = f"{PACKAGE_NAME}:global_settings"
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
            fields=["issuetype", "project", "priority", "updated", "status", "description", "attachment", "summary", "comment", "created", "resolutiondate"],
            json_result=True
        ).get("issues")

        # Format each dictionary
        for issue in issues_list:

            for key, value in issue.get("fields").items():
                issue[key] = value
            issue.pop("fields")

            # Change the value of the dict key to the one value that is used in that dict
            for key, value in {"issuetype": "name", "project": "key", "priority": "name", "status": "name", "comment": "comments"}.items():
                if issue.get(key):
                    issue[key] = issue[key].get(value)

            if not data_to_get_from_case.get(issue.get("key")):
                data_to_get_from_case[issue.get("key")] = {}

            data_to_get_from_case[issue.get("key")]["comments"] = False
            data_to_get_from_case[issue.get("key")]["attachments"] = False

            # Create a list of just comment string
            comments = issue.get("comment")
            if comments:
                data_to_get_from_case[issue.get("key")]["comments"] = True
                for comment_num in range(len(comments)):
                    comments[comment_num] = comments[comment_num].get("body")

            # Convert the string times to integer epoch time
            issue["created"] = str_time_to_int_time(issue.get("created"))
            issue["updated"] = str_time_to_int_time(issue.get("updated"))

            # Create a list of just attachment filenames
            attachments = issue.get("attachment")
            if attachments:
                data_to_get_from_case[issue.get("key")]["attachments"] = True
                for attach_num in range(len(attachments)):
                    attachments[attach_num] = {
                        "filename": attachments[attach_num].get("filename"),
                        "content": self.jira_client._session.get(attachments[attach_num].get("content")).content
                    }

            issue_description = issue.get("description")
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
