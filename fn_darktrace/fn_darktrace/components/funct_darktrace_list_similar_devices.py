# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields, clean_html
from fn_darktrace.lib.app_common import AppCommon, PACKAGE_NAME

FN_NAME = "darktrace_list_similar_devices"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'darktrace_list_similar_devices'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Function to list similar devices to the given device.
        Inputs:
            -   fn_inputs.darktrace_device_count
            -   fn_inputs.darktrace_device_id
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        self.app_common = AppCommon(self.rc, self.options, self.opts.get("integrations", {}))

        validate_fields(["darktrace_device_count", "darktrace_device_id"], fn_inputs)

        # grab inputs (device ids might be wrapped in anchor tags so need to clean them)
        device_id = clean_html(fn_inputs.darktrace_device_id)
        count = fn_inputs.darktrace_device_count

        similar_devices = self.app_common.get_similar_devices(device_id, count=count)

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))
        
        results = {"similar_devices": similar_devices, "base_url": self.app_common.base_url.rstrip("/")}

        yield FunctionResult(results)
