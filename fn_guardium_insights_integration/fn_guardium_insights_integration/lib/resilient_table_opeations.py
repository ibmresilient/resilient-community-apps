# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
import time

import six

from fn_guardium_insights_integration.lib.action_handler import thread_controller
from fn_guardium_insights_integration.lib.custom_exceptions import TableDataRestCallError
from fn_guardium_insights_integration.lib.time_conversions import convert_utc_date_time_milli_seconds
from fn_guardium_insights_integration.util.constants import TABLE_ADD_ROW, DELETE_TABLE_ROW, GET_TABLE_DATA_BY_ID


class ResilientTableOperations(object):
    """
    Class to handle the resilient table operations.
    """
    def __init__(self, table_id, incident_id, rest_client, log):
        self.rest_client = rest_client
        self.log = log
        self.table_id = table_id
        self.incident_id = incident_id

    def add_single_table_row_data(self, row_data):
        """
        Method to add table row data.
        """
        try:
            self.rest_client.post(TABLE_ADD_ROW.format(inc_id=self.incident_id, table_id=self.table_id), row_data)
        except Exception as err:
            self.log.error(str(err))

    def delete_resilient_table_row_data(self, row_id):
        """
        Wrapper to delete a row from the data table
        :param row_id: Resilient table row id to be deleted
        :return: on success return delete call result.
        """
        try:
            row_delete_status = self.rest_client.delete(
                DELETE_TABLE_ROW.format(inc_id=self.incident_id, table_id=self.table_id, row_id=row_id))
            return row_delete_status
        except Exception as err:
            self.log.error(str(err))

    def get_table_data(self):
        """
        :return: Table Data for the given table ID
        """
        try:
            __table_data = self.rest_client.get(
                GET_TABLE_DATA_BY_ID.format(inc_id=self.incident_id, table_id=self.table_id))
        except Exception as err:
            raise TableDataRestCallError("Fetch Table data Rest Call Error - {}".format(err))
        if __table_data:
            return __table_data
        else:
            self.log.debug("No Table Data found in Resilient Incident : {}".format(self.incident_id))
            return None

    @staticmethod
    def get_column_data_from_table(column_id, table_data):
        """
        :param column_id:
        :param table_data:
        :return: Task ID's from table data
        """
        __table_rows = table_data.get('rows')
        __column_data = list()
        for row_data in __table_rows:
            __column_data.append(row_data.get('cells').get(column_id).get('value'))
        return __column_data

    @staticmethod
    def construct_table_payload(event_data):
        """
        Method to construct the table row payload to add an table entry.
        """
        formatted_cell_data = dict()
        formatted_cell_data['cells'] = dict()
        _cell_map = {"gi_dt_cl_date_created": int(time.time() * 1000), "gi_dt_cl_start_datelocal_time": "1",
                     "gi_dt_cl_datasource_ip": "2", "gi_dt_cl_datasource_name": "3", "gi_dt_cl_datasource_type": "4",
                     "gi_dt_cl_port": "5", "gi_dt_cl_service_name": "6", "gi_dt_cl_schema": "7",
                     "gi_dt_cl_catalog": "8", "gi_dt_cl_table": "9", "gi_dt_cl_column": "10",
                     "gi_dt_cl_description": "11", "gi_dt_cl_classification_name": "12",
                     "gi_dt_cl_classification_rule": "13", "gi_dt_cl_category": "14", "gi_dt_cl_comprehensive": "15"}
        for map_key, map_value in _cell_map.items():
            if map_key not in ["gi_dt_cl_date_created", "gi_dt_cl_start_datelocal_time"]:
                formatted_cell_data['cells'][map_key] = {"value": event_data.get(map_value)}
            elif map_key == "gi_dt_cl_start_datelocal_time":
                start_local = convert_utc_date_time_milli_seconds(event_data.get(map_value),
                                                                  format_str='%Y-%m-%d %H:%M:%S.%f')
                formatted_cell_data["cells"][map_key] = {"value": start_local}
            else:
                formatted_cell_data["cells"][map_key] = {"value": map_value}
        return formatted_cell_data

    def return_table_data_by_table_id(self):
        """
        :return: Table Data for the given table ID
        """
        try:
            __table_data = self.rest_client.get(
                GET_TABLE_DATA_BY_ID.format(inc_id=self.incident_id, table_id=self.table_id), timeout=300)
        except Exception as err:
            raise TableDataRestCallError("Fetch Table data Rest Call Error - {}".format(err))
        if __table_data:
            return __table_data
        self.log.debug(u"No Table Data found in Resilient Incident : {}".format(self.incident_id))
        return None

    def clear_existing_table_data(self):
        """
        Method to clear/delete existing table data
        """
        try:
            existing_table_data = self.return_table_data_by_table_id()
            if existing_table_data.get("rows"):
                rows_data = existing_table_data.get("rows")
                rows_id_list = [x.get("id") for x in rows_data]
                if six.PY2:
                    for row_id in rows_id_list:
                        self.delete_resilient_table_row_data(row_id)
                        time.sleep(1)
                else:
                    thread_controller(self.delete_resilient_table_row_data, rows_id_list)
            else:
                self.log.debug("Selected table ID : {} is empty.".format(self.table_id))
        except Exception as er_msg:
            raise TableDataRestCallError(str(er_msg))

    def add_table_data(self, data_list):
        """
        Add table data for given data list, uses threading.
        """
        try:
            thread_controller(self.add_single_table_row_data, data_list)
        except Exception as er_msg:
            raise TableDataRestCallError(str(er_msg))
