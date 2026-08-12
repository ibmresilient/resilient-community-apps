# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2020
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
import json

from fn_guardium_insights_integration.lib.insights_services import InsightsServices
from fn_guardium_insights_integration.lib.resilient_incident_operations import ResilientIncidentHelper
from fn_guardium_insights_integration.lib.time_conversions import compute_query_times
from fn_guardium_insights_integration.util.data_parsers import map_details_assets


def retrieve_anomalies_create_incident(rest_client, options, log):
    """
    param rest_client: Resilient Restful service client
    param options: App configuration values dict
    """
    # Initializing Insights service class
    insights_service_obj = InsightsServices(options, log)

    # Initializing the Resilient RESTful services
    incident_helper = ResilientIncidentHelper(rest_client, log)

    # Query Insights for Anomalies
    start_time, stop_time = compute_query_times(options.get("analytics_poll_time"), options.get("delta_poll_range"))
    anomolies = insights_service_obj.retrieve_anamolies(start_time=start_time, end_time=stop_time)

    if anomolies:
        log.info("found anomalies, processing...")
        anomaly_records = anomolies.get("records")
        for each_anomaly_record in anomaly_records:
            event_id = each_anomaly_record.get("event_id")
            # search for each event id to check existing incidents
            search_data = incident_helper.search_incident(event_id)
            if not search_data.get("results"):
                log.info("No existing Resilient incident found, creating a new incident...")

                # get configured member information, & populating incident payload
                inc_member = options.get("incident_member").split(",")
                payload_data = incident_helper.generate_incident_payload(each_anomaly_record, inc_member)

                # Get additional anomaly_details on event like who, what, when & add those info to description field
                anomaly_details = insights_service_obj.get_anamolies_details_by_event_id(event_id)

                # Get Asset information
                _asset_affected = anomaly_details.get("record").get("asset_affected").lower()

                asset_data = insights_service_obj.get_assets_information(anomaly_details)

                # Mapping event anomaly_details with assets data
                map_dict, html_desc = map_details_assets(anomaly_details, asset_data)

                # Adding additional details to incident payload.
                if map_dict.get("user_data"):
                    _user_data = map_dict.get("user_data")[0]
                else:
                    _user_data = dict()
                payload_data["properties"]["field_guardium_insights_who"] = _user_data.get("who", "")
                payload_data["properties"]["field_guardium_insights_what"] = json.dumps(_user_data.get("what", {}))
                payload_data["properties"]["field_guardium_insights_when"] = json.dumps(_user_data.get("when", {}))
                payload_data["properties"]["field_guardium_insights_where"] = json.dumps(_user_data.get("where", {}))
                payload_data["properties"]["field_guardium_insights_why"] = json.dumps(_user_data.get("why", {}))

                # Adding artifacts to the incident
                _ar_user_acc = _user_data.get("who", "")
                if _ar_user_acc:
                    payload_data["artifacts"].append({"type": {"name": "User Account"}, "value": _ar_user_acc,
                                                      "description": {"format": "text", "content": "Who-Actor"}})

                _ar_port = _user_data.get("what", {}).get("server_port", "")
                if _ar_port:
                    payload_data["artifacts"].append({"type": {"name": "Port"}, "value": _ar_port,
                                                      "description": {"format": "text", "content": "Server Port"}})

                _ar_ip = _user_data.get("what", {}).get("server_ip", "")
                if _ar_ip:
                    payload_data["artifacts"].append({"type": {"name": "IP Address"}, "value": _ar_ip,
                                                      "description": {"format": "text", "content": "Server IP"}})

                _ar_host = _user_data.get("what", {}).get("sever_hostname", "")
                if _ar_host:
                    payload_data["artifacts"].append({"type": {"name": "System Name"}, "value": _ar_host,
                                                      "description": {"format": "text", "content": "Server Hostname"}})

                _ext_desc = payload_data["description"].get("content")
                payload_data["description"]["content"] = _ext_desc + html_desc

                # Creating an anomaly incident
                incident_helper.create_incident(payload_data)
            else:
                log.info("Found existing Resilient incident, so discarding an event...")
    else:
        log.info("No anomalies data found to process...")
