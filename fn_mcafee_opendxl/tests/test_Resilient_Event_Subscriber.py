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

        message_file = os.getcwd()
        message_file = message_file + "/data/message.txt"
        expected = os.getcwd()
        expected = expected + "/data/expected.txt"

        with open(message_file, 'r') as message, open(expected, 'r') as expected_data:
            incident_template = os.getcwd()
            incident_template = incident_template + "/data/incident_template.txt"

            # Read file and create dict
            message = json.loads(message.read())

            incident_data = map_values(incident_template, message)

            expected_data = json.loads(expected_data.read())
            actual_data = json.loads(incident_data)

            difference = {k: actual_data[k] for k in set(actual_data) - set(expected_data)}

            assert difference == {}

    def test_get_template_file(self):
        current_path = os.path.dirname(os.path.realpath(__file__))
        default_template = join(current_path, pardir, "fn_mcafee_opendxl/data/templates/_mcafee_event_epo_threat_response.jinja2")

        expected_dict = {
            "/mcafee/event/epo/threat/response": default_template
        }
        actual_dict = get_topic_template_dict()

        expected_dict["/mcafee/event/epo/threat/response"] = os.path.abspath(expected_dict.get("/mcafee/event/epo/threat/response"))
        actual_dict["/mcafee/event/epo/threat/response"] = os.path.abspath(actual_dict.get("/mcafee/event/epo/threat/response"))

        assert actual_dict == expected_dict

    def test_get_override_template_file(self):
        temp_dir = tempfile.mkdtemp()
        try:
            with open(temp_dir + "/_mcafee_event_epo_threat_response.jinja", "a") as temp:
                expected_dict = {
                    "/mcafee/event/epo/threat/response": temp.name
                }
                actual_dict = get_topic_template_dict(temp_dir)

                assert actual_dict == expected_dict
        finally:
            # Remove the temp directory created
            shutil.rmtree(temp_dir)
