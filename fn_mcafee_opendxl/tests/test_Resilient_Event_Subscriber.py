# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
from fn_mcafee_opendxl.util.helper import verify_config, create_incident, map_values, add_methods_to_global, \
    get_topic_template_dict
from mock import Mock
from os.path import join, pardir
import json
import os
import tempfile
import shutil



class ConfigClass:
    def __init__(self):
        self.ops = {
            "fn_mcafee_opendxl": {
                "dxlclient_config": "path/to/dxlclient.config",
                "topic_listener_on": "True",
            }
        }


class TestResilientEvenSubscriber:

    def test_verify_config_good(self):
        ops = ConfigClass().ops
        config = verify_config(ops)
        expected = {
            "config_client": ops["fn_mcafee_opendxl"]["dxlclient_config"],
            "topic_listener_on": ops["fn_mcafee_opendxl"]["topic_listener_on"],
            "custom_template_dir": None,
            "opts": ops
        }

        assert expected == config

    def test_verify_config_no_section(self):
        ops = {}
        try:
            verify_config(ops)
        except ValueError as e:
            assert e.args[0] == "[fn_mcafee_opendxl] section is not set in the config file"

    def test_verify_config_no_config_client(self):
        f = ConfigClass().ops
        f["fn_mcafee_opendxl"]["dxlclient_config"] = None
        try:
            verify_config(f)
        except ValueError as e:
            assert e.args[0] == "dxlclient_config is not set. You must set this path to run this service"

    def test_verify_config_no_topic_name(self):
        ops = ConfigClass().ops
        ops["fn_mcafee_opendxl"]["topic_name"] = None
        try:
            verify_config(ops)
        except ValueError as e:
            assert e.args[0] == "topic_name is not set. You must set this value to run this service"

    def test_verify_config_no_topic_listener(self):
        ops = ConfigClass().ops
        ops["fn_mcafee_opendxl"]["topic_listener_on"] = None
        try:
            verify_config(ops)
        except ValueError as e:
            assert e.args[0] == "topic_listener_on is not set. You must set this value to run this service"

    def test_verify_config_no_incident_template(self):
        ops = ConfigClass().ops
        ops["fn_mcafee_opendxl"]["incident_template"] = None
        try:
            verify_config(ops)
        except ValueError as e:
            assert e.args[0] == "incident_template is not set. You must set this path to run this service"

    def test_verify_config_no_incident_mapping(self):
        ops = ConfigClass().ops
        ops["fn_mcafee_opendxl"]["incident_mapping"] = None
        try:
            verify_config(ops)
        except ValueError as e:
            assert e.args[0] == "incident_mapping is not set. You must set this path to run this service"

    def test_create_incident(self):
        mock_client = Mock()
        mock_client.post.return_value = {"id": 1234}
        payload = json.dumps({"name": "New Incident"})
        response = create_incident(mock_client, payload)

        assert response.get("id") == 1234

    def test_map_values(self):
        # Need to call to be able to use when rendering a template
        add_methods_to_global()

        TEST_PATH = os.path.dirname(os.path.abspath(__file__))
        DATA_PATH = os.path.join(TEST_PATH, "data")
        MESSAGE_FILE = os.path.join(DATA_PATH, "message.txt")
        EXPECTED_FILE = os.path.join(DATA_PATH, "expected.txt")
        INCIDENT_TEMPLATE_FILE = os.path.join(DATA_PATH, "incident_template.txt")

        with open(MESSAGE_FILE, 'r') as message, open(EXPECTED_FILE, 'r') as expected_data:

            # Read file and create dict
            message = json.loads(message.read())

            incident_data = map_values(INCIDENT_TEMPLATE_FILE, message)

            expected_data = json.loads(expected_data.read())
            actual_data = json.loads(incident_data)

            difference = {k: actual_data[k] for k in set(actual_data) - set(expected_data)}

            assert difference == {}

