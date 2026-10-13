# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""AppFunction implementation"""
from fn_reaqta.lib.app_common import AppCommon, PACKAGE_NAME, get_hive_options
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

FN_NAME = "reaqta_create_note"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'reaqta_create_note'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Append a note to the ReaQta notes
        Inputs:
            -   fn_inputs.reaqta_alert_id
            -   fn_inputs.reaqta_note
            -   fn_inputs.reaqta_hive
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        validate_fields(["reaqta_hive", "reaqta_alert_id", "reaqta_note"], fn_inputs)

        hive_settings = get_hive_options(fn_inputs.reaqta_hive, self.opts)
        if not hive_settings:
            results = {}
            err_msg = "Hive section not found: {}".format(fn_inputs.reaqta_hive)
        else:
            app_common = AppCommon(self.rc, hive_settings)

            results, err_msg = app_common.create_note(fn_inputs.reaqta_alert_id, fn_inputs.reaqta_note)
            results = { "note": results } if not err_msg else results

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results, success=True if not err_msg else False, reason=err_msg)
