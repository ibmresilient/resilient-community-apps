# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# Generated with resilient-sdk v51.0.4.0.1351

"""AppFunction implementation"""

from fn_pa_panorama.util.panorama_util import PanoramaClient, PACKAGE_NAME, get_server_settings
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from xmltodict import parse

FN_NAME = "panorama_get_job_status"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'panorama_get_job_status'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get panorama job status from job ID.
        Inputs:
            -   fn_inputs.panorama_job_id
            -   fn_inputs.panorama_label
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")
        # Validate required inputs
        validate_fields(["panorama_job_id"], fn_inputs)
        # Log inputs
        self.LOG.info(fn_inputs)

        # Create connection to the user specific Panorama Server
        panorama_util = PanoramaClient(self.opts,
            get_server_settings(self.opts, getattr(fn_inputs, "panorama_label", None)))

        try:
            resp = panorama_util.get_job_status(getattr(fn_inputs, "panorama_job_id", None))
            results = parse(resp).get("response", {})

            yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")
