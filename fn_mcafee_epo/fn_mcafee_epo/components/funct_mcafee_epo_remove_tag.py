# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""AppFunction implementation"""

from fn_mcafee_epo.lib.epo_helper import init_client, PACKAGE_NAME
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
        Function: Remove a tag(s) associated with an ePO system(s). McAfee user requires Tag use permission for this function.
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate required parameters
        validate_fields(["mcafee_epo_systems", "mcafee_epo_tag"], fn_inputs)

        # Log parameters
        self.LOG.info(str(fn_inputs))

        # Determine if a list of tags was given
        if "," in fn_inputs.mcafee_epo_tag:
            # List of tags given
            temp_list = fn_inputs.mcafee_epo_tag.split(",")
            # This will filter out empty spaces after a comma and commas that have nothing after them (Helps prevent some user errors)
            tags_list = [tag.strip() for tag in temp_list if tag.strip()]
        else: # Single tag given
            tags_list = [fn_inputs.mcafee_epo_tag.strip()]

        # Determine if a list of systems was given
        if "," in fn_inputs.mcafee_epo_systems:
            # List of systems given
            temp_list = fn_inputs.mcafee_epo_systems.split(",")
            # This will filter out empty spaces after a comma and commas that have nothing after them (Helps prevent some user errors)
            systems_list = [system.strip() for system in temp_list if system.strip()]
        else: # Single system given
            systems_list = [fn_inputs.mcafee_epo_systems.strip()]

        # Connect to ePO server
        client = init_client(self.opts, self.options)

        # Loop through list of tags remove one tag at a time
        for tag in tags_list:
            # Loop through list of systems and remove a single tag to a single system at a time
            for system in systems_list:
                params = {
                    "names": system,
                    "tagName": tag
                }
                response = client.request("system.clearTag", params)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(response)
