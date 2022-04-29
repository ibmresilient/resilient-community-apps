# -*- coding: utf-8 -*-
#
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
#
from logging import getLogger
from resilient_lib import validate_fields, IntegrationError
from fn_splunk_integration.util.splunk_utils import SplunkServers
from fn_splunk_integration.util.splunk_constants import PACKAGE_NAME, GET_FIELD, UPDATE_FIELD

LOG = getLogger(__name__)

def make_query_string(query_string, params):
    """
    Substitute parameters into the query
    :param query: Input query with params
    :param params: Values used to substitute
    :return: (str) Query with params substitued
    """

    index = 1
    for param in params:
        if param:
            to_replace = "%%param%d%%" % index
            query_string = query_string.replace(to_replace, param)
        index += 1

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

def get_servers_list(opts):
    """
    Used for initilizing or reloading the options variable
    :param opts: List of options
    :return: List of splunk servers
    """
    servers_list = {}

    options = opts.get(PACKAGE_NAME, {})

    if options: # If no label given [fn_splunk_integration]
        server_list = {PACKAGE_NAME}
    else: # If label given [fn_splunk_integration:label]
        servers = SplunkServers(opts, options)
        server_list = servers.get_server_name_list()

    # Creates a dictionary that is filled with the splunk servers
    # and there configurations 
    for server_name in server_list:
        servers_list[server_name] = opts.get(server_name, {})
        validate_fields(["host", "port", "username", "splunkpassword"], servers_list[server_name])

    return servers_list

def update_splunk_servers_select_list(servers_list, res_rest_client, field_name):
    """
    Update values in splunk_servers select field
    :param servers_list: List of splunk servers in app.config
    :param res_rest_client: SOAR rest client connection
    :param field_name: Activity field name
    :return: None
    """

    # Create list of splunk server labels
    server_name_list = []
    for server in servers_list:
        if ":" in server:
            server_name_list.append(server[server.index(":")+1:])
        else:
            server_name_list.append(server)

    try:
        payload = res_rest_client.get(GET_FIELD.format(field_name))

        if type(payload) == list or payload.get("input_type") != "select":
            return None

        # Create payload 
        if server_name_list:

            # Put payload with no values to delete old values
            del payload["values"]
            res_rest_client.put(UPDATE_FIELD.format(field_name), payload)

            # Add values to the payload
            payload["values"] = [
                {"label": str(value), "enabled": True, "hidden": False}
                for value in server_name_list
            ]
            # Put payload with values to SOAR
            res_rest_client.put(UPDATE_FIELD.format(field_name), payload)

    except Exception as err_msg:
        LOG.warning("Action failed: {} error: {}".format(field_name, err_msg))
        raise IntegrationError("Error while updating action field: {}".format(field_name))
