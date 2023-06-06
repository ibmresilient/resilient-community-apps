# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_datatable_utils.util.helper import RESDatatable, PACKAGE_NAME, validate_search_inputs
from resilient_lib import validate_fields

FN_NAME = "dt_utils_delete_rows"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'dt_utils_delete_rows''"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.options = opts.get(PACKAGE_NAME, {})

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Function that deletes rows from a Data Table
            -   fn_inputs.incident_id
            -   fn_inputs.dt_utils_datatable_api_name
            -   fn_inputs.dt_utils_rows_ids
            -   fn_inputs.dt_utils_search_column
            -   fn_inputs.dt_utils_search_value
            -   fn_inputs.dt_utils_delete_all_rows"""

        # Instansiate new SOAR API object
        res_client = self.rest_client()

        # Get the wf_instance_id of the workflow this Function was called in, if not found return a backup string
        wf_instance_id = self.get_fn_msg().get("workflow_instance", {}).get("workflow_instance_id", "no instance id found")

        yield self.status_message("Starting App Function: '{}'".format(FN_NAME))

        validate_fields(["incident_id", "dt_utils_datatable_api_name"], fn_inputs)

        dt_utils_datatable_api_name = fn_inputs.dt_utils_datatable_api_name # text (required)
        incident_id = fn_inputs.incident_id # number (required)
        dt_utils_rows_ids = fn_inputs.dt_utils_rows_ids if hasattr(fn_inputs, "dt_utils_rows_ids") else None  # text (optional)
        dt_utils_search_column = fn_inputs.dt_utils_search_column if hasattr(fn_inputs, "dt_utils_search_column") else None  # text (optional)
        dt_utils_search_value = fn_inputs.dt_utils_search_value if hasattr(fn_inputs, "dt_utils_search_value") else None  # text (optional)
        dt_utils_delete_all_rows = bool(fn_inputs.dt_utils_delete_all_rows if hasattr(fn_inputs, "dt_utils_delete_all_rows") else False) # bool (optional)

        self.LOG.info("incident_id: %s", incident_id)
        self.LOG.info("dt_utils_datatable_api_name: %s", dt_utils_datatable_api_name)
        self.LOG.info("dt_utils_rows_ids: %s", dt_utils_rows_ids)
        self.LOG.info("dt_utils_search_column: %s", dt_utils_search_column)
        self.LOG.info(u"dt_utils_search_value: %s", dt_utils_search_value)
        self.LOG.info(u"dt_utils_delete_all_rows: %s", dt_utils_delete_all_rows)

        # Ensure correct search inputs are defined correctly
        valid_search_inputs = validate_search_inputs(rows_ids=dt_utils_rows_ids,
                                                        search_column=dt_utils_search_column,
                                                        search_value=dt_utils_search_value,
                                                        search_criteria_required=False)

        if not valid_search_inputs["valid"]:
            raise ValueError(valid_search_inputs["msg"])

        # Instantiate a new RESDatatable
        datatable = RESDatatable(res_client, incident_id, dt_utils_datatable_api_name)

        # Get datatable row_id if function used on a datatable
        row_id = datatable.get_row_id_from_workflow(wf_instance_id)
        row_id and self.LOG.debug("Current row_id: %s", row_id)

        # Get the data table data
        datatable.get_data()

        deleted_rows = datatable.delete_rows(dt_utils_rows_ids,
                                                dt_utils_search_column,
                                                dt_utils_search_value,
                                                dt_utils_delete_all_rows,
                                                row_id,
                                                wf_instance_id)

        if not deleted_rows:
            yield self.status_message("No row(s) found.")

        elif "error" in deleted_rows:
            yield self.status_message(u"Row(s) not deleted. Error: {}".format(deleted_rows.get("error")))
            raise ValueError("Failed to delete a row.")

        else:
            yield self.status_message("Row(s) {} in {} deleted.".format(deleted_rows, datatable.api_name))

        yield self.status_message("Finished running App Function: '{}'".format(FN_NAME))

        # Produce a FunctionResult with the results
        yield FunctionResult({"rows_ids": deleted_rows})
