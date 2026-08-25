# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# Generated with resilient-sdk v51.0.4.0.1351

"""AppFunction implementation"""

from fn_pa_panorama.util.panorama_util import PanoramaClient, PACKAGE_NAME, get_server_settings
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields, str_to_bool
from xmltodict import parse

FN_NAME = "panorama_commit_all"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'panorama_commit_all'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Commit and push changes to panorama firewall
        Inputs:
            -   fn_inputs.panorama_device_group
            -   fn_inputs.panorama_label
            -   fn_inputs.panorama_commit_without_default_template
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")
        # Validate required inputs
        validate_fields(["panorama_device_group"], fn_inputs)
        device_group = getattr(fn_inputs, "panorama_device_group", None)
        commit_without_default_template = str_to_bool(getattr(fn_inputs, "panorama_commit_without_default_template", "False"))
        # Log inputs
        self.LOG.info(fn_inputs)

        # Create connection to the user specific Panorama Server
        panorama_util = PanoramaClient(self.opts,
            get_server_settings(self.opts, getattr(fn_inputs, "panorama_label", None)))

        try:
            if commit_without_default_template:
                resp = panorama_util.specific_device_group_without_default_template(device_group)
            else:
                resp = panorama_util.specific_device_group(device_group)

            results = parse(resp).get("response", {})

            yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")
