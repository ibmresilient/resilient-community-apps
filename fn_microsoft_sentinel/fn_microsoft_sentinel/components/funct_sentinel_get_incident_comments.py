# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""Function implementation"""

from resilient_circuits import (AppFunctionComponent, FunctionResult,
                                app_function)
from resilient_lib import validate_fields

from fn_microsoft_sentinel.lib.function_common import (PACKAGE_NAME,
                                                       SentinelProfiles)
from fn_microsoft_sentinel.lib.resilient_common import ResilientCommon
from fn_microsoft_sentinel.lib.sentinel_common import SentinelAPI

FN_NAME = "sentinel_get_incident_comments"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'sentinel_get_incident_comments''"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.sentinel_profiles = SentinelProfiles(opts, self.options)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get Comments from a Sentinel Incident
        Inputs:
            -   fn_inputs.sentinel_profile
            -   fn_inputs.sentinel_label
            -   fn_inputs.sentinel_incident_id
            -   fn_inputs.incident_id
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")
        validate_fields(["sentinel_incident_id"], fn_inputs)

        # Get the function parameters:
        incident_id = getattr(fn_inputs, "incident_id", None)
        sentinel_incident_id = fn_inputs.sentinel_incident_id
        sentinel_profile = getattr(fn_inputs, "sentinel_profile", None)
        sentinel_label = getattr(fn_inputs, "sentinel_label", None)
        if not sentinel_profile and not sentinel_label:
            raise ValueError("Either sentinel_profile or sentinel_label need to be given.")

        self.LOG.info(f"Incident ID: {incident_id}")
        self.LOG.info(f"Sentinel Incident ID: {sentinel_incident_id}")
        self.LOG.info(f"Sentinel Profile: {sentinel_profile}")
        self.LOG.info(f"Sentinel Label: {sentinel_label}")

        # Get the configuration for the selected Sentinel profile from the app.config
        profile_data = self.sentinel_profiles.get_profile(sentinel_label if sentinel_label else sentinel_profile)

        # Create connection to Sentinel
        sentinel_api = SentinelAPI(self.opts, self.options, profile_data if sentinel_label else None)

        soar_api = ResilientCommon(self.rest_client())

        result, status, reason = sentinel_api.get_comments(profile_data, sentinel_incident_id)

        new_comments = []
        if status:
            new_comments = soar_api.filter_resilient_comments(incident_id, result['value'])

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult({ "value": new_comments }, success=status, reason=reason)
