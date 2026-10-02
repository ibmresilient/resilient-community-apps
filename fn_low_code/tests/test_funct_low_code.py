# -*- coding: utf-8 -*-
# Generated with resilient-sdk v51.0.1.1.1.dev16+g03d1460d
"""Tests using pytest_resilient_circuits"""

import pytest
import json
import os
import uuid
from mock import patch
from unittest.mock import patch
from mocks.subscription_mocks import ConnectorResilientMock
from circuits import Event
from resilient_circuits import LowCodeMessage, LowCodeResult
from resilient_circuits.util import get_config_data

PACKAGE_NAME = "fn_low_code"
FUNCTION_NAME = "low_code"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
#resilient_mock = "pytest_resilient_circuits.BasicResilientMock"
resilient_mock = ConnectorResilientMock

VIRUSTOTAL_JSON = json.loads(open(os.path.join(os.path.dirname(__file__), "data", "test_virustotal.json"), "r").read())

PET_JSON = json.loads(open(os.path.join(os.path.dirname(__file__), "data", "test_put_pet.json"), "r").read())

class SubmitTestLowCode(Event):
    """ Circuits event to insert a test Function Message """
    def __init__(self, lowcode_name, lowcode_params):
        if not lowcode_name or not isinstance(lowcode_params, dict):
            raise ValueError("lowcode_name and lowcode_params are required")
        msg_id = str(uuid.uuid4())
        super(SubmitTestLowCode, self).__init__(queue=lowcode_name, msg_id=msg_id, message=lowcode_params)

def call_low_code_function(circuits, lowcode_params, timeout=5):
    # Create the SubmitTestLowCode event
    evt = LowCodeMessage(queue_name="low_code",
                            headers=lowcode_params["headers"],
                            message=lowcode_params["message"],
                            frame=lowcode_params)

    # Fire a message to the function
    circuits.manager.fire(evt, "low_code")

    # circuits will fire an "exception" event if an exception is raised in the FunctionComponent
    # return this exception if it is raised
    exception_event = circuits.watcher.wait("exception", parent=None, timeout=timeout)

    if exception_event is not False:
        exception = exception_event.args[1]
        raise exception
    # else return the FunctionComponent's results
    else:
        event = circuits.watcher.wait("low_code_success", parent=evt, timeout=timeout)
        assert event
        lowcode_result = event.parent.value.getValue()[0]
        assert isinstance(lowcode_result, LowCodeResult)
        pytest.wait_for(event, "complete", True)
        return lowcode_result

class MockedResponse(LowCodeResult):
    def __init__(self):
        self.success = True
        self.status_code = 200
        self.text = '{"content": "mock data"}'

    def json(self):
        return {"content": "mock data"}

class TestLowCode:
    """ Tests for the low_code function"""

    mock_inputs_1 = VIRUSTOTAL_JSON

    expected_results_1 = {
        "content": "",
        "status_code": 200
    }

    #@pytest.mark.livetest
    @patch("resilient_lib.RequestsCommon.execute")
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1)
    ])
    def test_success(self, mock_response, circuits_app, mock_inputs, expected_results):
        mock_response.return_value = MockedResponse()

        """ Test calling with sample values for the parameters """
        results = call_low_code_function(circuits_app, mock_inputs)
        assert(expected_results.get("status_code") == results.value.get("status_code"))

    @pytest.mark.livetest
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (PET_JSON, {})
    ])
    def test_pet(self, circuits_app, mock_inputs, expected_results):
        results = call_low_code_function(circuits_app, mock_inputs)
        assert results.success
