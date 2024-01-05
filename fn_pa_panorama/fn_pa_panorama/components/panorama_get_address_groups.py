# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""Function implementation"""

from fn_pa_panorama.util.panorama_util import PanoramaClient, PACKAGE_NAME, get_server_settings
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

FN_NAME = "panorama_get_address_groups"

class FunctionComponent(AppFunctionComponent):
    """Component that implements Resilient function 'panorama_get_address_groups"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: List address groups in Panorama.
        Inputs:
            -   fn_inputs.panorama_name_parameter
            -   fn_inputs.panorama_vsys
            -   fn_inputs.panorama_label
            -   fn_inputs.panorama_location
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate required parameters
        validate_fields(["panorama_name_parameter", "panorama_location"], fn_inputs)

        # Log inputs
        self.LOG.info(fn_inputs)

        # Create connection to the user specific Panorama Server
        panorama_util = PanoramaClient(self.opts,
                                       get_server_settings(self.opts, getattr(fn_inputs, "panorama_label", None)),
                                       self.get_select_param(fn_inputs.panorama_location),
                                       getattr(fn_inputs, "panorama_vsys", None))

        try:
            response = panorama_util.get_address_groups(fn_inputs.panorama_name_parameter)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=err)

        yield self.status_message(f"{response.get('result', {}).get('@count')} groups returned.")
        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(response)
