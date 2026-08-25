# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_extrahop.lib.rx_client import RxClient
from fn_extrahop.lib.app_common import set_params

PACKAGE_NAME = "fn_extrahop"
FN_NAME = "funct_extrahop_rx_add_detection_note"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'funct_extrahop_rx_add_detection_note'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Add a note to an ExtraHop detection. Parameters detection_id, note,  update_time.
        Inputs:
            -   fn_inputs.extrahop_detection_id
            -   fn_inputs.extrahop_update_time
            -   fn_inputs.extrahop_note
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        fn_msg = self.get_fn_msg()
        self.LOG.info("fn_msg: %s", fn_msg)
        self.LOG.info("fn_inputs: %s", fn_inputs)

        # Validate required fields
        for i in ["extrahop_detection_id", "extrahop_note"]:
            if not hasattr(fn_inputs, i):
                raise ValueError("Missing '{}' function parameter".format(i))

        # Set params dict:
        params = {}
        params = set_params(fn_inputs, params)

        # Call 3rd party API :
        rx_cli = RxClient(self.opts, self.options)
        response = rx_cli.add_detection_note(**params)

        if response.status_code == 200:
            # Action succeeded with empty response message
            result = "success"
        elif response.status_code in [422, 500]:
            error_code = response.status_code
            if response.status_code == 422:
                text = response.json()["detail"]
            else:
                text = response.reason

            result =  {
                "error": error_code,
                "text": text
            }
        else:
            result = "failed"
            success = False

        results = {"result": result}

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)
