# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields
from fn_microsoft_defender.lib.defender_common import DefenderAPI, convert_date, MACHINES_URL, PACKAGE_NAME, make_filter_url

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

        # Example validating app_configs
        # validate_fields([
        #     {"name": "api_key", "placeholder": "<your-api-key>"},
        #     {"name": "base_url", "placeholder": "<api-base-url>"}],
        #     self._app_configs_as_dict)

        # Example getting access to self.get_fn_msg()
        # fn_msg = self.get_fn_msg()
        # self.LOG.info("fn_msg: %s", fn_msg)

        # Example raising an exception
        # raise IntegrationError("Example raising custom error")

        ##############################################
        # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE #
        ##############################################

        # Call API implemtation example:
        # params = {
        #     "api_key": self.app_configs.api_key,
        #     "ip_address": fn_inputs.artifact_value
        # }
        #
        # response = self.rc.execute(
        #     method="get",
        #     url=self.app_configs.api_base_url,
        #     params=params
        # )
        #
        # results = response.json()

        ##############################################

        validate_fields([{"name": "tenant_id"}, {"name": "client_id"}, {"name": "app_secret"}], self._app_configs_as_dict)
        validate_fields([{"name": "defender_machine_id"}, {"name": "defender_description"}], fn_inputs)

        # Get the function parameters:
        defender_machine_id = fn_inputs.defender_machine_id  # text
        action_description = fn_inputs.defender_description  # text

        defender_api = DefenderAPI(self._app_configs_as_dict.tenant_id,
                                   self._app_configs_as_dict.client_id,
                                   self._app_configs_as_dict.app_secret,
                                   None, None,
                                   self.rc)

        payload = {
            "Comment": action_description
        }
        self.LOG.debug(payload)

        # build the url
        url = "/".join([MACHINES_URL, defender_machine_id, COLLECT_PACKAGE])
        package_result, status, reason = defender_api.call(url, payload=payload, oper="POST")

        if not status:
            yield self.status_message(u"{} failure. Status: {} Reason: {}".format(FN_NAME, status, reason))

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(package_result, success=status, reason=reason)
