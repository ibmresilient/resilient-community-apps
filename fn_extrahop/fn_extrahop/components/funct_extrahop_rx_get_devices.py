# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields
from fn_extrahop.lib.rx_client import RxClient

PACKAGE_NAME = "fn_extrahop"
FN_NAME = "funct_extrahop_rx_get_devices"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'funct_extrahop_rx_get_devices'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get or search for devices information from Extrahop Reveal(x) . Optional parameter extrahop_device_id
        Inputs:
            -   fn_inputs.extrahop_device_id
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        validate_fields([
            {"name": "extrahop_rx_host_url", "placeholder": "<EXTRAHOP_RX_HOST_URL>"},
            {"name": "extrahop_rx_key_id", "placeholder": "<EXTRAHOP_RX_API_KEY_ID>"},
            {"name": "extrahop_rx_key_secret", "placeholder": "<EXTRAHOP_RX_API_KEY_SECRET>"},
            {"name": "extrahop_rx_api_version"}],
        self.options)

        # Example getting access to self.get_fn_msg()
        fn_msg = self.get_fn_msg()
        self.LOG.info("fn_msg: %s", fn_msg)

        ##############################################
        # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE #
        ##############################################

        # Set params dict:
        params = {}
        self.LOG.info("fn_inputs: %s", fn_inputs)
        if hasattr(fn_inputs, "extrahop_device_id"):
            params.update({"device_id": fn_inputs.extrahop_device_id})
        # Call 3rd party API :
        rx_cli = RxClient(self.opts, self.options)
        response = rx_cli.get_devices(**params)

        results = response.json()

        ##############################################

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))


        yield FunctionResult(results)

