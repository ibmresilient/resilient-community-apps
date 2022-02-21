# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from fn_reaqta.lib.app_common import AppCommon
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields

PACKAGE_NAME = "fn_reaqta"
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
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        validate_fields(["reaqta_url",
                        "api_version",
                        "cafile",
                        "api_key",
                        "api_secret"],
                        self.app_configs)

        validate_fields(["reaqta_endpoint_id", "reaqta_process_pid", "reaqta_starttime"], fn_inputs)

        # Example getting access to self.get_fn_msg()
        # fn_msg = self.get_fn_msg()
        # self.LOG.info("fn_msg: %s", fn_msg)

        app_common = AppCommon(self.rc, self.app_configs._asdict())
        results = app_common.kill_process(fn_inputs.reaqta_endpoint_id,
                                          fn_inputs.reaqta_process_pid,
                                          fn_inputs.reaqta_starttime)

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)
