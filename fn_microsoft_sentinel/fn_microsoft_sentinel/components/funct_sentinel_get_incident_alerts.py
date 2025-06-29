# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
"""Function implementation"""

from resilient_circuits import (AppFunctionComponent, FunctionResult, app_function)
from resilient_lib import validate_fields, str_to_bool
from fn_microsoft_sentinel.lib.function_common import (PACKAGE_NAME, SentinelProfiles)
from fn_microsoft_sentinel.lib.sentinel_common import SentinelAPI
from fn_microsoft_sentinel.lib.resilient_common import ResilientCommon

FN_NAME = "sentinel_get_incident_alerts"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'sentinel_get_incident_alerts''"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.sentinel_profiles = SentinelProfiles(opts, self.options)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get the alerts associated with a Sentinel Incident
        Inputs:
            -   fn_inputs.sentinel_profile
            -   fn_inputs.sentinel_label
            -   fn_inputs.sentinel_incident_id
            -   fn_inputs.soar_incident_id
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["sentinel_incident_id"], fn_inputs)

        # Get the function parameters:
        sentinel_incident_id = fn_inputs.sentinel_incident_id
        sentinel_profile = getattr(fn_inputs, "sentinel_profile", None)
        sentinel_label = getattr(fn_inputs, "sentinel_label", None)
        if not sentinel_profile and not sentinel_label:
            raise ValueError("Either sentinel_profile or sentinel_label need to be given.")

        self.LOG.info(f"Sentinel Incident ID: {sentinel_incident_id}")
        self.LOG.info(f"Sentinel Profile: {sentinel_profile}")
        self.LOG.info(f"Sentinel Label: {sentinel_label}")

        # Get the configuration for the selected Sentinel profile from the app.config
        profile_data = self.sentinel_profiles.get_profile(sentinel_label if sentinel_label else sentinel_profile)

        # Create connection to Sentinel
        sentinel_api = SentinelAPI(self.opts, self.options, profile_data if sentinel_label else None)

        # Read all alerts associated with a Sentinel incident
        result, status, reason = sentinel_api.get_incident_alerts(profile_data,
                                                                  sentinel_incident_id)

        # Clear Alerts data tables if clear_datatable setting is true in the app.config
        if str_to_bool(self.app_configs.get("clear_datatable", "false")):
            validate_fields(["soar_incident_id"], fn_inputs)
            ResilientCommon(self.rest_client()).clear_table("sentinel_incident_alerts", getattr(fn_inputs, "soar_incident_id", None))

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(result, success=status, reason=reason)
