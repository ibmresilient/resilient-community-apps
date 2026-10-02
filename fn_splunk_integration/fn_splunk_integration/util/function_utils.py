# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.

from logging import getLogger
from resilient_lib import validate_fields, IntegrationError, str_to_bool, RequestsCommon
from fn_splunk_integration.util.splunk_utils import SplunkServers, SplunkUtils

PACKAGE_NAME = "fn_splunk_integration"
QUERY_PARAM = "splunk_query_param"
LOG = getLogger(__name__)

def make_query_string(query_string, params):
    """
    Substitute parameters into the query
    :param query: Input query with params
    :param params: Values used to substitute
    :return: (str) Query with params substituted
    """

    for param in params:
        if param:
            index = params.index(param)+1
            query_string = query_string.replace(f"%param{index}%", param)

    return query_string

def make_item_dict(params):
    """
    Use the params List to build a dict
    :param params: Parameter list
    :return: dict
    """
    ret = {}

    list_len = len(params)
    if list_len%2 != 0:
        raise IntegrationError(str(params))

    for index in range(0, list_len, 2):
        if params[index]:
            # Allow the value (params[index + 1] here) to be empty (None)?
            # Let Splunk to return an error if it does not support empty value
            ret[params[index]] = params[index + 1]
        else:
            # If key is None, we can not add it to the dictionary
            LOG.debug(f"The {str(index)}th key is None with value {str(params[index + 1])}")

    return ret

def get_servers_list(opts):
    """
    Used for initializing or reloading the options variable
    :param opts: List of options
    :return: List of splunk servers
    """
    servers_list = {}

    options = opts.get(PACKAGE_NAME, {})

    if options: # If no label given [fn_splunk_integration]
        server_list = {PACKAGE_NAME}
    else: # If label given [fn_splunk_integration:label]
        servers = SplunkServers(opts)
        server_list = servers.get_server_name_list()

    # Creates a dictionary that is filled with the splunk servers
    # and there configurations 
    for server_name in server_list:
        servers_list[server_name] = opts.get(server_name, {})
        validate_fields(["host", "port"], servers_list[server_name])
        user = servers_list[server_name].get("username", None)
        splunk_pass = servers_list[server_name].get("splunkpassword", None)
        token = servers_list[server_name].get("token", None)
        if not ((user and splunk_pass) or token):
            raise ValueError("Either username/splunkpassword or token need to be given")
        elif token:
            servers_list[server_name]["username"] = None
            servers_list[server_name]["splunkpassword"] = None

    return servers_list

def function_basics(fn_inputs, servers_list, opts):
    # Make that calls that all of the functions use
    options = SplunkServers.splunk_label_test(getattr(fn_inputs, "splunk_label", None), servers_list)
    rc = RequestsCommon(opts, options)

    verify = options.get("verify_cert", True)
    # convert potential strings to boolean if necessary
    # NOTE: it is possible that a string path should be returned,
    # in which case we don't want there to be a boolean conversion
    if isinstance(verify, str) and verify.lower() in ["false", "true"]:
        verify = str_to_bool(verify)

    # Log all the info
    LOG.info(str(fn_inputs))

    # Log the splunk server we are using
    LOG.info(f"Splunk host: {options.get('host')}, port: {options.get('port')}")

    return SplunkUtils(host=options.get("host"),
                            port=options.get("port"),
                            username=options.get("username", None),
                            password=options.get("splunkpassword", None),
                            token=options.get("token", None),
                            verify=verify,
                            proxies=rc.get_proxies(),
                            rc=rc)
