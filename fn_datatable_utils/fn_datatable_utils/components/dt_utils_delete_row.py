# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# # -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_datatable_utils.util.helper import RESDatatable, PACKAGE_NAME
from resilient_lib import validate_fields, ResultPayload

FN_NAME = "dt_utils_delete_row"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'dt_utils_delete_row"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.options = opts.get(PACKAGE_NAME, {})

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Function that deletes a row from a Data Table given the row's ID
            -   fn_inputs.incident_id
            -   fn_inputs.dt_utils_datatable_api_name
            -   fn_inputs.dt_utils_row_id"""

        try:
            # Instansiate new SOAR API object
            res_client = self.rest_client()

            # Get the wf_instance_id of the workflow this Function was called in, if not found return a backup string
            wf_instance_id = self.get_fn_msg().get("workflow_instance", {}).get("workflow_instance_id", "no instance id found")

            yield self.status_message("Starting App Function: '{}'".format(FN_NAME))

            # Validate required fields
            validate_fields(["dt_utils_datatable_api_name", "incident_id"], fn_inputs)

            dt_utils_row_id = fn_inputs.dt_utils_row_id if hasattr(fn_inputs, "dt_utils_row_id") else None # number (optional)
            dt_utils_datatable_api_name = fn_inputs.dt_utils_datatable_api_name # text (required)
            incident_id = fn_inputs.incident_id # number (required)

            self.LOG.info("incident_id: %s", incident_id)
            self.LOG.info("dt_utils_datatable_api_name: %s", dt_utils_datatable_api_name)
            self.LOG.info("dt_utils_row_id: %s", dt_utils_row_id)

            # Create payload dict with inputs
            inputs_dict = fn_inputs._asdict()
            rp = ResultPayload(PACKAGE_NAME, **inputs_dict)

            # Instantiate a new RESDatatable
            datatable = RESDatatable(res_client, incident_id, dt_utils_datatable_api_name)

            # Get datatable row_id if function used on a datatable
            row_id = datatable.get_row_id_from_workflow(wf_instance_id)
            row_id and self.LOG.debug("Current row_id: %s", row_id)

            # If dt_utils_row_id == 0, use row_id
            if not dt_utils_row_id or not int(dt_utils_row_id):
                if not row_id:
                    raise ValueError("Run the workflow from a datatable to get the current row_id.")

                self.LOG.info("Using current row_id: %s", row_id)
                dt_utils_row_id = row_id

            if row_id == int(dt_utils_row_id):
                yield self.status_message("Queuing row {} for delete".format(dt_utils_row_id))
                deleted_row = datatable.queue_delete(wf_instance_id, dt_utils_row_id)
            else:
                deleted_row = datatable.delete_row(dt_utils_row_id)

            if "error" in deleted_row:
                yield self.status_message(u"Row {} in {} not deleted.".format(dt_utils_row_id, dt_utils_datatable_api_name))
                results = rp.done(False, None)
                raise ValueError(deleted_row["error"])

            yield self.status_message("Row {} in {} deleted.".format(dt_utils_row_id, dt_utils_datatable_api_name))
            results = rp.done(True, None)
            results['row'] = deleted_row

            yield self.status_message("Finished running App Function: '{}'".format(FN_NAME))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
