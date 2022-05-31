# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""AppFunction implementation"""

from json import loads
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_datatable_utils.util.helper import RESDatatable, PACKAGE_NAME
from resilient_lib import validate_fields

FN_NAME = "dt_utils_update_row"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'dt_utils_update_row"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.options = opts.get(PACKAGE_NAME, {})

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Function that takes a JSON String of 'column name/cell value' pairs to update a Data Table row
            -   fn_inputs.incident_id
            -   fn_inputs.dt_utils_datatable_api_name
            -   fn_inputs.dt_utils_row_id
            -   fn_inputs.dt_utils_cells_to_update"""

        try:
            # Instansiate new SOAR API object
            res_client = self.rest_client()

            # Get the wf_instance_id of the workflow this Function was called in, if not found return a backup string
            wf_instance_id = self.get_fn_msg().get("workflow_instance", {}).get("workflow_instance_id", "no instance id found")

            yield self.status_message("Starting App Function: '{}'".format(FN_NAME))

            validate_fields(["incident_id", "dt_utils_datatable_api_name", "dt_utils_row_id", "dt_utils_cells_to_update"], fn_inputs)

            dt_utils_datatable_api_name = fn_inputs.dt_utils_datatable_api_name  # text (required)
            incident_id = fn_inputs.incident_id  # number (required)
            dt_utils_row_id = fn_inputs.dt_utils_row_id  # number (required)
            dt_utils_cells_to_update = fn_inputs.dt_utils_cells_to_update  # text (required)

            self.LOG.info("incident_id: %s", incident_id)
            self.LOG.info("dt_utils_datatable_api_name: %s", dt_utils_datatable_api_name)
            self.LOG.info("dt_utils_row_id: %s", dt_utils_row_id)
            self.LOG.info("dt_utils_cells_to_update: %s", dt_utils_cells_to_update)

            try:
                # The fixes the format of lists
                dt_utils_cells_to_update = loads(dt_utils_cells_to_update.replace("\'",'"'))
            except Exception:
                raise ValueError("Failed to parse JSON string: {}".format(dt_utils_cells_to_update))

            # Instantiate a new RESDatatable
            datatable = RESDatatable(res_client, incident_id, dt_utils_datatable_api_name)

            # Get the data table data
            datatable.get_data()

            # Use the current row_id if dt_utils_row_id = 0
            if not dt_utils_row_id or not int(dt_utils_row_id):
                row_id = datatable.get_row_id_from_workflow(wf_instance_id)
                if not row_id:
                    raise ValueError("Run the workflow from a datatable to get the current row_id.")

                self.LOG.info("Using current row_id: %s", row_id)
                dt_utils_row_id = row_id

            # Update the row
            updated_row = datatable.update_row(dt_utils_row_id, dt_utils_cells_to_update)

            if "error" in updated_row:
                yield self.status_message("Row in {} NOT updated.".format(datatable.api_name))
                raise ValueError(updated_row["error"])

            else:
                yield self.status_message("Row {} in {} updated.".format(updated_row["id"], datatable.api_name))

            yield self.status_message("Finished running App Function: '{}'".format(FN_NAME))

            # Produce a FunctionResult with the results
            yield FunctionResult({"row": updated_row})
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
