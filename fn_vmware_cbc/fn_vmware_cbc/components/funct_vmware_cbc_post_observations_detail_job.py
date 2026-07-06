# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v52.0.0.0.927

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_vmware_cbc.lib.app_common import AppCommon

PACKAGE_NAME = "fn_vmware_cbc"
FN_NAME = "vmware_cbc_post_observations_detail_job"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'vmware_cbc_post_observations_detail_job'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Creates an Observations details job. The details will include information about the given event that’s not normally accessible during a search.
        Inputs:
            -   fn_inputs.vmware_cbc_observations
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["vmware_cbc_observations"], fn_inputs)

        app_common = AppCommon(PACKAGE_NAME, self.options)

        results, error_msg = app_common.post_observation_details(fn_inputs.vmware_cbc_observations)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results, success=False if error_msg else True, reason=error_msg)