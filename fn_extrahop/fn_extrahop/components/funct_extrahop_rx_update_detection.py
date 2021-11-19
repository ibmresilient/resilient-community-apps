# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields
from fn_extrahop.lib.rx_client import RxClient

PACKAGE_NAME = "fn_extrahop"
FN_NAME = "funct_extrahop_rx_update_detection"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'funct_extrahop_rx_update_detection'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Update a detection in Extrahop Reveal(x).
                  Required parameter incident_id, detection_id, owner_id, plan_status, resolution.
                  Optional parameter participants.
        Inputs:
            -   fn_inputs.incident_id
            -   fn_inputs.extrahop_detection_id
            -   fn_inputs.soar_inc_owner_id
            -   fn_inputs.soar_inc_resolution_id
            -   fn_inputs.soar_inc_plan_status
            -   fn_inputs.extrahop_participants
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

        for i in ["incident_id", "extrahop_detection_id",
                  "soar_inc_owner_id", "soar_inc_resolution_id",
                  "soar_inc_plan_status"]:
            if not hasattr(fn_inputs, i):
                raise ValueError("Missing function parameter '{}'.".format(i))

        params.update({"incident_id": fn_inputs.incident_id})

        for i in ["soar_inc_owner_id", "soar_inc_resolution_id", "soar_inc_plan_status"]:
            params.update({i.split('_', 2)[2]: getattr(fn_inputs, i)})

        if hasattr(fn_inputs, i):
            for i in ["extrahop_detection_id", "extrahop_participants"]:
                params.update({i.split('_', 1)[1]: getattr(fn_inputs, i)})

        # Call 3rd party API :
        rx_cli = RxClient(self.opts, self.options)
        response = rx_cli.update_detection(**params)

        if response.status_code == 201:
            # Action succeeded with empty response message
            result = "success"
        else:
            result = "failed"

        results = {"result": result}

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)
