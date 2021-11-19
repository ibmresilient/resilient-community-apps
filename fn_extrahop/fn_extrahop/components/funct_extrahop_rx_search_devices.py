# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_extrahop.lib.rx_client import RxClient

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

        validate_fields([
            {"name": "extrahop_rx_host_url", "placeholder": "<EXTRAHOP_RX_HOST_URL>"},
            {"name": "extrahop_rx_key_id", "placeholder": "<EXTRAHOP_RX_API_KEY_ID>"},
            {"name": "extrahop_rx_key_secret", "placeholder": "<EXTRAHOP_RX_API_KEY_SECRET>"},
            {"name": "extrahop_rx_api_version"}],
        self.options)

        fn_msg = self.get_fn_msg()
        self.LOG.info("fn_msg: %s", fn_msg)

        # Set params dict:
        params = {}
        self.LOG.info("fn_inputs: %s", fn_inputs)
        for i in ["extrahop_search_filter", "extrahop_active_from",
                  "extrahop_active_until", "extrahop_limit",
                  "extrahop_offset"]:
            if hasattr(fn_inputs, i):
                # Strip off "extrahop_" prefix from input paramter value before adding to params.
                params.update({i.split('_', 1)[1]: getattr(fn_inputs, i)})

        # Call 3rd party API :
        rx_cli = RxClient(self.opts, self.options)
        response = rx_cli.search_devices(**params)
        # Response is a list, returned result needs to be a dict
        results = {"result": response.json()}

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)
