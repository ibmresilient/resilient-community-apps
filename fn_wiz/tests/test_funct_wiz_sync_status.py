# -*- coding: utf-8 -*-
# Generated with resilient-sdk v51.0.1.0.695
"""Tests using pytest_resilient_circuits"""

import pytest
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from mock import patch

PACKAGE_NAME = "fn_wiz"
FUNCTION_NAME = "wiz_sync_status"

# Mock out configs
config_data = """[fn_wiz]
client_id=abcd-efgh
client_secret=abcdefg-hijklmno
endpoint_url=https://fake.app.wiz.com
api_url=https://wizapi.io/graphql
token_url=https://wizauth.io
polling_interval=0
polling_lookback=0
"""

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_wiz_sync_status_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("wiz_sync_status", function_params)

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
        event = circuits.watcher.wait("wiz_sync_status_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestWizSyncStatus:
    """ Tests for the wiz_sync_status function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "wiz_issue_id": "12345",
        "wiz_resolution_reason": "Resolved"
    }
    expected_results_1 = {"response": {}}

    mock_inputs_2 = {
        "wiz_issue_id": "12345",
        "wiz_resolution_reason": "Duplicate"
    }
    expected_results_2 = {"response": {}}

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1),
        (mock_inputs_2, expected_results_2)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """
        with patch("fn_wiz.components.funct_wiz_sync_status.AppCommon.sync_status_with_wiz") as mock_app_common:
            mock_app_common.return_value = expected_results.get('response')
            results = call_wiz_sync_status_function(circuits_app, mock_inputs)
            assert(expected_results == results.get('content'))
