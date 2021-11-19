# -*- coding: utf-8 -*-
#
# (c) Copyright IBM Corp. 2021. All Rights Reserved.
#
# Util functions
import six
from resilient_lib import validate_fields
import fn_qradar_enhanced_data.util.qradar_constants as qradar_constants
from fn_qradar_enhanced_data.util import qradar_utils
from fn_qradar_enhanced_data.util.resilient_utils import resilient_utils

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
                if not isinstance(event[key], six.string_types):
                    event[key] = u"{}".format(event[key])

    return events

def get_servers_list(opts, choose):
    """
    Used for initilizing or reloading the options variable
    :param opts: list of options
    :param choose: either init or reload
    :return: list of qradar servers
    """
    servers_list = {}

    options = opts.get(qradar_constants.PACKAGE_NAME, {})

    if options:
        server_list = {qradar_constants.PACKAGE_NAME}
    else:
        servers = qradar_utils.QRadarServers(opts, options)
        server_list = servers.get_server_name_list()

    for server_name in server_list:
        servers_list[server_name] = opts.get(server_name, {})
        if choose == "init":
            options = servers_list[server_name]
            validate_fields(["host", "verify_cert"], options)

    return servers_list

def update_qradar_servers_select_list(opts, servers_list):
    """
    Populate the qradar_servers select list
    :param opts: list of options
    :param servers_list: list of qradar servers in app.config
    :return: None
    """
    server_name_list = [
        server[server.index(":")+1:]
        for server in servers_list
    ]
    resilient_utils(opts).update_rule_action_field_values("qradar_servers", server_name_list)
