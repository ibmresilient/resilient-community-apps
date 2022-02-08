# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_extrahop.lib.rx_client import RxClient

PACKAGE_NAME = "fn_extrahop"
FN_NAME = "funct_extrahop_rx_get_activitymaps"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'funct_extrahop_rx_get_activitymaps'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get activitymap information from Extrahop Reveal(x) .
                  Optional parameters activitymap_id.
        Inputs:
            -   fn_inputs.extrahop_activitymap_id
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        fn_msg = self.get_fn_msg()
        self.LOG.info("fn_msg: %s", fn_msg)


        # Set params dict:
        params = {}
        self.LOG.info("fn_inputs: %s", fn_inputs)
        if hasattr(fn_inputs, "extrahop_activitymap_id"):
            params.update({"activitymap_id": fn_inputs.extrahop_activitymap_id})

        # Call 3rd party API :
        rx_cli = RxClient(self.opts, self.options)
        response = rx_cli.get_activitymaps(**params)

        # Response can be a list, returned result needs to be a dict
        results = {"result": response.json()}

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)
