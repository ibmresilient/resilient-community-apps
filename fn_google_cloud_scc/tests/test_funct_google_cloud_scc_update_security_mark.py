# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""
from unittest.mock import MagicMock, patch

import pytest
from resilient_circuits import FunctionResult, SubmitTestFunction
from resilient_circuits.util import get_config_data, get_function_definition

PACKAGE_NAME = "fn_google_cloud_scc"
FUNCTION_NAME = "google_cloud_scc_update_security_mark"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_google_cloud_scc_update_security_mark_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("google_cloud_scc_update_security_mark", function_params)

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
        event = circuits.watcher.wait("google_cloud_scc_update_security_mark_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestGoogleCloudSccUpdateSecurityMark:
    """ Tests for the google_cloud_scc_update_security_mark function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "google_scc_update_key": "IBM_SOAR_ID",
        "google_scc_update_value": "101",
        "google_scc_finding_name": "test_name"
    }

    mock_marks = {
        "IBM_SOAR_ID": "101",
        "ANOTHER": "MARK"
    }

    expected_results_1 =  {
        "updated_key": "IBM_SOAR_ID", 
        "updated_value": "101", 
        "updated_marks": mock_marks
    }

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        with patch("fn_google_cloud_scc.components.funct_google_cloud_scc_update_security_mark.GoogleSCCCommon") as mock_scc_common:
            mock_app_common_instance = MagicMock()
            mock_app_common_instance.update_security_mark.return_value = (self.mock_marks, None)
            mock_scc_common.return_value = mock_app_common_instance

            results = call_google_cloud_scc_update_security_mark_function(circuits_app, mock_inputs)
            assert(expected_results == results.get("content"))
