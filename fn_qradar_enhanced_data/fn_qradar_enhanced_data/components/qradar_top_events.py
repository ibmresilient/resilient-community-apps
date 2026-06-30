# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
"""AppFunction implementation"""

from re import IGNORECASE, search, sub
from time import time, sleep, time_ns
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
        try:
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
            qradar_label = getattr(fn_inputs, "qradar_label", None) # QRadar server to connect to
            soar_table_name = getattr(fn_inputs, "soar_table_name", None) # Name of data table
            soar_incident_id = getattr(fn_inputs, "soar_incident_id", None) # ID of incident

            # Log inputs
            self.LOG.info(str(fn_inputs))

            yield self.status_message(f"Starting App Function: '{FN_NAME}'")

            # Get global settings from the app.config
            global_settings = self.opts.get(GLOBAL_SETTINGS, {})
            # Get configuration for QRadar server specified
            options = get_server_settings(self.opts, qradar_label)
            # Create connection to QRadar server
            qradar_client = get_qradar_client(self.opts, options)
            # Get search_timeout from app.config or set it to default 600 seconds
            timeout = get_search_timeout(global_settings, options)

            # Collect the retry settings, if any
            empty_query_max = int(global_settings.get("empty_query_max", 1))
            empty_query_wait_secs = int(global_settings.get("empty_query_wait_secs", 0))
            empty_query_skip = [item.strip() for item in global_settings.get("empty_query_skip_types").split(',')] \
                if global_settings.get("empty_query_skip_types") else []
            # Result structure template
            results = {
                    "qrhost": options.get("host"),
                    "offenseid": qradar_search_param3,
                    "events": [], # Empty response
                    "current_time": 0
            }

            # Loop through the queries
            query_count = 0
            response = None
            while query_count < empty_query_max:
                temp_query_string, search_query_string = make_queries(qradar_fn_type,
                                                                    qradar_search_param1,
                                                                    qradar_search_param2,
                                                                    qradar_search_param3,
                                                                    qradar_search_param4,
                                                                    qradar_search_param5,
                                                                    qradar_search_param6,
                                                                    qradar_query)

                self.LOG.info(f"({query_count}) Running query: {temp_query_string}")
                response = qradar_client.ariel_graphql_search(temp_query_string, search_query_string, timeout=timeout)

                # A response means the query completed
                if response:
                    break

                # Skip retry?
                if qradar_fn_type in empty_query_skip or check_db_for_skip(qradar_query, empty_query_skip):
                    break

                # Continue through the loop if no response received
                query_count += 1
                self.LOG.info(f"Waiting {empty_query_wait_secs}s retry: {query_count} for: {qradar_fn_type}")
                sleep(empty_query_wait_secs)

            if not response:
                if query_count >= empty_query_max:
                    msg = f"Max queries: {query_count} returned no results for: {qradar_fn_type}"
                    self.LOG.warning(msg)
                    self.status_message(msg)
            else:
                # Enrich sourceip data by getting additional props using a graphql call to QRadar
                if qradar_fn_type == "sourceip" and response["events"]:
                    offense_source = qradar_client.graphql_query({"id": qradar_search_param3}, qradar_graphql_queries.GRAPHQL_OFFENSESOURCE, "sourceAddresses")

                    for event in response["events"]:
                        domain = list(filter(lambda x: x["sourceIp"] == event["sourceip"], offense_source["content"]))
                        event["domainid"] = domain[0]["domainId"] if len(domain) > 0 else 0 # Assign sourceip domain
                        data = qradar_client.graphql_query({"domainId": event["domainid"], "ipAddress": event["sourceip"]}, qradar_graphql_queries.GRAPHQL_SOURCEIP)
                        event["vulnerabilityCount"] = data["content"]["vulnerabilityCount"] if data["content"] else 0
                        event["macAddress"] = data["content"]["interfaces"][0]["macAddress"] if data["content"] and len(data["content"]["interfaces"]) > 0 and "macAddress" in data["content"]["interfaces"][0] else ""
                        event["network"] = data["content"]["interfaces"][0]["currentIpAddress"]["network"]["networkName"] if data["content"] and len(data["content"]["interfaces"]) > 0 and data["content"]["interfaces"][0]["currentIpAddress"] and data["content"]["interfaces"][0]["currentIpAddress"]["network"] else ""
                        event["domain"] = data["content"]["domain"]["name"] if data["content"] and data["content"]["domain"]["name"] else "Default Domain"

                response["events"] = list(map(lambda x: self.mapEventData(x), response["events"]))

                # Complete results to return
                results["events"] = response["events"]

            if results["events"]:
                # Clear specified data table in SOAR based on app.config settings
                clear_table(self.rest_client(), soar_table_name, soar_incident_id, global_settings)

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

            results["current_time"] = int(time())*1000
            function_result = FunctionResult(results)
            # Ensure backward compatibility with previous version of results
            for key, value in results.items():
                setattr(function_result, key, value)

            yield function_result
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))

    # Convert integers that are string to int type
    def mapEventData(self, event):
        for key in event.keys():
            if key in ["eventtime", "lastpackettime", "FirstPacketTime", "sourcebytes", "sourcepackets", "destinationbytes", "destinationpackets"]:
                event[key] = int(float(event[key]))

        return event

