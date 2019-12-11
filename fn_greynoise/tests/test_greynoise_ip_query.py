# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

"""
    pytest --resilient_app_config=/path/to/app.config tests/test_greynoise_ip_query
"""

PACKAGE_NAME = "fn_greynoise"
FUNCTION_NAME = "greynoise_ip_query"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_greynoise_ip_query_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("greynoise_ip_query", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("greynoise_ip_query_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestGreynoiseIpQuery:
    """ Tests for the greynoise_ip_query function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("greynoise_value, greynoise_type, expected_results", [
        ("8.8.8.8", "context", {"error":"commonly spoofed ip"}),
        ("8.8.8.8", "quick", {u'code': u'0x05', u'ip': u'8.8.8.8', u'noise': False})
    ])
    def test_success(self, circuits_app, greynoise_value, greynoise_type, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "greynoise_value": greynoise_value,
            "greynoise_type": greynoise_type
        }
        results = call_greynoise_ip_query_function(circuits_app, function_params)
        assert(expected_results == results['content'])
