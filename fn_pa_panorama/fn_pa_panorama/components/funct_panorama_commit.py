# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.2.1096

"""AppFunction implementation"""

from fn_pa_panorama.util.panorama_util import PanoramaClient, PACKAGE_NAME, get_server_settings
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from xmltodict import parse

FN_NAME = "panorama_commit"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'panorama_commit'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Commit changes that have been made on the Panorama server
        Inputs:
            -   fn_inputs.panorama_label
            -   fn_inputs.panorama_location
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")
        # Log inputs
        self.LOG.info(fn_inputs)

        # Create connection to the user specific Panorama Server
        panorama_util = PanoramaClient(self.opts,
            get_server_settings(self.opts, getattr(fn_inputs, "panorama_label", None)),
            getattr(fn_inputs, "panorama_location", None),
            None)

        xml_response = panorama_util.commit_changes()
        results = parse(xml_response).get("response", {})

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)
