# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_mcafee_epo"
FUNCTION_NAME = "mcafee_tag_an_epo_asset"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_mcafee_tag_an_epo_asset_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("mcafee_tag_an_epo_asset", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("mcafee_tag_an_epo_asset_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestMcAfeeTagAnEpoAsset:
    """ Tests for the mcafee_tag_an_epo_asset function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("mcafee_epo_systems, mcafee_epo_tag, expected_results", [
        ("10.0.2.15", "Resilient", u'OK:\r\n0\r\n')
    ])
    def test_success(self, circuits_app, mcafee_epo_systems, mcafee_epo_tag, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "mcafee_epo_systems": mcafee_epo_systems,
            "mcafee_epo_tag": mcafee_epo_tag
        }
        results = call_mcafee_tag_an_epo_asset_function(circuits_app, function_params)
        assert(expected_results == results)