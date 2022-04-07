# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_extrahop.lib.rx_client import RxClient

PACKAGE_NAME = "fn_extrahop"
FN_NAME = "funct_extrahop_rx_create_tag"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'funct_extrahop_rx_create_tag'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Create a new tag for  Extrahop Reveal(x). Optional parameters tag_id.
        Inputs:
            -   fn_inputs.extrahop_tag_name
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        fn_msg = self.get_fn_msg()
        self.LOG.info("fn_msg: %s", fn_msg)

        # Set params dict:
        params = {}
        self.LOG.info("fn_inputs: %s", fn_inputs)

        if not hasattr(fn_inputs, "extrahop_tag_name"):
            raise ValueError("Missing 'extrahop_tag_name' function parameter")

        params.update({"tag_name": getattr(fn_inputs, "extrahop_tag_name")})

        # Call 3rd party API :
        rx_cli = RxClient(self.opts, self.options)
        response = rx_cli.create_tag(**params)

        if response.status_code == 201:
            # Action succeeded with empty response message
            result = "success"
        else:
            result = "failed"

        results = {"result": result}

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)
