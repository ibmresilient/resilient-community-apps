# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_datatable_utils.util.helper import RESDatatable, PACKAGE_NAME
from resilient_lib import IntegrationError, validate_fields, ResultPayload
from json import loads

FN_NAME = "dt_utils_add_row"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'dt_utils_add_row'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.options = opts.get(PACKAGE_NAME, {})

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Add a row to a given datatable
        Inputs:
            -   fn_inputs.incident_id
            -   fn_inputs.dt_utils_cells_to_update
            -   fn_inputs.dt_utils_datatable_api_name
        """

        try:
            # Instansiate new SOAR API object
            res_client = self.rest_client()

            yield self.status_message("Starting App Function: '{}'".format(FN_NAME))

            validate_fields(["incident_id", "dt_utils_datatable_api_name", "dt_utils_cells_to_update"], fn_inputs)

            self.LOG.info(str(fn_inputs))

            dt_utils_cells_to_update = fn_inputs.dt_utils_cells_to_update

            try:
                dt_utils_cells_to_update = loads(fn_inputs.dt_utils_cells_to_update)
            except Exception as err:
                raise ValueError("Failed to parse JSON string: {}".format(fn_inputs.dt_utils_cells_to_update))

            # Create payload dict with inputs
            rp = ResultPayload(PACKAGE_NAME, **fn_inputs)

            # Instantiate a new RESDatatable
            datatable = RESDatatable(res_client, fn_inputs.incident_id, fn_inputs.dt_utils_datatable_api_name)

            # Get the data table data
            datatable.get_data()

            add_row = datatable.dt_add_rows(dt_utils_cells_to_update)

            if "error" in add_row:
                yield self.status_message("Row in {} NOT added.".format(datatable.api_name))
                results = rp.done(False, None)
                raise ValueError(add_row["error"])
            else:
                yield self.status_message("Row in {} added.".format(datatable.api_name))
                results = rp.done(True, None)
                results["row"] = dt_utils_cells_to_update

            yield self.status_message("Finished running App Function: '{}'".format(FN_NAME))

            yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
