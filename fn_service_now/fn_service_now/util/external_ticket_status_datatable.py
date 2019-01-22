# (c) Copyright IBM Corp. 2019. All Rights Reserved.
"""Class to handle manipulating the External ServiceNow Ticket Status Data table"""

class ExternalTicketStatusDatatable(object):
    """Class that handles the sn_external_ticket_status datatable"""
    def __init__(self, res_client, incident_id):
        self.res_client = res_client
        self.incident_id = incident_id
        self.api_name = "sn_external_ticket_status"
        self.data = None
        self.rows = None

        self.get_data()

    def as_dict(self):
        """Returns this class object as a dictionary"""
        return self.__dict__

    def get_data(self):
        """Gets that data and rows of the data table"""
        uri = "/incidents/{0}/table_data/{1}?handle_format=names".format(self.incident_id, self.api_name)
        try:
            self.data = self.res_client.get(uri)
            self.rows = self.data["rows"]
        except Exception as err:
            raise ValueError("Failed to get sn_external_ticket_status Datatable", err)

    def get_row(self, cell_name, cell_value):
        """Returns the row if found. Returns None if no matching row found"""
        for row in self.rows:
            cells = row["cells"]
            if cells[cell_name] and cells[cell_name].get("value") and cells[cell_name].get("value") == cell_value:
                return row
        return None

    def get_sn_ref_id(self, res_id):
        """Returns the sn_ref_id that relates to the res_id"""
        row = self.get_row("res_id", res_id)

        if row is not None:
            cells = row["cells"]
            return str(cells["sn_ref_id"]["value"])

        return None

    def add_row(self, time, res_id, sn_ref_id, resilient_status, servicenow_status, link):
        """Adds a new row to the data table and returns that row"""
        # Generate uri to POST datatable row
        uri = "/incidents/{0}/table_data/{1}/row_data?handle_format=names".format(self.incident_id, self.api_name)

        cells = [
            ("time", time),
            ("res_id", res_id),
            ("sn_ref_id", sn_ref_id),
            ("resilient_status", resilient_status),
            ("servicenow_status", servicenow_status),
            ("link", link)
        ]

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
        uri = "/incidents/{0}/table_data/{1}/row_data/{2}?handle_format=names".format(self.incident_id, self.api_name, row["id"])

        def get_value(cell_name):
            """Gets the new or old value of the cell"""
            if cell_name in cells_to_update:
                return cells_to_update[cell_name]

            return row["cells"][cell_name]["value"]

        cells = [
            ("time", get_value("time")),
            ("res_id", get_value("res_id")),
            ("sn_ref_id", get_value("sn_ref_id")),
            ("resilient_status", get_value("resilient_status")),
            ("servicenow_status", get_value("servicenow_status")),
            ("link", get_value("link"))
        ]

        formatted_cells = {}

        # Format the cells
        for cell in cells:
            formatted_cells[cell[0]] = {"value": cell[1]}

        formatted_cells = {
            "cells": formatted_cells
        }

        return self.res_client.put(uri, formatted_cells)
