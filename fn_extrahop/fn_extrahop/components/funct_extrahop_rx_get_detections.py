# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields
from fn_extrahop.lib.rx_client import RxClient

PACKAGE_NAME = "fn_extrahop"
FN_NAME = "funct_extrahop_rx_get_detections"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'funct_extrahop_rx_get_detections'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get detections information from Extrahop Reveal(x) . Optional parameters extrahop_detecion_id
        Inputs:
            -   fn_inputs.extrahop_limit
            -   fn_inputs.extrahop_detection_id
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
        for i in ["extrahop_detection_id", "extrahop_limit"]:
            if hasattr(fn_inputs, i):
                params.update({i.split('_', 1)[1]: getattr(fn_inputs, i)})

        # Call 3rd party API :
        rx_cli = RxClient(self.opts, self.options)
        response = rx_cli.get_detections(**params)

        results = response.json()

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        results = {"mock_key": "Mock Value!"}

        yield FunctionResult(results)

