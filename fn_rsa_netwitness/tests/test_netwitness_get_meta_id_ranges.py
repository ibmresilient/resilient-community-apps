# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_rsa_netwitness"
FUNCTION_NAME = "netwitness_get_meta_id_ranges"

# Read the default configuration-data section from the package
# config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
# resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_netwitness_get_meta_id_ranges_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("netwitness_get_meta_id_ranges", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("netwitness_get_meta_id_ranges_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestNetwitnessGetMetaIdRanges:
    """ Tests for the netwitness_get_meta_id_ranges function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("nw_session_id1, nw_session_id2, nw_results_size, expected_results", [
        (23787, 23983, 10, {"value": "xyz"})
    ])
    def test_success(self, circuits_app, nw_session_id1, nw_session_id2, nw_results_size, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "nw_session_id1": nw_session_id1,
            "nw_session_id2": nw_session_id2,
            "nw_results_size": nw_results_size
        }
        results = call_netwitness_get_meta_id_ranges_function(circuits_app, function_params)
        assert results.get("content") is not None
