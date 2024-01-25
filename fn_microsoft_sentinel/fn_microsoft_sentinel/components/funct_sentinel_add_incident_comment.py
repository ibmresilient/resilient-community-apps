# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
"""Function implementation"""

from resilient_circuits import (AppFunctionComponent, FunctionResult,
                                app_function)
from resilient_lib import clean_html, validate_fields

from fn_microsoft_sentinel.lib.constants import (FROM_SENTINEL_COMMENT_HDR,
                                                 SENT_TO_SENTINEL_HDR)
from fn_microsoft_sentinel.lib.function_common import (PACKAGE_NAME,
                                                       SentinelProfiles)
from fn_microsoft_sentinel.lib.sentinel_common import SentinelAPI

FN_NAME = "sentinel_add_incident_comment"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'sentinel_add_incident_comment''"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.sentinel_profiles = SentinelProfiles(opts, self.options)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Create a comment for a given Sentinel incident
        Inputs:
            -   fn_inputs.sentinel_profile
            -   fn_inputs.sentinel_incident_id
            -   fn_inputs.sentinel_incident_comment
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")
        validate_fields(
            ["sentinel_profile", "sentinel_incident_id", "sentinel_incident_comment"],
            fn_inputs
        )

        # Get the function parameters:
        sentinel_profile = fn_inputs.sentinel_profile
        sentinel_incident_id = fn_inputs.sentinel_incident_id
        sentinel_incident_comment = fn_inputs.sentinel_incident_comment

        self.LOG.info(f"sentinel_profile: {sentinel_profile}")
        self.LOG.info(f"sentinel_incident_id: {sentinel_incident_id}")
        self.LOG.info(f"sentinel_incident_comment: {sentinel_incident_comment}")

        sentinel_api = SentinelAPI(self.opts, self.options)

        # Do not resync comments originating from Sentinel
        if FROM_SENTINEL_COMMENT_HDR in sentinel_incident_comment or SENT_TO_SENTINEL_HDR in sentinel_incident_comment:
            yield self.status_message(f"Bypassing synchronization of note: {sentinel_incident_comment}")
            result = {}
            reason = None
            status = False
        else:
            profile_data = self.sentinel_profiles.get_profile(sentinel_profile)
            result, status, reason = sentinel_api.create_comment(profile_data,
                                                                sentinel_incident_id,
                                                                clean_html(sentinel_incident_comment))
            if status:
                yield self.status_message(f"Sentinel comment added to incident: {sentinel_incident_id}")
            else:
                yield self.status_message(f"Sentinel comment failure for incident {sentinel_incident_id}: {reason}")

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(result, success=status, reason=reason)
