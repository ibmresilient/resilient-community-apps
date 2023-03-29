# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""AppFunction implementation"""

from fn_reaqta.lib.app_common import AppCommon, PACKAGE_NAME, get_hive_options
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

FN_NAME = "reaqta_kill_process"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'reaqta_kill_process'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Kill a process on a machine by the process PID
        Inputs:
            -   fn_inputs.reaqta_process_pid
            -   fn_inputs.reaqta_endpoint_id
            -   fn_inputs.reaqta_hive
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        validate_fields([
            "reaqta_hive",
            "reaqta_endpoint_id",
            "reaqta_process_pid",
            "reaqta_starttime"
            ],
            fn_inputs)

        hive_settings = get_hive_options(fn_inputs.reaqta_hive, self.opts)
        if not hive_settings:
            results = {}
            err_msg = "Hive section not found: {}".format(fn_inputs.reaqta_hive)
        else:
            app_common = AppCommon(self.rc, hive_settings)
            results = app_common.kill_process(fn_inputs.reaqta_endpoint_id,
                                              fn_inputs.reaqta_process_pid,
                                              fn_inputs.reaqta_starttime)
            err_msg = None

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results, success=True if not err_msg else False, reason=err_msg)
