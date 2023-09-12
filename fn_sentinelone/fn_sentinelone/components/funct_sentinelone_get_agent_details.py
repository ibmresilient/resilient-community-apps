# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_sentinelone.lib.app_common import (AppCommon, PACKAGE_NAME)

FN_NAME = "sentinelone_get_agent_details"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'sentinelone_get_agent_details'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: None
        Inputs:
            -   fn_inputs.sentinelone_agent_id
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        app_common = AppCommon(self.rc, PACKAGE_NAME, self.options)
        agent_id = fn_inputs.sentinelone_agent_id
        results = app_common.get_agent_details(agent_id)

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)
