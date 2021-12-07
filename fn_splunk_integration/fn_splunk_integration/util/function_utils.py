# -*- coding: utf-8 -*-
#
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
#
import logging
import fn_splunk_integration.util.splunk_constants as splunk_constants
from resilient_lib import validate_fields, IntegrationError
from fn_splunk_integration.util.resilient_utils import resilient_utils
from fn_splunk_integration.util import splunk_utils

LOG = logging.getLogger(__name__)

def make_query_string(query, params):
    """
    Substitute parameters into the query
    :param query: input query with params
    :param params: values used to substitute
    :return:
    """
    query_string = query

    index = 1
    for param in params:
        if param:
            to_replace = "%%param%d%%" % index
            query_string = query_string.replace(to_replace, param)
        index += 1

    return query_string

def make_item_dict(params):
    """
    Use the params list to build a dict
    :param params: parameter list
    :return: dict
    """
    ret = {}

    list_len = len(params)
    if list_len%2 != 0:
        raise IntegrationError(str(params))

    index = 0
    while index < list_len:
        if params[index]:
            # Allow the value (params[index + 1] here) to be empty (None)?
            # Let Splunk to return an error if it does not support empty value
            ret[params[index]] = params[index + 1]
        else:
            # If key is None, we can not add it to the dictionary
            LOG.debug("The {}th key is None with value {}".format(str(index), str(params[index + 1])))
        index += 2

    return ret

def get_servers_list(opts, choose):
    """
    Used for initilizing or reloading the options variable
    :param opts: list of options
    :param choose: either init or reload
    :return: list of splunk servers
    """
    servers_list = {}

    options = opts.get(splunk_constants.PACKAGE_NAME, {})

    if options:
        server_list = {splunk_constants.PACKAGE_NAME}
    else:
        servers = splunk_utils.SplunkServers(opts, options)
        server_list = servers.get_server_name_list()

    for server_name in server_list:
        servers_list[server_name] = opts.get(server_name, {})
        if choose == "init":
            options = servers_list[server_name]

            required_fields = ["host", "port", "verify_cert"]
            validate_fields(required_fields, options)

    return servers_list

def update_splunk_servers_select_list(opts, servers_list):
    """
    Populate the splunk_servers select list
    :param opts: list of options
    :param servers_list: list of splunk servers in app.config
    :return: None
    """

    server_name_list = []
    for server in servers_list:
        if ":" in server:
            server_name_list.append(server[server.index(":")+1:])
        else:
            server_name_list.append(server)

    resilient_utils(opts).update_rule_action_field_values("splunk_servers", server_name_list)
