# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
import pytest


PACKAGE_NAME = "fn_whois_rdap"
FUNCTION_NAME = "whois_query"

# Read the default configuration-data section from the package
#config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_whois_query_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("whois_query", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("whois_query_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestWhoisQuery:
    @pytest.mark.livetest

    @pytest.mark.parametrize("whois_query, expected_results", [
        ("ibm.com", {"success" : True}),
        ("https://www.ibm.com", {"success" : True})
])
    def test_success(self, circuits_app, whois_query, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "whois_query": whois_query
        }
        results = call_whois_query_function(circuits_app, function_params)
        assert results["success"] == True