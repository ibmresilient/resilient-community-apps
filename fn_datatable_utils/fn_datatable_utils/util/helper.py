# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
""" This is a helper module for GET, UPDATE and DELETE
    Functions for a Resilient Data Table """

import json
import logging
import threading
import time
from cachetools import cached, LRUCache
from resilient_lib import get_workflow_status

DATATABLE_TYPE = 8
LOG = logging.getLogger(__name__)

class RESDatatable(object):
    """ A helper class for manipulate a Resilient Data Table"""
    def __init__(self, res_client, incident_id, dt_api_name):
        self.res_client = res_client
        self.incident_id = incident_id
        self.api_name = dt_api_name
        self.data = None
        self.rows = None

    def get_data(self):
        """ Function that gets all the data and rows of a Data Table
            using the Resilient API """

        uri = "/incidents/{0}/table_data/{1}?handle_format=names".format(self.incident_id, self.api_name)

        try:
            self.data = self.res_client.get(uri)
            self.rows = self.data["rows"]
        except Exception:
            raise ValueError("Failed to get {0} Datatable".format(self.api_name))

    def get_rows(self, max_rows=0, sort_by=None, sort_direction="ASC", search_column=None, search_value=None):
        """ Searches and returns rows based on a search/sort criteria, else None """

        if self.rows:
            rows_to_return = []
            is_reverse = True if sort_direction == "DESC" else False

            for row in self.rows:
                cells = row["cells"]
                if search_column not in cells:
                    raise ValueError("{0} is not a valid column api name for the data table: {1}".format(search_column, self.api_name))
                column = cells.get(search_column)
                value = column.get("value", None)
                if value is not None:
                    if value == search_value:
                        rows_to_return.append(row)

            if sort_by:
                if sort_by not in cells:
                    raise ValueError(
                        "{0} is not a valid column api name for the data table: {1}".format(sort_by, self.api_name))
                rows_to_return = sorted(rows_to_return, key=lambda item: item['cells'][sort_by]['value'],
                                        reverse=is_reverse)
            if max_rows != 0:
                rows_to_return = rows_to_return[:max_rows]

            return rows_to_return
        else:
            return None

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
                    raise ValueError("{0} is not a valid column api name in for the data table {1}".format(search_column, self.api_name))
                column = cells.get(search_column)
                value = column.get("value", None)
                if value is not None:
                    if value == search_value:
                        return row

        return None

    def update_row(self, row_id, cells_to_update):
        """ Updates the row with given updates in cells_to_update.
            Returns the updated row or dict with the entry 'error'. """

        err_msg, return_value = None, None
        current_cells, formatted_cells = [], {}

        uri = "/incidents/{0}/table_data/{1}/row_data/{2}?handle_format=names".format(self.incident_id, self.api_name, row_id)

        def get_cell_value(cell_name, cells_to_update):
            """Function to get the new/old cell value"""
            if cell_name in cells_to_update:
                return cells_to_update[cell_name]

            if "value" not in row["cells"][cell_name]:
                return None

            return row["cells"][cell_name]["value"]

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

        except Exception as err:
            if err.message:
                err_msg = err.message

                if u"not found" in err_msg.lower():
                    err_msg = "Data Table {0} could not be found".format(self.api_name)

                return_value = {"error": err_msg}

            else:
                raise ValueError("Could not update row in {0}. Unknown Error".format(self.api_name))

        return return_value

    def delete_row(self, row_id):
        """ Deletes the row.
            Returns the response from Resilient API
            or dict with the entry 'error'. """

        return_value = None

        uri = "/incidents/{0}/table_data/{1}/row_data/{2}?handle_format=names".format(self.incident_id, self.api_name, row_id)

        try:
            return_value = self.res_client.delete(uri)

        except Exception as err:
            if err:
                return_value = {"error": err}

            else:
                raise ValueError("Could not delete row in {0}. Unknown Error: {1}".format(self.api_name, err))

        return return_value

    def delete_rows(self, rows_ids=None, search_column=None, search_value=None, 
                    row_id=None, workflow_id=None):
        """ Deletes rows.
            Returns the response from Resilient API
            or dict with the entry 'error'. """

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
                        LOG.warning("Queuing delete of current row: %s", row_id)
                        self.queue_delete(workflow_id, row_id)
                        queued_row_id = row_id
                    else:
                        rows_ids_list.append(row["id"])

        # Else search by column name and cell value
        elif search_column and search_value:
            for row in self.rows:
                cells = row["cells"]
                if search_column not in cells:
                    raise ValueError("{0} is not a valid column api name in for the data table {1}".format(search_column, self.api_name))
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
                    LOG.error("Unable to remove row_id: %s. Error: %s", row_id, deleted_row['error'])
                    return_value.remove(row_id)                

        if queued_row_id:
            return_value.append(queued_row_id)

        return return_value
    
    def get_row_id_from_workflow(self, workflow_instance_id):
        """
        Get row information from the workflow instance

        Args:
            workflow_instance_id (int):

        Returns:
            int: row_id or None if error or datatype is not a datatable
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
        """ Function that gets all the data and rows of a Data Table
            using the Resilient API """
        uri = "/types/{0}?handle_format=names".format(self.api_name)

        try:
            self.data = self.res_client.get(uri)
            return self.data["fields"]
        except Exception:
            raise ValueError("Failed to get {0} Datatable".format(self.api_name))

    def dt_add_rows(self, rows):
        """ Adds rows to datatable
            from uploaded CSV data """

        uri = "/incidents/{0}/table_data/{1}/row_data?handle_format=names".format(self.incident_id, self.api_name)

        formatted_cells = {
            "cells": rows
        }
        try:
            return_value = self.res_client.post(uri, formatted_cells)
        except Exception as err:
            return_value = {"error": err}

        return return_value

    @cached(cache=LRUCache(maxsize=100))
    def get_object_type(self, id):
        """
        Get information about a Resilient object. This call is cached for multiple calls

        Args:
            id (int): object_id

        Returns:
            json: returned object information
        """
        uri = "/types/{}".format(id)

        return self.res_client.get(uri)

    def queue_delete(self, workflow_id, row_id):
        """
        queue the delete action for when the workflow completes

        Args:
            workflow_id ([int]): workflow id to ensure it's complete before deleting row
            row_id ([int]): row to queue for delete

        Returns:
            [json]: similar API json for a delete action
        """
        t = threading.Thread(target=threaded_delete, args=[self, workflow_id, row_id])
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
    """Given input_name, checks if it defined. Raises ValueError if a mandatory input is None"""
    the_input = inputs.get(input_name)

    if the_input is None and optional is False:
        err = "'{0}' is a mandatory function input".format(input_name)
        raise ValueError(err)
    else:
        return the_input


def validate_search_inputs(**options):
    """Function that determines if row_id, search_column and search_value are defined correctly"""
    return_value = {
        "valid": True,
        "msg": None
    }

    is_row_id = True if "row_id" in options else False
    is_rows_ids = True if "rows_ids" in options else False
    is_search_column = True if "search_column" in options else False
    is_search_value = True if "search_value" in options else False
    is_sort_by_var_defined = True if "sort_by" in options and options["sort_by"] else False
    is_reverse = True if "sort_direction" in options and options["sort_direction"] == "DESC" else False
    a_search_var_defined = True if (is_search_column and options["search_column"]) and (is_search_value and options["search_value"]) else False

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
    """
    wait for the workflow to complete before performing the delete row action

    Args:
        rest_client ([object]): resilient helper object
        workflow_id ([int]): workflow id to ensure it's complete before deleting row
        datatable ([object]): helper object
        row_id ([int]): row to queue for delete

    Returns:
        None
    """
    MAX_SLEEP_UNTIL_WF_COMPLETES = 60
    MAX_LOOP = 60
    sleep_time = 10
    # check that the workflow is still active, sleep if still active
    wf = get_workflow_status(datatable.res_client, workflow_id)
    ndx = 0
    while wf.status == 'running' and ndx < MAX_LOOP:
        time.sleep(sleep_time)
        sleep_time += sleep_time
        sleep_time = min(sleep_time, MAX_SLEEP_UNTIL_WF_COMPLETES)
        wf = get_workflow_status(datatable.res_client, workflow_id)

    if wf.status != 'running':
        # perform the delete rows()
        result = datatable.delete_row(row_id)
        if 'error' in result:
            LOG.error("Queued delete failed for row_id: %s. Error: %s", row_id, result['error'])
        else:
            LOG.debug("Queued delete succeeded for row_id: %s", row_id)
