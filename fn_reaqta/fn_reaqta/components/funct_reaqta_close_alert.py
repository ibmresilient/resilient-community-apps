# -*- coding: utf-8 -*-

"""AppFunction implementation"""
from fn_reaqta.lib.app_common import AppCommon
from fn_reaqta.lib.poller_common import IBM_SOAR
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields

PACKAGE_NAME = "fn_reaqta"
FN_NAME = "reaqta_close_alert"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'reaqta_close_alert'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Close a ReaQta Alert
        Inputs:
            -   fn_inputs.reaqta_alert_id
            -   fn_inputs.reaqta_note
            -   fn_inputs.reaqta_is_malicious
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        validate_fields(["reaqta_url",
                        "api_version",
                        "cafile",
                        "api_key",
                        "api_secret"],
                        self.app_configs)

        validate_fields(["reaqta_alert_id", "reaqta_is_malicious"], fn_inputs)

        app_common = AppCommon(self.rc, self.app_configs._asdict())

        # write a note if one present
        inputs_dict = fn_inputs._asdict()
        if inputs_dict.get('reaqta_note'):
            results, err_msg = app_common.create_note(fn_inputs.reaqta_alert_id, fn_inputs.reaqta_note)
            if err_msg:
                self.LOG.error("create note failed: %s", err_msg)

        results, err_msg = app_common.close_alert(fn_inputs.reaqta_alert_id, fn_inputs.reaqta_is_malicious)

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results, success=True if not err_msg else False, reason=err_msg)
