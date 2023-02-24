# -*- coding: utf-8 -*-
# Generated with resilient-sdk v48.0.3934
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields
from fn_trusteer_ppd.lib.trusteer_ppd_client import TrusteerPPDClient, PACKAGE_NAME

FN_NAME = "trusteer_ppd_update_alert_classification"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'trusteer_ppd_update_alert_classification'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Update the alert classification in Trusteer to : confirmed_fraud, confirmed_legitimate, undetermined, or pending_confirmation.
        Inputs:
            -   fn_inputs.trusteer_ppd_session_id
            -   fn_inputs.trusteer_ppd_application_id
            -   fn_inputs.trusteer_ppd_classification
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["trusteer_ppd_session_id", "trusteer_ppd_application_id", "trusteer_ppd_classification"], fn_inputs)

        trusteer_ppd_client = TrusteerPPDClient(self.rc, self.PACKAGE_NAME, self.options)

        results = trusteer_ppd_client.update_classification(fn_inputs.trusteer_ppd_session_id,
                                                            fn_inputs.trusteer_ppd_application_id,
                                                            fn_inputs.trusteer_ppd_classification) 

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)

