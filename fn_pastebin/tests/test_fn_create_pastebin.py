# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from test_helper import get_mock_config
from mock import patch

PACKAGE_NAME = "fn_pastebin"
FUNCTION_NAME = "fn_create_pastebin"

# Read the default configuration-data section from the package
config_data = get_mock_config()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def mocked_requests_get(*args, **kwargs):
  class MockResponse:
      """
      A mock class intended to mock the entire Response attribute for a requests.
      """
      def __init__(self, status_code, content):
          self.content = content
          self.status_code = status_code

  if kwargs.get('success') == True:
    return MockResponse(200, "https://pastebin.com/briH6zi2")

  else:
    return MockResponse(200, "Bad API request")

def call_fn_create_pastebin_function(circuits, function_params, timeout=10):
  # Fire a message to the function
  evt = SubmitTestFunction("fn_create_pastebin", function_params)
  circuits.manager.fire(evt)
  event = circuits.watcher.wait("fn_create_pastebin_result", parent=evt, timeout=timeout)
  assert event
  assert isinstance(event.kwargs["result"], FunctionResult)
  pytest.wait_for(event, "complete", True)
  return event.kwargs["result"].value

class TestFnCreatePastebin:
  """ Tests for the fn_create_pastebin function"""
  
  inputs = {
    "pastebin_code": "print 'Hello World'",
    "pastebin_name": "My New Pastebin",
    "pastebin_format": "python",
    "pastebin_privacy": 2,
    "pastebin_expiration": "1H"
  }

  output = {
    "success": True,

    "inputs": {
      "pastebin_code": inputs["pastebin_code"],
      "pastebin_name": inputs["pastebin_name"],
      "pastebin_format": inputs["pastebin_format"],
      "pastebin_privacy": inputs["pastebin_privacy"],
      "pastebin_expiration": inputs["pastebin_expiration"]
    },

    "pastebin_link": "https://pastebin.com/briH6zi2"
  }

  def test_function_definition(self):
    """ Test that the package provides customization_data that defines the function """
    func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
    assert func is not None

  @pytest.mark.parametrize("inputs, expected_results", [(inputs, output)])
  def test_success(self, circuits_app, inputs, expected_results):
    """ Test calling with sample values for the parameters """
    function_params = inputs

    with patch("fn_pastebin.components.fn_create_pastebin.requests.post") as mock_requests_get:

      # Replace the return value of our mock_session with a custom function
      mock_requests_get.return_value = mocked_requests_get(success=True)

      # Fire the function with mocked functionality
      results = call_fn_create_pastebin_function(circuits_app, function_params)
      assert(expected_results == results)

  @pytest.mark.parametrize("inputs", [(inputs)])
  def test_fail(self, circuits_app, inputs):
    """ Test calling with sample values for the parameters """
    function_params = inputs

    with patch("fn_pastebin.components.fn_create_pastebin.requests.post") as mock_requests_get:

      # Replace the return value of our mock_session with a custom function
      mock_requests_get.return_value = mocked_requests_get(success=False)

      # Fire the function with mocked functionality
      evt = SubmitTestFunction("fn_create_pastebin", function_params)
      circuits_app.manager.fire(evt)
      try:
        event = circuits_app.watcher.wait("fn_create_pastebin_result", parent=evt, timeout=3)
        assert event == False
      except ValueError:
        assert True