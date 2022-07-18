# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from unittest.mock import MagicMock, patch

import pytest
from fn_google_cloud_scc.util.scc_common import PACKAGE_NAME, FindingResult, GoogleSCCCommon
from google.cloud.securitycenter import Finding, ListFindingsResponse
from resilient_circuits import FunctionResult, SubmitTestFunction
from resilient_circuits.util import get_config_data, get_function_definition

from .data.mock_objs import findings, updated_findings, config_data_str

FUNCTION_NAME = "google_cloud_scc_update_finding"

config_data = config_data_str

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_google_cloud_scc_update_finding_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("google_cloud_scc_update_finding", function_params)

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
        event = circuits.watcher.wait("google_cloud_scc_update_finding_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestGoogleCloudSccUpdateFinding:
    """ Tests for the google_cloud_scc_update_finding function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "google_scc_filter": "name = \"test\"",
        "google_scc_update_key": "next_steps",
        "google_scc_update_value": "Nothing to do next"
    }

    expected_results_1 = {
        "findings_list": [{"finding": updated_findings[0].get("finding")}],
        "updated_key": "next_steps",
        "updated_value": "Nothing to do next"
    }

    mock_inputs_2 = {
        "google_scc_filter": "name = \"test\"",
        "google_scc_update_key": "source_properties.prop_a",
        "google_scc_update_value": "test"
    }

    expected_results_2 = {
        "findings_list": [{"finding": updated_findings[0].get("finding")}],
        "updated_key": "source_properties.prop_a",
        "updated_value": "test"
    }

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1),
        (mock_inputs_2, expected_results_2)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        with patch("fn_google_cloud_scc.components.funct_google_cloud_scc_update_finding.GoogleSCCCommon") as mock_scc_common:
            mock_app_common_instance = MagicMock()

            mock_app_common_instance.get_findings.return_value = [ListFindingsResponse.ListFindingsResult(findings[0], ignore_unknown_fields=True)]
            mock_app_common_instance.update_finding.return_value = Finding(updated_findings[0].get("finding"), ignore_unknown_fields=True)
            mock_app_common_instance.enrich_finding.return_value = updated_findings[0].get("finding")
            mock_scc_common.return_value = mock_app_common_instance

            results = call_google_cloud_scc_update_finding_function(circuits_app, mock_inputs)
            assert(expected_results == results.get("content"))
