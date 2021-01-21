# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from mock import patch
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_api_void"
FUNCTION_NAME = "fn_api_void_request"

# Read the default configuration-data section from the package
config_data = """[{0}]
apivoid_base_url=https://www.example.com
apivoid_sub_url=v1/pay-as-you-go/
apivoid_api_key=12345ABCDEF
""".format(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


class MockedResponse:
    def __init__(self):
        self.success = True

    def json(self):
        return {"content": "mock data"}


def call_fn_api_void_request_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_api_void_request", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_api_void_request_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnApiVoidRequest:
    """ Tests for the fn_api_void_request function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch("fn_api_void.components.funct_fn_api_void_request.RequestsCommon.execute_call_v2")
    @pytest.mark.parametrize("api_void_request_type, api_void_artifact_type, api_void_artifact_value", [
        ("selftest", "IP Address", True)
    ])
    def test_success(self, mock_get, circuits_app, api_void_request_type, api_void_artifact_type, api_void_artifact_value):
        """ Test calling with sample values for the parameters """

        mock_get.return_value = MockedResponse()

        function_params = {
            "api_void_request_type": api_void_request_type,
            "api_void_artifact_type": api_void_artifact_type,
            "api_void_artifact_value": api_void_artifact_value
        }

        call_fn_api_void_request_function(circuits_app, function_params)

        mock_get.assert_called_with(
            method="get",
            url="https://www.example.com/sitetrust/v1/pay-as-you-go/?key=12345ABCDEF&stats=True",
        )
