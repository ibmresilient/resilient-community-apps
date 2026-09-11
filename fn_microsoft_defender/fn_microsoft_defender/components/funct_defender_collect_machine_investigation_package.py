# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# Copyright IBM Corp. 2010, 2025 - Confidential Information

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields, IntegrationError
from fn_microsoft_defender.lib.defender_common import DefenderAPI, MACHINES_URL, PACKAGE_NAME, \
    MACHINE_ACTIONS_URL

FN_NAME = "defender_collect_machine_investigation_package"
COLLECT_PACKAGE = "collectInvestigationPackage"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'defender_collect_machine_investigation_package'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Collect the machine investigation package
        Inputs:
            -   fn_inputs.defender_machine_id
            -   fn_inputs.defender_description
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate required inputs
        validate_fields(["defender_machine_id", "defender_description"], fn_inputs)

        try:
            defender_api = DefenderAPI(self.app_configs.tenant_id,
                                    self.app_configs.client_id,
                                    self.app_configs.app_secret,
                                    self.opts, self.options)

            payload = {"Comment": fn_inputs.defender_description}
            self.LOG.debug(payload)

            package_result, status, reason = defender_api.call(
                "/".join([MACHINES_URL, fn_inputs.defender_machine_id, COLLECT_PACKAGE]),
                payload=payload, oper="POST")

            # If 201, run GET https://api.securitycenter.microsoft.com/api/machineactions/7327b54fd718525cbca07dacde913b5ac3c85673/GetPackageUri

            if status:
                # Get the uri for the report
                package_result, status, reason = defender_api.wait_for_action(
                    "/".join([MACHINE_ACTIONS_URL, package_result['id']]))
            else:
                err_msg = f"{FN_NAME} failure. Status: {status} Reason: {reason}"
                yield self.status_message(err_msg)
                raise IntegrationError(err_msg)

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

            yield FunctionResult(package_result, success=status, reason=reason)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
