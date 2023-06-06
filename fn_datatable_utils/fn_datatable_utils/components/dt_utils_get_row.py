# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_datatable_utils.util.helper import RESDatatable, PACKAGE_NAME, validate_search_inputs
from resilient_lib import validate_fields

FN_NAME = "dt_utils_get_row"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'dt_utils_get_row"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.options = opts.get(PACKAGE_NAME, {})

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Function that searches for a row using a 'column name/cell value' pair or the row id and returns the cells of the row found
            -   fn_inputs.incident_id
            -   fn_inputs.dt_utils_datatable_api_name
            -   fn_inputs.dt_utils_row_id
            -   fn_inputs.dt_utils_search_column
            -   fn_inputs.dt_utils_search_value"""

        # Instansiate new SOAR API object
        res_client = self.rest_client()

        # Get the wf_instance_id of the workflow this Function was called in, if not found return a backup string
        wf_instance_id = self.get_fn_msg().get("workflow_instance", {}).get("workflow_instance_id", "no instance id found")

        yield self.status_message("Starting App Function: '{}'".format(FN_NAME))

        validate_fields(["incident_id", "dt_utils_datatable_api_name"], fn_inputs)

        dt_utils_datatable_api_name = fn_inputs.dt_utils_datatable_api_name  # text (required)
        incident_id = fn_inputs.incident_id  # number (required)
        dt_utils_row_id = fn_inputs.dt_utils_row_id if hasattr(fn_inputs, "dt_utils_row_id") else None  # number (optional)
        dt_utils_search_column = fn_inputs.dt_utils_search_column if hasattr(fn_inputs, "dt_utils_search_column") else None  # text (optional)
        dt_utils_search_value = fn_inputs.dt_utils_search_value if hasattr(fn_inputs, "dt_utils_search_value") else None  # text (optional)

        self.LOG.info("incident_id: %s", incident_id)
        self.LOG.info("dt_utils_datatable_api_name: %s",dt_utils_datatable_api_name)
        self.LOG.info("dt_utils_row_id: %s", dt_utils_row_id)
        self.LOG.info("dt_utils_search_column: %s", dt_utils_search_column)
        self.LOG.info("dt_utils_search_value: %s", dt_utils_search_value)

        # Instantiate a new RESDatatable
        datatable = RESDatatable(res_client, incident_id, dt_utils_datatable_api_name)
        # Get datatable row_id if function used on a datatable
        row_id = datatable.get_row_id_from_workflow(wf_instance_id)

        # If the dt_utils_row_id given is 0 and row_id does not exist the validate will fail
        if dt_utils_row_id == 0:
            if not row_id:
                raise ValueError("Run the workflow from a datatable to get the current row_id.")

            self.LOG.info("Using current row_id: %s", row_id)
            # dt_utils_row_id will equal the datatable row_id the function was used on
            dt_utils_row_id = row_id

        # Ensure correct search inputs are defined correctly
        valid_search_inputs = validate_search_inputs(row_id=dt_utils_row_id,
                                                        search_column=dt_utils_search_column,
                                                        search_value=dt_utils_search_value)

        if not valid_search_inputs["valid"]:
            raise ValueError(valid_search_inputs["msg"])

        # Get the data table data
        datatable.get_data()

        # Get the row
        row = datatable.get_row(
            dt_utils_row_id, dt_utils_search_column, dt_utils_search_value)

        # If no row found, create a log and set success to False
        if not row:
            yield self.status_message(u"No row found in {} for: search_column: {}, search_value: {}".format(
                datatable.api_name, dt_utils_search_column, dt_utils_search_value))
        # Else, set the row in the payload
        else:
            yield self.status_message(u"Row found in {}. row_id: {}, search_column: {}, search_value: {}".format(
                datatable.api_name, row["id"], dt_utils_search_column, dt_utils_search_value))

        yield self.status_message("Finished running App Function: '{}'".format(FN_NAME))

        # Produce a FunctionResult with the results
        yield FunctionResult({"row": row})
