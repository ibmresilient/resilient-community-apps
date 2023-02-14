# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

from logging import getLogger
from urllib.parse import urljoin

from requests.exceptions import JSONDecodeError
from resilient_lib import IntegrationError, readable_datetime, str_to_bool, validate_fields, RequestsCommon

LOG = getLogger(__name__)

PACKAGE_NAME = "fn_jira"
GLOBAL_SETTINGS = f"{PACKAGE_NAME}:global_settings"
SUPPORTED_AUTH_METHODS = ("AUTH", "BASIC", "TOKEN", "OAUTH")

# change the header as necessary
HEADER = { 'Content-Type': 'application/json' }

class AppCommon():
    def __init__(self, rc, opts, app_configs):
        """
        Initialize the parameters needed to communicate to the endpoint solution

        :param opts: All of the settings from the app.config
        :type opts: dict
        :param rc: object to resilient_lib.requests_common for making API calls
        :type rc: ``resilient_lib.RequestsCommon``
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

        self.rc = rc

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
            self.proxies = RequestsCommon(opts, app_configs).get_proxies()

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

    def __init_session_obj(self):
        """
        
        """
        if not hasattr(AppCommon, "jira_session"):
            AppCommon.jira_session = Session()

    def _get_uri(self, cmd):
        """
        Build API url
        <- ::CHANGE_ME:: change this to reflect the correct way to build an API call ->

        :param cmd: portion of API: alerts, endpoints, policies
        :type cmd: str
        :return: complete URL
        :rtype: str
        """
        return urljoin(self.endpoint_url, cmd)

    def _make_headers(self, token):
        """Build API header using authorization token

        :param token: authorization token
        :type token: str
        :return: complete header
        :rtype: dict
        """
        header = HEADER.copy()
        # modify to represent how to build the header

        return header

    def _api_call(self, method, url, payload=None):
        """
        Make an API call to the endpoint solution and get back the response

        :param method: REST method to execute (GET, POST, PUT, ...)
        :type method: str
        :param url: URL to send request to
        :type url: str
        :param payload: JSON payload to send if a POST, defaults to None
        :type payload: dict|None
        :return: requests.Response object returned from the endpoint call
        :rtype: ``requests.Response``
        """    
        # <- ::CHANGE_ME:: there may be changes needed in here to
        # work with your endpoint solution ->

        return self.rc.execute(method,
                               url,
                               params=params,
                               json=payload,
                               headers=self._make_headers(),
                               verify=self.verify,
                               callback=callback)

    def query_entities_since_ts(self, timestamp, *args, **kwargs):
        """
        Get changed entities since last poller run

        :param timestamp: datetime when the last poller ran
        :type timestamp: datetime
        :param *args: additional positional parameters needed for endpoint queries
        :param **kwargs: additional key/value pairs needed for endpoint queries
        :return: changed entity list
        :rtype: list
        """
        # <- ::CHANGE_ME:: -> for the specific API calls
        # and make sure to properly handle pagination!
        query = {
            "query_field_name": readable_datetime(timestamp) # utc datetime format
        }

        LOG.debug("Querying endpoint with %s", query)
        response, err_msg = self._api_call("GET", 'alerts', query, refresh_authentication=True)
        if err_msg:
            LOG.error("%s API call failed: %s", PACKAGE_NAME, err_msg)
            return None

        return response.json()

    def make_linkback_url(self, entity_id, linkback_url):
        """
        Create a url to link back to the endpoint entity

        :param entity_id: id representing the entity
        :type entity_id: str
        :param linkback_url: string to in which one can format the entity ID to join to the base url
        :type linkback_url: str
        :return: completed url for linkback
        :rtype: str
        """
        return urljoin(self.endpoint_url, linkback_url.format(entity_id))


def callback(response):
    """
    Callback needed for certain REST API calls to return a formatted error message

    :param response: the requests response object
    :type response: ``requests.Response``
    :return: response, error_msg
    :rtype: tuple(``requests.Reponse``, str)
    """
    error_msg = None
    if response.status_code >= 300 and response.status_code <= 500:
        try:
            resp = response.json()
            msg = resp.get('messages') or resp.get('message')
            details = resp.get('details')
        except JSONDecodeError as err:
            msg = str(err)
            details = response.text

        error_msg  = u"Error: \n    status code: {0}\n    message: {1}\n    details: {2}".format(
            response.status_code,
            msg,
            details)

    return response, error_msg

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

class JiraServers():
    def __init__(self, opts):
        self.servers, self.server_name_list = self._load_servers(opts)

    def _load_servers(self, opts):
        """
        Create list of label names and a dictionary of the servers and their configs
        :param opts: Dict of app_configs
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
        :return: Dictionary of app_configs for choosen server
        """
        # If label not given and using previous versions app.config [fn_jira]
        if not jira_label and servers_list.get(PACKAGE_NAME):
            return servers_list[PACKAGE_NAME]
        elif not jira_label:
            raise IntegrationError("No label was given and is required if servers are labeled in the app.config")

        label = f"{PACKAGE_NAME}:{jira_label}"
        if jira_label and label in servers_list:
            app_configs = servers_list[label]
        elif len(servers_list) == 1:
            app_configs = servers_list[list(servers_list.keys())[0]]
        else:
            raise IntegrationError("{} did not match labels given in the app.config".format(jira_label))

        return app_configs

    def _get_server_name_list(self, opts):
        """
        Return the list of jira server names defined in the app.config in fn_jira.
        :param opts: List of app_configs
        :return: List of servers
        """
        return [key for key in opts.keys() if key.startswith(f"{PACKAGE_NAME}:") and key != GLOBAL_SETTINGS]

    def get_server_name_list(self):
        """
        Return list of all server names
        """
        return self.server_name_list