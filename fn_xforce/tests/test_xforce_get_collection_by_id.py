# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_xforce"
FUNCTION_NAME = "xforce_get_collection_by_id"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def call_xforce_get_collection_by_id_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("xforce_get_collection_by_id", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("xforce_get_collection_by_id_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)

    return event.kwargs["result"].value

# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if kwargs.get('success') == True:
        return MockResponse(json_data={'contents': [{"test1":"test"},{"test2":"test"}]},status_code=200)
    else:
        return MockResponse(json_data={}, status_code=400)


class TestXforceGetCollectionById:
    """ Tests for the xforce_get_collection_by_id function"""

    @pytest.mark.parametrize("xforce_collection_id, expected_results", [
        ("e7dd02a139820860866a4fdd82cf9d8e", {"success": True, "contents":"hello"})
    ])
    def test_success(self, circuits_app, xforce_collection_id, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "xforce_collection_id": xforce_collection_id
        }
        with patch('requests.get') as mock:
            mock.side_effect = mocked_requests_get(success=True)
            results = call_xforce_get_collection_by_id_function(circuits_app, function_params)

            assert(expected_results["success"] == results["success"])


    @pytest.mark.parametrize("xforce_collection_id, expected_results", [
        ("badcaseID", {"success": False}),
        ("c6856123", {"success": False})
    ])
    def test_failure(self, circuits_app, xforce_collection_id, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "xforce_collection_id": xforce_collection_id
        }
        with patch('requests.get') as mock:
            mock.side_effect = mocked_requests_get()
            results = call_xforce_get_collection_by_id_function(circuits_app, function_params)
            assert(expected_results["success"] == results["success"])


class TestXforceDefinition:
    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None
