# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""AppFunction implementation"""

from fn_mcafee_epo.lib.epo_helper import init_client, PACKAGE_NAME
from resilient_circuits import FunctionResult, AppFunctionComponent, app_function

FN_NAME = "mcafee_epo_list_tags"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'mcafee_epo_list_tags''"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.opts = opts
        self.options = opts.get(PACKAGE_NAME, {})

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: list all tags defined in ePO"""
        yield self.status_message("Starting App Function: '{}'".format(FN_NAME))

        # Connect to ePO server
        client = init_client(self.opts, self.options)

        yield self.status_message("Finished running App Function: '{}'".format(FN_NAME))

        # Produce a FunctionResult with the results
        yield FunctionResult(client.request("system.findTag", {}))
