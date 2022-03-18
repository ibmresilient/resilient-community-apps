# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""AppFunction implementation"""
from fn_reaqta.lib.app_common import AppCommon, PACKAGE_NAME, get_hive_options
from fn_reaqta.lib.poller_common import IBM_SOAR
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

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
            -   fn_inputs.reaqta_hive
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        validate_fields(["reaqta_hive", "reaqta_alert_id", "reaqta_is_malicious"], fn_inputs)

        hive_settings = get_hive_options(fn_inputs.reaqta_hive, self.opts)
        if not hive_settings:
            results = {}
            err_msg = "Hive section not found: {}".format(fn_inputs.reaqta_hive)
        else:
            app_common = AppCommon(self.rc, hive_settings)

            # write a note if one present
            inputs_dict = fn_inputs._asdict()
            if inputs_dict.get('reaqta_note'):
                results, err_msg = app_common.create_note(fn_inputs.reaqta_alert_id, fn_inputs.reaqta_note)
                if err_msg:
                    self.LOG.error("create note failed: %s", err_msg)

            results, err_msg = app_common.close_alert(fn_inputs.reaqta_alert_id, fn_inputs.reaqta_is_malicious)

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results, success=True if not err_msg else False, reason=err_msg)
