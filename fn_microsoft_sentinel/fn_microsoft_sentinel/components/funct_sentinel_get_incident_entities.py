# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""Function implementation"""

from resilient_circuits import (AppFunctionComponent, FunctionResult,
                                app_function)
from resilient_lib import validate_fields

from fn_microsoft_sentinel.lib.function_common import (PACKAGE_NAME,
                                                       SentinelProfiles)
from fn_microsoft_sentinel.lib.sentinel_common import SentinelAPI

FN_NAME = "sentinel_get_incident_entities"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'sentinel_get_incident_entities''"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.sentinel_profiles = SentinelProfiles(opts, self.options)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get the Entities associated with a Sentinel Incident
        Inputs:
            -   fn_inputs.sentinel_profile
            -   fn_inputs.sentinel_incident_id
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")
        validate_fields(["sentinel_profile", "sentinel_incident_id"], fn_inputs)

        # Get the function parameters:
        sentinel_incident_id = fn_inputs.sentinel_incident_id
        sentinel_profile = fn_inputs.sentinel_profile

        self.LOG.info(f"sentinel_incident_id: {sentinel_incident_id}")
        self.LOG.info(f"sentinel_profile: {sentinel_profile}")

        # Create connection to Sentinel
        sentinel_api = SentinelAPI(self.opts, self.options)

        # Get the configuration for the selected Sentinel profile from the app.config
        profile_data = self.sentinel_profiles.get_profile(sentinel_profile)
        # Read all entities associated with a Sentinel incident
        result, status, reason = sentinel_api.get_incident_entities(profile_data,
                                                                    sentinel_incident_id)

        # Iterate over the alerts and get all the entities
        entities = {}
        if status:
            for alert in result['value']:
                self.LOG.debug(f"Alert: {alert['name']}")
                entity_result, entity_status, entity_reason = \
                    sentinel_api.get_incident_alert_entities(alert['properties']['relatedResourceId'])
                # Organize entities using the key of the alert_id
                if entity_status:
                    entities[alert['name']] = entity_result['value']['entities']
                else:
                    reason = entity_reason

        # Produce a FunctionResult with the results
        yield FunctionResult(entities, success=status, reason=reason)
