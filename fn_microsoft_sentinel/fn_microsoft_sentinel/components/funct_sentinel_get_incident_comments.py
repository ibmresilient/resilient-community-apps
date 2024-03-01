# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
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
    """Component that implements SAOR function 'sentinel_get_incident_comments''"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.sentinel_profiles = SentinelProfiles(opts, self.options)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get Comments from a Sentinel Incident
        Inputs:
            -   fn_inputs.sentinel_profile
            -   fn_inputs.sentinel_incident_id
            -   fn_inputs.incident_id
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")
        validate_fields(["sentinel_profile", "sentinel_incident_id"], fn_inputs)

        # Get the function parameters:
        incident_id = fn_inputs.incident_id
        sentinel_incident_id = fn_inputs.sentinel_incident_id
        sentinel_profile = fn_inputs.sentinel_profile

        self.LOG.info(f"incident_id: {incident_id}")
        self.LOG.info(f"sentinel_incident_id: {sentinel_incident_id}")
        self.LOG.info(f"sentinel_profile: {sentinel_profile}")

        sentinel_api = SentinelAPI(self.opts, self.options)

        soar_api = ResilientCommon(self.rest_client())

        profile_data = self.sentinel_profiles.get_profile(sentinel_profile)
        result, status, reason = sentinel_api.get_comments(profile_data, sentinel_incident_id)

        new_comments = []
        if status:
            new_comments = soar_api.filter_resilient_comments(incident_id, result['value'])

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult({ "value": new_comments }, success=status, reason=reason)
