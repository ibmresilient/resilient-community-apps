# -*- coding: utf-8 -*-
#
# (c) Copyright IBM Corp. 2022. All Rights Reserved.
#
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from time import time
from logging import getLogger
from re import sub, search, IGNORECASE
from resilient_lib import validate_fields
import fn_qradar_enhanced_data.util.qradar_graphql_queries as qradar_graphql_queries
from fn_qradar_enhanced_data.util.qradar_constants import ARIEL_SEARCH_EVENTS, ARIEL_SEARCH_FLOWS, GLOBAL_SETTINGS
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_qradar_enhanced_data.util.function_utils import make_query_string, clear_table, get_server_settings, get_qradar_client

LOG = getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'qradar_top_events"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts

    @function("qradar_top_events")
    def _qradar_top_events(self, event, *args, **kwargs):
        """Function: QRadar Top Events"""

        try:
            validate_fields(["qradar_query_type", "qradar_query"], kwargs)
            # Get the function parameters:
            qradar_query = self.get_textarea_param(kwargs.get("qradar_query"))  # textarea
            qradar_fn_type = kwargs.get("qradar_query_type")  # text
            qradar_search_param1 = kwargs.get("qradar_search_param1")  # text
            qradar_search_param2 = kwargs.get("qradar_search_param2")  # text
            qradar_search_param3 = kwargs.get("qradar_search_param3")  # text
            qradar_search_param4 = kwargs.get("qradar_search_param4")  # text
            qradar_search_param5 = kwargs.get("qradar_search_param5")  # text
            qradar_search_param6 = kwargs.get("qradar_search_param6")  # text
            qradar_label = kwargs.get("qradar_label") # QRadar server to connect to
            soar_table_name = kwargs.get("soar_table_name", None) # Name of data table
            soar_incident_id = kwargs.get("soar_incident_id") # ID of incident

            LOG.info("qradar_query: %s", qradar_query)
            LOG.info("qradar_search_param1: %s", qradar_search_param1)
            LOG.info("qradar_search_param2: %s", qradar_search_param2)
            LOG.info("qradar_search_param3: %s", qradar_search_param3)
            LOG.info("qradar_search_param4: %s", qradar_search_param4)
            LOG.info("qradar_search_param5: %s", qradar_search_param5)
            LOG.info("qradar_search_param6: %s", qradar_search_param6)
            LOG.info("qradar_label: %s", qradar_label)

            global_settings = self.opts.get(GLOBAL_SETTINGS, {})

            # Get configuration for QRadar server specified
            options = get_server_settings(self.opts, qradar_label)
            # Create connection to QRadar server
            qradar_client = get_qradar_client(self.opts, options)
            # Clear specified data table in SOAR based on app.config settings
            clear_table(self.rest_client(), soar_table_name, soar_incident_id, global_settings)

            timeout = 600 # Default timeout to 10 minutes
            # Check if search_timeout setting is configured in edm_global_settings
            if global_settings and global_settings.get("search_timeout"):
                timeout = float(global_settings.get("search_timeout"))
            # Check if search_timeout setting is configured for given QRadar server
            elif options.get("search_timeout"):
                timeout = float(options.get("search_timeout"))

            temp_table = "offense-{0}-events-{1}-1000-{2}".format(qradar_search_param3, qradar_fn_type, str(time()))

            qradar_temp_query = sub("FROM\s+{}".format(ARIEL_SEARCH_EVENTS if search(ARIEL_SEARCH_EVENTS,qradar_query, flags=IGNORECASE) else ARIEL_SEARCH_FLOWS),
                                       "FROM {} INTO \"{}\"".format(ARIEL_SEARCH_EVENTS if search(ARIEL_SEARCH_EVENTS,qradar_query, flags=IGNORECASE) else ARIEL_SEARCH_FLOWS, temp_table),
                                       qradar_query, flags=IGNORECASE)

            qradar_search_query = sub("FROM\s+{}".format(ARIEL_SEARCH_EVENTS if search(ARIEL_SEARCH_EVENTS,qradar_query, flags=IGNORECASE) else ARIEL_SEARCH_FLOWS),
                                         "FROM \"{}\"".format(temp_table),
                                         qradar_query, flags=IGNORECASE)

            temp_query_string = make_query_string(qradar_temp_query,
                                                                 ["*",
                                                                  qradar_search_param2,
                                                                  qradar_search_param3,
                                                                  " ",
                                                                  " ",
                                                                  " "])

            search_query_string = make_query_string(qradar_search_query,
                                                                   [qradar_search_param1,
                                                                    " ",
                                                                    " ",
                                                                    qradar_search_param4 or " ",
                                                                    qradar_search_param5,
                                                                    qradar_search_param6
                                                                    ])

            LOG.info("Running query: " + temp_query_string)

            # Get the wf_instance_id of the workflow this Function was called in, if not found return a backup string
            wf_instance_id = event.message.get("workflow_instance", {}).get("workflow_instance_id", "no instance id found")
            yield StatusMessage("Starting 'qradar_top_events' that was running in workflow '{0}'".format(wf_instance_id))

            result = qradar_client.ariel_graphql_search(temp_query_string, search_query_string, timeout=timeout)

            # Enrich sourceip data by getting additional props using a graphql call to QRadar
            if qradar_fn_type == "sourceip":

                offense_source = qradar_client.graphql_query({"id":qradar_search_param3}, qradar_graphql_queries.GRAPHQL_OFFENSESOURCE, "sourceAddresses")

                for event in result["events"]:
                    domain = list(filter(lambda x: x["sourceIp"]==event["sourceip"], offense_source["content"]))
                    event["domainid"] = domain[0]["domainId"] if len(domain)>0 else 0  # Assign sourceip domain
                    data = qradar_client.graphql_query({"domainId":event["domainid"],"ipAddress":event["sourceip"]}, qradar_graphql_queries.GRAPHQL_SOURCEIP)
                    event["vulnerabilityCount"] = data["content"]["vulnerabilityCount"] if data["content"] else 0
                    event["macAddress"] = data["content"]["interfaces"][0]["macAddress"] if data["content"] and len(data["content"]["interfaces"])>0 and "macAddress" in data["content"]["interfaces"][0] else ""
                    event["network"] = data["content"]["interfaces"][0]["currentIpAddress"]["network"]["networkName"] if data["content"] and len(data["content"]["interfaces"])>0 and data["content"]["interfaces"][0]["currentIpAddress"] and data["content"]["interfaces"][0]["currentIpAddress"]["network"] else ""
                    event["domain"] = data["content"]["domain"]["name"] if data["content"] and  data["content"]["domain"]["name"] else "Default Domain"

            result["events"] = list(map(lambda x: self.mapEventData(x), result["events"]))

            results = {
                "qrhost": options.get("host"),
                "offenseid": qradar_search_param3,
                "events": result["events"],
                "current_time": int(time())*1000
            }

            yield StatusMessage("Finished 'qradar_top_events' that was running in workflow '{0}'".format(wf_instance_id))
            yield FunctionResult(results)
        except Exception as e:
            LOG.error(str(e))
            yield FunctionError()

    def mapEventData(self, event):

        for key in event.keys():
            if key in ["eventtime", "lastpackettime", "FirstPacketTime", "sourcebytes", "sourcepackets", "destinationbytes", "destinationpackets"]:
                event[key] = int(float(event[key]))

        return event
