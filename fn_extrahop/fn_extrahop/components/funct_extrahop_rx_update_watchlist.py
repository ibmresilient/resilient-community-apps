# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_extrahop.lib.rx_client import RxClient

PACKAGE_NAME = "fn_extrahop"
FN_NAME = "funct_extrahop_rx_update_watchlist"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'funct_extrahop_rx_update_watchlist'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Add or remove devices from the watchlist on Extrahop reveal(x)).
        Inputs:
            -   fn_inputs.extrahop_unassign
            -   fn_inputs.extrahop_assign
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        fn_msg = self.get_fn_msg()
        self.LOG.info("fn_msg: %s", fn_msg)

        # Set params dict:
        params = {}
        self.LOG.info("fn_inputs: %s", fn_inputs)
        if not any(hasattr(fn_inputs, i) for i in ["extrahop_assign", "extrahop_unassign"]):
            raise ValueError("Missing function parameter, at least one of 'extrahop_assign' "
                             "or 'extrahop_unassign' should be set.")

        for i in ["extrahop_assign", "extrahop_unassign"]:
            if hasattr(fn_inputs, i):
                # Strip off "extrahop_" prefix from input paramter value before adding to params.
                params.update({i.split('_', 1)[1]: getattr(fn_inputs, i)})

        # Call 3rd party API :
        rx_cli = RxClient(self.opts, self.options)
        response = rx_cli.update_watchlist(**params)

        if response.status_code in [200, 201, 204]:
            # Action succeeded with empty response message
            result = "success"
        else:
            result = "failed"

        results = {"result": result}

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)
