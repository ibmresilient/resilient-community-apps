# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'mitre_groups_technique_intersection"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_mitre_integration", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_mitre_integration", {})

    @function("mitre_groups_technique_intersection")
    def _mitre_groups_technique_intersection_function(self, event, *args, **kwargs):
        """Function: For given Techniques return the Groups that are know to use all of them."""
        try:
            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            # Get the function parameters:
            mitre_technique_name = kwargs.get("mitre_technique_name")  # text
            mitre_technique_id = kwargs.get("mitre_technique_id")  # text

            log = logging.getLogger(__name__)
            log.info("mitre_technique_name: %s", mitre_technique_name)
            log.info("mitre_technique_id: %s", mitre_technique_id)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            #  yield StatusMessage("starting...")
            #  yield StatusMessage("done...")

            results = {
                "value": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()