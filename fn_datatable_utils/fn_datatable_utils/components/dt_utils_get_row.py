# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from logging import getLogger
from fn_datatable_utils.util.helper import validate_search_inputs, RESDatatable
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields

LOG = getLogger(__name__)

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
    """Component that implements SOAR function 'dt_utils_get_row"""

    def __init__(self, opts):
        """Constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_datatable_utils", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_datatable_utils", {})

    @function("dt_utils_get_row")
    def _dt_utils_get_row_function(self, event, *args, **kwargs):
        """Function: Function that searches for a row using a 'column name/cell value' pair or the row id and returns the cells of the row found"""

        try:
            # Instansiate new SOAR API object
            res_client = self.rest_client()

            # Get the wf_instance_id of the workflow this Function was called in, if not found return a backup string
            wf_instance_id = event.message.get("workflow_instance", {}).get("workflow_instance_id", "no instance id found")
            yield StatusMessage("Starting 'dt_utils_get_row' that was running in workflow '{}'".format(wf_instance_id))

            validate_fields(["incident_id", "dt_utils_datatable_api_name"], kwargs)

            inputs = {
                "incident_id": kwargs.get("incident_id"),  # number (required)
                "dt_utils_datatable_api_name": kwargs.get("dt_utils_datatable_api_name"),  # text (required)
                "dt_utils_row_id": kwargs.get("dt_utils_row_id"),  # number (optional)
                "dt_utils_search_column": kwargs.get("dt_utils_search_column"),  # text (optional)
                "dt_utils_search_value": kwargs.get("dt_utils_search_value"),  # text (optional)
            }

            # Create payload dict with inputs
            payload = FunctionPayload(inputs)

            # Instantiate a new RESDatatable
            datatable = RESDatatable(res_client, payload.inputs["incident_id"], payload.inputs["dt_utils_datatable_api_name"])
            # Get datatable row_id if function used on a datatable
            row_id = datatable.get_row_id_from_workflow(wf_instance_id)

            # If the dt_utils_row_id given is 0 and row_id does not exist the validate will fail
            if inputs["dt_utils_row_id"] == 0:
                if not row_id:
                    raise ValueError("Run the workflow from a datatable to get the current row_id.")

                LOG.info("Using current row_id: %s", row_id)
                # dt_utils_row_id will equal the datatable row_id the function was used on
                inputs["dt_utils_row_id"] = row_id

            # Ensure correct search inputs are defined correctly
            valid_search_inputs = validate_search_inputs(row_id=inputs["dt_utils_row_id"],
                                                         search_column=inputs["dt_utils_search_column"],
                                                         search_value=inputs["dt_utils_search_value"])

            if not valid_search_inputs["valid"]:
                raise ValueError(valid_search_inputs["msg"])

            yield StatusMessage("Function Inputs OK")

            # Get the data table data
            datatable.get_data()

            # Get the row
            row = datatable.get_row(payload.inputs["dt_utils_row_id"], payload.inputs["dt_utils_search_column"], payload.inputs["dt_utils_search_value"])

            # If no row found, create a log and set success to False
            if not row:
                yield StatusMessage(u"No row found in {} for: search_column: {}, search_value: {}".format(
                    datatable.api_name, payload.inputs["dt_utils_search_column"], payload.inputs["dt_utils_search_value"]))
                payload.success = False
            # Else, set the row in the payload
            else:
                yield StatusMessage(u"Row found in {}. row_id: {}, search_column: {}, search_value: {}".format(
                    datatable.api_name, row["id"], payload.inputs["dt_utils_search_column"], payload.inputs["dt_utils_search_value"]))
                payload.success = True
                payload.row = row

            results = payload.as_dict()

            LOG.info("Complete")
            yield StatusMessage("Finished 'dt_utils_get_row' that was running in workflow '{}'".format(wf_instance_id))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
