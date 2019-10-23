# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_resilient_ml.lib import util_functions

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'resilient_nlp_search"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_resilient_ml", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_resilient_ml", {})

    @function("resilient_nlp_search")
    def _resilient_nlp_search_function(self, event, *args, **kwargs):
        """Function: None"""
        try:
            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            # Get the function parameters:
            search_incident_id = kwargs.get("search_incident_id")  # number
            number_incidents = kwargs.get("number_incidents")  # number
            res_client = self.rest_client()

            log = logging.getLogger(__name__)
            log.info("search_incident_id: %s", search_incident_id)
            log.info("number_incidents: %s", number_incidents)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")

            inc_hrefs = util_functions.get_indent_href(inc_id=search_incident_id,
                                                       org_id=res_client.org_id,
                                                       base_url=res_client.base_url,
                                                       num_return=number_incidents)

            yield StatusMessage("done...")


            results = {
                "incidents":inc_hrefs
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()