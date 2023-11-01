# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
"""Function implementation"""

from fn_pa_panorama.util.panorama_util import PanoramaClient, PACKAGE_NAME, get_server_settings
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

FN_NAME = "panorama_create_address"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'panorama_create_address'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Creates a new address object in Panorama.
        Inputs:
            -   fn_inputs.panorama_request_body
            -   fn_inputs.panorama_vsys
            -   fn_inputs.panorama_location
            -   fn_inputs.panorama_name_parameter
            -   fn_inputs.panorama_label
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate required parameters
        validate_fields(["panorama_name_parameter", "panorama_request_body", "panorama_location"], fn_inputs)

        # Log inputs
        self.LOG.info(fn_inputs)

        # Create connection to the user specific Panorama Server
        panorama_util = PanoramaClient(self.opts,
                                       get_server_settings(self.opts, getattr(fn_inputs, "panorama_label", None)),
                                       self.get_select_param(fn_inputs.panorama_location),
                                       getattr(fn_inputs, "panorama_vsys", None))

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(panorama_util.add_address(fn_inputs.panorama_name_parameter,
                             self.get_textarea_param(fn_inputs.panorama_request_body)))
