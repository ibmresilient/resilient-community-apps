# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_extrahop.lib.rx_client import RxClient
from fn_extrahop.lib.app_common import set_params

PACKAGE_NAME = "fn_extrahop"
FN_NAME = "funct_extrahop_rx_search_devices"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'funct_extrahop_rx_search_devices'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Search for devices information from Extrahop Reveal(x).
                  Optional parameter search_filter, active_from, active_util, limit and offset
        Inputs:
            -   fn_inputs.extrahop_search_filter
            -   fn_inputs.extrahop_active_until
            -   fn_inputs.extrahop_active_from
            -   fn_inputs.extrahop_limit
            -   fn_inputs.extrahop_offset
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        fn_msg = self.get_fn_msg()
        self.LOG.info("fn_msg: %s", fn_msg)
        self.LOG.info("fn_inputs: %s", fn_inputs)

        # Set params dict:
        params = {}
        params = set_params(fn_inputs, params)

        # Call 3rd party API :
        rx_cli = RxClient(self.opts, self.options)
        response = rx_cli.search_devices(**params)
        # Response is a list, returned result needs to be a dict
        if response.status_code == 400:
            results = {"error": response.json()["error_message"]}
        else:
            results = {"result": response.json()}

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)
