# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_extrahop.lib.rx_client import RxClient

PACKAGE_NAME = "fn_extrahop"
FN_NAME = "funct_extrahop_rx_assign_tag"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'funct_extrahop_rx_assign_tag'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Assign a tag to a list of devices ids forExtrahop Reveal(x).
                  Optional parameters tag_id. devices_ids.
        Inputs:
            -   fn_inputs.extrahop_tag_id
            -   fn_inputs.extrahop_device_ids
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        fn_msg = self.get_fn_msg()
        self.LOG.info("fn_msg: %s", fn_msg)

        # Set params dict:
        params = {}
        self.LOG.info("fn_inputs: %s", fn_inputs)
        for i in ["extrahop_tag_id", "extrahop_device_ids"]:
            if not hasattr(fn_inputs, i):
                raise ValueError("Missing '{}' function parameter".format(i))
            # Strip off "extrahop_" prefix from input paramter value before adding to params.
            params.update({i.split('_', 1)[1]: getattr(fn_inputs, i)})

        # Call 3rd party API :
        rx_cli = RxClient(self.opts, self.options)
        response = rx_cli.assign_tag(**params)

        if response.status_code == 204:
            result = "success"
        elif response.status_code == 207:
            result = "limited_success"
        else:
            result = "failed"

        results = {"result": result}

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)
