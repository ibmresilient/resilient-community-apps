# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use, line-too-long
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function

from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from resilient_lib import RequestsCommon
import pytest
from mock import MagicMock, Mock
from test_helper import get_mock_config_data, get_mock_device_response, get_mock_results_content

PACKAGE_NAME = "fn_crowdstrike_falcon"
FUNCTION_NAME = "fn_cs_falcon_search"

# Read the default configuration-data section from the package
config_data = get_mock_config_data()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_cs_falcon_search_function(circuits, function_params, timeout=10):
    """call the function"""
    # Fire a message to the function
    evt = SubmitTestFunction("fn_cs_falcon_search", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_cs_falcon_search_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnCsFalconSearch:
    """ Tests for the fn_cs_falcon_search function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs = {
        "cs_filter_string": None,
        "cs_query": None
    }

    @pytest.mark.parametrize("inputs", [(mock_inputs)])
    def test_inputs_not_defined(self, circuits_app, inputs):
        """ test inputs not defined """

        with pytest.raises(Exception):
            call_fn_cs_falcon_search_function(circuits_app, inputs)

    mock_inputs = {
        "cs_filter_string": u"hostname:'localhost*'",
        "cs_query": None
    }

    mock_output = {
        'inputs': {'cs_query': None, 'cs_filter_string': u"hostname:'localhost*'"},
        'success': False,
        'content': None,
        'reason': u'> No devices found in CrowdStrike. Filter: "hostname:\'localhost*\'" Query: None'
    }

    @pytest.mark.parametrize("inputs, expected_results", [(mock_inputs, mock_output)])
    def test_no_devices_found(self, circuits_app, inputs, expected_results):
        """ test no devices found """

        mock_post_response = {
            "resources": []
        }

        RequestsCommon.execute_call = MagicMock(return_value=mock_post_response)

        results = call_fn_cs_falcon_search_function(circuits_app, inputs)

        assert expected_results.get("inputs") == results.get("inputs")
        assert expected_results.get("success") == results.get("success")
        assert expected_results.get("reason") == results.get("reason")

    mock_output = {
        'inputs': {'cs_query': None, 'cs_filter_string': u"hostname:'localhost*'"},
        'success': False,
        'content': None,
        'reason': u'> Could not get device details from CrowdStrike. Filter: "hostname:\'localhost*\'" Query: None'
    }

    @pytest.mark.parametrize("inputs, expected_results", [(mock_inputs, mock_output)])
    def test_could_not_get_device_details(self, circuits_app, inputs, expected_results):
        """ test could_not_get_device_details """

        mock_get_response_1 = {
            "resources": ['xxxxxx']
        }

        mock_get_response_2 = {
            "resources": []
        }

        RequestsCommon.execute_call = Mock()
        RequestsCommon.execute_call.side_effect = [mock_get_response_1, mock_get_response_2]

        results = call_fn_cs_falcon_search_function(circuits_app, inputs)

        assert expected_results.get("inputs") == results.get("inputs")
        assert expected_results.get("success") == results.get("success")
        assert expected_results.get("reason") == results.get("reason")

    mock_inputs = {
        "cs_filter_string": u"hostname:'localhost*'",
        "cs_query": None
    }

    mock_output = {
        'inputs': {'cs_query': None, 'cs_filter_string': u"hostname:'localhost*'"},
        'success': True,
        'content': get_mock_results_content()
    }

    @pytest.mark.parametrize("inputs, expected_results", [(mock_inputs, mock_output)])
    def test_success_getting_device(self, circuits_app, inputs, expected_results):
        """ test could_not_get_device_details """

        mock_get_response_1 = {
            "resources": ['xxxxxx']
        }

        mock_get_response_2 = {
            "resources": get_mock_device_response()
        }

        RequestsCommon.execute_call = Mock()
        RequestsCommon.execute_call.side_effect = [mock_get_response_1, mock_get_response_2]

        results = call_fn_cs_falcon_search_function(circuits_app, inputs)

        assert expected_results.get("inputs") == results.get("inputs")
        assert expected_results.get("success") == results.get("success")
        assert expected_results.get("content") == results.get("content")
