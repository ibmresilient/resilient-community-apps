# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_google_maps_directions"
FUNCTION_NAME = "fn_google_maps_directions"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_google_maps_directions_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_google_maps_directions", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_google_maps_directions_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnGoogleMapsDirections:
    """ Tests for the fn_google_maps_directions function"""


    inputs = ['IBM, Armonk, New York', 'IBM Resilient, Cambridge, Boston, MA']
    outputs = [
      {
        "success": True,
        "directions_link": "https://www.google.com/maps/dir/?api=1&origin=IBM%2C%20Armonk%2C%20New%20York&destination=IBM%20Resilient%2C%20Cambridge%2C%20Boston%2C%20MA",
        "inputs": {
          "google_maps_origin": inputs[0],
          "google_maps_destination": inputs[1]
        }
      }
    ]

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("google_maps_origin, google_maps_destination, expected_results", [
        (inputs[0], inputs[1], outputs[0])
    ])
    def test_success(self, circuits_app, google_maps_origin, google_maps_destination, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "google_maps_origin": google_maps_origin,
            "google_maps_destination": google_maps_destination
        }
        results = call_fn_google_maps_directions_function(circuits_app, function_params)
        assert(expected_results == results)

    @pytest.mark.parametrize("google_maps_origin, google_maps_destination, expected_results", [
      (inputs[0], inputs[1], outputs[0])
    ])
    def test_result_is_dict(self, circuits_app, google_maps_origin, google_maps_destination, expected_results):
        """ Test calling with sample values for the parameters and result is of type dict"""
        function_params = { 
            "google_maps_origin": google_maps_origin,
            "google_maps_destination": google_maps_destination
        }
        results = call_fn_google_maps_directions_function(circuits_app, function_params)
        assert (isinstance(results, dict))