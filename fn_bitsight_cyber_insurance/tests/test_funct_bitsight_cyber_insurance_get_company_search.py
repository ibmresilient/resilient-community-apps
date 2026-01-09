# -*- coding: utf-8 -*-
# Generated with resilient-sdk v51.0.5.0.1475
"""Tests using pytest_resilient_circuits"""

import pytest, helper
from unittest.mock import patch
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

FUNCTION_NAME = "bitsight_cyber_insurance_get_company_search"

# Read the default configuration-data section from the package
config_data = helper.config

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_bitsight_cyber_insurance_get_company_search_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("bitsight_cyber_insurance_get_company_search", function_params)

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
        event = circuits.watcher.wait("bitsight_cyber_insurance_get_company_search_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value

class TestBitsightCyberInsuranceGetCompanySearch:
    """ Tests for the bitsight_cyber_insurance_get_company_search function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(helper.PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "bitsight_ci_limit": 100,
        "bitsight_ci_in_portfolio": True,
        "bitsight_ci_offset": 0,
        "bitsight_ci_domain": "test domain"
    }

    expected_results_1 = helper.get_company_search_results

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """
        with patch("fn_bitsight_cyber_insurance.components.funct_bitsight_cyber_insurance_get_company_search.bitsight_client") as patch_ack:
            patch_ack.return_value = helper.mock_init()
            results = call_bitsight_cyber_insurance_get_company_search_function(circuits_app, mock_inputs)
            assert(expected_results == results.get("content", []))
