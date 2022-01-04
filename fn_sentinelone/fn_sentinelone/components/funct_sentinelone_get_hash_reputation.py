# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_sentinelone.lib.sentinelone_common import SentinelOneClient

PACKAGE_NAME = "fn_sentinelone"
FN_NAME = "sentinelone_get_hash_reputation"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'sentinelone_get_hash_reputation'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get the SentinelOne reputation of a hash.
        Inputs:
            -   fn_inputs.sentinelone_hash
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        sentinelone_client = SentinelOneClient(self.opts, self.options)
        s1_hash = fn_inputs.sentinelone_hash
        results = sentinelone_client.get_hash_reputation(s1_hash)

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)
