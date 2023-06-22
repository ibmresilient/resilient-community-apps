# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pylint: disable=R0913,C0103,E1101,W0707,W0703
""" DataTable.py exposes a helper module for GET, UPDATE and DELETE
    Functions for a SOAR / CP4S Data Table """

from logging import getLogger

# Constants
DATATABLE_TYPE = 8
LOG = getLogger(__name__)

class Datatable(object):
    """ A helper class which provides a facade to interface with a SOAR / CP4S Data Table. """

    def __init__(self, res_client, incident_id, dt_api_name):
        self.res_client = res_client
        self.incident_id = incident_id
        self.api_name = dt_api_name
        self.data = None
        self.rows = None

    def get_data(self):
        """get_data Function that gets all the data and rows of a Data Table
            using the SOAR API

        :raises ValueError: If the datatable api call fails or the result contains no rows, raise an Exception
        """

        uri = "/incidents/{0}/table_data/{1}?handle_format=names".format(
            self.incident_id, self.api_name)

        try:
            self.data = self.res_client.get(uri)
            self.rows = self.data["rows"]
        except Exception:
            raise ValueError(
                "Failed to get {0} Datatable".format(self.api_name))

    def get_rows(self, max_rows=0, sort_by=None, sort_direction="ASC", search_column=None, search_value=None):
        """get_rows Searches and returns rows based on a search/sort criteria, else None

        :param max_rows: The most amount of rows to return, defaults to 0
        :type max_rows: int, optional
        :param sort_by: Which column should be used for sorting, defaults to None
        :type sort_by: str, optional
        :param sort_direction: Which direction sorting should be applied, defaults to "ASC"
        :type sort_direction: str, optional
        :param search_column: The name of a specific datatable column to search, defaults to None
        :type search_column: str, optional
        :param search_value: The value to be searched, defaults to None
        :type search_value: str, optional
        :raises ValueError: If a search column is provided but that column is not found in the datatable, a ValueError is raised
        :raises ValueError: If the sort_by column is provided but that column is not found in the datatable, a ValueError is raised
        :return: The rows of the datatable
        :rtype: dict
        """
        if self.rows:
            rows_to_return = []
            is_reverse = bool(sort_direction == "DESC")

            for row in self.rows:
                if search_column not in row.get("cells"):
                    raise ValueError(f"{search_column} is not a valid column api name for the data table: {self.api_name}")
                column = row.get("cells", {}).get(search_column)
                value = column.get("value", None)
                if value and value == search_value:
                    rows_to_return.append(row)

                if sort_by:
                    if sort_by not in row.get("cells"):
                        raise ValueError(f"{sort_by} is not a valid column api name for the data table: {self.api_name}")
                    rows_to_return = sorted(rows_to_return, key=lambda item: item.get('cells', {}).get(sort_by, {}).get('value'),
                                            reverse=is_reverse)
            if max_rows != 0:
                rows_to_return = rows_to_return[:max_rows]

            return rows_to_return

    def get_row(self, row_id=None, search_column=None, search_value=None):
        """get_row Searches and returns row if row found, else None

        :param row_id: ID number of the row to get, defaults to None
        :type row_id: int, optional
        :param search_column: The name of a specific datatable column to search, defaults to None
        :type search_column: str, optional
        :param search_value: The value to be searched, defaults to None
        :type search_value: str, optional
        :raises ValueError: If a search_column is provided but not found in the cells of the gathered row, a ValueError is raised
        :return: The row
        :rtype: dict
        """

        # Search by row_id if defined
        if row_id:
            for row in self.rows:
                if row.get("id") == row_id:
                    return row

        # Else search by column name and cell value
        else:
            for row in self.rows:
                cells = row.get("cells", {})

                if search_column not in cells:
                    raise ValueError(f"{search_column} is not a valid column api name in for the data table {self.api_name}")
                column = cells.get(search_column)
                value = column.get("value", None)
                if value and value == search_value:
                    return row

    def update_row(self, row_id, cells_to_update):
        """update_row Updates the row with given updates in cells_to_update.
            Returns the updated row or dict with the entry 'error'.

        :param row_id: The ID of the row to updated
        :type row_id: int
        :param cells_to_update: Which columns of the row to be updates as well as the new values
        :type cells_to_update: dict
        :raises ValueError: After attempting to get the row, a value error is raised if no row is found
        :return: The result from the API call to update the datatable row
        :rtype: dict
        """

        err_msg, return_value = None, None
        current_cells, formatted_cells = [], {}

        uri = f"/incidents/{self.incident_id}/table_data/{self.api_name}/row_data/{row_id}?handle_format=names"

        def get_cell_value(cell_name, cells_to_update):
            """Function to get the new/old cell value"""
            if cell_name in cells_to_update:
                return cells_to_update.get(cell_name)

            if "value" in row.get("cells", {}).get(cell_name):
                return row.get("cells", {}).get(cell_name, {}).get("value", None)

        # Get the row we want to update
        row = self.get_row(row_id)

        if row == None:
            raise ValueError(f"Could not find row to update for row_id: '{row_id}'")

        for entry in row.get("cells"):
            cell_name = entry
            current_cells.append((cell_name, get_cell_value(cell_name, cells_to_update)))

        # Format the cells
        for cell in current_cells:
            formatted_cells[cell[0]] = {"value": cell[1]}

        formatted_cells = {"cells": formatted_cells}

        try:
            return_value = self.res_client.put(uri, formatted_cells)

        except Exception as err:
            if err.message:
                err_msg = err.message

                if "not found" in err_msg.lower():
                    err_msg = f"Data Table {self.api_name} could not be found"

                return_value = {"error": err_msg}

            else:
                raise ValueError(f"Could not update row in {self.api_name}. Unknown Error")

        return return_value
