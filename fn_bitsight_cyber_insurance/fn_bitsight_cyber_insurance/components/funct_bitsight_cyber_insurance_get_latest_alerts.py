# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# Generated with resilient-sdk v51.0.5.0.1475

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_bitsight_cyber_insurance.util.helper import bitsight_client, PACKAGE_NAME,\
    DEFAULT_LIMIT, DEFAULT_OFFSET, clear_datatable

FN_NAME = "bitsight_cyber_insurance_get_latest_alerts"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'bitsight_cyber_insurance_get_latest_alerts'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get alerts generated during the most recent daily platform update.
        Inputs:
            -   fn_inputs.bitsight_ci_severity
            -   fn_inputs.bitsight_ci_alert_type
            -   fn_inputs.bitsight_ci_company_guid
            -   fn_inputs.bitsight_ci_folder_guid
            -   fn_inputs.bitsight_ci_limit
            -   fn_inputs.bitsight_ci_offset
            -   fn_inputs.bitsight_ci_expand
            -   fn_inputs.bitsight_ci_clear_datatable
            -   fn_inputs.bitsight_ci_soar_incident_id
            -   fn_inputs.bitsight_ci_soar_datatable_name
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")
        try:
            # Make call to BitSight to get latest alerts.
            resp = bitsight_client(self.rc, self.options).get_latest_alerts(
                limit=fn_inputs.bitsight_ci_limit if getattr(fn_inputs, "bitsight_ci_limit", None) else DEFAULT_LIMIT,
                offset=fn_inputs.bitsight_ci_offset if getattr(fn_inputs, "bitsight_ci_offset", None) else DEFAULT_OFFSET,
                alert_type=fn_inputs.bitsight_ci_alert_type if getattr(fn_inputs, "bitsight_ci_alert_type", None) else None,
                company_guid=fn_inputs.bitsight_ci_company_guid.strip() if getattr(fn_inputs, "bitsight_ci_company_guid", None) else None,
                expand=fn_inputs.bitsight_ci_expand if getattr(fn_inputs, "bitsight_ci_expand", None) else None,
                folder_guid=fn_inputs.bitsight_ci_folder_guid.strip() if getattr(fn_inputs, "bitsight_ci_folder_guid", None) else None,
                severity=fn_inputs.bitsight_ci_severity if getattr(fn_inputs, "bitsight_ci_severity", None) else None
            )
            # Clear the data table before returning results if bitsight_ci_clear_datatable is True. Default is False
            if getattr(fn_inputs, "bitsight_ci_clear_datatable", False):
                if not getattr(fn_inputs, "bitsight_ci_soar_incident_id", None) and not getattr(fn_inputs, "bitsight_ci_soar_datatable_name", None):
                    raise ValueError("If bitsight_ci_clear_datatable is True then bitsight_ci_soar_incident_id and bitsight_ci_soar_datatable_name must be provided.")
                else:
                    clear_datatable(self.rest_client(), fn_inputs.bitsight_ci_soar_incident_id, fn_inputs.bitsight_ci_soar_datatable_name)

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

            yield FunctionResult(resp.get("results", []))
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
