# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.

from json import loads
from logging import getLogger
from threading import Thread
from time import sleep
from cachetools import cached, LRUCache
from resilient_lib import get_workflow_status

DATATABLE_TYPE = 8
LOG = getLogger(__name__)

class TrusteerDatatable(object):
    """ A helper class for manipulate a SOAR Data Table """
    def __init__(self, res_client, incident_id, dt_api_name):
        self.res_client = res_client
        self.incident_id = incident_id
        self.api_name = dt_api_name
        self.rows = None

    def get_data(self):
        """ Function that gets all the data and rows of a Data Table using the SOAR API """

        uri = "/incidents/{}/table_data/{}?handle_format=names".format(self.incident_id, self.api_name)

        try:
            self.rows = self.res_client.get(uri)["rows"]
        except Exception:
            raise ValueError(u"Failed to get {} Datatable".format(self.api_name))

    def get_rows(self, max_rows=0, sort_by=None, sort_direction="ASC", search_column=None, search_value=None):
        """ Searches and returns rows based on a search/sort criteria, else None """

        if self.rows:
            is_reverse = True if sort_direction == "DESC" else False

            if not search_column:
                rows_to_return = self.rows
                cells = self.rows[0]["cells"]
            else:
                rows_to_return = []
                for row in self.rows:
                    cells = row["cells"]
                    if search_column not in cells:
                        raise ValueError(u"{} is not a valid column api name for the data table: {}".format(search_column, self.api_name))
                    column = cells.get(search_column, {})
                    value = column.get("value", None)
                    if value and value == search_value:
                        rows_to_return.append(row)

            if sort_by:
                if sort_by not in cells:
                    raise ValueError(
                        u"{} is not a valid column api name for the data table: {}".format(sort_by, self.api_name))
                rows_to_return = sorted(rows_to_return, key=lambda item: item['cells'][sort_by].get('value'),
                                        reverse=is_reverse)
            if max_rows:
                rows_to_return = rows_to_return[:max_rows]

            return rows_to_return

    def get_row(self, row_id=None, search_column=None, search_value=None):
        """ Searches and returns row if row found, else None """

        # Search by row_id if defined
        if row_id:
            for row in self.rows:
                if row["id"] == row_id:
                    return row

        # Else search by column name and cell value
        else:
            for row in self.rows:
                cells = row["cells"]

                if search_column not in cells:
                    raise ValueError(u"{} is not a valid column api name in for the data table {}".format(search_column, self.api_name))
                column = cells.get(search_column)
                value = column.get("value", None)
                if value and value == search_value:
                    return row

    def update_row(self, row_id, cells_to_update):
        """ Updates the row with given updates in cells_to_update.
            Returns the updated row or dict with the entry 'error'. """

        err_msg, return_value = None, None
        current_cells, formatted_cells = [], {}

        uri = "/incidents/{}/table_data/{}/row_data/{}?handle_format=names".format(self.incident_id, self.api_name, row_id)

        def get_cell_value(cell_name, cells_to_update):
            """Function to get the new/old cell value"""
            if cell_name in cells_to_update:
                return cells_to_update[cell_name]

            if "value" not in row["cells"][cell_name]:
                return

            return row["cells"][cell_name].get("value", None)

        # Get the row we want to update
        row = self.get_row(row_id)

        if not row:
            raise ValueError("Could not find row to update for row_id: '{}'".format(row_id))

        for entry in row["cells"]:
            current_cells.append((entry, get_cell_value(entry, cells_to_update)))

        # Format the cells
        for cell in current_cells:
            formatted_cells[cell[0]] = {"value": cell[1]}

        formatted_cells = { "cells": formatted_cells }

        try:
            return_value = self.res_client.put(uri, formatted_cells)
        except Exception as err:
            if err:
                err_msg = str(err)

                if u"not found" in err_msg.lower():
                    err_msg = "Data Table {} could not be found".format(self.api_name)

                return_value = {"error": err_msg}

            else:
                raise ValueError(u"Could not update row in {}. Unknown Error".format(self.api_name))

        return return_value

