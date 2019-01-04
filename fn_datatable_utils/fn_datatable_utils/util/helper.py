class RESDatatable:
    def __init__(self, res_client, incident_id, dt_api_name):
        self.res_client = res_client
        self.incident_id = incident_id
        self.api_name = dt_api_name
        self.data = None
        self.rows = None

    def get_data(self):
        uri = "/incidents/{0}/table_data/{1}?handle_format=names".format(self.incident_id, self.api_name)
        try:
            self.data = self.res_client.get(uri)
            self.rows = self.data["rows"]
        except Exception:
            raise ValueError("Failed to get {0} Datatable".format(self.api_name))

    def get_row(self, row_id=None, search_column=None, search_value=None):
        """Returns row if row found, else None"""

        if row_id:
            for row in self.rows:
                if row["id"] == row_id:
                    return row

        else:
            for row in self.rows:
                cells = row["cells"]

                if cells[search_column]["value"] == search_value:
                    return row

        return None

    def update_row(self, row_id, cells_to_update):

        err_msg = None
        return_value = None

        def get_cell_value(cell_name, cells_to_update):
            """Function to get the new/old cell value"""
            if cell_name in cells_to_update:
                return cells_to_update[cell_name]
            else:
                return row["cells"][cell_name]["value"]

        # Generate uri to POST datatable row
        uri = "/incidents/{0}/table_data/{1}/row_data/{2}?handle_format=names".format(self.incident_id, self.api_name, row_id)
        current_cells = []
        formatted_cells = {}

        # Get the row we want to update
        row = self.get_row(row_id)

        if row is None:
            raise ValueError("Could not find row to update for row_id: '{0}'".format(row_id))

        for entry in row["cells"]:
            cell_name = entry
            current_cells.append((cell_name, get_cell_value(cell_name, cells_to_update)))

        # Format the cells
        for cell in current_cells:
            formatted_cells[cell[0]] = {"value": cell[1]}

        formatted_cells = {
            "cells": formatted_cells
        }

        try:
            return_value = self.res_client.put(uri, formatted_cells)

        except Exception as e:
            if e.message:
                err_msg = e.message

                if u"not found" in err_msg.lower():
                    err_msg = "Data Table {0} could not be found".format(self.api_name)

                return_value = {"error": err_msg}

            else:
                raise ValueError("Could not update row in {0}. Unknown Error".format(self.api_name))

        return return_value

    def delete_row(self, row_id):

        return_value = None

        uri = "/incidents/{0}/table_data/{1}/row_data/{2}?handle_format=names".format(self.incident_id, self.api_name, row_id)

        try:
            return_value = self.res_client.delete(uri)

        except Exception as e:
            if e.message:
                return_value = {"error": e.message}

            else:
                raise ValueError("Could not delete row in {0}. Unknown Error".format(self.api_name))

        return return_value


def get_function_input(inputs, input_name, optional=False):
    """Given input_name, checks if it defined. Raises ValueError if a mandatory input is None"""
    input = inputs.get(input_name)

    if input is None and optional is False:
        err = "'{0}' is a mandatory function input".format(input_name)
        raise ValueError(err)
    else:
        return input


def validate_search_inputs(row_id, search_column, search_value):
    """Function that determines if row_id, search_column and search_value are defined correctly"""
    return_value = {
        "valid": True,
        "msg": None
    }

    a_search_var_defined = True if search_column or search_value else False

    if row_id and a_search_var_defined:
        return_value["valid"] = False
        return_value["msg"] = "Only 'row_id' or the 'search_column and search_value' pair can be defined"

    elif not row_id and not a_search_var_defined:
        return_value["valid"] = False
        return_value["msg"] = "You must define either 'row_id' or the 'search_column and search_value' pair"

    return return_value
