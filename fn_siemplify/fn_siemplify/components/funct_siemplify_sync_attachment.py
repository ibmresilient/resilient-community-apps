# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""AppFunction implementation"""

import base64
from fn_siemplify.lib.siemplify_common import SiemplifyCommon, PACKAGE_NAME
from fn_siemplify.lib.resilient_common import ResilientCommon
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields

FN_NAME = "siemplify_sync_attachment"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'siemplify_sync_attachment'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Create a Siemplify Attachment from a SOAR Case Attachment
        Inputs:
            -   fn_inputs.siemplify_case_id
            -   fn_inputs.siemplify_alert_id
            -   fn_inputs.siemplify_incident_id
            -   fn_inputs.siemplify_attachment_id
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        validate_fields([
                {"name": "api_key"},
                {"name": "base_url"},
            ],
            self.app_configs._asdict())

        validate_fields([
                {"name": "siemplify_case_id"},
                {"name": "siemplify_alert_id"},
                {"name": "siemplify_attachment_id"}
            ],
            fn_inputs._asdict())

        # get the contents of the attachment
        res_common = ResilientCommon(self.rest_client())
        file_name, file_content = res_common.get_incident_attachment(fn_inputs.siemplify_incident_id,
                                                                   None,
                                                                   None,
                                                                   fn_inputs.siemplify_attachment_id)

        siemplify_env = SiemplifyCommon(self.rc, self.app_configs)
        results, error_msg = siemplify_env.sync_attachment(fn_inputs.siemplify_case_id,
                                                file_content, file_name)

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results, success=isinstance(error_msg, type(None)), reason=error_msg)
