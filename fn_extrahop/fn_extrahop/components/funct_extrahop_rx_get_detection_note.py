# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_extrahop.lib.rx_client import RxClient
from fn_extrahop.lib.app_common import set_params

PACKAGE_NAME = "fn_extrahop"
FN_NAME = "funct_extrahop_rx_get_detection_note"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'funct_extrahop_rx_get_detection_note'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get a note from an ExtraHop detection. Parameter detection_id.
        Inputs:
            -   fn_inputs.extrahop_detection_id
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        fn_msg = self.get_fn_msg()
        self.LOG.info("fn_msg: %s", fn_msg)
        self.LOG.info("fn_inputs: %s", fn_inputs)

        # Validate required fields
        if not hasattr(fn_inputs, "extrahop_detection_id"):
            raise ValueError("Missing '{}' function parameter".format("extrahop_detection_id"))

        # Set params dict:
        params = {}
        params = set_params(fn_inputs, params)

        # Call 3rd party API :
        rx_cli = RxClient(self.opts, self.options)
        response = rx_cli.get_detection_note(**params)

        # Response can be a list, returned result needs to be a dict
        if response.status_code in [422, 500]:
            error_code = response.status_code
            if response.status_code == 422:
                text = response.json()["detail"]
            else:
                text = response.reason

            results = {
                "error": error_code,
                "text": text
            }
        else:
            results = {"result": response.json()}

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)
