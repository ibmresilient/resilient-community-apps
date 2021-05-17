# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
from resilient import SimpleHTTPException
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, RequestsCommon, validate_fields

PACKAGE_NAME = "fn_incident_utils"
FN_NAME = "search_incidents"

INCIDENT_QUERY_PAGED = "/incidents/query_paged"

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'search_incidents''"""

    def __init__(self, opts):
        """Constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.fn_options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.fn_options = opts.get(PACKAGE_NAME, {})

    @function(FN_NAME)
    def _search_incidents_function(self, event, *args, **kwargs):
        """Function: Search for incidents based on filter criteria. Sorting field are optional"""
        try:
            LOG = logging.getLogger(__name__)
            rc = RequestsCommon(self.opts, self.fn_options)
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting '{0}' running in workflow '{1}'".format(FN_NAME, wf_instance_id))

            # Get and validate app configs
            # app_configs = validate_fields([
            #     {"name": "api_key", "placeholder": "<your-api-key>"},
            #     {"name": "base_url", "placeholder": "<api-base_url>"}],
            #     self.fn_options)

            # Get and validate required function inputs:
            # If input is optional, remove it from list
            # Optional inputs will still be available in fn_inputs
            fn_inputs = validate_fields(
                ["inc_filter_conditions"],
                kwargs
            )

            LOG.info("'{0}' inputs: %s", fn_inputs)

            filter_conditions = json.loads(fn_inputs['inc_filter_conditions'])

            # build the filter json structure
            filter = {
                "filters": [
                    {
                        "conditions": filter_conditions
                    }
                ],
                "sorts": []
            }

            if fn_inputs['inc_sort_fields']:
                sort_fields = json.loads(fn_inputs['inc_sort_fields'])
                filter['sorts'] = sort_fields

            # Run the search and return the results
            yield StatusMessage("Searching...")
            try:
                search_results = self.rest_client().post(INCIDENT_QUERY_PAGED, filter)
                reason = None
            except SimpleHTTPException as err:
                search_results = None
                reason = "Check input fields: {}".format(str(err))
                LOG.error(reason)

            yield StatusMessage("Finished '{0}' that was running in workflow '{1}'".format(FN_NAME, wf_instance_id))

            results = rp.done(True if not reason else False, search_results, reason=reason)

            LOG.info("'%s' complete", FN_NAME)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
