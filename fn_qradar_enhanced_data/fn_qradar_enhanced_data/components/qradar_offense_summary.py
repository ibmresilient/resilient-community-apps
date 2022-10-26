# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from time import time
from resilient_lib import validate_fields
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_qradar_enhanced_data.util.qradar_constants import GLOBAL_SETTINGS, PACKAGE_NAME
import fn_qradar_enhanced_data.util.qradar_graphql_queries as qradar_graphql_queries
from fn_qradar_enhanced_data.util.function_utils import clear_table, get_qradar_client, get_server_settings

FN_NAME = "qradar_offense_summary"

#For a given Offense ID and QRadar Destination, get the offense summary.
class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'qradar_offense_summary"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Fetch QRadar Offense Details
        Inputs:
            -   fn_inputs.qradar_label
            -   fn_inputs.qradar_offense_id
            -   fn_inputs.soar_table_name
            -   fn_inputs.soar_incident_id
            -   fn_inputs.qradar_query_type
        """

        # Validate required parameters
        validate_fields(["qradar_query_type", "qradar_offense_id"], fn_inputs)

        # Get the function parameters:
        qradar_offenseid = fn_inputs.qradar_offense_id # QRadar Offense ID
        qradar_fn_type = fn_inputs.qradar_query_type # Function type based on the datatable/fields to populate
        qradar_label = getattr(fn_inputs, "qradar_label", None) # QRadar server to connect to
        soar_table_name = getattr(fn_inputs, "soar_table_name", None) # Name of data table
        soar_incident_id = getattr(fn_inputs, "soar_incident_id", None) # ID of incident

        self.LOG.info(f"qradar_offenseid: {qradar_offenseid}")
        self.LOG.info(f"qradar_label: {qradar_label}")

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Get global settings from the app.config
        global_settings = self.opts.get(GLOBAL_SETTINGS, {})
        # Get configuration for QRadar server specified
        options = get_server_settings(self.opts, qradar_label)
        # Create connection to QRadar server
        qradar_client = get_qradar_client(self.opts, options)

        results = {
            "qrhost": options.get("host"),
            "offenseid": qradar_offenseid,
            "current_time": int(time())*1000
        }

        # Fetch the Offense Summary if function type is OFFENSE_SUMMARY
        if qradar_fn_type == "offensesummary":
            offense_summary = qradar_client.graphql_query({"id": qradar_offenseid}, qradar_graphql_queries.GRAPHQL_OFFENSEQUERY)
            results["offense"] = offense_summary["content"]

        # Fetch the Contributing Rules if function type is OFFENSE_RULES
        elif qradar_fn_type == "offenserules":
            rules_data = qradar_client.graphql_query({"id": qradar_offenseid}, qradar_graphql_queries.GRAPHQL_RULESQUERY)
            rules_data = rules_data["content"]["rules"]
            results["rules_data"] = rules_data

        # Fetch the Assets Info if function type is OFFENSE_ASSETS
        elif qradar_fn_type == "offenseassets":
            # Get all sources for the given Offense ID
            offense_source = qradar_client.graphql_query({"id": qradar_offenseid}, qradar_graphql_queries.GRAPHQL_OFFENSESOURCE, "sourceAddresses")
            results["assets"] = []

            # Get Asset Info for each source
            for source in offense_source["content"]:
                variables = {"domainId": source["domainId"], "ipAddress": source["sourceIp"]}
                offense_assets = qradar_client.graphql_query(variables, qradar_graphql_queries.GRAPHQL_OFFENSEASSETS)["content"]

                if offense_assets:
                    offense_assets["sourceip"] = source["sourceIp"]
                    # Sorting the asset users list based on the last seen time
                    offense_assets["users"].sort(key = lambda x: int(x["lastSeenProfiler"]), reverse=True)

                    # Get the Operating System ID for the Asset
                    asset_prop = list(filter(lambda x: x["propertyType"]["name"] == "Primary OS ID",
                                                offense_assets["properties"]))
                    offense_assets["osid"] = asset_prop[0]["value"] if len(asset_prop) > 0 else ""

                    # Get the Unified Name for the Asset
                    asset_prop = list(filter(lambda x: x["propertyType"]["name"] == "Unified Name",
                                                offense_assets["properties"]))
                    offense_assets["name"] = asset_prop[0]["value"] if len(asset_prop) > 0 else ""
                    results["assets"].append(offense_assets)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        if results:
            # Clear specified data table in SOAR based on app.config settings
            clear_table(self.rest_client(), soar_table_name, soar_incident_id, global_settings)

        # Produce a FunctionResult with the results
        yield FunctionResult(results)
