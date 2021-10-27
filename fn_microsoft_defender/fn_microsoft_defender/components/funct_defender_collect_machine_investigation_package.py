# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# Copyright IBM Corp. 2010, 2020 - Confidential Information

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_microsoft_defender.lib.defender_common import DefenderAPI, MACHINES_URL, PACKAGE_NAME, \
    MACHINE_ACTIONS_URL, PACKAGE_URI

FN_NAME = "defender_collect_machine_investigation_package"
COLLECT_PACKAGE = "collectInvestigationPackage"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'defender_collect_machine_investigation_package'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: None
        Inputs:
            -   fn_inputs.defender_machine_id
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        validate_fields([{"name": "tenant_id"}, {"name": "client_id"}, {"name": "app_secret"}], self._app_configs_as_dict)

        # Get the function parameters:
        defender_machine_id = fn_inputs.defender_machine_id  # text
        action_description = fn_inputs.defender_description  # text

        defender_api = DefenderAPI(self.app_configs.tenant_id,
                                   self.app_configs.client_id,
                                   self.app_configs.app_secret,
                                   self.opts,
                                   self._app_configs_as_dict)

        payload = {
            "Comment": action_description
        }
        self.LOG.debug(payload)

        # build the url
        url = "/".join([MACHINES_URL, defender_machine_id, COLLECT_PACKAGE])
        package_result, status, reason = defender_api.call(url, payload=payload, oper="POST")

        # if 201, run GET https://api.securitycenter.microsoft.com/api/machineactions/7327b54fd718525cbca07dacde913b5ac3c85673/GetPackageUri

        if status:
            # get the uri for the report
            url = "/".join([MACHINE_ACTIONS_URL, package_result['id']])
            package_result, status, reason = defender_api.wait_for_action(url)

        else:
            yield self.status_message(u"{} failure. Status: {} Reason: {}".format(FN_NAME, status, reason))

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(package_result, success=status, reason=reason)
