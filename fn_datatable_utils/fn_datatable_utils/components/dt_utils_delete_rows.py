# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_datatable_utils.util.helper import RESDatatable, get_function_input, validate_search_inputs

class FunctionPayload(object):
    """Class that contains the payload sent back to UI and available in the post-processing script"""
    def __init__(self, inputs):
        self.success = True
        self.inputs = inputs
        self.rows_ids = None

    def as_dict(self):
        """Return this class as a Dictionary"""
        return self.__dict__


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'dt_utils_delete_rows''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_datatable_utils", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_datatable_utils", {})

    @function("dt_utils_delete_rows")
    def _dt_utils_delete_rows_function(self, event, *args, **kwargs):
        """Function: Function that deletes rows from a Data Table"""

        log = logging.getLogger(__name__)

        try:
            # Instansiate new Resilient API object
            res_client = self.rest_client()

            inputs = {
                "incident_id": get_function_input(kwargs, "incident_id"),  # number (required)
                "dt_utils_datatable_api_name": get_function_input(kwargs, "dt_utils_datatable_api_name"),  # text (required)
                "dt_utils_rows_ids": get_function_input(kwargs, "dt_utils_rows_ids", optional=True),  # text (optional)
                "dt_utils_search_column": get_function_input(kwargs, "dt_utils_search_column", optional=True),  # text (optional)
                "dt_utils_search_value": get_function_input(kwargs, "dt_utils_search_value", optional=True), # text (optional)
            }

            log.info("incident_id: {0}".format(inputs["incident_id"]))
            log.info("dt_utils_datatable_api_name: {0}".format(inputs["dt_utils_datatable_api_name"]))
            log.info("dt_utils_rows_ids: {0}".format(inputs["dt_utils_rows_ids"]))
            log.info("dt_utils_search_column: {0}".format(inputs["dt_utils_search_column"]))
            log.info("dt_utils_search_value: {0}".format(inputs["dt_utils_search_value"]))

            # Ensure correct search inputs are defined correctly
            valid_search_inputs = validate_search_inputs(rows_ids=inputs["dt_utils_rows_ids"],
                                                         search_column=inputs["dt_utils_search_column"],
                                                         search_value=inputs["dt_utils_search_value"])

            if not valid_search_inputs["valid"]:
                raise ValueError(valid_search_inputs["msg"])

            # Create payload dict with inputs
            payload = FunctionPayload(inputs)

            # Instantiate a new RESDatatable
            datatable = RESDatatable(res_client, payload.inputs["incident_id"],
                                     payload.inputs["dt_utils_datatable_api_name"])
            
            # get datatable row_id if function used on a datatable
            row_id = datatable.get_row_id_from_workflow(event.message['workflow_instance']['workflow_instance_id']) 
            row_id and log.debug("Current row_id: %s", row_id)

            # Get the data table data
            datatable.get_data()

            deleted_rows = datatable.delete_rows(payload.inputs["dt_utils_rows_ids"], 
                                                 payload.inputs["dt_utils_search_column"], 
                                                 payload.inputs["dt_utils_search_value"],
                                                 row_id)

            if not deleted_rows:
                yield StatusMessage("No row(s) found.")
                payload.success = False

            elif "error" in deleted_rows:
                yield StatusMessage("Row(s) NOT deleted. Error: {0}".format(deleted_rows["error"]))
                payload.success = False
                raise FunctionError("Failed to delete a row.")

            else:
                yield StatusMessage("Row(s) {0} in {1} deleted.".format(deleted_rows, datatable.api_name))
                payload.rows_ids = deleted_rows
                payload.success = True

            results = payload.as_dict()

            log.info("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
