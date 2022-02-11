# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
import mock
from .mock_artifact import mock_successful_result
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_abuseipdb"
FUNCTION_NAME = "fn_abuseipdb"

# Read the default configuration-data section from the package
# Fill in key to run livetests
config_data = """[fn_abuseipdb]
abuseipdb_url=https://api.abuseipdb.com/api/v2/check
abuseipdb_key=$ABUSEIPDB_KEY
ignore_white_listed=True
"""

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_abuseipdb_function(circuits, function_params, timeout=10):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("fn_abuseipdb", function_params)

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
        event = circuits.watcher.wait("fn_abuseipdb_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value

class TestFnAbuseipdb:
    """ Tests for the fn_abuseipdb function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "abuseipdb_artifact_type": "IP Address",
        "abuseipdb_artifact_value": "8.8.8.8"
    }

    expected_results = {"success": True}

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """
        with mock.patch('fn_abuseipdb.components.funct_fn_abuseipdb.AppFunctionComponent') as mock_execute:
            mock_execute.rc.execute.return_value = mock_successful_result
            results = call_fn_abuseipdb_function(circuits_app, mock_inputs)
            assert(expected_results.get('success') == results.get('success'))

    artifact = {
        "abuseipdb_artifact_type": "IP Address",
        "abuseipdb_artifact_value": "8.8.8.8"
    }
    @pytest.mark.parametrize("mock_inputs, expected_results", [ 
        (artifact, True)
    ])
    @pytest.mark.livetest
    def test_live_isPublic(self, circuits_app, mock_inputs, expected_results):
        results = call_fn_abuseipdb_function(circuits_app, mock_inputs)
        assert results.get('content').get('data').get('isPublic') == expected_results