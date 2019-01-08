# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_datatable_utils.util.helper import RESDatatable, get_function_input


class FunctionPayload(object):
    """Class that contains the payload sent back to UI and available in the post-processing script"""
    def __init__(self, inputs):
        self.success = True
        self.inputs = inputs
        self.row = None

    def as_dict(self):
        """Return this class as a Dictionary"""
        return self.__dict__


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'dt_utils_update_row"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_datatable_utils", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_datatable_utils", {})

    @function("dt_utils_update_row")
    def _dt_utils_update_row_function(self, event, *args, **kwargs):
        """Function: Function that takes a JSON String of 'column name/cell value' pairs to update a Data Table row"""

        log = logging.getLogger(__name__)

        try:
            # Instansiate new Resilient API object
            res_client = self.rest_client()

            inputs = {
                "incident_id": get_function_input(kwargs, "incident_id"),  # number (required)
                "dt_utils_datatable_api_name": get_function_input(kwargs, "dt_utils_datatable_api_name"),  # text (required)
                "dt_utils_row_id": get_function_input(kwargs, "dt_utils_row_id", optional=True),  # number (optional)
                "dt_utils_cells_to_update": get_function_input(kwargs, "dt_utils_cells_to_update", optional=True)  # text (optional)
            }

            try:
                inputs["dt_utils_cells_to_update"] = json.loads(inputs["dt_utils_cells_to_update"])
            except Exception:
                raise ValueError("Failed to parse JSON string: {0}".format(inputs["dt_utils_cells_to_update"]))

            # Create payload dict with inputs
            payload = FunctionPayload(inputs)

            yield StatusMessage("Function Inputs OK")

            # Instantiate a new RESDatatable
            datatable = RESDatatable(res_client, payload.inputs["incident_id"], payload.inputs["dt_utils_datatable_api_name"])

            # Get the data table data
            datatable.get_data()

            # Update the row
            updated_row = datatable.update_row(payload.inputs["dt_utils_row_id"], payload.inputs["dt_utils_cells_to_update"])

            if "error" in updated_row:
                yield StatusMessage("Row in {1} NOT updated.".format(datatable.api_name))
                payload.success = False
                raise ValueError(updated_row["error"])

            else:
                yield StatusMessage("Row {0} in {1} updated.".format(updated_row["id"], datatable.api_name))
                payload.row = updated_row
                payload.success = True

            results = payload.as_dict()

            log.info("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
