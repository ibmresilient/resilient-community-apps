# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-

from jira import JIRA
from resilient_lib import IntegrationError, validate_fields, str_to_bool, build_incident_url, build_resilient_url, MarkdownParser

CONFIG_DATA_SECTION = "fn_jira"
SUPPORTED_AUTH_METHODS = ("AUTH", "BASIC")

# Markdown Constants
STRIKEOUT_CHAR = "-"
BOLD_CHAR = "*"
UNDERLINE_CHAR = "+"
ITALIC_CHAR = "_"


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
        {"name": "user", "placeholder": "<jira user>"},
        {"name": "password", "placeholder": "<jira user password>"},
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
    auth_method = app_configs.get("auth_method", SUPPORTED_AUTH_METHODS[0])
    server = app_configs.get("url")
    verify = app_configs.get("verify_cert")
    proxies = rc.get_proxies()

    try:
        timeout = int(app_configs.get("timeout", 10))
    except ValueError:
        raise IntegrationError("Ensure 'timeout' is an integer in your config file")

    # AUTH
    if auth_method == SUPPORTED_AUTH_METHODS[0]:
        return JIRA(
            auth=(app_configs.get("user"), app_configs.get("password")),
            options={"server": server, "verify": verify},
            proxies=proxies,
            timeout=timeout,
        )

    # BASIC
    elif auth_method == SUPPORTED_AUTH_METHODS[1]:
        return JIRA(
            basic_auth=(app_configs.get("user"), app_configs.get("password")),
            options={"server": server, "verify": verify},
            proxies=proxies,
            timeout=timeout,
        )

    else:
        raise IntegrationError("{0} auth_method is not supported. Supported methods: {1}".format(auth_method, SUPPORTED_AUTH_METHODS))


def prepend_text(a, b=None):
    """Prepends a to b if b exists, else just returns a"""
    if not b:
        return a

    return u"{0}\n\n{1}".format(a, b)


def build_url_to_resilient(host, port, incident_id, task_id=None):
    """Builds the URL to resilient. If a task_id is provided builds
    the URL to include the task"""
    url = build_incident_url(build_resilient_url(host, port), incident_id)

    if task_id:
        url = "{0}?task_id={1}".format(url, task_id)

    return url


def to_markdown(html):
    """Takes a string of html converts it to Markdown
    and returns it"""
    parser = MarkdownParser(strikeout=STRIKEOUT_CHAR,
                            bold=BOLD_CHAR,
                            underline=UNDERLINE_CHAR,
                            italic=ITALIC_CHAR)

    return parser.convert(html)


def format_dict(dict_to_format):
    """
    Function that formats the passed dictionary
    and returns a string

    :param dict_to_format: A dict you want to format

    :return: String of the keys and values in the dict formatted
    :rtype: str
    """
    str_to_rtn = "\n-----------------\n"

    if not dict_to_format:
        str_to_rtn += "NONE\n"

    for (k, v) in dict_to_format.items():

        str_to_rtn += "{0}: {1}\n".format(k, v)

    str_to_rtn += "-----------------\n"

    return str_to_rtn
