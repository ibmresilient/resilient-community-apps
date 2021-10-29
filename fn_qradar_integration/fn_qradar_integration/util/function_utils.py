# -*- coding: utf-8 -*-
#
# (c) Copyright IBM Corp. 2021. All Rights Reserved.
#
#   Util functions
#

import six
from resilient_lib import validate_fields
import fn_qradar_integration.util.qradar_constants as qradar_constants
from fn_qradar_integration.util import qradar_utils

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

            required_fields = ["host", "verify_cert"]
            validate_fields(required_fields, options)

    return servers_list

def get_resilient_opts(opts):
    """
    Used for initilizing or reloading the res_opts variable
    :param opts: list of options
    :return: dictionary of resilient configuration
    """
    res_opts = opts.get("resilient", {})
    res_opts["proxies"] = opts.get("proxy")
    res_opts["org_id"] = opts.get("org_id")
    res_opts["timeout"] = 30
    if opts.get("timeout"):
        res_opts["timeout"] = opts.get("timeout")
    
    return res_opts
