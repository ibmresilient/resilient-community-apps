# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
import mock
from .mock_artifact import MockedResponse
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_yeti"
FUNCTION_NAME = "fn_yeti"

# Read the default configuration-data section from the package
config_data = """[fn_yeti]
urlbase=http://localhost:8080/api
username=yeti
password=
api_key=dda39a89be602a714ca2dd834582509585ab0b146a1094d385226988e0a67398e646acc08f6f3738"""

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_yeti_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("fn_yeti", function_params)

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
        event = circuits.watcher.wait("fn_yeti_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestFnYeti:
    """ Tests for the fn_yeti function"""

    
    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs = {
        "yeti_artifact_type": "File Path",
        "yeti_artifact_value": "C:\\Users\\admin\\AppData\\Roaming\\Adada\\stolen.dat"
    }

    expected_results = {"success": True}
    @pytest.mark.parametrize("mock_inputs, expected_results", [

        (mock_inputs, expected_results)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """
        with mock.patch("pyeti.YetiApi") as mock_execute:
            mock_execute.return_value = MockedResponse()
            results = call_fn_yeti_function(circuits_app, mock_inputs)
            assert(expected_results.get('success') == results.get('success'))

    @pytest.mark.parametrize("mock_inputs, expected_results", [ 
        (mock_inputs, True)
    ])
    @pytest.mark.livetest
    def test_live_isPublic(self, circuits_app, mock_inputs, expected_results):
        results = call_fn_yeti_function(circuits_app, mock_inputs)
        assert results.get('success') == expected_results