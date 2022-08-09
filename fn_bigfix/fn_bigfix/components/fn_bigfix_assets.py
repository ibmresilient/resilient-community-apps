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
    """Component that implements SOAR function 'fn_bigfix_assets' of package fn_bigfix.

        The Function does a BigFix query to retrieve properties of a BigFix endpoint and takes the following
        parameters:

            bigfix_asset_name, bigfix_asset_id, bigfix_incident_id


        An example of a set of query parameter might look like the following:

                bigfix_asset_name
                bigfix_asset_id
                bigfix_incident_id

        The BigFix Query will execute a REST call against a Bigfix server and the Function returns a result
        in JSON format similar to the following.

            {'status': 'OK',
             'att_name': u'bigfix-properties-DESKTOP-TUKM3HF-20180718.xml'
            }
        The Function will also create an attachment with a name similar to following:
            bigfix-properties-DESKTOP-TUKM3HF-20180718.xml
    """

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.opts = opts
        self.options = opts.get("fn_bigfix", {})

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Resilient Function : Bigfix assets - Get properties in BigFix for an endpoint."""

        validate_fields(["bigfix_asset_name", "bigfix_asset_id",
                        "bigfix_incident_id"], fn_inputs)

        params = {"asset_name": fn_inputs.bigfix_asset_name,
                  "asset_id": fn_inputs.bigfix_asset_id, "incident_id": fn_inputs.bigfix_incident_id}

        self.LOG.info(str(params))

        yield self.status_message(u"Running BigFix Query for Endpoint id {}, with name {} ...".format(params["asset_id"], params["asset_name"]))
        bigfix_client = BigFixClient(self.opts, self.options)

        try:
            # Perform the BigFix Query
            response = bigfix_client.get_bf_computer_properties(
                params["asset_id"])
        except Exception as e:
            yield self.status_message("Failed with exception '{}' while trying to query a BigFix asset".format(type(e).__name__))

        results = {}
        if not response:
            yield self.status_message("No properties retrieved for the asset id '{}'".format(params["asset_id"]))
        else:
            # Create a SOAR attachment
            file_name = "bigfix-properties-{}-{}.xml".format(
                params["asset_name"], datetime.today().strftime('%Y%m%d'))
            att_report = create_attachment(
                self.rest_client(), file_name, response, params)
            results = {"status": "OK", "att_name": att_report["name"]}

        yield self.status_message("Finished running App Function: '{}'".format(FN_NAME))

        # Produce a FunctionResult with the results
        yield FunctionResult(results)
