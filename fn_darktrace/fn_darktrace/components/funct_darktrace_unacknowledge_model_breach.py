# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from fn_darktrace.lib.app_common import PACKAGE_NAME, AppCommon
from resilient_circuits import (AppFunctionComponent, FunctionResult,
                                app_function)
from resilient_lib import validate_fields

FN_NAME = "darktrace_unacknowledge_model_breach"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'darktrace_unacknowledge_model_breach'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Function to unacknowledge a model breach.
        Inputs:
            -   fn_inputs.darktrace_model_breach_pbid
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        app_common = AppCommon(self.rc, self.options, self.opts.get("integrations", {}))

        validate_fields(["darktrace_model_breach_pbid"], fn_inputs)

        pbid = fn_inputs.darktrace_model_breach_pbid
        results = app_common.unacknowledge_model_breach(pbid)

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)
