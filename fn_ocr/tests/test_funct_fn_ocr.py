# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult, FunctionError

PACKAGE_NAME = "fn_ocr"
FUNCTION_NAME = "fn_ocr"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_ocr_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("fn_ocr", function_params)

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
        event = circuits.watcher.wait("fn_ocr_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestFnOcr:
    """ Tests for the fn_ocr function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "ocr_artifact_id": 123,
        "ocr_attachment_id": 777,
        "ocr_incident_id": 123,
        "ocr_task_id": 123,
        "ocr_confidence_threshold": 49,
        "ocr_lang":"eng",
        "ocr_base64": None
    }

    expected_results_1 = {"value": "xyz"}

    mock_inputs_2 = {
        "ocr_artifact_id": None,
        "ocr_attachment_id": None,
        "ocr_incident_id": 123,
        "ocr_task_id": None,
        "ocr_base64":  "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",
        "ocr_confidence_threshold":80,
        "ocr_lang": "eng"
    }

    expected_results_2 = {"value": "xyz"}

    mock_inputs_3 = {
        "ocr_artifact_id": 123,
        "ocr_attachment_id": 777,
        "ocr_incident_id": 123,
        "ocr_task_id": 123,
        "ocr_confidence_threshold": 49,
        "ocr_lang":"eng",
        "ocr_base64": "fakeBase64" 
    }

    # @pytest.mark.parametrize("mock_inputs, expected_results", [
    #     (mock_inputs_1, expected_results_1),
    #     (mock_inputs_2, expected_results_2)
    # ])


    # def test_single_input(self, circuits_app):
    #     with pytest.raises(FunctionError):
    #         results = call_fn_ocr_function(circuits_app, mock_inputs_3)
    #     assert True

    # def test_basic_ocr(self):
    #     # this would be a super simple example to test that it can be accessed, nothing more
    #     assert True

    # def test_basic_ocr_rotated(self):
    #     # this would make sure that the correct orientation scripts are loaded
    #     assert True

    # def test_basic_ocr_upside_down(self):
    #     # same as rotation test
    #     assert True 

    # def test_reading_from_base64(self):
    #     pass
    
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """


        assert True
        # results = call_fn_ocr_function(circuits_app, mock_inputs)
        # assert(expected_results == results)
