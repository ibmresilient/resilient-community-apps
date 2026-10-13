# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2020
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
"""
This module is responsible for processing outlier data and updating data to resilient table.
"""
import time
import six
from fn_guardium_integration.lib.action_handler import thread_controller
from fn_guardium_integration.lib.custom_exceptions import TabledataRestCallError


def update_outlier_details_table(cls_ref, table_id, inc_id, search_data):
    """
    Function to Update the guardium outlier details to table
    :param cls_ref:
    :param table_id: Resilient Outlier table ID
    :param inc_id: Action called incident ID
    :param search_data: outlier data returned from guardium
    :return:
    """
    # clearing the existing table data
    try:
        existing_table_data = cls_ref.return_table_data_by_table_id(table_id=table_id, incident_id=inc_id)
        if existing_table_data.get("rows"):
            rows_data = existing_table_data.get("rows")
            rows_id_list = [x.get("id") for x in rows_data]
            if six.PY2:
                for row_id in rows_id_list:
                    cls_ref.delete_resilient_table_row_data(row_id, inc_id, table_id)
                    time.sleep(2)
            else:
                thread_controller(cls_ref.delete_resilient_table_row_data, rows_id_list, inc_id, table_id)
        else:
            cls_ref.log.info("Selected table ID : {} is empty.".format(table_id))
    except Exception as er_msg:
        raise TabledataRestCallError(str(er_msg))

    # constructing table payload
    data_list = []
    update_time = int(round(time.time() * 1000))
    for detail_obj in search_data[0].get("items"):
        data_format = {
            "cells": {"grd_table_outlier_date_generated": {"value": update_time},
                      "grd_table_outlier_outliers_description": {"value": detail_obj.get("Textual Description")},
                      "grd_table_outlier_outliers_confidence_score": {"value": detail_obj.get("Anomaly Score")},
                      "grd_table_outlier_high_volume_outlier": {"value": detail_obj.get("High volume Outlier")},
                      "grd_table_outlier_vulnerable_obj_outlier": {"value": detail_obj.get("Vulnerable obj. Outlier")},
                      "grd_table_outlier_outliers_rare_or_new_behavior": {"value": detail_obj.get("New Outlier")},
                      "grd_table_outlier_outliers_diverse_behavior": {"value": detail_obj.get("Diverse Outlier")},
                      "grd_table_outlier_error_outlier": {"value": detail_obj.get("Error Outlier")},
                      "grd_table_outlier_outliers_server": {"value": detail_obj.get("Server")},
                      "grd_table_outlier_outliers_database": {"value": detail_obj.get("Database")},
                      "grd_table_outlier_outliers_db_user": {"value": detail_obj.get("DB User")},
                      "grd_table_outlier_outliers_unusual_working_hours": {"value": detail_obj.get("Time frame")},
                      "grd_table_outlier_date_time": {"value": "{}T{}".format(detail_obj.get("Date"), detail_obj.get("Time"))},
                      "grd_table_outlier_sensitive_object": {"value": detail_obj.get("Sensitive Object")},
                      "grd_table_outlier_number_of_instances": {"value": detail_obj.get("Number of Instances")},
                      "grd_table_outlier_outliers_total_records_affected": {"value": detail_obj.get("Total Records Affected")},
                      "grd_table_outlier_outliers_source_program": {"value": detail_obj.get("Source Program")},
                      "grd_table_outlier_outliers_os_user": {"value": detail_obj.get("OS User")},
                      "grd_table_outlier_client_host_name": {"value": detail_obj.get("Client Host name")},
                      "grd_table_outlier_outliers_database_table": {"value": detail_obj.get("Object")},
                      "grd_table_outlier_outliers_database_command": {"value": detail_obj.get("Verb")}
                      }
        }
        data_list.append(data_format)

    # Add data to the table
    thread_controller(cls_ref.add_sigle_table_row_data, data_list, inc_id, table_id)
