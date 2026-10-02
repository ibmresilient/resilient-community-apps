# -*- coding: utf-8 -*-
# Generated with resilient-sdk v51.0.5.0.1475
"""Tests using pytest_resilient_circuits"""

import pytest, helper
from unittest.mock import patch
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

FUNCTION_NAME = "bitsight_cyber_insurance_get_portfolio_details"

# Read the default configuration-data section from the package
config_data = helper.config

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_bitsight_cyber_insurance_get_portfolio_details_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("bitsight_cyber_insurance_get_portfolio_details", function_params)

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
        event = circuits.watcher.wait("bitsight_cyber_insurance_get_portfolio_details_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestBitsightCyberInsuranceGetPortfolioDetails:
    """ Tests for the bitsight_cyber_insurance_get_portfolio_details function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(helper.PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "bitsight_ci_countries": "sample text",
        "bitsight_ci_risk_vectors_grade": "sample text",
        "bitsight_ci_limit": 123,
        "bitsight_ci_filter_group": "risk_vectors",
        "bitsight_ci_relationship_slug": "vendor",
        "bitsight_ci_exclude_subscription_type_slug": "sample text",
        "bitsight_ci_software_name": "sample text",
        "bitsight_ci_vendor_action_plan": "monitor",
        "bitsight_ci_open_ports": "sample text",
        "bitsight_ci_rating_type": "CURATED",
        "bitsight_ci_offset": 123,
        "bitsight_ci_subscription_type_slug": "applicants",
        "bitsight_ci_industry": "sample text",
        "bitsight_ci_products": "sample text",
        "bitsight_ci_product_types": "sample text",
        "bitsight_ci_risk_vectors_slug": "sample text",
        "bitsight_ci_rating_gte": 123,
        "bitsight_ci_rating": 123,
        "bitsight_ci_rating_lte": 123,
        "bitsight_ci_rating_lt": 123,
        "bitsight_ci_infections": "sample text",
        "bitsight_ci_providers": "sample text",
        "bitsight_ci_software_category": "Supported",
        "bitsight_ci_security_incident_categories": "breach",
        "bitsight_ci_tier": "sample text",
        "bitsight_ci_life_cycle_slug": "onboarding",
        "bitsight_ci_rating_gt": 123,
        "bitsight_ci_vulnerabilities": "sample text",
        "bitsight_ci_folder_guid": "sample text",
        "bitsight_ci_industry_slug": "sample text"
    }

    expected_results_1 = helper.get_portfolio_details_results

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """
        with patch("fn_bitsight_cyber_insurance.components.funct_bitsight_cyber_insurance_get_portfolio_details.bitsight_client") as patch_ack:
            patch_ack.return_value = helper.mock_init()
            results = call_bitsight_cyber_insurance_get_portfolio_details_function(circuits_app, mock_inputs)
            assert(expected_results == results.get("content"))
