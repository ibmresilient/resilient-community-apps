# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from fn_darktrace.lib.app_common import PACKAGE_NAME, AppCommon
from resilient_circuits import (AppFunctionComponent, FunctionResult,
                                app_function)
from resilient_lib import IntegrationError, validate_fields

FN_NAME = "darktrace_get_incident_group"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'darktrace_get_incident_group'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get the details of all the incident events of an AI Analyst Incident Group
        Inputs:
            -   fn_inputs.darktrace_incident_group_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        app_common = AppCommon(self.rc, self.options, self.opts.get("integrations", {}))

        validate_fields(["darktrace_incident_group_id"], fn_inputs)

        # group ID is required as that is needed to get incident event details
        group_id = fn_inputs.darktrace_incident_group_id.strip()

        incident_group = app_common.get_incident_groups({"includegroupurl": "true", "groupid": group_id})

        if len(incident_group) > 1:
            raise IntegrationError(f"Multiple groups found for group_id {group_id}")
        if len(incident_group) < 1:
            raise IntegrationError(f"No groups found for group_id {group_id}")
        incident_group = incident_group[0]

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        results = {"incident_group": incident_group}

        yield FunctionResult(results)
