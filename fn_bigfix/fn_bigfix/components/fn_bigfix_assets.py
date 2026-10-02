# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""AppFunction implementation"""

# Set up:
# Destination: a Queue named "bigfix_assets".
# Manual Action: Execute a REST query against a BigFix server return endpoint properties.

from datetime import datetime
from resilient_lib import validate_fields
from fn_bigfix.lib.bigfix_client import BigFixClient
from fn_bigfix.util.helpers import create_attachment, PACKAGE_NAME
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult

FN_NAME = "fn_bigfix_assets"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'fn_bigfix_assets' of package fn_bigfix."""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Resilient Function : Bigfix assets - Get properties in BigFix for an endpoint."""

        validate_fields(["bigfix_asset_name", "bigfix_asset_id", "bigfix_incident_id"], fn_inputs)

        params = {"asset_name": fn_inputs.bigfix_asset_name,
                  "asset_id": fn_inputs.bigfix_asset_id,
                  "incident_id": fn_inputs.bigfix_incident_id}

        self.LOG.info(str(params))

        yield self.status_message(f"Running BigFix Query for Endpoint id {params['asset_id']}, with name {params['asset_name']} ...")
        response = None

        try:
            # Perform the BigFix Query
            response = BigFixClient(self.opts, self.options).get_bf_computer_properties(params["asset_id"])
        except Exception as e:
            yield self.status_message(f"Failed with exception '{type(e).__name__}' while trying to query a BigFix asset")

        if not response:
            yield self.status_message(f"No properties retrieved for the asset id '{params['asset_id']}'")
            results = {}
        else:
            # Create a SOAR attachment
            file_name = f"bigfix-properties-{params['asset_name']}-{datetime.today().strftime('%Y%m%d')}.xml"
            att_report = create_attachment(self.rest_client(), file_name, response, params)
            results = {"status": "OK", "att_name": att_report.get("name")}

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(results)
