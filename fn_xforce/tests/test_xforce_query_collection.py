# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

"""Tests using pytest_resilient_circuits"""

import pytest
from mock import patch

from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_xforce"
FUNCTION_NAME = "xforce_query_collection"

# Use mock config_data
config_data = """[{0}]
xforce_apikey = abc
xforce_password = 1234
#xforce_https_proxy = <YOUR_PROXY_URL>
#xforce_http_proxy = <YOUR_PROXY_URL>
xforce_baseurl = https://example.com
""".format(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

class MockedResponse:
    def __init__(self, success=True):
        if success:
            self.status_code = 200
            self.json_data = {'casefiles': [{"case1":"mock"},{"case2":"mock2"}]}

        else:
            self.status_code = 400
            self.json_data = {}

    def json(self):
        return self.json_data


def call_xforce_query_collection_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("xforce_query_collection", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("xforce_query_collection_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestXforceQueryCollection:
    """ Tests for the xforce_query_collection function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("xforce_collection_type, xforce_query, expected_results", [
        ({'name': 'public'}, "coinminer", {"success": True}),
        ({'name': 'public'}, "mirai", {"success": True}),
        ({'name': 'public'}, "E08BEFB4D791E8B9218020292B2FECAD", {"success": True})  # MD5
    ])
    def test_success(self, circuits_app, xforce_collection_type, xforce_query, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "xforce_collection_type": xforce_collection_type,
            "xforce_query": xforce_query
        }
        with patch('fn_xforce.components.xforce_query_collection.RequestsCommon.execute_call_v2') as mock:
            mock.return_value = MockedResponse(True)
            results = call_xforce_query_collection_function(circuits_app, function_params)
            assert(expected_results["success"] == results["success"])

    @pytest.mark.parametrize("xforce_collection_type, xforce_query, expected_results", [
        ({'name': 'public'}, "badquery123", {"success": True}),
        ({'name': 'public'}, "badquery999", {"success": True}),
        ({'name': 'private'}, "mirai", {"success": True}) #Assumes the current user has no private collections
    ])
    # Even no results are returned, the function is a success since there was no error code
    def test_failure(self, circuits_app, xforce_collection_type, xforce_query, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "xforce_collection_type": xforce_collection_type,
            "xforce_query": xforce_query
        }
        with patch('fn_xforce.components.xforce_query_collection.RequestsCommon.execute_call_v2') as mock:
            mock.return_value = MockedResponse(False)
            results = call_xforce_query_collection_function(circuits_app, function_params)
            assert(expected_results["success"] == results["success"])

    @pytest.mark.parametrize("xforce_collection_type, xforce_query, expected_results", [
        ({'name': 'public'}, "coinminer", {"success": True}),
        ({'name': 'public'}, "mirai", {"success": True})
    ])
    def test_num_of_casefiles(self, circuits_app, xforce_collection_type, xforce_query, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "xforce_collection_type": xforce_collection_type,
            "xforce_query": xforce_query
        }
        with patch('fn_xforce.components.xforce_query_collection.RequestsCommon.execute_call_v2') as mock:
            mock.return_value = MockedResponse(True)
            results = call_xforce_query_collection_function(circuits_app, function_params)
            assert(expected_results["success"] == results["success"])
            assert(results["num_of_casefiles"] >= 1)

    