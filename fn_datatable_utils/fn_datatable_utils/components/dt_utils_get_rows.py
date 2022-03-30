# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from logging import getLogger
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_datatable_utils.util.helper import *

LOG = getLogger(__name__)

class FunctionPayload(object):
    """Class that contains the payload sent back to UI and available in the post-processing script"""
    def __init__(self, inputs):
        self.success = True
        self.inputs = inputs
        self.rows = None

    def as_dict(self):
        """Return this class as a Dictionary"""
        return self.__dict__

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'dt_utils_get_rows''"""

    def __init__(self, opts):
        """Constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_datatable_utils", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_datatable_utils", {})

    @function("dt_utils_get_rows")
    def _dt_utils_get_rows_function(self, event, *args, **kwargs):
        """Function: Function that returns rows found based on searching/sorting criteria."""

        try:
            # Instansiate new SOAR API object
            res_client = self.rest_client()

            inputs = {
                "incident_id": get_function_input(kwargs, "incident_id"),  # number (required)
                "dt_utils_datatable_api_name": get_function_input(kwargs, "dt_utils_datatable_api_name"),  # text (required)
                "dt_utils_sort_by": get_function_input(kwargs, "dt_utils_sort_by", optional=True),  # text (optional)
                "dt_utils_sort_direction": get_function_input(kwargs, "dt_utils_sort_direction", optional=True)["name"],  # select, values: "ASC", "DESC" (optional)
                "dt_utils_max_rows": get_function_input(kwargs, "dt_utils_max_rows", optional=True),  # number (optional)
                "dt_utils_search_column": get_function_input(kwargs, "dt_utils_search_column", optional=True),  # text (optional)
                "dt_utils_search_value": get_function_input(kwargs, "dt_utils_search_value", optional=True),  # text (optional)
            }

            # Ensure correct search inputs are defined correctly
            valid_search_inputs = validate_search_inputs(sort_by=inputs["dt_utils_sort_by"],
                                                         sort_direction=inputs["dt_utils_sort_direction"],
                                                         search_column=inputs["dt_utils_search_column"],
                                                         search_value=inputs["dt_utils_search_value"],
                                                         search_criteria_required=False)

            if not valid_search_inputs["valid"]:
                raise ValueError(valid_search_inputs["msg"])

            # Create payload dict with inputs
            payload = FunctionPayload(inputs)

            # Instantiate a new RESDatatable
            datatable = RESDatatable(res_client, payload.inputs["incident_id"], payload.inputs["dt_utils_datatable_api_name"])

            # Get the data table data
            datatable.get_data()

            # Get rows
            rows = datatable.get_rows(payload.inputs["dt_utils_max_rows"], payload.inputs["dt_utils_sort_by"],
                                      payload.inputs["dt_utils_sort_direction"],
                                      payload.inputs["dt_utils_search_column"], payload.inputs["dt_utils_search_value"])

            # If no rows found, create a log and set success to False
            if not rows:
                yield StatusMessage("No rows found")
                payload.success = False

            # Else, set rows in the payload
            else:
                yield StatusMessage("{0} row/s found".format(len(rows)))
                payload.success = True
                payload.rows = rows

            results = payload.as_dict()

            LOG.info("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
