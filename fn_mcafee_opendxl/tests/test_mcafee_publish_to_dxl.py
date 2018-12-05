# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
import os
import json
from mock import patch
from fn_mcafee_opendxl.components import mcafee_publish_to_dxl
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_mcafee_opendxl"
FUNCTION_NAME = "mcafee_publish_to_dxl"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_mcafee_publish_to_dxl_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("mcafee_publish_to_dxl", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("mcafee_publish_to_dxl_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


def get_mock_ops():
    return {
        "fn_mcafee_opendxl": {
            "dxlclient_config": os.getcwd() + "/data/mock_dxlclient.config"
        },
        "email": "mock_email",
        "password": "mock_password",
        "host": "1.1.1.1",
        "org": "mock_org",
        "logdir": "/tmp",
        "cafile": "false"
    }


class TestMcafeePublishToDxl:
    """ Tests for the mcafee_publish_to_dxl function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("mcafee_topic_name, mcafee_dxl_payload, mcafee_publish_method, "
                             "mcafee_return_response, expected_results", [
        ("/mcafee/service/tie/file/reputation/set", "{\"hashes\": [{\"type\": \"md5\", \"value\": "
                                            "\"Dk0TzJrwTMZLaPw4/goNrA==\"}], \"providerId\": 3, \"trustLevel\":"
                                            " 1}", "Service", "No", {
                "mcafee_topic_name": "/mcafee/service/tie/file/reputation/set",
                "mcafee_dxl_payload": "{\"hashes\": [{\"type\": \"md5\", \"value\": \"Dk0TzJrwTMZLaPw4/goNrA==\"}], \"providerId\": 3, \"trustLevel\": 1}",
                "mcafee_publish_method": "Service",
                "mcafee_wait_for_response": "No"
            })
    ])
    def test_success(self, circuits_app, mcafee_topic_name, mcafee_dxl_payload,
                     mcafee_publish_method, mcafee_return_response, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = {
            "mcafee_topic_name": mcafee_topic_name,
            "mcafee_dxl_payload": mcafee_dxl_payload,
            "mcafee_publish_method": mcafee_publish_method,
            "mcafee_return_response": mcafee_return_response
        }
        results = call_mcafee_publish_to_dxl_function(circuits_app, function_params)
        assert(expected_results == results)

    # Util function to generate simulated requests response
    def _generateResponse(self, content, status):
        class simResponse:
            def __init__(self, content, status):
                self.status_code = status
                self.content = content
                self.text = json.dumps(content)
                self.cookies = {"JSESSIONID": "mock_id"}

            def json(self):
                return self.content

        return simResponse(content, status)


    @patch("dxlclient.client.DxlClient.connect")
    @patch("resilient.SimpleClient.get")
    @patch("requests.Session.get")
    @patch("requests.Session.post")
    def test_open_dxl_section_not_present(self, mocked_requests_session_post, mocked_requests_get,
                                          mocked_resilient_client_get, mock_dxl_connect):

        try:
            mock_ops = get_mock_ops()
            mock_ops.pop("fn_mcafee_opendxl")

            mock_session = {
                "orgs": [{
                    "name": "mock_org",
                    "enabled": True,
                    "id": 1234
                }],
                "csrf_token": "mock_csrf_token",
                "user_id": 456
            }
            mocked_requests_session_post.return_value = self._generateResponse(mock_session, 200)
            mocked_requests_get.side_effect = [self._generateResponse({"actions_framework_enabled": True}, 200),
                                               self._generateResponse({"name": "mock"}, 200),
                                               self._generateResponse({"name": "mock"}, 200),
                                               self._generateResponse({"id": "mock"}, 200)]
            mock_dxl_connect.return_value = True

            mcafee_publish_to_dxl.FunctionComponent(mock_ops)
        except AttributeError as e:
            assert e.args[0] == "[fn_mcafee_opendxl] section is not set in the config file"

    @patch("dxlclient.client.DxlClient.connect")
    @patch("resilient.SimpleClient.get")
    @patch("requests.Session.get")
    @patch("requests.Session.post")
    def test_config_file_not_set(self, mocked_requests_session_post, mocked_requests_get,
                                          mocked_resilient_client_get, mock_dxl_connect):

        try:
            mock_ops = get_mock_ops()
            mock_ops["fn_mcafee_opendxl"]["dxlclient_config"] = None

            mock_session = {
                "orgs": [{
                    "name": "mock_org",
                    "enabled": True,
                    "id": 1234
                }],
                "csrf_token": "mock_csrf_token",
                "user_id": 456
            }
            mocked_requests_session_post.return_value = self._generateResponse(mock_session, 200)
            mocked_requests_get.side_effect = [self._generateResponse({"actions_framework_enabled": True}, 200),
                                               self._generateResponse({"name": "mock"}, 200),
                                               self._generateResponse({"name": "mock"}, 200),
                                               self._generateResponse({"id": "mock"}, 200)]
            mock_dxl_connect.return_value = True

            mcafee_publish_to_dxl.FunctionComponent(mock_ops)
        except ValueError as e:
            assert e.args[0] == "dxlclient_config is not set. You must set this path to run this function"
