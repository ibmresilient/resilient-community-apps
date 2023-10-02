# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
"""AppFunction implementation"""

from fn_mcafee_epo.lib.epo_helper import init_client, get_list, PACKAGE_NAME
from resilient_lib import validate_fields
from resilient_circuits import FunctionResult, AppFunctionComponent, app_function

FN_NAME = "mcafee_epo_remove_tag"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'mcafee_epo_remove_tag''"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Remove a tag associated with an ePO system(s). McAfee user requires Tag use permission for this function.
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate required parameters
        validate_fields(["mcafee_epo_systems", "mcafee_epo_tag"], fn_inputs)

        # Log parameters
        self.LOG.info(str(fn_inputs))

        # determine if a list of tags was given
        tag_list = get_list(fn_inputs.mcafee_epo_tag)

        # Connect to ePO server
        client = init_client(self.opts, self.options)

        for tag in tag_list:
            params = {
                "names": fn_inputs.mcafee_epo_systems.strip(),
                "tagName": tag
            }
            response = client.request("system.clearTag", params)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(response)
