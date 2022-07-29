# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""AppFunction implementation"""

from fn_mcafee_epo.lib.epo_helper import init_client, get_list, PACKAGE_NAME
from resilient_lib import validate_fields
from resilient_circuits import FunctionResult, AppFunctionComponent, app_function

FN_NAME = "mcafee_tag_an_epo_asset"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'mcafee_tag_an_epo_asset"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.opts = opts
        self.options = opts.get(PACKAGE_NAME, {})

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: A function which takes two inputs:

        mcafee_epo_system: Comma separated list of Hostnames/IpAddress. These systems must be managed on ePO.
        mcafee_epo_tag: A Tag managed on ePO.

        Applies tag to the systems in ePO.
        """
        yield self.status_message("Starting App Function: '{}'".format(FN_NAME))

        # Get the function parameters:
        validate_fields(["mcafee_epo_systems", "mcafee_epo_tag"], fn_inputs)

        self.LOG.info("mcafee_epo_systems: %s", fn_inputs.mcafee_epo_systems)
        self.LOG.info("mcafee_epo_tag: %s", fn_inputs.mcafee_epo_tag)

        # determine if a list of tags was given
        tag_list = get_list(fn_inputs.mcafee_epo_tag)

        # Connect to ePO server
        client = init_client(self.opts, self.options)

        for tag in tag_list:
            params = {
                "names": fn_inputs.mcafee_epo_systems.strip(),
                "tagName": tag
            }
            response = client.request("system.applyTag", params)

        yield self.status_message("Finished running App Function: '{}'".format(FN_NAME))

        # Produce a FunctionResult with the results
        yield FunctionResult(response)
