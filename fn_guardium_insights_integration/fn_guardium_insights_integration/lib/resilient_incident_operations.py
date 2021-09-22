# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2020
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
import re
import time

from resilient import NoChange

from fn_guardium_insights_integration.lib.custom_exceptions import ResilientRestfulServiceError
from fn_guardium_insights_integration.lib.time_conversions import convert_utc_date_time_milli_seconds
from fn_guardium_insights_integration.util.constants import ADD_INCIDENT, INCIDENT_URL, BREACH_DATA_MAP


class ResilientIncidentHelper:
    """
    This class will handle the resilient incident related stuffs.
    """
    def __init__(self, rest_client, log):
        self.rest_client = rest_client
        self.log = log

    def create_incident(self, payload):
        """
        Creates new incident in resilient
        :param payload: Incident data payload
        :return:
        """
        try:
            data = self.rest_client.post(ADD_INCIDENT, payload=payload, timeout=300)
            self.log.info(u"--------------Resilient Incident Created--------------: {}".format(data.get('id')))
            return data.get('id')
        except Exception as er_msg:
            self.log.error(u"Failed to create New Incident: {}".format(er_msg))
            return None

    def search_incident(self, query, name_value=""):
        """
        Search on resilient incident for given query elements.
        """
        _search_pay = {"org_id": "", "query": query, "types": ["incident"], "min_required_results": 0, "filters": {
            "incident": [{"conditions": [
                {"method": "contains", "field_name": "name", "value": "Guardium-Insights", "type": "incident"},
                {"method": "equals", "field_name": "properties.guardium_insights_event_id", "value": query,
                 "type": "incident"},
                {"method": "has_a_value", "field_name": "properties.guardium_insights_event_id", "type": "incident"}],
                "logic_type": "ALL"}]}}
        if name_value:
            _search_pay["filters"]["incident"][0]["conditions"][0]["value"] = name_value

        try:
            search_data = self.rest_client.search(_search_pay)
            return search_data
        except Exception as err:
            raise ResilientRestfulServiceError("Resilient search query- Error : {0}".format(err))

    @staticmethod
    def generate_incident_payload(event, *args):
        """
        Method to generate the incident payload to create a new incident based on retrieved anomalies.
        """
        __desc = ""
        __tmp_store_1 = ""
        __tmp_store_2 = ""
        milli_sec = int(time.time() * 1000)
        # Populating the Incident Description
        for key, value in event.items():
            __desc += "<div><strong>{} : </strong>{}</div>".format(key, value)

        _name = "Guardium-Insights-{0}-Confidence score - {1}".format(re.sub("_", " ", event.get("category")).title(),
                                                                      event.get("confidence_level"))
        _conv_time = convert_utc_date_time_milli_seconds(event.get("trigger_event_timestamp"))
        payload = {"name": _name, "discovered_date": _conv_time, "start_date": _conv_time,
                   "create_date": milli_sec, "description": {"format": "html", "content": __desc},
                   "severity_code": {"name": "Low"}, "plan_status": "Active",
                   "properties": {"guardium_insights_event_id": event.get("event_id"),
                                  "field_guardium_insights_config_id": event.get("config_id", ""),
                                  "field_guardium_insights_global_id": event.get("global_id", "")},
                   "artifacts": []}
        # If Incident Member is given then add to the payload else no member info added.
        if args[0][0] != "":
            payload["members"] = args[0]
        return payload

    def populate_breach_data_types(self, incident_id, report_data):
        """
        Method to populate the breach data types based on classification report rules data.
        """
        def _modify_payload(payload):
            data = report_data.get("result").get("data", {})
            if data:
                classification_rules = []
                for each_data in data:
                    classification_rules.append(each_data.get("results").get("13"))
                classification_rules = set(classification_rules)

                for rule in classification_rules:
                    if rule in BREACH_DATA_MAP:
                        rule = BREACH_DATA_MAP.get(rule)
                    else:
                        rule = rule.title()
                    payload["dtm"][rule] = True
                return payload
            else:
                raise NoChange

        self.rest_client.get_put(INCIDENT_URL.format(incident_id),
                                 lambda payload: _modify_payload(payload), timeout=1000)
