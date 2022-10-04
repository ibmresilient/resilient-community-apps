# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""Function implementation"""

from fn_pa_panorama.util.panorama_util import PanoramaClient, PACKAGE_NAME
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult

FN_NAME = "panorama_get_address"

class FunctionComponent(AppFunctionComponent):
    """Component that implements Resilient function 'panorama_get_address"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Panorama get addresses returns a list of the address objects"""
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Log inputs
        self.LOG.info(fn_inputs)

        panorama_util = PanoramaClient(self.opts,
                                       self.options,
                                       self.get_select_param(getattr(fn_inputs, "panorama_location", None)),
                                       getattr(fn_inputs, "panorama_vsys", None))
        response = panorama_util.get_addresses()

        yield self.status_message(f"{response['result']['@count']} addresses returned.")
        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(response)
