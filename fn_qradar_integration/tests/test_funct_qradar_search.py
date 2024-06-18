# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.0.4423
"""Tests using pytest_resilient_circuits"""

import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from fn_qradar_integration.util.qradar_constants import PACKAGE_NAME
from mock import patch

FUNCTION_NAME = "qradar_search"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

MOCK_SEARCH_RESPONSE = {
    "events": [
        {
            "StartTime": "2023-06-14 14:14",
            "categoryname_category": "User Login Attempt",
            "logsourcename_logsourceid": "Experience Center: AWS Syslog @ 192.168.0.17",
            "protocolname_protocolid": "Reserved",
            "rulename_creeventlist": "['BB:NetworkDefinition: Honeypot like Addresses', 'EC: AWS Cloud - Detected A Successful Login From Different Geographies For the Same Username', 'BB:CategoryDefinition: Medium Magnitude Events', 'BB:CategoryDefinition: High Magnitude Events', 'Source Asset Weight is Low', 'ECBB:CategoryDefinition: Destination IP is a Third Country/Region', 'Destination Asset Weight is Low', 'BB:NetworkDefinition: Darknet Addresses', 'Load Basic Building Blocks']"
        },
        {
            "StartTime": "2023-06-14 14:14",
            "categoryname_category": "Misc Login Succeeded",
            "logsourcename_logsourceid": "Custom Rule Engine-8 :: qavm118-43",
            "protocolname_protocolid": "Reserved",
            "rulename_creeventlist": "['EC: AWS Cloud - Detected A Successful Login From Different Geographies For the Same Username', 'BB:NetworkDefinition: Honeypot like Addresses', 'BB:CategoryDefinition: Authentication Success', 'BB:CategoryDefinition: Medium Magnitude Events', 'BB:CategoryDefinition: High Magnitude Events', 'Source Asset Weight is Low', 'ECBB:CategoryDefinition: Destination IP is a Third Country/Region', 'Destination Asset Weight is Low', 'BB:CategoryDefinition: Post Exploit Account Activity', 'BB:NetworkDefinition: Darknet Addresses', 'Load Basic Building Blocks']"
        },
        {
            "StartTime": "2023-06-14 14:14",
            "categoryname_category": "Virtual Machine Creation Attempt",
            "logsourcename_logsourceid": "Experience Center: AWS Syslog @ 192.168.0.17",
            "protocolname_protocolid": "Reserved",
            "rulename_creeventlist": "['BB:NetworkDefinition: Honeypot like Addresses', 'EC: AWS Cloud - An AWS API Has Been Invoked From Kali', 'BB:CategoryDefinition: Medium Magnitude Events', 'BB:CategoryDefinition: High Magnitude Events', 'Source Asset Weight is Low', 'ECBB:CategoryDefinition: Destination IP is a Third Country/Region', 'Destination Asset Weight is Low', 'BB:NetworkDefinition: Darknet Addresses', 'Load Basic Building Blocks']"
        },
        {
            "StartTime": "2023-06-14 14:14",
            "categoryname_category": "Virtual Machine Creation Attempt",
            "logsourcename_logsourceid": "Experience Center: AWS Syslog @ 192.168.0.17",
            "protocolname_protocolid": "Reserved",
            "rulename_creeventlist": "['BB:NetworkDefinition: Honeypot like Addresses', 'EC: AWS Cloud - An AWS API Has Been Invoked From Kali', 'BB:CategoryDefinition: Medium Magnitude Events', 'BB:CategoryDefinition: High Magnitude Events', 'Source Asset Weight is Low', 'ECBB:CategoryDefinition: Destination IP is a Third Country/Region', 'Destination Asset Weight is Low', 'BB:NetworkDefinition: Darknet Addresses', 'Load Basic Building Blocks']"
        },
        {
            "StartTime": "2023-06-14 14:14",
            "categoryname_category": "Virtual Machine Creation Attempt",
            "logsourcename_logsourceid": "Experience Center: AWS Syslog @ 192.168.0.17",
            "protocolname_protocolid": "Reserved",
            "rulename_creeventlist": "['BB:NetworkDefinition: Honeypot like Addresses', 'EC: AWS Cloud - An AWS API Has Been Invoked From Kali', 'BB:CategoryDefinition: Medium Magnitude Events', 'BB:CategoryDefinition: High Magnitude Events', 'Source Asset Weight is Low', 'ECBB:CategoryDefinition: Destination IP is a Third Country/Region', 'Destination Asset Weight is Low', 'BB:NetworkDefinition: Darknet Addresses', 'Load Basic Building Blocks']"
        }
    ]
}

def call_qradar_search_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction(FUNCTION_NAME, function_params)

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
        event = circuits.watcher.wait("qradar_search_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value

class TestQradarSearch:
    """ Tests for the qradar_search function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func

    mock_inputs_1 = {
        "qradar_label": "SOAR_Plugin_Destination_Name1",
        "qradar_search_param3": "7",
        "qradar_query_all_results": "No",
        "qradar_query": "SELECT %param1% FROM events WHERE INOFFENSE(%param2%) LAST %param3% Days",
        "qradar_search_param5": None,
        "qradar_query_range_end": 5,
        "qradar_search_param2": "6241",
        "qradar_query_range_start": 1,
        "qradar_search_param4": None,
        "qradar_search_param1": "DATEFORMAT(starttime, 'YYYY-MM-dd HH:mm') as StartTime, CATEGORYNAME(category), LOGSOURCENAME(logsourceid), PROTOCOLNAME(protocolid), RULENAME(creeventlist)"
    }

    expected_results_1 = MOCK_SEARCH_RESPONSE

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """
        with patch("fn_qradar_integration.util.qradar_utils.QRadarClient.ariel_search") as patched_add_element:
            patched_add_element.return_value = expected_results
            results = call_qradar_search_function(circuits_app, mock_inputs)
            assert(expected_results.get("events", []) == results.get("events", []))
