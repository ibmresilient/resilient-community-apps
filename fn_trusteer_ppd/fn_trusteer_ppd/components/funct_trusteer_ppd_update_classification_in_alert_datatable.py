# -*- coding: utf-8 -*-
# Generated with resilient-sdk v48.0.3934
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_trusteer_ppd.lib.datatable_helper import TrusteerDatatable
from resilient_lib import IntegrationError, validate_fields

PACKAGE_NAME = "fn_trusteer_ppd"
FN_NAME = "trusteer_ppd_update_classification_in_alert_datatable"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'trusteer_ppd_update_classification_in_alert_datatable'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Update the Trusteer Alert data table Classification column for all rows with the same session ID.
        Inputs:
            -   fn_inputs.incident_id
            -   fn_inputs.trusteer_ppd_session_id
            -   fn_inputs.trusteer_ppd_classification
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["incident_id", "trusteer_ppd_session_id", "trusteer_ppd_classification"], fn_inputs)

        # Instantiate new Resilient API object
        res_client = self.rest_client()

        # Instantiate a new TrusteerDatatable
        datatable = TrusteerDatatable(res_client, fn_inputs.incident_id, "trusteer_ppd_dt_trusteer_alerts")

        # Get the data table data
        datatable.get_data()

        # Get rows with the specified Trusteer session ID.
        rows = datatable.get_rows(max_rows=0, sort_by=None, sort_direction="ASC", 
                                  search_column="trusteer_ppd_dt_session_id", 
                                  search_value=fn_inputs.trusteer_ppd_session_id)

        # For each row with the specified session ID, update the classification cell.
        for row in rows:
            cell_to_update = {"trusteer_ppd_dt_classification": fn_inputs.trusteer_ppd_classification}
            updated_row = datatable.update_row(row.get('id'), cell_to_update)

            if "error" in updated_row:
                raise IntegrationError("Row in Trusteer Alerts data table NOT updated.")

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        results = {"num_rows_updated": len(rows)}

        yield FunctionResult(results)

