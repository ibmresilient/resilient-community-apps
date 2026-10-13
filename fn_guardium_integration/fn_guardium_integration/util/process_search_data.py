# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2020
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
"""
This module is responsible for processing guardium search data and updating to resilient search table
"""
import time
import six
from fn_guardium_integration.lib.action_handler import thread_controller
from fn_guardium_integration.lib.custom_exceptions import TabledataRestCallError


def update_search_to_table(resilient_object, table_id, inc_id, search_data, report_name):
    """
    :param resilient_object: Resilient service class object
    :param table_id: Search table ID
    :param inc_id: Action Called Resilient Incident ID
    :param search_data: Guardium Search Data
    :param report_name: Name of report to be searched in Guardium
    :return:
    """
    # clearing the existing table data
    try:
        existing_table_data = resilient_object.return_table_data_by_table_id(table_id=table_id, incident_id=inc_id)
        if existing_table_data.get("rows"):
            rows_data = existing_table_data.get("rows")
            rows_id_list = [x.get("id") for x in rows_data]
            if six.PY2:
                for row_id in rows_id_list:
                    resilient_object.delete_resilient_table_row_data(row_id, inc_id, table_id)
                    time.sleep(1)
            else:
                thread_controller(resilient_object.delete_resilient_table_row_data, rows_id_list, inc_id, table_id)
        else:
            resilient_object.log.debug("Selected table ID : {} is empty.".format(table_id))
    except Exception as er_msg:
        raise TabledataRestCallError(str(er_msg))

    # constructing table payload
    data_list = []
    update_time = int(round(time.time() * 1000))
    if not isinstance(search_data, list):
        search_data = [search_data]
    for data in search_data:
        column_string = ""
        for data_k, data_v in data.items():
            column_string += "<div><b>{}</b>: {}</div>".format(data_k, data_v)
        data_format = {"cells": {"grd_table_search_report_name": {"value": report_name},
                                 "grd_table_search_generated_date": {"value": update_time},
                                 "grd_table_search_column_data": {"value": column_string}
                                 }
                       }
        data_list.append(data_format)

    # Add data to the table
    thread_controller(resilient_object.add_sigle_table_row_data, data_list, inc_id, table_id)
