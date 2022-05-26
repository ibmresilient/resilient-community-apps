
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# # -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_datatable_utils.util.helper import RESDatatable, PACKAGE_NAME
from resilient_lib import validate_fields, ResultPayload

FN_NAME = "dt_utils_clear_datatable"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'dt_utils_clear_datatable'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.options = opts.get(PACKAGE_NAME, {})

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Delete all of the contents of a datatable
            -   fn_inputs.incident_id
            -   fn_inputs.dt_utils_datatable_api_name
        """

        try:
            # Instansiate new SOAR API object
            res_client = self.rest_client()

            yield self.status_message("Starting App Function: '{}'".format(FN_NAME))

            validate_fields(["incident_id", "dt_utils_datatable_api_name"], fn_inputs)

            inputs_dict = fn_inputs._asdict()

            self.LOG.info("incident_id: %s", fn_inputs.incident_id)
            self.LOG.info("dt_utils_datatable_api_name: %s", fn_inputs.dt_utils_datatable_api_name)

            # Create payload dict with inputs
            rp = ResultPayload(PACKAGE_NAME, **inputs_dict)

            # Instantiate a new RESDatatable
            datatable = RESDatatable(res_client, fn_inputs.incident_id, fn_inputs.dt_utils_datatable_api_name)

            # Get the data table data
            datatable.get_data()

            # Delete all rows in the given datatable on SOAR
            deleted_rows = datatable.clear_datatable()

            if "error" in deleted_rows:
                yield self.status_message("Datatable '{}' not cleared. Error: {}".format(datatable.api_name, deleted_rows.get("error")))
                raise ValueError(deleted_rows["error"])
            else:
                yield self.status_message("Datatable '{}' cleared.".format(datatable.api_name))
                results = rp.done(True, deleted_rows)

            yield self.status_message("Finished running App Function: '{}'".format(FN_NAME))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
