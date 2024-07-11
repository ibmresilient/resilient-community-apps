# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""Class to handle manipulating the ServiceNow Records Data Table"""

class ServiceNowRecordsDataTable(object):
    """Class that handles the sn_records_dt datatable"""
    def __init__(self, res_client, incident_id):
        self.res_client = res_client
        self.incident_id = incident_id
        self.api_name = "sn_records_dt"
        self.data = None
        self.rows = None

        self.get_data()

    def as_dict(self):
        """Returns this class object as a dictionary"""
        return self.__dict__

    def get_data(self):
        """Gets that data and rows of the data table"""
        uri = f"/incidents/{self.incident_id}/table_data/{self.api_name}?handle_format=names"
        try:
            self.data = self.res_client.get(uri)
            self.rows = self.data["rows"]
        except Exception as err:
            raise ValueError("Failed to get sn_records_dt Datatable", err)

    def get_row(self, cell_name, cell_value):
        """Returns the row if found. Returns None if no matching row found"""
        for row in self.rows:
            cells = row["cells"]
            if cells[cell_name] and cells[cell_name].get("value") and cells[cell_name].get("value") == cell_value:
                return row
        return None

    def get_sn_ref_id(self, res_id):
        """Returns the sn_ref_id that relates to the res_id"""
        row = self.get_row("sn_records_dt_res_id", res_id)

        if row:
            cells = row["cells"]
            return str(cells["sn_records_dt_sn_ref_id"]["value"])

        return None

    def get_sn_table_name(self, res_id):
        row = self.get_row("sn_records_dt_res_id", res_id)

        if row:
            cells = row["cells"]
            return str(cells["sn_records_dt_snow_table"]["value"])

        return None

    def add_row(self, time, name, res_type, res_id, sn_ref_id, res_status, snow_status, snow_table, link, parent_ref_id=None):
        """Adds a new row to the data table and returns that row"""
        # Generate uri to POST datatable row
        uri = f"/incidents/{self.incident_id}/table_data/{self.api_name}/row_data?handle_format=names"

        cells = [
            ("sn_records_dt_time", time),
            ("sn_records_dt_name", name),
            ("sn_records_dt_type", res_type),
            ("sn_records_dt_res_id", res_id),
            ("sn_records_dt_sn_ref_id", sn_ref_id),
            ("sn_records_dt_res_status", res_status),
            ("sn_records_dt_snow_status", snow_status),
            ("sn_records_dt_snow_table", snow_table),
            ("sn_records_dt_links", link)
        ]

        if parent_ref_id:
            cells.append(
                ("sn_records_dt_sn_parent_ref_id", parent_ref_id)
            )

        formatted_cells = {}

        # Format the cells
        for cell in cells:
            formatted_cells[cell[0]] = {"value": cell[1]}

        formatted_cells = {
            "cells": formatted_cells
        }

        return self.res_client.post(uri, formatted_cells)

    def update_row(self, row, cells_to_update):
        """Updates the row with the given cells_to_update and returns the updated row"""
        # Generate uri to POST datatable row
        uri = f"/incidents/{self.incident_id}/table_data/{self.api_name}/row_data/{row['id']}?handle_format=names"

        def get_value(cell_name):
            """Gets the new or old value of the cell"""
            if cell_name in cells_to_update:
                return cells_to_update[cell_name]

            return row["cells"][cell_name].get("value")

        cells = [
            ("sn_records_dt_time", get_value("sn_records_dt_time")),
            ("sn_records_dt_name", get_value("sn_records_dt_name")),
            ("sn_records_dt_type", get_value("sn_records_dt_type")),
            ("sn_records_dt_res_id", get_value("sn_records_dt_res_id")),
            ("sn_records_dt_sn_ref_id", get_value("sn_records_dt_sn_ref_id")),
            ("sn_records_dt_res_status", get_value("sn_records_dt_res_status")),
            ("sn_records_dt_sn_parent_ref_id", get_value("sn_records_dt_sn_parent_ref_id")),
            ("sn_records_dt_snow_status", get_value("sn_records_dt_snow_status")),
            ("sn_records_dt_snow_table", get_value("sn_records_dt_snow_table")),
            ("sn_records_dt_links", get_value("sn_records_dt_links"))
        ]

        formatted_cells = {}

        # Format the cells
        for cell in cells:
            formatted_cells[cell[0]] = {"value": cell[1]}

        formatted_cells = {
            "cells": formatted_cells
        }

        return self.res_client.put(uri, formatted_cells)
