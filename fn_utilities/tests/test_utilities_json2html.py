# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from resilient_circuits.action_message import FunctionException_, FunctionError_

PACKAGE_NAME = "fn_utilities"
FUNCTION_NAME = "utilities_json2html"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_utilities_json2html_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("utilities_json2html", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("utilities_json2html_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestUtilitiesJson2Html:
    """ Tests for the utilities_json2html function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("json2html_data, json2html_keys, expected_results", [
        ('{ "key10": { "key20": { "a": "a1", "b": "b1", "key30": [1, 2, 3, 4] } } }',
         None, {"content": "<table border=\"1\"><tr><th>key10</th><td><table border=\"1\"><tr><th>key20</th><td><table border=\"1\"><tr><th>a</th><td>a1</td></tr><tr><th>b</th><td>b1</td></tr><tr><th>key30</th><td><ul><li>1</li><li>2</li><li>3</li><li>4</li></ul></td></tr></table></td></tr></table></td></tr></table>"}),
        ('{ "key10": { "key20": { "a": "a1", "b": "b1", "key30": [1, 2, 3, 4] } } }',
         "key10.key20.key30", {"content": "<ul><li>1</li><li>2</li><li>3</li><li>4</li></ul>"})
    ])
    def test_success(self, circuits_app, json2html_data, json2html_keys, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "json2html_data": json2html_data,
            "json2html_keys": json2html_keys
        }
        results = call_utilities_json2html_function(circuits_app, function_params)
        assert(expected_results == results)


    @pytest.mark.parametrize("json2html_data, json2html_keys, expected_results", [
            ('{ "key10": { "key20": { "a": "a1", "b": "b1", "key30": [1, 2, 3, 4] } } }',
             "xx", {})
        ])
    def test_key_failures(self, circuits_app, json2html_data, json2html_keys, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = {
            "json2html_data": json2html_data,
            "json2html_keys": json2html_keys
        }

        with pytest.raises((AssertionError)) as err:
            results = call_utilities_json2html_function(circuits_app, function_params)

        # should be able to parse err for 'key not found'