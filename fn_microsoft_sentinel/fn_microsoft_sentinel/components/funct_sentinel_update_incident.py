# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""Function implementation"""

from resilient_circuits import (AppFunctionComponent, FunctionResult,
                                app_function)
from resilient_lib import validate_fields

from fn_microsoft_sentinel.lib.resilient_common import ResilientCommon
from fn_microsoft_sentinel.lib.constants import SENTINEL_INCIDENT_NUMBER
from fn_microsoft_sentinel.lib.function_common import (
    DEFAULT_SENTINEL_CLOSE_INCIDENT_TEMPLATE,
    DEFAULT_SENTINEL_UPDATE_INCIDENT_TEMPLATE, PACKAGE_NAME, SentinelProfiles)
from fn_microsoft_sentinel.lib.jinja_common import JinjaEnvironment
from fn_microsoft_sentinel.lib.sentinel_common import SentinelAPI

FN_NAME = "sentinel_update_incident"

class FunctionComponent(AppFunctionComponent):
    """ This component handles initial population of a feed and ongoing
    modifications from the associated queue. """

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.sentinel_profiles = SentinelProfiles(opts, self.options)
        self.jinja_env = JinjaEnvironment()

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Updates Sentinel incident when linked SOAR incident is updated.
        Inputs:
            -   fn_inputs.incident_id
            -   fn_inputs.sentinel_incident_id
            -   fn_inputs.sentinel_profile
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Verify we have the required inputs
        validate_fields(["incident_id", "sentinel_profile", "sentinel_incident_id"], fn_inputs)

        # Create variables for inputs
        incident_id = fn_inputs.incident_id
        sentinel_incident_id = fn_inputs.sentinel_incident_id
        sentinel_profile = fn_inputs.sentinel_profile

        # Log inputs
        self.LOG.info(f"Incident ID: {incident_id}")
        self.LOG.info(f"Sentinel Incident ID: {sentinel_incident_id}")
        self.LOG.info(f"Sentinel Profile: {sentinel_profile}")

        # Get the SOAR incident data
        soar_incident = ResilientCommon(self.rest_client()).get_soar_incident(incident_id)

        # Confirm that we have custom fields
        for confirm_field in ["sentinel_profile", SENTINEL_INCIDENT_NUMBER]:
            if not soar_incident['properties'].get(confirm_field):
                raise ValueError(f"Custom field: {confirm_field} and/or value not found.")

        # Create connection to Sentinel
        sentinel_api = SentinelAPI(self.opts, self.options)

        # Get the configuration for the selected Sentinel profile from the app.config
        profile_data = self.sentinel_profiles.get_profile(sentinel_profile)

        # Is this SOAR incident active or closed?
        if soar_incident["plan_status"] == "A":
            template = profile_data.get("sentinel_update_incident_template")
            default_template = DEFAULT_SENTINEL_UPDATE_INCIDENT_TEMPLATE
        else:
            template = profile_data.get("sentinel_close_incident_template")
            default_template = DEFAULT_SENTINEL_CLOSE_INCIDENT_TEMPLATE

        incident_payload = self.jinja_env.make_payload_from_template(
            template,
            default_template,
            soar_incident
        )

        result, status, reason = sentinel_api.create_update_incident(
            profile_data,
            sentinel_incident_id,
            incident_payload
        )

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(result, success=status, reason=reason)
