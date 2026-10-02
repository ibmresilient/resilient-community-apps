# -*- coding: utf-8 -*-
# Generated with resilient-sdk v51.0.5.0.1475
"""Tests using pytest_resilient_circuits"""

import pytest, helper
from unittest.mock import patch
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

FUNCTION_NAME = "bitsight_cyber_insurance_get_finding_details"

# Read the default configuration-data section from the package
config_data = helper.config

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def call_bitsight_cyber_insurance_get_finding_details_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("bitsight_cyber_insurance_get_finding_details", function_params)

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
        event = circuits.watcher.wait("bitsight_cyber_insurance_get_finding_details_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value

class TestBitsightCyberInsuranceGetFindingDetails:
    """ Tests for the bitsight_cyber_insurance_get_finding_details function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(helper.PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "bitsight_ci_last_remediation_status_date": 1518480000000,
        "bitsight_ci_last_remediation_status_date_lt": 1518480000000,
        "bitsight_ci_last_seen_lte": 1518480000000,
        "bitsight_ci_assets_combined_importance": "low",
        "bitsight_ci_offset": 123,
        "bitsight_ci_first_seen": 1518480000000,
        "bitsight_ci_affects_rating": True,
        "bitsight_ci_assets_asset": "sample text",
        "bitsight_ci_details_grade_lt": "GOOD",
        "bitsight_ci_last_remediation_status_date_lte": 1518480000000,
        "bitsight_ci_vulnerabilities": "sample text",
        "bitsight_ci_last_remediation_status_date_gte": 1518480000000,
        "bitsight_ci_first_seen_gte": 1518480000000,
        "bitsight_ci_last_remediation_status_date_gt": 1518480000000,
        "bitsight_ci_last_seen_lt": 1518480000000,
        "bitsight_ci_first_seen_lte": 1518480000000,
        "bitsight_ci_attributed_companies_guid": "sample text",
        "bitsight_ci_details_infection_family": "sample text",
        "bitsight_ci_last_seen_gte": 1518480000000,
        "bitsight_ci_affects_rating_details": "AFFECTS_RATING",
        "bitsight_ci_details_observed_ips_contains": "sample text",
        "bitsight_ci_attributed_companies_name": "sample text",
        "bitsight_ci_first_seen_lt": 1518480000000,
        "bitsight_ci_details_grade_gt": "GOOD",
        "bitsight_ci_first_seen_gt": 1518480000000,
        "bitsight_ci_unsampled": True,
        "bitsight_ci_last_seen": 1518480000000,
        "bitsight_ci_evidence_key": "sample text",
        "bitsight_ci_remediation_assignments": "sample text",
        "bitsight_ci_tags_contains": "sample text",
        "bitsight_ci_assets_hosted_by": "sample text",
        "bitsight_ci_assets_category": "low",
        "bitsight_ci_details_grade": "GOOD",
        "bitsight_ci_last_remediation_status_label": "No Status",
        "bitsight_ci_details_vulnerabilities_severity": "minor",
        "bitsight_ci_company_guid": "sample text",
        "bitsight_ci_risk_vector_label": "sample text",
        "bitsight_ci_last_seen_gt": 1518480000000,
        "bitsight_ci_limit": 123,
        "bitsight_ci_expand_findings": "attributed_companies"
    }

    expected_results_1 = helper.get_finding_details_results

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """
        with patch("fn_bitsight_cyber_insurance.components.funct_bitsight_cyber_insurance_get_finding_details.bitsight_client") as patch_ack:
            patch_ack.return_value = helper.mock_init()
            results = call_bitsight_cyber_insurance_get_finding_details_function(circuits_app, mock_inputs)
            assert(expected_results == results.get("content"))
