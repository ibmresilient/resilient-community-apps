# -*- coding: utf-8 -*-
#
# (c) Copyright IBM Corp. 2022. All Rights Reserved.
#
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from time import time
from logging import getLogger
from urllib.parse import quote
from resilient_lib import validate_fields
from fn_qradar_enhanced_data.util.function_utils import clear_table
from fn_qradar_enhanced_data.util.qradar_constants import GLOBAL_SETTINGS
from fn_qradar_enhanced_data.util.qradar_utils import QRadarServers, AuthInfo
import fn_qradar_enhanced_data.util.qradar_graphql_queries as qradar_graphql_queries
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

#For a given Offense ID and QRadar Destination, get the offense summary.

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'qradar_offense_summary"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.global_settings = opts.get(GLOBAL_SETTINGS, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.global_settings = opts.get(GLOBAL_SETTINGS, {})

    @function("qradar_offense_summary")
    def _qradar_offense_summary(self, event, *args, **kwargs):
        """Function: QRadar Offense "summary"""
        log = getLogger(__name__)
        try:
            validate_fields(["qradar_query_type","qradar_offense_id"], kwargs)
            # Get the function parameters:
            qradar_offenseid = kwargs.get("qradar_offense_id")  # QRadar Offense ID
            qradar_fn_type = kwargs.get("qradar_query_type")  # Function type based on the datatable/fields to populate
            qradar_label = kwargs.get("qradar_label") # QRadar server to connect to
            soar_table_name = kwargs.get("soar_table_name", None) # Name of data table
            soar_incident_id = kwargs.get("soar_incident_id") # ID of incident

            log.info("qradar_offenseid: %s", qradar_offenseid)
            log.info("qradar_label: %s", qradar_label)

            # Get the wf_instance_id of the workflow this Function was called in, if not found return a backup string
            wf_instance_id = event.message.get("workflow_instance", {}).get("workflow_instance_id", "no instance id found")
            yield StatusMessage("Starting 'qradar_offense_summary' that was running in workflow '{0}'".format(wf_instance_id))

            # Get qradar_client and options
            qradar_client, options = QRadarServers.get_qradar_client(self.opts, qradar_label)

            if soar_table_name:
                if self.global_settings:
                    # If clear_datatables in app.config equals True then clear given data table
                    # If clear_datatables does not exist then it defaults to True
                    if self.global_settings.get("clear_datatables", True) == True:
                        clear_table(self.rest_client(), soar_table_name, soar_incident_id)
                else: # If global_settings does not exist then clear given data table
                    clear_table(self.rest_client(), soar_table_name, soar_incident_id)

            results = {
                "qrhost": options.get("host"),
                "offenseid": qradar_offenseid,
                "received_time": int(time())*1000
            }

            # Fetch the Offense Summary if function type is OFFENSE_SUMMARY
            if qradar_fn_type == "offensesummary":

                offense_summary = qradar_client.graphql_query({"id": qradar_offenseid}, qradar_graphql_queries.GRAPHQL_OFFENSEQUERY)
                results["offense"] = offense_summary["content"]

            elif qradar_fn_type == "offensetime":
                fields = quote("id, last_persisted_time")
                filters = quote("id={}".format(qradar_offenseid))
                auth_info = AuthInfo.get_authInfo()
                # Create url to get all offenses in SOAR from the given QRadar server
                url = auth_info.api_url + "siem/offenses?fields={}&filter={}".format(fields, filters)
                response = auth_info.make_call("GET", url)
                for content in response.json():
                    results["last_persisted_time"] = content["last_persisted_time"]

            # Fetch the Contributing Rules if function type is OFFENSE_RULES
            elif qradar_fn_type == "offenserules":

                rules_data = qradar_client.graphql_query({"id": qradar_offenseid}, qradar_graphql_queries.GRAPHQL_RULESQUERY)
                rules_data = rules_data["content"]["rules"]
                results["rules_data"] = rules_data

            # Fetch the Assets Info if function type is OFFENSE_ASSETS
            elif qradar_fn_type == "offenseassets":

                # Get all sources for the given Offense ID
                offense_source = qradar_client.graphql_query({"id":qradar_offenseid}, qradar_graphql_queries.GRAPHQL_OFFENSESOURCE, "sourceAddresses")
                results["assets"] = []

                # Get Asset Info for each source
                for source in offense_source["content"]:
                    variables = {"domainId": source["domainId"], "ipAddress":  source["sourceIp"]}
                    offense_assets = qradar_client.graphql_query(variables, qradar_graphql_queries.GRAPHQL_OFFENSEASSETS)["content"]

                    if offense_assets:
                        offense_assets["sourceip"] = source["sourceIp"]
                        # Sorting the asset users list based on the last seen time
                        offense_assets["users"].sort(key=lambda x:int(x["lastSeenProfiler"]), reverse=True)

                        # Get the Operating System ID for the Asset
                        asset_prop = list(filter(lambda x:x["propertyType"]["name"] == "Primary OS ID",
                                                 offense_assets["properties"]))
                        offense_assets["osid"] = asset_prop[0]["value"] if len(asset_prop)>0 else ""

                        # Get the Unified Name for the Asset
                        asset_prop = list(filter(lambda x: x["propertyType"]["name"] == "Unified Name",
                                                 offense_assets["properties"]))
                        offense_assets["name"] = asset_prop[0]["value"] if len(asset_prop) > 0 else ""
                        results["assets"].append(offense_assets)

            yield StatusMessage("Finished 'qradar_offense_summary' that was running in workflow '{0}'".format(wf_instance_id))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            log.error(str(e))
            yield FunctionError()
