# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from fn_darktrace.lib.app_common import PACKAGE_NAME, AppCommon
from resilient_circuits import (AppFunctionComponent, FunctionResult,
                                app_function)
from resilient_lib import IntegrationError, validate_fields

FN_NAME = "darktrace_get_devices"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'darktrace_get_devices'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get the details of all the devices of an AI Analyst Incident
        Inputs:
            -   fn_inputs.darktrace_incident_group_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        app_common = AppCommon(self.rc, self.options, self.opts.get("integrations", {}))

        validate_fields(["darktrace_incident_group_id"], fn_inputs)

        # query group details for "devices" list
        group_id = fn_inputs.darktrace_incident_group_id
        group = app_common.get_incident_groups({"groupid": group_id})
        # NOTE: this endpoint returns a list, but with groupid set to one ID
        # it will return only one incident
        if len(group) > 1:
            raise IntegrationError(f"Multiple incidents found for group_id {group_id}")
        if len(group) < 1:
            raise IntegrationError(f"No incidents found for group_id {group_id}")
        group = group[0]

        # NOTE: the endpoint allows for comma-separated list of did's
        # but will only return a list if there is at least a comma in there -- thus we
        # need to include the last comma there otherwise if there was only one device
        # we'd get a dict result rather than a list
        query = {"did": ",".join(map(str, group.get("devices", []))) + ",", "includetags": "true"}
        devices_details = app_common.get_devices(query)

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        results = {
            "devices": devices_details, 
            "base_device_url": f"{app_common.base_url.rstrip('/')}/#device/"
        }

        yield FunctionResult(results)
