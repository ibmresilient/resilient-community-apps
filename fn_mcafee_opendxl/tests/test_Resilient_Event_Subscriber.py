# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
from fn_mcafee_opendxl.util.helper import verify_config, _create_incident, _map_values, event_subscriber
from mock import Mock, patch
import json
import os
from dxlclient.client import DxlClient
from dxlclient import EventCallback
from dxlclient.client_config import DxlClientConfig
from jinja2 import Template



class ConfigClass:
    def __init__(self):
        self.ops = {
            "fn_mcafee_opendxl": {
                "dxlclient_config": "path/to/dxlclient.config",
                "topic_name": "resilient/event/subscriber/topic",
                "topic_listener_on": "True",
                "incident_template": "incident/jinja2/template.jinja",
                "incident_template_mapping": "incident/jinja2/mappingTemplate.jinja"
            }
        }


class TestResilientEvenSubscriber:

    def test_verify_config_good(self):
        ops = ConfigClass().ops
        config = verify_config(ops)
        expected = {
            "config_client": ops["fn_mcafee_opendxl"]["dxlclient_config"],
            "topic_name": ops["fn_mcafee_opendxl"]["topic_name"],
            "topic_listener_on": ops["fn_mcafee_opendxl"]["topic_listener_on"],
            "incident_template": ops["fn_mcafee_opendxl"]["incident_template"],
            "incident_mapping": ops["fn_mcafee_opendxl"]["incident_template_mapping"]
        }

        assert expected == config

    def test_verify_config_no_section(self):
        ops = {}
        try:
            verify_config(ops)
        except ValueError as e:
            assert e.message == "[fn_mcafee_opendxl] section is not set in the config file"

    def test_verify_config_no_config_client(self):
        f = ConfigClass().ops
        f["fn_mcafee_opendxl"]["dxlclient_config"] = None
        try:
            verify_config(f)
        except ValueError as e:
            assert e.message == "dxlclient_config is not set. You must set this path to run this service"

    def test_verify_config_no_topic_name(self):
        ops = ConfigClass().ops
        ops["fn_mcafee_opendxl"]["topic_name"] = None
        try:
            verify_config(ops)
        except ValueError as e:
            assert e.message == "topic_name is not set. You must set this value to run this service"

    def test_verify_config_no_topic_listener(self):
        ops = ConfigClass().ops
        ops["fn_mcafee_opendxl"]["topic_listener_on"] = None
        try:
            verify_config(ops)
        except ValueError as e:
            assert e.message == "topic_listener_on is not set. You must set this value to run this service"

    def test_verify_config_no_incident_template(self):
        ops = ConfigClass().ops
        ops["fn_mcafee_opendxl"]["incident_template"] = None
        try:
            verify_config(ops)
        except ValueError as e:
            assert e.message == "incident_template is not set. You must set this path to run this service"

    def test_verify_config_no_incident_mapping(self):
        ops = ConfigClass().ops
        ops["fn_mcafee_opendxl"]["incident_mapping"] = None
        try:
            verify_config(ops)
        except ValueError as e:
            assert e.message == "incident_mapping is not set. You must set this path to run this service"

    def test_create_incident(self):
        mock_client = Mock()
        mock_client.post.return_value = {"id": 1234}
        payload = json.dumps({"name": "New Incident"})
        response = _create_incident(mock_client, payload)

        assert response.get("id") == 1234

    def test_map_values(self):

        message = '{"artifact_type": "IP Address", "discovered_date": "1523569779000", "artifact_value": "8.8.8.8", "incident_name": "Malware Incident"}'

        incident_template = os.getcwd()
        incident_template = incident_template + "/incident_template.txt"
        mapping_template = os.getcwd()
        mapping_template = mapping_template + "/mapping_template.txt"

        incident_data = _map_values(incident_template, mapping_template, message)

        expected_data = {
            "description": {
               "format": "html",
               "content": "New Malware Incident created using the Resilient DXL Service Listener"
            },
            "discovered_date": 1523569779000,
            "incident_type_ids": [19],
            "artifacts": [

                {"type": {"name": "IP Address"}, "value": "8.8.8.8"}
            ],
            "name": "Malware Incident"
        }
        actual_data = json.loads(incident_data)

        assert actual_data == expected_data

