# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

PACKAGE_NAME = "fn_sdk_test"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'utilities_resilient_search''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("utilities_resilient_search")
    def _utilities_resilient_search_function(self, event, *args, **kwargs):
        """Function: This function searches the Resilient platform for incident data according to the criteria specified, and returns the results to your workflow. It can be used to find incidents containing data that matches any string, or incidents currently assigned to a given user, or a very wide range of other search conditions.

**NOTE:** The search results may include data from incidents that the current Resilient user (the person who triggered the workflow) cannot access. Often your Resilient users have the `Default` role that allows them to only see incidents where they are members. This function runs with the permissions of your integration account, which typically may have much wider access privileges. **Use with caution, to avoid information disclosure.**"""
        try:

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting 'utilities_resilient_search' running in workflow '{0}'".format(wf_instance_id))

            # Get the function parameters:
            resilient_search_template = self.get_textarea_param(kwargs.get("resilient_search_template"))  # textarea
            resilient_search_query = kwargs.get("resilient_search_query")  # text

            log = logging.getLogger(__name__)
            log.info("resilient_search_template: %s", resilient_search_template)
            log.info("resilient_search_query: %s", resilient_search_query)

            ##############################################
            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE #
            ##############################################

            yield StatusMessage("Finished 'utilities_resilient_search' that was running in workflow '{0}'".format(wf_instance_id))

            results = {
                "content": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
