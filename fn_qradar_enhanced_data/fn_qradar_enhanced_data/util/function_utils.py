# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# Util functions

from logging import getLogger
from resilient_lib import IntegrationError, str_to_bool, validate_fields
from fn_qradar_enhanced_data.util import qradar_utils
from fn_qradar_enhanced_data.util.qradar_constants import (GLOBAL_SETTINGS, PACKAGE_NAME)

LOG = getLogger(__name__)

def get_search_timeout(global_settings, options):
    """
    Get the search_timeout either from app.config or make default value
    :param global_settings: Global settings for the integration
    :param options: Settings for specified QRadar server
    """
    timeout = 600 # Default timeout to 10 minutes
    # Check if search_timeout setting is configured in edm_global_settings
    if global_settings and global_settings.get("search_timeout"):
        timeout = float(global_settings.get("search_timeout"))
    # Check if search_timeout setting is configured for given QRadar server
    elif options.get("search_timeout"):
        timeout = float(options.get("search_timeout"))

    return timeout

def make_query_string(query_string, params):
    """
    Substitute parameters into the query
    :param query_string: Input query with params
    :param params: Values used to substitute
    :return: (str) Query with params substitued
    """
    for index, param in enumerate(params):
        query_string = query_string.replace(f"%param{index+1}%", param if param else '')

    return " ".join(query_string.split())

def fix_dict_value(events):
    """
    When the returned data from QRadar is used to update a datatable, we need to
    convert types like dict/list into strings
    :param events: List of dicts
    :return: (list) List of dicts
    """
    return [{key: f"{event[key]}" for key in event} for event in events if isinstance(event, dict)]

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
        server_list = qradar_utils.QRadarServers(opts).get_server_name_list()
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
    LOG.debug(f'Connection to {options.get("host")}')

    return options

def get_qradar_client(opts, options):
    """
    Connects to given QRadar server
    :param opts: All settings including SOAR settings
    :param options: Settings for specified QRadar server
    :return: Client connection to QRadar server
    """
    # Get Certificates for QRadar
    qradar_verify_cert = False if options.get("verify_cert", "false").lower() in ["false", "false|/path/to/cert"] else options.get("verify_cert")

    return qradar_utils.QRadarClient(host=options.get("host"),
                                     username=options.get("username", None),
                                     password=options.get("qradarpassword", None),
                                     token=options.get("qradartoken", None),
                                     cafile=qradar_verify_cert,
                                     opts=opts, function_opts=options)

def clear_table(rest_client, table_name, incident_id, global_settings):
    """
    Clear data in given table on SOAR
    :param res_rest_client: SOAR rest client connection
    :param table_name: API access name of the table to clear
    :param incident_id: SOAR ID for the incident
    :param global_settings: Global settings for the integration
    :return: None
    """
    if table_name:
        if global_settings and str_to_bool(global_settings.get("clear_datatables", True)) or not global_settings:
            # If clear_datatables in app.config equals True then clear given data table
            # If clear_datatables does not exist then it defaults to True
            # If global_settings does not exist then clear given data table
            try:
                rest_client.delete(f"/incidents/{incident_id}/table_data/{table_name}/row_data?handle_format=names")
                LOG.info(f"Data in table {table_name} in incident {incident_id} has been cleared")

            except Exception as err_msg:
                LOG.error(f"Failed to clear table: {table_name} error: {err_msg}")
                raise IntegrationError(f"Error while clearing table: {table_name}")
