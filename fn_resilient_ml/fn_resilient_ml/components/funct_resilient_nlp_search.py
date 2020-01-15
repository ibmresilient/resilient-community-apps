# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_resilient_ml.lib import util_functions
from fn_resilient_ml.lib.res_utils import ResUtils
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
        """Function: """
        try:
            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            # Get the function parameters:
            search_incident_id = kwargs.get("search_incident_id")  # number
            nlp_search_string = kwargs.get("nlp_search_string")  # text
            number_incidents = kwargs.get("number_incidents")  # number

            log = logging.getLogger(__name__)
            log.info("search_incident_id: %s", search_incident_id)
            log.info("nlp_search_string: %s", nlp_search_string)
            log.info("number_incidents: %s", number_incidents)

            # Figure out where the saved model is
            model_path = self.options.get("model_path", None)
            if model_path is None:
                log.error("No model_path specified in app.config")
                raise Exception("Need model_path in app.config")

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")
            res_client = self.rest_client()
            res_utils = ResUtils(resclient=res_client,
                                 in_log=log)
            nlp_str = nlp_search_string
            if nlp_str is None or len(nlp_str) == 0:
                nlp_str = res_utils.get_inc_art_des(search_incident_id)

            inc_hrefs = util_functions.get_incident_href(nlp_str=nlp_str,
                                                         org_id=res_client.org_id,
                                                         base_url=res_client.base_url,
                                                         num_return=number_incidents,
                                                         model_path=model_path)

            yield StatusMessage("done...")

            results = {
                "incidents": inc_hrefs
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            log.exception(e)
            yield FunctionError()