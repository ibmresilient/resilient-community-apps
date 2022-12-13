# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""Test fn_bigfix_assets function"""

from __future__ import print_function
import pytest
from mock import patch
from datetime import datetime
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from mock_artifacts import mocked_bigfix_client, mocked_res_client

"""Suite of tests to test fn_bigfix_assets SOAR Function"""

PACKAGE_NAME = "fn_bigfix"
FUNCTION_NAME = "fn_bigfix_assets"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the SOAR REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def call_fn_bigfix_assets_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_bigfix_assets", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_bigfix_assets_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value

class TestFnBigfixAssets:
    """ Tests for the fn_bigfix_assets function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func

    @patch('fn_bigfix.components.fn_bigfix_assets.BigFixClient', side_effect=mocked_bigfix_client)
    @patch('resilient_circuits.actions_component.ResilientComponent.rest_client', side_effect=mocked_res_client)
    @pytest.mark.parametrize("bigfix_asset_id, bigfix_asset_name, bigfix_incident_id, expected_results_1, expected_results_2", [
        (13550086, "DESKTOP-TUKM3HF", 2095, "OK", "bigfix-properties-" + "DESKTOP-TUKM3HF" + "-" + \
                            datetime.today().strftime('%Y%m%d') + ".xml")
    ])
    def test_success(self, mock_get_1, mock_get_2, circuits_app, bigfix_asset_id, bigfix_asset_name, bigfix_incident_id, expected_results_1, expected_results_2):
        """ Tests for fn_bigfix_assets using mocked data. """

        function_params = {
            "bigfix_asset_id": bigfix_asset_id,
            "bigfix_asset_name": bigfix_asset_name,
            "bigfix_incident_id": bigfix_incident_id
        }
        results = call_fn_bigfix_assets_function(circuits_app, function_params)
        assert (expected_results_1 == results.get("content")["status"])
        assert (expected_results_2 == results.get("content")["att_name"])
