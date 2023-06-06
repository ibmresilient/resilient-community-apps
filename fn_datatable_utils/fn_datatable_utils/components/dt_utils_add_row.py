# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_datatable_utils.util.helper import RESDatatable, PACKAGE_NAME
from resilient_lib import validate_fields
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

        # Instansiate new SOAR API object
        res_client = self.rest_client()

        yield self.status_message("Starting App Function: '{}'".format(FN_NAME))

        validate_fields(["incident_id", "dt_utils_datatable_api_name", "dt_utils_cells_to_update"], fn_inputs)

        self.LOG.info(str(fn_inputs))

        dt_utils_cells_to_update = fn_inputs.dt_utils_cells_to_update
        inputs_dict = fn_inputs._asdict()

        # The fixes the format of lists
        dt_utils_cells_to_update = loads(dt_utils_cells_to_update.replace("u\'",'"').replace("\'", '"'))
        inputs_dict["dt_utils_cells_to_update"] = dt_utils_cells_to_update

        row_to_add = {}
        for key in dt_utils_cells_to_update:
            value = dt_utils_cells_to_update[key]
            row_to_add[key] = {"value": value}

        # Instantiate a new RESDatatable
        datatable = RESDatatable(res_client, fn_inputs.incident_id, fn_inputs.dt_utils_datatable_api_name)

        # Get the data table data
        datatable.get_data()

        # Add row to the given datatable on SOAR
        add_row = datatable.dt_add_rows(row_to_add)

        if "error" in add_row:
            yield self.status_message("Row in {} NOT added.".format(datatable.api_name))
            raise ValueError(add_row["error"])
        else:
            yield self.status_message("Row in {} added.".format(datatable.api_name))

        yield self.status_message("Finished running App Function: '{}'".format(FN_NAME))

        # Produce a FunctionResult with the results
        yield FunctionResult({"row": dt_utils_cells_to_update})
