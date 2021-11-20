# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields
from fn_sentinelone.lib.sentinelone_common import SentinelOneClient

PACKAGE_NAME = "fn_sentinelone"
FN_NAME = "sentinelone_shutdown_agent"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'sentinelone_shutdown_agent'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Shutdown an agent managed by SentinelOne.
        Inputs:
            -   fn_inputs.sentinelone_agent_id
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        sentinelOne_client = SentinelOneClient(self.opts, self.options)
        agent_id = fn_inputs.sentinelone_agent_id
        results = sentinelOne_client.shutdown_agent(agent_id)

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)