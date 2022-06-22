# -*- coding: utf-8 -*-
#
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
#
# Util functions

from six import string_types
from logging import getLogger
from resilient_lib import validate_fields, IntegrationError, str_to_bool
from fn_qradar_enhanced_data.util import qradar_utils
from fn_qradar_enhanced_data.util.qradar_constants import PACKAGE_NAME, GLOBAL_SETTINGS

LOG = getLogger(__name__)

def make_query_string(query_string, params):
    """
    Substitute parameters into the query
    :param query_string: Input query with params
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

def fix_dict_value(events):
    """
    When the returned data from QRadar is used to update a datatable, we need to
    convert types like dict/list into strings
    :param events: List of dicts
    :return: (list) List of dicts
    """

    for event in events:
        # event is a dict
        if isinstance(event, dict):
            for key in event:
                if not isinstance(event[key], string_types):
                    event[key] = u"{}".format(event[key])

    return events

def get_server_settings(opts, qradar_label):
    """
    Used for initilizing or reloading the options variable
    :param opts: List of options
    :return: QRadar server settings for specified server
    """
    servers_list = {}

    options = opts.get(PACKAGE_NAME, {})

    if options: # If no label given [fn_qradar_integration]
        server_list = {PACKAGE_NAME}
    else: # If label given [fn_qradar_integration:label]
        servers = qradar_utils.QRadarServers(opts, options)
        server_list = servers.get_server_name_list()
        # If GLOBAL_SETTINGS is in server_list then remove it from list and validate fields
        if GLOBAL_SETTINGS in server_list:
            server_list.remove(GLOBAL_SETTINGS)
            validate_fields(["polling_interval", "polling_lookback"], opts.get(GLOBAL_SETTINGS, {}))

    # Creates a dictionary that is filled with the QRadar servers
    # and there configurations
    for server_name in server_list:
        servers_list[server_name] = opts.get(server_name, {})
        validate_fields(["host", "verify_cert"], servers_list[server_name])

    # Get configuration for QRadar server specified
    options = qradar_utils.QRadarServers.qradar_label_test(qradar_label, servers_list)
    LOG.debug("Connection to {} using {}".format(options.get("host"),
                                                options.get("username", None) or options.get("qradartoken", None)))

    return options

def get_qradar_client(opts, options):
    """
    Connects to given QRadar server
    :param opts: All settings including SOAR settings
    :param options: Settings for specified QRadar server
    :return: Client connection to QRadar server
    """
    # Get Certificates for QRadar
    qradar_verify_cert = False if options.get("verify_cert", "false").lower() == "false" else options.get("verify_cert")

    return qradar_utils.QRadarClient(host=options.get("host"),
                                    username=options.get("username", None),
                                    password=options.get("qradarpassword", None),
                                    token=options.get("qradartoken", None),
                                    cafile=qradar_verify_cert,
                                    opts=opts, function_opts=options)

def clear(rest_client, table_name, incident_id):
    """
    Clear data in given table on SOAR
    :param res_rest_client: SOAR rest client connection
    :param table_name: API access name of the table to clear
    :param incident_id: SOAR ID for the incident
    :return: None
    """
    try:
        rest_client.delete("/incidents/{}/table_data/{}/row_data?handle_format=names".format(incident_id, table_name))
        LOG.info("Data in table {} in incident {} has been cleared".format(table_name, incident_id))

    except Exception as err_msg:
        LOG.error("Failed to clear table: {} error: {}".format(table_name, err_msg))
        raise IntegrationError("Error while clearing table: {}".format(table_name))

def clear_table(rest_client, table_name, incident_id, global_settings):
    """
    Calls function to clear SOAR data table based on app.config
    :param res_rest_client: SOAR rest client connection
    :param table_name: API access name of the table to clear
    :param incident_id: SOAR ID for the incident
    :param global_settings: Global settings for the integration
    :return: None
    """
    if table_name:
        if global_settings:
            # If clear_datatables in app.config equals True then clear given data table
            # If clear_datatables does not exist then it defaults to True
            if str_to_bool(global_settings.get("clear_datatables", True)) == True:
                clear(rest_client, table_name, incident_id)
        else: # If global_settings does not exist then clear given data table
            clear(rest_client, table_name, incident_id)
