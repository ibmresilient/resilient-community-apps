# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_extrahop.lib.rx_client import RxClient
from fn_extrahop.lib.app_common import set_params

PACKAGE_NAME = "fn_extrahop"
FN_NAME = "funct_extrahop_rx_get_watchlist"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'funct_extrahop_rx_get_watchlist'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get watchlist information from Extrahop Reveal(x) .
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        fn_msg = self.get_fn_msg()
        self.LOG.info("fn_msg: %s", fn_msg)

        # Set params dict:
        params = {}
        params = set_params(fn_inputs, params)

        # Call 3rd party API :
        rx_cli = RxClient(self.opts, self.options)
        response = rx_cli.get_watchlist(**params)

        # Response can be a list, returned result needs to be a dict
        results = {"result": response.json()}

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)
