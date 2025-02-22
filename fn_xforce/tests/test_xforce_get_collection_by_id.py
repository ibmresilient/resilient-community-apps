# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.

"""Tests using pytest_resilient_circuits"""

import pytest
from mock import patch
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from fn_xforce.util.helper import PACKAGE_NAME

FUNCTION_NAME = "xforce_get_collection_by_id"

# Use mock config_data
config_data = f"""[{PACKAGE_NAME}]
xforce_apikey = abc
xforce_password = 1234
#xforce_https_proxy = <YOUR_PROXY_URL>
#xforce_http_proxy = <YOUR_PROXY_URL>
xforce_baseurl = https://example.com
"""

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

class MockedResponse:
    def __init__(self, success=True):
        if success:
            self.status_code = 200
            self.json_data = {"caseFileID": "e7dd02a139820860866a4fdd82cf9d8e", "contents": "hello"}

        else:
            self.status_code = 400
            self.json_data = {}

    def json(self):
        return self.json_data


def call_xforce_get_collection_by_id_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction(FUNCTION_NAME, function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait(f"{FUNCTION_NAME}_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


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
        with patch('fn_xforce.util.helper.RequestsCommon.execute') as mock:
            mock.return_value = MockedResponse(True)
            results = call_xforce_get_collection_by_id_function(circuits_app, function_params)

            assert(expected_results.get("success") == results.get("success"))


    @pytest.mark.parametrize("xforce_collection_id, expected_results", [
        ("badcaseID", {"success": True}),
        ("c6856123", {"success": True})
    ])
    # Even no results are returned, the function is a success since there was no error code
    def test_failure(self, circuits_app, xforce_collection_id, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "xforce_collection_id": xforce_collection_id
        }
        with patch('fn_xforce.util.helper.RequestsCommon.execute') as mock:
            mock.return_value = MockedResponse(True)
            results = call_xforce_get_collection_by_id_function(circuits_app, function_params)
            assert(expected_results.get("success") == results.get("success"))


class TestXforceDefinition:
    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None
