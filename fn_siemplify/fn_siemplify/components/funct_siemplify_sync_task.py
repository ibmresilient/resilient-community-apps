# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""AppFunction implementation"""

from fn_siemplify.lib.soar_common import SOARCommon
from fn_siemplify.lib.siemplify_common import SiemplifyCommon, PACKAGE_NAME
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

FN_NAME = "siemplify_sync_task"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'siemplify_sync_task'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Sync a SOAR Task to Siemplify
        Inputs:
            -   fn_inputs.siemplify_case_id
            -   fn_inputs.siemplify_task_due_date
            -   fn_inputs.siemlify_task_assignee
            -   fn_inputs.siemplify_task_content
            -   fn_inputs.siemplify_task_name
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        fn_inputs_dict = fn_inputs._asdict()
        # validate app.config settings
        validate_fields([
                {"name": "api_key"},
                {"name": "base_url"}
            ],
            self.app_configs._asdict())

        validate_fields([
                {"name": "siemplify_case_id"},
                {"name": "siemplify_soar_task_id"}
            ],
            fn_inputs_dict)

        siemplify_env = SiemplifyCommon(self.rc, self.app_configs)

        # get the contents of the
        res_common = SOARCommon(self.rest_client())
        task_info, siemplify_task_id = res_common.get_incident_task(fn_inputs.siemplify_soar_task_id)

        results, error_msg = siemplify_env.sync_task(fn_inputs.siemplify_case_id, fn_inputs.siemplify_task_assignee,
                                                     siemplify_task_id, task_info)

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results, success=isinstance(error_msg, type(None)), reason=error_msg)
