# -*- coding: utf-8 -*-
# Generated with resilient-sdk v51.0.2.2.1096
"""Tests using pytest_resilient_circuits"""

import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from tests import test_helper
from unittest.mock import patch

PACKAGE_NAME = "fn_algosec"
FUNCTION_NAME = "algosec_traffic_change_request_details"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def call_algosec_traffic_change_request_details_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("algosec_traffic_change_request_details", function_params)

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
        event = circuits.watcher.wait("algosec_traffic_change_request_details_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value

class TestAlgosecTrafficChangeRequestDetails:
    """ Tests for the algosec_traffic_change_request_details function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "algosec_change_request_id": 11
    }

    expected_results_1 = {
    "status": "Success",
    "messages": [],
    "data": {
      "id": 11,
      "fields": [
        {
          "name": "Owner",
          "values": [
            "admin<admin@example.com>"
          ]
        },
        {
          "name": "Workflow",
          "values": [
            "Basic"
          ]
        },
        {
          "name": "Creator",
          "values": [
            "admin<admin@example.com>"
          ]
        },
        {
          "name": "Subject",
          "values": [
            "IBM SOAR Isolation Request for 1.1.1.1"
          ]
        },
        {
          "name": "Ticket Template Name",
          "values": [
            "Basic Change Traffic Request"
          ]
        },
        {
          "name": "Change Request Description",
          "values": [
            "Isolation Request initiated by the IBM SOAR Integration."
          ]
        },
        {
          "name": "LastUpdated",
          "values": [
            "2024-08-02 09:26:26"
          ]
        },
        {
          "name": "Requestor",
          "values": [
            "admin<admin@example.com>"
          ]
        },
        {
          "name": "Form Type",
          "values": [
            "Traffic Change"
          ]
        },
        {
          "name": "status",
          "values": [
            "open"
          ]
        }
      ],
      "originalTraffic": [
        {
          "source": {
            "items": [
              {
                "value": "1.1.1.1"
              },
              {
                "value": "any"
              }
            ]
          },
          "destination": {
            "items": [
              {
                "value": "any"
              },
              {
                "value": "1.1.1.1"
              }
            ]
          },
          "service": {
            "items": [
              {
                "value": "any"
              }
            ]
          },
          "application": {
            "items": [
              {
                "value": "any"
              }
            ]
          },
          "user": {
            "items": [
              {
                "value": "any"
              }
            ]
          },
          "fields": [
            {
              "name": "Requested URL Category",
              "values": [
                "any"
              ]
            }
          ],
          "action": "Drop"
        }
      ],
      "plannedTraffic": [
        {
          "source": {
            "items": [
              {
                "value": "1.1.1.1"
              },
              {
                "value": "any"
              }
            ]
          },
          "destination": {
            "items": [
              {
                "value": "any"
              },
              {
                "value": "1.1.1.1"
              }
            ]
          },
          "service": {
            "items": [
              {
                "value": "*"
              }
            ]
          },
          "application": {
            "items": [
              {
                "value": "any"
              }
            ]
          },
          "user": {
            "items": [
              {
                "value": "any"
              }
            ]
          },
          "fields": [
            {
              "name": "Change URL Category",
              "values": [
                "any"
              ]
            }
          ],
          "action": "Drop"
        }
      ]
    }
  }

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """
        with patch("fn_algosec.components.funct_algosec_traffic_change_request_details.algosec_client") as patch_client:
          with patch("fn_algosec.components.funct_algosec_traffic_change_request_details.fireflow") as patch_fireflow:
            patch_client.return_value = test_helper.mock_init_client()
            patch_fireflow.return_value = test_helper.mock_fireflow()
            results = call_algosec_traffic_change_request_details_function(circuits_app, mock_inputs)
            assert(expected_results == results.get("content", {}))