def check_db_for_skip(qradar_query, empty_query_skip):
    """
    The qradar_query contains the db to select from such as "SELECT %param1% FROM flows ..."
    This logic will match "FROM flows" with the empty_query_skill_types list in order to 
    bypass retry logic (if specified)

    :param qradar_query: query string
    :type qradar_query: str
    :param empty_query_skip: list of types to bypass: ['flows']
    :type empty_query_skip: list
    :return: True if query db is found in the empty_query_skip_types
    :rtype: boolean
    """
    b_skip = False
    query = qradar_query.lower().replace(' ', '') # Remove spaces to facilitate matching
    for skip_type in empty_query_skip:
        if f"from{skip_type}" in query:
            b_skip = True
            break

    return b_skip

def make_queries(qradar_fn_type,
                 qradar_search_param1,
                 qradar_search_param2,
                 qradar_search_param3,
                 qradar_search_param4,
                 qradar_search_param5,
                 qradar_search_param6,
                 qradar_query):
    """
    Build the queries used to populate the temporary table and to collect the results

    :param qradar_fn_type: 'flows', 'events', 'sourceip', 'destinationip'
    :param qradar_search_param1: the field names portion of the query
    :param qradar_search_param2: the 'where' portion of the query
    :param qradar_search_param3: the qradar_id to add to the query
    :param qradar_search_param4: the 'limit' or 'group by' portion
    :param qradar_search_param5: the 'order by' portion
    :param qradar_search_param6: the 'limit' portion, as needed (see param4)
    :param qradar_query: the 'select' portion of the query.
    :return: (temp_query, data_query)
    """

    # Build temp table name
    temp_table = f"offense-{qradar_search_param3}-events-{qradar_fn_type}-1000-{str(time_ns())}"

    qradar_temp_query = sub("FROM\s+{}".format(ARIEL_SEARCH_EVENTS if search(ARIEL_SEARCH_EVENTS,qradar_query, flags=IGNORECASE) else ARIEL_SEARCH_FLOWS),
                                "FROM {} INTO \"{}\"".format(ARIEL_SEARCH_EVENTS if search(ARIEL_SEARCH_EVENTS, qradar_query, flags=IGNORECASE) else ARIEL_SEARCH_FLOWS, temp_table),
                                qradar_query, flags=IGNORECASE)

    qradar_search_query = sub("FROM\s+{}".format(ARIEL_SEARCH_EVENTS if search(ARIEL_SEARCH_EVENTS,qradar_query, flags=IGNORECASE) else ARIEL_SEARCH_FLOWS),
                                    "FROM \"{}\"".format(temp_table), qradar_query, flags=IGNORECASE)

    # Temp table query
    temp_query_string = make_query_string(qradar_temp_query,
                                          ["*",
                                            qradar_search_param2,
                                            qradar_search_param3,
                                            " ",
                                            " ",
                                            " "])

    # Query against results in temp table
    search_query_string = make_query_string(qradar_search_query,
                                            [qradar_search_param1,
                                            " ",
                                            " ",
                                            qradar_search_param4 or " ",
                                            qradar_search_param5,
                                            qradar_search_param6])

    return temp_query_string, search_query_string
