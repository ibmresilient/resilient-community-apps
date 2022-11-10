# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from fn_darktrace.lib.app_common import PACKAGE_NAME, AppCommon
from resilient_circuits import (AppFunctionComponent, FunctionResult,
                                app_function)
from resilient_lib import clean_html, validate_fields

FN_NAME = "darktrace_add_device_tags"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'darktrace_add_device_tags'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Function to add tag(s) to a device.
        Inputs:
            -   fn_inputs.darktrace_device_tags
            -   fn_inputs.darktrace_device_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        app_common = AppCommon(self.rc, self.options, self.opts.get("integrations", {}))

        validate_fields(["darktrace_device_id", "darktrace_device_tags"], fn_inputs)

        device_id = clean_html(fn_inputs.darktrace_device_id)
        tags = [tag.strip() for tag in fn_inputs.darktrace_device_tags.split(",")]
        added_tags = []
        error_tags= []

        for tag in tags:
            self.LOG.debug(f"Adding tag {tag} to device {device_id}")
            resp = app_common.add_tag_to_device(device_id, tag, capture_error=False)
            if resp.get("tags", "").upper() == "DATANOTFOUND ERROR":
                self.LOG.warning(f"Tag {tag} doesn't exist on the Darktrace server.")
                error_tags.append(tag)
            else:
                self.LOG.debug(f"Successfully added tag {tag} to device {device_id}")
                added_tags.append(tag)

        # query back to the device to get the full list of tags
        self.LOG.debug(f"Querying device for full list of tags")
        device_info = app_common.get_devices(params={"did": device_id, "includetags": "true"}, capture_error=False)
        all_tags = [tag.get("name") for tag in device_info.get("tags", [])]

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        results = {"all_tags": all_tags, "added_tags": added_tags, "error_tags": error_tags}

        yield FunctionResult(results)
