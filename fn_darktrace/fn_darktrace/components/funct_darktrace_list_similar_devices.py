# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""AppFunction implementation"""

from fn_darktrace.lib.app_common import PACKAGE_NAME, AppCommon
from resilient_circuits import (AppFunctionComponent, FunctionResult,
                                app_function)
from resilient_lib import clean_html, validate_fields

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

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        app_common = AppCommon(self.rc, self.options, self.opts.get("integrations", {}))

        validate_fields(["darktrace_device_count", "darktrace_device_id"], fn_inputs)

        # grab inputs (device ids might be wrapped in anchor tags so need to clean them)
        device_id = clean_html(fn_inputs.darktrace_device_id)
        count = fn_inputs.darktrace_device_count

        similar_devices = app_common.get_similar_devices(device_id, count=count)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        results = {"similar_devices": similar_devices, "base_url": app_common.base_url.rstrip("/")}

        yield FunctionResult(results)
