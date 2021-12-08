# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_sentinelone.lib.sentinelone_common import SentinelOneClient

PACKAGE_NAME = "fn_sentinelone"
FN_NAME = "sentinelone_update_threat_analyst_verdict"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'sentinelone_update_threat_analyst_verdict'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Update the verdict of a threat in SentinelOne.
        Inputs:
            -   fn_inputs.sentinelone_threat_analyst_verdict
            -   fn_inputs.sentinelone_threat_id
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        sentinelone_client = SentinelOneClient(self.opts, self.options)
        threat_id = fn_inputs.sentinelone_threat_id
        threat_analyst_verdict = fn_inputs.sentinelone_threat_analyst_verdict
        results = sentinelone_client.update_threat_analyst_verdict(threat_id, 
                                                                   threat_analyst_verdict)

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)
