# -*- coding: utf-8 -*-
# Generated with resilient-sdk v48.0.3934
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields
from fn_trusteer_ppd.lib.app_common import AppCommon, PACKAGE_NAME
from fn_trusteer_ppd.lib.configure_tab import init_trusteer_ppd_tab

PACKAGE_NAME = "fn_trusteer_ppd"
FN_NAME = "trusteer_ppd_update_case"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'trusteer_ppd_update_case'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

        # Initialize the Trusteer tab
        init_trusteer_ppd_tab()

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Update the Trusteer Pinpoint Detect custom fields in SOAR.
        Inputs:
            -   fn_inputs.trusteer_ppd_puid
        """

        validate_fields(["trusteer_ppd_puid"], fn_inputs)

        app_common = AppCommon(self.PACKAGE_NAME, self.options)

        link_url = app_common.make_linkback_url(fn_inputs.trusteer_ppd_puid)

        results = {"link_url": link_url}

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)
