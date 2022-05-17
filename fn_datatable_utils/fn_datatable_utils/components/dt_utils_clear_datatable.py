# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# # -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""AppFunction implementation"""

from logging import getLogger
from resilient_circuits import AppFunctionComponent, function, FunctionResult, handler
from resilient_lib import validate_fields, ResultPayload, IntegrationError
from fn_datatable_utils.util.helper import RESDatatable, PACKAGE_NAME

FN_NAME = "dt_utils_clear_datatable"
LOG = getLogger(__name__)

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'dt_utils_clear_datatable'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function(FN_NAME)
    def _dt_utils_clear_datatable_function(self, event, *args, **kwargs):
        """Function: Delete all of the contents of a datatable"""

        try:
            # Instansiate new SOAR API object
            res_client = self.rest_client()

            yield self.status_message("Starting App Function: '{}'".format(FN_NAME))

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

            # Delete all rows in the givem datatable
            deleted = datatable.clear_datatable()

            if deleted['success']:
                yield self.status_message("Datatable {} cleared.".format(dt_api_name))
                results = rp.done(True, None)
                results['deleted_rows'] = datatable.get_rows()
            else:
                results = rp.done(False, None)
                results['reason'] = deleted['message']
                raise IntegrationError("Datatable {} not cleared.".format(dt_api_name))

            yield self.status_message("Finished running App Function: '{}'".format(FN_NAME))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
