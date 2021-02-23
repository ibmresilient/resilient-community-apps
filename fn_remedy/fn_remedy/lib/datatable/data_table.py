# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# pylint: disable=R0913,C0103,E1101,W0707,W0703
""" DataTable.py exposes a helper module for GET, UPDATE and DELETE
    Functions for a Resilient / CP4S Data Table """

import json
import logging
import threading
import time
from cachetools import cached, LRUCache
from resilient_lib import get_workflow_status

# Constants
DATATABLE_TYPE = 8
LOG = logging.getLogger(__name__)


class Datatable(object):
    """ A helper class which provides a facade to interface with a Resilient / CP4S Data Table
    Example:
    .. code-block:: python

        dt = Datatable(mocked_res_client, <incident_id>, <datatable_api_name>)
        dt.get_data()
        print(dt.rows)
        ...

    .. code-block:: python

        dt = Datatable(mocked_res_client, <incident_id>, <datatable_api_name>)
        dt.get_data()
        dt.get_row(<row_id>, <column_to_search>, <value_to_search_in_column>)
        ..."""

    def __init__(self, res_client, incident_id, dt_api_name):
        self.res_client = res_client
        self.incident_id = incident_id
        self.api_name = dt_api_name
        self.data = None
        self.rows = None

    def get_data(self):
        """get_data Function that gets all the data and rows of a Data Table
            using the Resilient API

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
        :param search_value: The value to be searched , defaults to None
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
                if search_column not in row["cells"]:
                    raise ValueError("{0} is not a valid column api name for the data table: {1}".format(
                        search_column, self.api_name))
                column = row["cells"].get(search_column)
                value = column.get("value", None)
                if value is not None:
                    if value == search_value:
                        rows_to_return.append(row)

                if sort_by:
                    if sort_by not in row["cells"]:
                        raise ValueError(
                            "{0} is not a valid column api name for the data table: {1}".format(sort_by, self.api_name))
                    rows_to_return = sorted(rows_to_return, key=lambda item: item['cells'][sort_by].get('value'),
                                            reverse=is_reverse)
            if max_rows != 0:
                rows_to_return = rows_to_return[:max_rows]

            return rows_to_return

        return None

    def get_row(self, row_id=None, search_column=None, search_value=None):
        """get_row Searches and returns row if row found, else None


        :param row_id: ID number of the row to get, defaults to None
        :type row_id: int, optional
        :param search_column: The name of a specific datatable column to search, defaults to None
        :type search_column: str, optional
        :param search_value: The value to be searched , defaults to None
        :type search_value: str, optional
        :raises ValueError: If a search_column is provided but not found in the cells of the gathered row, a ValueError is raised
        :return: The row
        :rtype: dict
        """

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
                    raise ValueError("{0} is not a valid column api name in for the data table {1}".format(
                        search_column, self.api_name))
                column = cells.get(search_column)
                value = column.get("value", None)
                if value is not None:
                    if value == search_value:
                        return row

        return None

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

        uri = "/incidents/{0}/table_data/{1}/row_data/{2}?handle_format=names".format(
            self.incident_id, self.api_name, row_id)

        def get_cell_value(cell_name, cells_to_update):
            """Function to get the new/old cell value"""
            if cell_name in cells_to_update:
                return cells_to_update[cell_name]

            if "value" not in row["cells"][cell_name]:
                return None

            return row["cells"][cell_name].get("value", None)

        # Get the row we want to update
        row = self.get_row(row_id)

        if row is None:
            raise ValueError(
                "Could not find row to update for row_id: '{0}'".format(row_id))

        for entry in row["cells"]:
            cell_name = entry
            current_cells.append(
                (cell_name, get_cell_value(cell_name, cells_to_update)))

        # Format the cells
        for cell in current_cells:
            formatted_cells[cell[0]] = {"value": cell[1]}

        formatted_cells = {
            "cells": formatted_cells
        }

        try:
            return_value = self.res_client.put(uri, formatted_cells)

        except Exception as err:
            if err.message:
                err_msg = err.message

                if u"not found" in err_msg.lower():
                    err_msg = "Data Table {0} could not be found".format(
                        self.api_name)

                return_value = {"error": err_msg}

            else:
                raise ValueError(
                    "Could not update row in {0}. Unknown Error".format(self.api_name))

        return return_value

    def delete_row(self, row_id):
        """delete_row Deletes the row.
            Returns the response from Resilient API
            or dict with the entry 'error'.

        :param row_id: The ID of the row to delete
        :type row_id: int
        :raises ValueError: If the row is not found and the error is unknown a ValueError is thrown instead
        :return: The result of the deletion
        """

        return_value = None

        uri = "/incidents/{0}/table_data/{1}/row_data/{2}?handle_format=names".format(
            self.incident_id, self.api_name, row_id)

        try:
            return_value = self.res_client.delete(uri)

        except Exception as err:
            if err:
                return_value = {"error": err}

            else:
                raise ValueError(
                    "Could not delete row in {0}. Unknown Error: {1}".format(self.api_name, err))

        return return_value

    def delete_rows(self, rows_ids=None, search_column=None, search_value=None,
                    row_id=None, workflow_id=None):
        """delete_rows Deletes rows.
            Returns the response from Resilient API
            or dict with the entry 'error'.

        :param rows_ids: ID numbers of the rows to be deleted, defaults to None
        :type rows_ids: list, optional
        :param search_column: The name of a specific datatable column to search, defaults to None
        :type search_column: str, optional
        :param search_value: The value to be searched , defaults to None
        :type search_value: str, optional
        :param row_id: The ID of a given row to delete, defaults to None
        :type row_id: int, optional
        :param workflow_id: The ID of the current workflow, deletions are attempt using a safe threading system which monitors and waits for the workflow to complete, defaults to None
        :type workflow_id: int, optional
        :raises ValueError: If a search_column is provided but not found in the cells of the gathered row, a ValueError is raised
        """

        return_value = None
        rows_ids_list = []
        queued_row_id = None

        # Search by rows_ids if defined
        if rows_ids:
            # Convert input str to a list of rows ids
            rows_ids_input = json.loads(rows_ids)

            # for each row returned from the datatable, compare row_ids with our list to delete
            for row in self.rows:
                if row["id"] in rows_ids_input:
                    if row["id"] == row_id:
                        LOG.warning(
                            "Queuing delete of current row: %s", row_id)
                        self.queue_delete(workflow_id, row_id)
                        queued_row_id = row_id
                    else:
                        rows_ids_list.append(row["id"])

        # Else search by column name and cell value
        elif search_column and search_value:
            for row in self.rows:
                cells = row["cells"]
                if search_column not in cells:
                    raise ValueError("{0} is not a valid column api name in for the data table {1}".format(
                        search_column, self.api_name))
                if "value" in cells[search_column] and cells[search_column]["value"] == search_value:
                    if row["id"] == row_id:
                        LOG.info("Queuing delete of current row: %s", row_id)
                        self.queue_delete(workflow_id, row_id)
                        queued_row_id = row_id
                    else:
                        rows_ids_list.append(row["id"])

        return_value = list(rows_ids_list)
        if rows_ids_list:
            for row_id in rows_ids_list:
                deleted_row = self.delete_row(row_id)
                if "error" in deleted_row:
                    LOG.error("Unable to remove row_id: %s. Error: %s",
                              row_id, deleted_row['error'])
                    return_value.remove(row_id)

        if queued_row_id:
            return_value.append(queued_row_id)

        return return_value

    def get_row_id_from_workflow(self, workflow_instance_id):
        """get_row_id_from_workflow Get row information from the workflow instance

        :param workflow_instance_id:
        :type workflow_instance_id: int
        :return: row_id or None if error or datatype is not a datatable
        :rtype: int
        """
        uri = "/workflow_instances/{}".format(workflow_instance_id)
        try:
            response = self.res_client.get(uri)

            # determine if we have a custom object type and it's a datatable
            if response['object']['type_id'] >= 1000:
                # confirm this is a data table
                type_info = self.get_object_type(response['object']['type_id'])
                if type_info['type_id'] == DATATABLE_TYPE:
                    return response['object']['object_id']

        except Exception as err:
            LOG.error("Error with url: %s %s", uri, str(err))

        return None

    def get_dt_headers(self):
        """get_dt_headers Function that gets all the data and rows of a Data Table
            using the Resilient API

        :raises ValueError: Any exception that is raised during the API call raises a ValueError
        :return: The fields for a datatable
        :rtype: list
        """
        uri = "/types/{0}?handle_format=names".format(self.api_name)

        try:
            self.data = self.res_client.get(uri)
            return self.data["fields"]
        except Exception:
            raise ValueError(
                "Failed to get {0} Datatable".format(self.api_name))

    def dt_add_rows(self, rows):
        """ Adds rows to datatable
            from uploaded CSV data """

        uri = "/incidents/{0}/table_data/{1}/row_data?handle_format=names".format(
            self.incident_id, self.api_name)

        formatted_cells = {
            "cells": rows
        }
        try:
            return_value = self.res_client.post(uri, formatted_cells)
        except Exception as err:
            return_value = {"error": err}

        return return_value

    @cached(cache=LRUCache(maxsize=100))
    def get_object_type(self, obj_id):
        """get_object_type Get information about a Resilient object. This call is cached for multiple calls

        :param obj_id: The ID of the object type to get
        :type obj_id: int
        :return: The objects types information
        :rtype: json
        """

        uri = "/types/{}".format(obj_id)

        return self.res_client.get(uri)

    def queue_delete(self, workflow_id, row_id):
        """queue_delete queue the delete action for when the workflow completes

        :param workflow_id: workflow id to ensure the workflow is complete before performing a deletion
        :type workflow_id: int
        :param row_id: the row to queue for deletion
        :type row_id: int
        :return: A json structure with the response of the delete action
        :rtype: dict
        """

        t = threading.Thread(target=threaded_delete, args=[
                             self, workflow_id, row_id])
        t.daemon = True
        t.start()

        # return a json result similar to the delete API json
        return {
            'success': True,
            'title': None,
            'message': None,
            'hints': [row_id]
        }


def get_function_input(inputs, input_name, optional=False):
    """get_function_input Given input_name, checks if it defined. Raises ValueError if a mandatory input is None

    :param inputs: [description]
    :type inputs: [type]
    :param input_name: [description]
    :type input_name: [type]
    :param optional: [description], defaults to False
    :type optional: bool, optional
    :raises ValueError: [description]
    :return: [description]
    :rtype: [type]
    """
    the_input = inputs.get(input_name)

    if the_input is None and optional is False:
        err = "'{0}' is a mandatory function input".format(input_name)
        raise ValueError(err)
    
    return the_input


def validate_search_inputs(**options):
    """validate_search_inputs Function that determines if row_id, search_column and search_value are defined correctly

    :return: [description]
    :rtype: [type]
    """
    return_value = {
        "valid": True,
        "msg": None
    }

    is_row_id = bool("row_id" in options)
    is_rows_ids = bool("row_ids" in options)
    is_search_column = bool("search_column" in options)
    is_search_value = bool("search_value" in options)
    is_sort_by_var_defined = bool("sort_by" in options and options["sort_by"])
    is_reverse = bool("sort_direction" in options and options[
        "sort_direction"] == "DESC")
    a_search_var_defined = bool((is_search_column and options["search_column"]) and (
        is_search_value and options["search_value"]))

    if is_row_id:
        if options["row_id"] and a_search_var_defined:
            return_value["valid"] = False
            return_value["msg"] = "Only 'row_id' or the 'search_column and search_value' pair can be defined"
        elif not options["row_id"] and not a_search_var_defined:
            return_value["valid"] = False
            return_value["msg"] = "You must define either 'row_id' or the 'search_column and search_value' pair"
    elif not is_row_id and is_rows_ids:
        if options["rows_ids"] and a_search_var_defined:
            return_value["valid"] = False
            return_value["msg"] = "Only 'rows_ids' or the 'search_column and search_value' pair can be defined"
        elif not options["rows_ids"] and not a_search_var_defined:
            return_value["valid"] = False
            return_value["msg"] = "You must define either 'rows_ids' or the 'search_column and search_value' pair"
    elif not is_row_id and not is_rows_ids:
        if not a_search_var_defined:
            return_value["valid"] = False
            return_value["msg"] = "You must define the 'search_column and search_value' pair"
        if is_reverse and not is_sort_by_var_defined:
            return_value["valid"] = False
            return_value["msg"] = "You must define 'sort_direction and sort_by' pair"

    return return_value


def threaded_delete(datatable, workflow_id, row_id):
    """threaded_delete wait for the workflow to complete before performing the delete row action

    :param datatable: The datatable helper object
    :type datatable: object
    :param workflow_id: workflow id to ensure it's complete before deleting row
    :type workflow_id: int
    :param row_id: row to queue for delete
    :type row_id: int
    """
    MAX_SLEEP_UNTIL_WF_COMPLETES = 60  # no sleep time should exceed 60s
    MAX_LOOP = 60  # roughly an hour of waiting
    sleep_time = 10
    # check that the workflow is still active, sleep if still active
    wf = get_workflow_status(datatable.res_client, workflow_id)
    ndx = 0
    while wf.status == 'running' and ndx < MAX_LOOP:
        time.sleep(sleep_time)
        sleep_time += sleep_time
        sleep_time = min(sleep_time, MAX_SLEEP_UNTIL_WF_COMPLETES)
        wf = get_workflow_status(datatable.res_client, workflow_id)
        ndx += 1

    if wf.status != 'running':
        # perform the delete rows()
        result = datatable.delete_row(row_id)
        if 'error' in result:
            LOG.error("Queued delete failed for row_id: %s. Error: %s",
                      row_id, result['error'])
        else:
            LOG.debug("Queued delete succeeded for row_id: %s", row_id)
    else:
        LOG.error("Unable to delete row_id: %s with workflow %s state: %s",
                  row_id, workflow_id, wf.status)
