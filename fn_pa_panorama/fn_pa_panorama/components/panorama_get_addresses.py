# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""Function implementation"""

from fn_pa_panorama.util.panorama_util import PanoramaClient, PACKAGE_NAME, get_server_settings
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult

FN_NAME = "panorama_get_addresses"


class FunctionComponent(AppFunctionComponent):
    """Component that implements Resilient function 'panorama_get_addresses"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Panorama get addresses returns a list of the address objects
        Inputs:
            -   fn_inputs.panorama_vsys
            -   fn_inputs.panorama_label
            -   fn_inputs.panorama_location
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Log inputs
        self.LOG.info(fn_inputs)

        # Create connection to the user specific Panorama Server
        panorama_util = PanoramaClient(self.opts,
                                       get_server_settings(self.opts, getattr(
                                           fn_inputs, "panorama_label", None)),
                                       self.get_select_param(
                                           getattr(fn_inputs, "panorama_location", None)),
                                       getattr(fn_inputs, "panorama_vsys", None))

        # Initialize variables
        results = {}
        success = True
        reason = ""

        try:
            results = panorama_util.get_addresses()
        except Exception as err:
            success = False
            reason = err

        # Produce a FunctionResult with the results
        yield FunctionResult(results, success=success, reason=reason)

        yield self.status_message(f"{results.get('result', {}).get('@count')} addresses returned.")
        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")
