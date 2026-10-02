# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""AppFunction implementation"""
from fn_reaqta.lib.app_common import AppCommon, PACKAGE_NAME, get_hive_options
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields, soar_datetimeformat

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
            -   fn_inputs.reaqta_hive
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        validate_fields(["reaqta_hive", "reaqta_alert_id"], fn_inputs)

        hive_settings = get_hive_options(fn_inputs.reaqta_hive, self.opts)
        if not hive_settings:
            results = {}
            err_msg = "Hive section not found: {}".format(fn_inputs.reaqta_hive)
        else:
            app_common = AppCommon(self.rc, hive_settings)
            results, err_msg = app_common.get_alert(fn_inputs.reaqta_alert_id)
            if not err_msg:
                results['alert_url'] = app_common.make_linkback_url(fn_inputs.reaqta_alert_id)
                for event in results.get('triggerEvents'):
                    event['happenedAt_ts'] = soar_datetimeformat(event.get('happenedAt'), split_at='.')

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results, success=True if not err_msg else False, reason=err_msg)
