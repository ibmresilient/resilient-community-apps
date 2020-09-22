# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# # -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
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
    """Component that implements Resilient function 'dt_utils_delete_row"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_datatable_utils", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_datatable_utils", {})

    @function("dt_utils_delete_row")
    def _dt_utils_delete_row_function(self, event, *args, **kwargs):
        """Function: Function that deletes a row from a Data Table given the row's ID"""

        log = logging.getLogger(__name__)

        try:
            # Instansiate new Resilient API object
            res_client = self.rest_client()

            dt_utils_row_id = get_function_input(kwargs, "dt_utils_row_id", optional=True)# number (optional)
            dt_utils_datatable_api_name = get_function_input(kwargs, "dt_utils_datatable_api_name") # text (required)

            inputs = {
                "incident_id": get_function_input(kwargs, "incident_id"),  # number (required)
                "dt_utils_datatable_api_name": dt_utils_datatable_api_name,  
                "dt_utils_row_id": dt_utils_row_id  
            }

            # Create payload dict with inputs
            payload = FunctionPayload(inputs)

            yield StatusMessage("Function Inputs OK")

            # Instantiate a new RESDatatable
            datatable = RESDatatable(res_client, payload.inputs["incident_id"], dt_utils_datatable_api_name)

            # get datatable row_id if function used on a datatable
            row_id = datatable.get_row_id_from_workflow(event.message.get('workflow_instance', {}).get('workflow_instance_id'))
            row_id and log.debug("Current row_id: %s", row_id)

            if row_id == int(dt_utils_row_id):
                deleted_row = {
                    "error": "Cannot delete the invoking row. Row {0} in {1} NOT deleted".format(dt_utils_row_id,
                                                                                                 dt_utils_datatable_api_name)
                }
            else:
                deleted_row = datatable.delete_row(dt_utils_row_id)

            if "error" in deleted_row:
                yield StatusMessage("Row {0} in {1} NOT deleted.".format(dt_utils_row_id, dt_utils_datatable_api_name))
                payload.success = False
                raise ValueError(deleted_row["error"])

            yield StatusMessage("Row {0} in {1} deleted.".format(dt_utils_row_id, dt_utils_datatable_api_name))
            payload.row = deleted_row
            payload.success = True

            results = payload.as_dict()

            log.info("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
