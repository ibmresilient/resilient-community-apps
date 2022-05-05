# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-

import re

import requests

from jira import JIRA
from resilient_lib import (IntegrationError, MarkdownParser,
                           build_incident_url, build_resilient_url,
                           str_to_bool, validate_fields)

CONFIG_DATA_SECTION = "fn_jira"
SUPPORTED_AUTH_METHODS = ("AUTH", "BASIC", "OAUTH")

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

    elif auth_method == SUPPORTED_AUTH_METHODS[2]:
        key_cert_data = None
        try:
            with open(app_configs.get("private_rsa_key_file_path"), "r") as private_rsa_key:
                key_cert_data = private_rsa_key.read()
        except FileNotFoundError as e:
            raise IntegrationError("Private Key file not valid: {0}".format(str(e)))

        oauth_dict = {
            "access_token": app_configs.get("access_token"),
            "access_token_secret": app_configs.get("access_token_secret"),
            "consumer_key": app_configs.get("consumer_key_name"),
            "key_cert": key_cert_data
        }

        # check for missing configs:
        for key in oauth_dict:
            if not oauth_dict[key]:
                raise IntegrationError("app.config is missing {0} which is a required configration for auth_method={1}.".format(key, auth_method))

        return JIRA(
            oauth=oauth_dict,
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
    """Builds the URL to SOAR. If a task_id is provided builds
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


def extract_images(html):
    """Takes a string of HTML text from a SOAR note and extracts a list of 
    images as src links with associated alt text.
    Also modifies the html to fit the Jira-style image syntax (ex: !my_pic.png!)"""

    # extract src values and alt values from SOAR's image tags
    # ex: <img src='https://ibm.com/some_pic.jpg' alt='some_pic.jpg' />
    srcs = re.findall(r'<img[^>]+src="([^">]+)', html)
    alts = re.findall(r'<img[^>]+alt="([^">]+)', html)

    # sub in Jira image syntax for each image tag
    for alt in alts:
        html = re.subn(r'<img.*?>', " !{0}! ".format(alt), html, count=1)[0]

    # zip together the src and alts and return that as well as the adjusted html
    return tuple(zip(srcs, alts)), html


def read_img(res_client, img_url):
    """Reads a url image to a filestream"""

    if img_url.startswith("http"):
        # external resource
        return requests.get(img_url, headers={"User-agent": "SOAR Apphost"}).content
    else:
        # resource from the platform
        resource_prefix = "/rest"
        return res_client.get(img_url[img_url.index(resource_prefix)+len(resource_prefix):], is_uri_absolute=True, get_response_object=True).content


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

def validate_task_id_for_jira_issue_id(res_client, app_configs, incident_id, task_id, fn_inputs):
    """Validates the input for task_id and sets the value of the task's associated Jira ID
    by searching for the value in the Jira Datatable
    
    :param res_client: the rest client object to communicate to SOAR platform
    :type res_client: resilient.SimpleClient <resilient.co3.SimpleClient>
    :param incident_id: ID of the incident within SOAR
    :type incident_id: string
    :param task_id: ID of the task within SOAR (note this function is only necessary for tasks)
    :type task_id: string
    :param fn_inputs: current set of inputs to the function being called
    :type fn_inputs: dict
    :return: Whether the task was a valid task with an associated Jira ID. 
             if so, modifies fn_inputs obj to store correct jira_issue_id and jira_url
    :rtype: bool
    """

    # using datatable in SOAR, grab the jira id and jira url from the correct row in the table
    # if the table row associated with this task id doesn't exist, returns (None, None)
    jira_issue_id, jira_link = _get_jira_issue_id(res_client, app_configs.get("jira_dt_name", DEFAULT_JIRA_DT_NAME), incident_id, task_id)

    if not jira_issue_id:
        # task not yet synced to Jira
        return False

    # success
    # set the jira_issue_id in fn_inputs to overwrite the value of the parent incident
    fn_inputs[JIRA_ISSUE_ID_FUNCT_INPUT_NAME] = jira_issue_id
    fn_inputs[JIRA_ISSUE_LINK] = jira_link
    return True

def _get_jira_issue_id(res_client, dt_name, incident_id, task_id):
    """Returns the jira_issue_id and jira_url that relates to the task_id"""
    row = _get_row(res_client, dt_name, incident_id, "task_id", task_id)

    if row is not None:
        cells = row["cells"]
        return str(cells[JIRA_DT_ISSUE_ID_COL_NAME]["value"]), str(cells[JIRA_DT_ISSUE_LINK_COL_NAME]["value"])
    else:
        return None, None

def _get_row(res_client, dt_name, incident_id, cell_name, cell_value):
    """Returns the row with a matching value to cell_name and cell_value if found. Returns None if no matching row found"""
    uri = "/incidents/{0}/table_data/{1}?handle_format=names".format(incident_id, dt_name)
    try:
        data = res_client.get(uri)
        rows = data["rows"]
    except Exception as err:
        raise IntegrationError("Failed to get '{0}' Datatable. This is required to send task notes to Jira".format(dt_name), err)

    for row in rows:
        cells = row["cells"]
        if cells.get(cell_name) and cells[cell_name].get("value") and str(cells[cell_name].get("value")) == str(cell_value):
            return row
    return None
