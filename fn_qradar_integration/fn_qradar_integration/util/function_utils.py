# -*- coding: utf-8 -*-
#
# (c) Copyright IBM Corp. 2021. All Rights Reserved.
#
#   Util functions
#

from six import string_types
import logging
from resilient_lib import validate_fields, IntegrationError
from fn_qradar_integration.util.qradar_constants import PACKAGE_NAME, UPDATE_FIELD, GET_FIELD
from fn_qradar_integration.util import qradar_utils

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

def fix_dict_value(events):
    """
    When the returned data from QRadar is used to update a datatable, we need to
    convert types like dict/list into strings
    :param events: list of dicts
    :return:
    """
    for event in events:
        # event is a dict
        if isinstance(event, dict):
            for key in event:
                if not isinstance(event[key], string_types):
                    event[key] = u"{}".format(event[key])

    return events

def get_servers_list(opts):
    """
    Used for initilizing or reloading the options variable
    :param opts: list of options
    :return: list of qradar servers
    """
    servers_list = {}

    options = opts.get(PACKAGE_NAME, {})

    if options: # If no labels given [fn_qradar_integration]
        server_list = {PACKAGE_NAME}
    else: # If labels given [fn_qradar_integration:label]
        servers = qradar_utils.QRadarServers(opts, options)
        server_list = servers.get_server_name_list()

    # Creates a dictionary that is filled with the QRadar servers
    # and there configurations
    for server_name in server_list:
        servers_list[server_name] = opts.get(server_name, {})
        validate_fields(["host", "verify_cert"], servers_list[server_name])

    return servers_list

def update_qradar_servers_select_list(servers_list, res_rest_client, field_name):
    """
    Update values in qradar_servers select field
    :param servers_list: list of qradar servers in app.config
    :param res_rest_client: resilient rest client connection
    :param field_name: activity field name
    :return: None
    """

    # Create list of qradar server labels
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
            payload["values"] = [
                {"label": str(value), "enabled": True, "hidden": False}
                for value in server_name_list
            ]

            res_rest_client.put(UPDATE_FIELD.format(field_name), payload, timeout=1000)

    except Exception as err_msg:
        LOG.warning("Action failed: {} error: {}".format(field_name, err_msg))
        raise IntegrationError("Error while updating action field: {}".format(field_name))
