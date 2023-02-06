# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""AppFunction implementation"""

from re import IGNORECASE, search, sub
from time import time
from resilient_circuits import (AppFunctionComponent, FunctionResult, app_function)
from resilient_lib import validate_fields
import fn_qradar_enhanced_data.util.qradar_graphql_queries as qradar_graphql_queries
from fn_qradar_enhanced_data.util.function_utils import (clear_table, get_qradar_client, get_search_timeout, get_server_settings, make_query_string)
from fn_qradar_enhanced_data.util.qradar_constants import (ARIEL_SEARCH_EVENTS, ARIEL_SEARCH_FLOWS, GLOBAL_SETTINGS, PACKAGE_NAME)

FN_NAME = "qradar_top_events"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'qradar_top_events"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: QRadar Top Events
        Inputs:
            -   fn_inputs.qradar_label
            -   fn_inputs.soar_table_name
            -   fn_inputs.soar_incident_id
            -   fn_inputs.qradar_query_type
            -   fn_inputs.qradar_query
            -   fn_inputs.qradar_search_param1
            -   fn_inputs.qradar_search_param2
            -   fn_inputs.qradar_search_param3
            -   fn_inputs.qradar_search_param4
            -   fn_inputs.qradar_search_param5
            -   fn_inputs.qradar_search_param6
            -   fn_inputs.qradar_search_param7
        """

        # Validate required parameters
        validate_fields(["qradar_query_type", "qradar_query"], fn_inputs)

        # Get the function parameters:
        qradar_query = self.get_textarea_param(fn_inputs.qradar_query) # textarea
        qradar_fn_type = fn_inputs.qradar_query_type # text
        qradar_search_param1 = getattr(fn_inputs, "qradar_search_param1", None) # text
        qradar_search_param2 = getattr(fn_inputs, "qradar_search_param2", None) # text
        qradar_search_param3 = getattr(fn_inputs, "qradar_search_param3", None) # text
        qradar_search_param4 = getattr(fn_inputs, "qradar_search_param4", None) # text
        qradar_search_param5 = getattr(fn_inputs, "qradar_search_param5", None) # text
        qradar_search_param6 = getattr(fn_inputs, "qradar_search_param6", None) # text
        qradar_search_time = getattr(fn_inputs, "qradar_search_param7", None) # text, time to search example: 36 Days
        qradar_label = getattr(fn_inputs, "qradar_label", None) # QRadar server to connect to
        soar_table_name = getattr(fn_inputs, "soar_table_name", None) # Name of data table
        soar_incident_id = getattr(fn_inputs, "soar_incident_id", None) # ID of incident

        # Log inputs
        self.LOG.info(str(fn_inputs))

        # Get global settings from the app.config
        global_settings = self.opts.get(GLOBAL_SETTINGS, {})
        # Get configuration for QRadar server specified
        options = get_server_settings(self.opts, qradar_label)
        # Create connection to QRadar server
        qradar_client = get_qradar_client(self.opts, options)
        # Get search_timeout from app.config or set it to default 600 seconds
        timeout = get_search_timeout(global_settings, options)

        temp_table = f"offense-{qradar_search_param3}-events-{qradar_fn_type}-1000-{str(time())}"

        qradar_temp_query = sub("FROM\s+{}".format(ARIEL_SEARCH_EVENTS if search(ARIEL_SEARCH_EVENTS,qradar_query, flags=IGNORECASE) else ARIEL_SEARCH_FLOWS),
                                    "FROM {} INTO \"{}\"".format(ARIEL_SEARCH_EVENTS if search(ARIEL_SEARCH_EVENTS, qradar_query, flags=IGNORECASE) else ARIEL_SEARCH_FLOWS, temp_table),
                                    qradar_query, flags=IGNORECASE)

        qradar_search_query = sub("FROM\s+{}".format(ARIEL_SEARCH_EVENTS if search(ARIEL_SEARCH_EVENTS,qradar_query, flags=IGNORECASE) else ARIEL_SEARCH_FLOWS),
                                        "FROM \"{}\"".format(temp_table), qradar_query, flags=IGNORECASE)

        temp_query_string = make_query_string(qradar_temp_query,
                                                ["*",
                                                qradar_search_param2,
                                                qradar_search_param3,
                                                " ",
                                                " ",
                                                " ",
                                                qradar_search_time])

        search_query_string = make_query_string(qradar_search_query,
                                                [qradar_search_param1,
                                                " ",
                                                " ",
                                                qradar_search_param4 or " ",
                                                qradar_search_param5,
                                                qradar_search_param6,
                                                qradar_search_time])

        self.LOG.info(f"Running query: {temp_query_string}")

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        result = qradar_client.ariel_graphql_search(temp_query_string, search_query_string, timeout=timeout)

        # Enrich sourceip data by getting additional props using a graphql call to QRadar
        if qradar_fn_type == "sourceip":

            offense_source = qradar_client.graphql_query({"id": qradar_search_param3}, qradar_graphql_queries.GRAPHQL_OFFENSESOURCE, "sourceAddresses")

            for event in result["events"]:
                domain = list(filter(lambda x: x["sourceIp"] == event["sourceip"], offense_source["content"]))
                event["domainid"] = domain[0]["domainId"] if len(domain) > 0 else 0 # Assign sourceip domain
                data = qradar_client.graphql_query({"domainId": event["domainid"], "ipAddress": event["sourceip"]}, qradar_graphql_queries.GRAPHQL_SOURCEIP)
                event["vulnerabilityCount"] = data["content"]["vulnerabilityCount"] if data["content"] else 0
                event["macAddress"] = data["content"]["interfaces"][0]["macAddress"] if data["content"] and len(data["content"]["interfaces"]) > 0 and "macAddress" in data["content"]["interfaces"][0] else ""
                event["network"] = data["content"]["interfaces"][0]["currentIpAddress"]["network"]["networkName"] if data["content"] and len(data["content"]["interfaces"]) > 0 and data["content"]["interfaces"][0]["currentIpAddress"] and data["content"]["interfaces"][0]["currentIpAddress"]["network"] else ""
                event["domain"] = data["content"]["domain"]["name"] if data["content"] and data["content"]["domain"]["name"] else "Default Domain"

        result["events"] = list(map(lambda x: self.mapEventData(x), result["events"]))

        results = {
            "qrhost": options.get("host"),
            "offenseid": qradar_search_param3,
            "events": result["events"],
            "current_time": int(time())*1000
        }

        if results:
            # Clear specified data table in SOAR based on app.config settings
            clear_table(self.rest_client(), soar_table_name, soar_incident_id, global_settings)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")
        yield FunctionResult(results)

    # Convert integers that are string to int type
    def mapEventData(self, event):
        for key in event.keys():
            if key in ["eventtime", "lastpackettime", "FirstPacketTime", "sourcebytes", "sourcepackets", "destinationbytes", "destinationpackets"]:
                event[key] = int(float(event[key]))

        return event
