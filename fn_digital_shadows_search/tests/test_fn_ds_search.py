# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from test_helper import *
from mock import patch
import json

PACKAGE_NAME = "fn_digital_shadows_search"
FUNCTION_NAME = "fn_ds_search"

# Read the default configuration-data section from the package
config_data = get_mocked_config()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def get_mocked_post_request(*args, **kwargs):
  class MockResponse:
      """
      A mock class intended to mock the entire Response attribute for a post request.
      """
      def __init__(self, status_code, text):
          self.text = json.dumps({"content": text})
          self.status_code = status_code

      def raise_for_status(self):
        pass

  if kwargs.get('success') == True:
    return MockResponse(200, get_mocked_data())

  else:
    return MockResponse(400, "Bad API request")

def call_fn_ds_search_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_ds_search", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_ds_search_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnDigitalShadowsSearch:
    """ Tests for the fn_ds_search function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    inputs = {
      "ds_search_value": "192.168.0.1"
    }

    output = {
      "success": True,
      "inputs": inputs,
      "link": "https://portal-digitalshadows.com/search?q=192.168.0.1&view=List",
      "href": "<a href=https://portal-digitalshadows.com/search?q=192.168.0.1&view=List>Link</a>",
      "data": get_mocked_data()
    }

    @pytest.mark.parametrize("inputs, expected_results", [(inputs, output)])
    def test_success(self, circuits_app, inputs, expected_results):
        """ Test calling with sample values for the parameters """
        
        with patch("fn_digital_shadows_search.components.fn_ds_search.requests.post") as mocked_post_request:

          # Replace the return value of our mock_session with a custom function
          mocked_post_request.return_value = get_mocked_post_request(success=True)

          # Fire the function with mocked functionality
          results = call_fn_ds_search_function(circuits_app, inputs)
          assert(expected_results == results)

    @pytest.mark.parametrize("inputs, expected_results", [(inputs, output)])
    def test_fail(self, circuits_app, inputs, expected_results):
        """ Test calling with sample values for the parameters """

        expected_results["link"] = None
        expected_results["href"] = None

        with patch("fn_digital_shadows_search.components.fn_ds_search.requests.post") as mocked_post_request:

          # Replace the return value of our mock_session with a custom function
          mocked_post_request.return_value = get_mocked_post_request(success=False)

          evt = SubmitTestFunction("fn_ds_search", inputs)
          circuits_app.manager.fire(evt)

          try:
            event = circuits_app.watcher.wait("fn_ds_search_result", parent=evt, timeout=10)
            assert event == False
          except ValueError:
            assert True