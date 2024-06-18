# -*- coding: utf-8 -*-
# Generated with resilient-sdk v51.0.1.0.695
"""Tests using pytest_resilient_circuits"""

import pytest
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from resilient_lib import IntegrationError
from mock import patch
from json import loads

PACKAGE_NAME = "fn_wiz"
FUNCTION_NAME = "wiz_pull_vulnerabilities"

# Mock out configs
config_data = """[fn_wiz]
client_id=abcd-efgh
client_secret=abcdefg-hijklmno
endpoint_url=https://fake.app.wiz.com
api_url=https://wizapi.io/graphql
token_url=https://wizauth.io
polling_interval=0
polling_lookback=0
"""

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_wiz_pull_vulnerabilities_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("wiz_pull_vulnerabilities", function_params)

    # Fire a message to the function
    circuits.manager.fire(evt)

    # circuits will fire an "exception" event if an exception is raised in the FunctionComponent
    # return this exception if it is raised
    exception_event = circuits.watcher.wait("exception", parent=None, timeout=timeout)

    if exception_event is not False:
        exception = exception_event.args[1]
        raise exception

    # else return the FunctionComponent's results
    else:
        event = circuits.watcher.wait("wiz_pull_vulnerabilities_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestWizPullVulnerabilities:
    """ Tests for the wiz_pull_vulnerabilities function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    # Test if a list of project ids are provided (for example, in Populate Case playbook)
    mock_inputs_1 = {
        "wiz_project_ids": "a,b,c,d"
    }
    expected_results_1 = { "response": {"test": "response"} }
    expected_projects_list_1 = ["a", "b", "c", "d"]

    # Test if a list of project ids are provided **and** a value for max num results
    # (for example, in Populate Case playbook)
    mock_inputs_2 = {
        "wiz_project_ids": "a,b,c,d",
        "wiz_num_results": 10
    }
    expected_results_2 = { "response": {"test": "response"} }
    expected_projects_list_2 = ["a", "b", "c", "d"]

    # Test if only num_results is passed in
    mock_inputs_3 = {
        "wiz_num_results": 10
    }
    expected_results_3 = { "response": {"test": "response"} }
    expected_projects_list_3 = []

    # Test if wiz_query_filter is passed in (for example in Pull Vulnerabilities playbook)
    mock_inputs_4 = {"wiz_query_filter": '{"first": 5}'}
    expected_results_4 = { "response": {"test": "response"} }
    expected_projects_list_4 = []

    # Test if no inputs are passed in
    mock_inputs_5 = {}
    expected_results_5 = { "response": {"test": "response"} }
    expected_projects_list_5 = []

    @pytest.mark.parametrize("mock_inputs, expected_results, expected_projects", [
        (mock_inputs_1, expected_results_1, expected_projects_list_1),
        (mock_inputs_2, expected_results_2, expected_projects_list_2),
        (mock_inputs_3, expected_results_3, expected_projects_list_3),
        (mock_inputs_4, expected_results_4, expected_projects_list_4),
        (mock_inputs_5, expected_results_5, expected_projects_list_5)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results, expected_projects):
        """ Test calling with sample values for the parameters """
        with patch("fn_wiz.components.funct_wiz_pull_vulnerabilities.AppCommon.get_vulnerabilities") as mock_app_common:
            mock_app_common.return_value = {"test": "response"}
            results = call_wiz_pull_vulnerabilities_function(circuits_app, mock_inputs)
            assert(expected_results == results.get('content'))
            if "wiz_query_filter" in mock_inputs.keys():
                custom_filter = loads(mock_inputs.get('wiz_query_filter'))
                mock_app_common.assert_called_with(expected_projects, custom_filter=custom_filter, num_results=mock_inputs.get('wiz_num_results', 50))
            else:
                mock_app_common.assert_called_with(expected_projects, custom_filter=None, num_results=mock_inputs.get('wiz_num_results', 50))
    
    
    def test_failure(self, circuits_app):
        """ Test calling with sample values for the parameters """
        with patch("fn_wiz.components.funct_wiz_pull_vulnerabilities.AppCommon.get_vulnerabilities") as mock_app_common:
            # Test if bad custom filter is passed in -- JSONDecoder error
            mock_inputs_6 = {"wiz_query_filter": "{[]}"}
            expected_results_6 = []
            mock_app_common.return_value = {"test": "response"}
            with pytest.raises(IntegrationError) as interror:
                results = call_wiz_pull_vulnerabilities_function(circuits_app, mock_inputs_6)
                assert "Please ensure input is JSON formatted:" in interror.value.value
                assert(expected_results_6 == results.get('content'))
            

             # Test if bad custom filter is passed in -- integer 
            mock_inputs_6 = {"wiz_query_filter": "123456"}
            expected_results_6 = []
            mock_app_common.return_value = {"test": "response"}
            with pytest.raises(IntegrationError) as interror:
                results = call_wiz_pull_vulnerabilities_function(circuits_app, mock_inputs_6)
                assert "Please ensure input is JSON formatted, found input with" in interror.value.value
                assert(expected_results_6 == results.get('content'))