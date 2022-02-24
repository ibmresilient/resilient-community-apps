# -*- coding: utf-8 -*-

"""AppFunction implementation"""
from fn_reaqta.lib.app_common import AppCommon
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields, soar_datetimeformat

PACKAGE_NAME = "fn_reaqta"
FN_NAME = "reaqta_get_alert_information"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'reaqta_get_alert_information'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get all the ReaQta Alert information to populate custom fields and datatables
        Inputs:
            -   fn_inputs.reaqta_alert_id
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        validate_fields(["reaqta_url",
                        "api_version",
                        "cafile",
                        "api_key",
                        "api_secret"],
                        self.app_configs)

        validate_fields(["reaqta_alert_id"], fn_inputs)

        app_common = AppCommon(self.rc, self.app_configs._asdict())
        results, err_msg = app_common.get_alert(fn_inputs.reaqta_alert_id)
        if not err_msg:
            results['alert_url'] = app_common.make_linkback_url(fn_inputs.reaqta_alert_id)
            for event in results.get('triggerEvents'):
                event['happenedAt_ts'] = soar_datetimeformat(event.get('happenedAt'), split_at='.')

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results, success=True if not err_msg else False, reason=err_msg)
