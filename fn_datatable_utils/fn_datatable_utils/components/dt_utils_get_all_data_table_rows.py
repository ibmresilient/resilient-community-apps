# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# # -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""AppFunction implementation"""

from logging import getLogger
from json import loads
from resilient_circuits import AppFunctionComponent, function, FunctionResult, handler
from resilient_lib import validate_fields, ResultPayload
from fn_datatable_utils.util.helper import RESDatatable, PACKAGE_NAME

FN_NAME = "dt_utils_get_all_data_table_rows"
LOG = getLogger(__name__)

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'dt_utils_get_all_data_table_rows'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.options = opts.get("fn_datatable_utils", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_datatable_utils", {})

    @function(FN_NAME)
    def _dt_utils_get_all_data_table_rows_function(self, event, *args, **kwargs):
        """Function: Return all of the rows from a data table in SOAR"""

        try:
            # Instansiate new SOAR API object
            res_client = self.rest_client()

            yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

            validate_fields(['incident_id', 'dt_utils_datatable_api_name'], kwargs)

            incident_id = kwargs.get("incident_id") # text (required)
            dt_api_name = kwargs.get("dt_utils_datatable_api_name") # text (required)

            LOG.info("incident_id: %s", incident_id)
            LOG.info("dt_utils_datatable_api_name: %s", dt_api_name)

            # Create payload dict with inputs
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            # Instantiate a new RESDatatable
            datatable = RESDatatable(res_client, incident_id, dt_api_name)

            # Get the data table data
            datatable.get_data()

            rows = datatable.get_rows()

            # If no rows found, create a log and set success to False
            if not rows:
                yield self.status_message("No rows found")
                results = rp.done(False, None)

            # Else, set rows in the payload
            else:
                yield self.status_message("{0} row/s found".format(len(rows)))
                results = rp.done(True, None)
                results["rows"] = rows

            yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

            yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason="Bad call")
