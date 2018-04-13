# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_mcafee_opendxl"
FUNCTION_NAME = "mcafee_publish_to_dxl"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_mcafee_publish_to_dxl_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("mcafee_publish_to_dxl", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("mcafee_publish_to_dxl_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestMcafeePublishToDxl:
    """ Tests for the mcafee_publish_to_dxl function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("mcafee_topic_name, mcafee_dxl_payload, mcafee_publish_method, "
                             "mcafee_return_response, expected_results", [
        ("/mcafee/service/tie/file/reputation/set", "{\"hashes\": [{\"type\": \"md5\", \"value\": "
                                            "\"Dk0TzJrwTMZLaPw4/goNrA==\"}], \"providerId\": 3, \"trustLevel\":"
                                            " 1}", "Service", "No", {
                "mcafee_topic_name": "/mcafee/service/tie/file/reputation/set",
                "mcafee_dxl_payload": "{\"hashes\": [{\"type\": \"md5\", \"value\": \"Dk0TzJrwTMZLaPw4/goNrA==\"}], \"providerId\": 3, \"trustLevel\": 1}",
                "mcafee_publish_method": "Service",
                "mcafee_wait_for_response": "No"
            })
    ])
    def test_success(self, circuits_app, mcafee_topic_name, mcafee_dxl_payload,
                     mcafee_publish_method, mcafee_return_response, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = {
            "mcafee_topic_name": mcafee_topic_name,
            "mcafee_dxl_payload": mcafee_dxl_payload,
            "mcafee_publish_method": mcafee_publish_method,
            "mcafee_return_response": mcafee_return_response
        }
        results = call_mcafee_publish_to_dxl_function(circuits_app, function_params)
        assert(expected_results == results)