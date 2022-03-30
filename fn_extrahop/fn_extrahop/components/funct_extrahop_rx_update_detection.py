# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
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
            # Strip off "soar_inc_" prefix from input paramter value before adding to params.
            params.update({i.split('_', 2)[2]: getattr(fn_inputs, i)})

        for i in ["extrahop_detection_id", "extrahop_participants"]:
            if hasattr(fn_inputs, i):
                # Strip off "extrahop_" prefix from input paramter value before adding to params.
                params.update({i.split('_', 1)[1]: getattr(fn_inputs, i)})

        # Call 3rd party API :
        rx_cli = RxClient(self.opts, self.options)
        response = rx_cli.update_detection(**params)

        if response.status_code in [200, 201, 204]:
            # Action succeeded with empty response message
            result = "success"
        else:
            result = "failed"

        results = {"result": result}

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)
