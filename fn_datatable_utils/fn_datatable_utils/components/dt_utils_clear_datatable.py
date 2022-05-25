# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# # -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""AppFunction implementation"""

from logging import getLogger
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, ResultPayload
from fn_datatable_utils.util.helper import RESDatatable, PACKAGE_NAME

LOG = getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements function 'dt_utils_clear_datatable'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("dt_utils_clear_datatable")
    def _dt_utils_clear_datatable_function(self, event, *args, **kwargs):
        """Function: Delete all of the contents of a datatable"""

        try:
            # Instansiate new SOAR API object
            res_client = self.rest_client()

            # Get the wf_instance_id of the workflow this Function was called in, if not found return a backup string
            wf_instance_id = event.message.get("workflow_instance", {}).get("workflow_instance_id", "no instance id found")
            yield StatusMessage("Starting 'dt_utils_clear_datatable' that was running in workflow '{}'".format(wf_instance_id))

            validate_fields(["incident_id", "dt_utils_datatable_api_name"], kwargs)

            incident_id = kwargs.get("incident_id")
            dt_utils_datatable_api_name = kwargs.get("dt_utils_datatable_api_name")

            LOG.info("incident_id: %s", incident_id)
            LOG.info("dt_utils_datatable_api_name: %s", dt_utils_datatable_api_name)

            # Create payload dict with inputs
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            # Instantiate a new RESDatatable
            datatable = RESDatatable(res_client, incident_id, dt_utils_datatable_api_name)

            # Get the data table data
            datatable.get_data()

            # Delete all rows in the given datatable on SOAR
            # deleted = datatable.clear_datatable()
            deleted_rows = datatable.delete_rows(delete_all_rows=True)

            if "error" in deleted_rows:
                yield StatusMessage("Datatable {} not cleared.".format(datatable.api_name))
                results = rp.done(False, None)
                results["reason"] = deleted_rows["error"]
            else:
                yield StatusMessage("Datatable {} cleared.".format(datatable.api_name))
                results = rp.done(True, None)
                results["deleted_rows"] = deleted_rows

            yield StatusMessage("Finished 'dt_utils_clear_datatable' that was running in workflow '{}'".format(wf_instance_id))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
