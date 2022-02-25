# -*- coding: utf-8 -*-
#
# (c) Copyright IBM Corp. 2022. All Rights Reserved.
#
# Util functions

import six
import logging
from resilient_lib import validate_fields, IntegrationError
from fn_qradar_enhanced_data.util.qradar_constants import PACKAGE_NAME, GLOBAL_SETTINGS
from fn_qradar_enhanced_data.util import qradar_utils

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
                if not isinstance(event[key], six.string_types):
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
        if GLOBAL_SETTINGS not in server_list:
            raise IntegrationError('Unable to find [{}]'.format(GLOBAL_SETTINGS))
        server_list.remove(GLOBAL_SETTINGS)

    # Validate global_settings
    validate_fields(["polling_interval", "polling_lookback"], opts.get(GLOBAL_SETTINGS, {}))

    # Creates a dictionary that is filled with the QRadar servers
    # and there configurations
    for server_name in server_list:
        servers_list[server_name] = opts.get(server_name, {})
        validate_fields(["host", "verify_cert"], servers_list[server_name])

    return servers_list

def clear_table(rest_client, table_name, incident_id):
    """
    Clear data in given table on SOAR
    :param res_rest_client: SOAR rest client connection
    :param table_name: API access name of the table to clear
    :return: None
    """

    try:
        rest_client.delete("/incidents/{}/table_data/{}/row_data?handle_format=names".format(incident_id, table_name))

    except Exception as err_msg:
        LOG.warning("Failed to clear table: {} error: {}".format(table_name, err_msg))
        raise IntegrationError("Error while clearing table: {}".format(table_name))
