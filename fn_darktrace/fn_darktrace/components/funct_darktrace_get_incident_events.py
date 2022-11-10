# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from fn_darktrace.lib.app_common import PACKAGE_NAME, AppCommon
from resilient_circuits import (AppFunctionComponent, FunctionResult,
                                app_function)
from resilient_lib import validate_fields

FN_NAME = "darktrace_get_incident_events"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'darktrace_get_incident_events'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get the details of all the incident events of an AI Analyst Incident Group
        Inputs:
            -   fn_inputs.darktrace_incident_group_id
            -   fn_inputs.darktrace_include_model_breach_data
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        app_common = AppCommon(self.rc, self.options, self.opts.get("integrations", {}))

        validate_fields(["darktrace_incident_group_id"], fn_inputs)

        # group ID is required as that is needed to get incident event details
        group_id = fn_inputs.darktrace_incident_group_id
        # model breach data is only included if requested by the playbook/workflow
        include_model_breach = getattr(fn_inputs, "darktrace_include_model_breach_data", False)

        # get baseline incident event data for events in the group
        incident_events = app_common.get_incident_events(group_id=group_id)

        if include_model_breach:
            # gather detailed data on each model breach associated with the event if requested
            for event in incident_events:
                for breach in event.get("relatedBreaches"):
                    pbid = breach.get("pbid")
                    query = {
                        "pbid": pbid,
                        "includeacknowledged": "true",
                        "expandenums": "true",
                        "includebreachurl": "true"
                    }
                    model_breach_details = app_common.get_model_breaches(query)
                    breach.update(model_breach_details)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        results = {
            "incident_events": incident_events,
            "base_model_breach_url": f"{app_common.base_url.rstrip('/')}/#modelbreach/"
        }

        yield FunctionResult(results)
