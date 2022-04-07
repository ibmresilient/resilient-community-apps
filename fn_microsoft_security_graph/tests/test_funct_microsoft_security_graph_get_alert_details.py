# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from json import dumps
from mock import patch
from fn_microsoft_security_graph.lib.ms_graph_helper import MSGraphHelper
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_microsoft_security_graph"
FUNCTION_NAME = "microsoft_security_graph_get_alert_details"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def generate_response(content, status):
    class simResponse:
        def __init__(self, content, status):
            self.status_code = status
            self.content = content
            self.text = dumps(content)

        def json(self):
            return self.content

    return simResponse(content, status)

def call_microsoft_security_graph_get_alert_details_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("microsoft_security_graph_get_alert_details", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("microsoft_security_graph_get_alert_details_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value

class TestMicrosoftSecurityGraphGetAlertDetails:
    """ Tests for the microsoft_security_graph_get_alert_details function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('fn_microsoft_security_graph.lib.ms_graph_helper.OAuth2ClientCredentialsSession.get')
    @patch('fn_microsoft_security_graph.lib.ms_graph_helper.OAuth2ClientCredentialsSession.authenticate')
    def test_get_alert_details(self, mocked_requests_post, mocked_requests_get):
        content = {
            "access_token": "fake_access_token"
        }
        content2 = {
            "alert_details": {
                "details": 1234
            }
        }
        mocked_requests_post.return_value = generate_response(content, 200)
        mocked_requests_get.return_value = generate_response(content2, 200)
        ms_helper = MSGraphHelper("ms_token_url", "ms_graph_url", "tenant_id1234", "client_id1234", "client_secret1234")
        response = ms_helper.ms_graph_session.get("{}/security/alerts/{}".format("ms_graph_url", "1223456788"))

        assert response.json() == content2
