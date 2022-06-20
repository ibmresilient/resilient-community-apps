# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from unittest.mock import MagicMock, patch
from fn_google_cloud_scc.util.scc_common import GoogleSCCCommon

import pytest
from resilient_circuits import FunctionResult, SubmitTestFunction
from resilient_circuits.util import get_function_definition
from pytest_resilient_circuits import BasicResilientMock

from .data.mock_objs import findings

PACKAGE_NAME = "fn_google_cloud_scc"
FUNCTION_NAME = "google_scc_get_findings"

config_data = """[fn_google_cloud_scc]
google_application_credentials_path="fake/path"
google_cloud_organization_id=123456789
google_cloud_base_url=https://console.cloud.google.com
findings_filter=
polling_interval=10
polling_lookback=120
"""


# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_google_scc_get_findings_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("google_scc_get_findings", function_params)

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
        event = circuits.watcher.wait("google_scc_get_findings_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestGoogleSccGetFindings:
    """ Tests for the google_scc_get_findings function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "google_scc_filter": "name = \"test\"",
        "google_scc_close_case_on_change": False
    }

    expected_results_1 = {"findings_list": findings, "cases_closed_from_function": []}

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        with patch("fn_google_cloud_scc.components.funct_google_scc_get_findings.GoogleSCCCommon") as mock_scc_common:
            mock_app_common_instance = MagicMock()
            mock_app_common_instance.get_findings.return_value = findings
            mock_scc_common.return_value = mock_app_common_instance
            results = call_google_scc_get_findings_function(circuits_app, mock_inputs)
            assert(expected_results == results.get("content"))
