# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import sys

import cv2
import pandas as pd
import pytesseract
import pytest
from mock import patch
from resilient_circuits import (BaseFunctionError, FunctionResult,
                                SubmitTestFunction)
from resilient_circuits.util import get_config_data, get_function_definition

PACKAGE_NAME = "fn_ocr"
FUNCTION_NAME = "fn_ocr"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_ocr_function(circuits, function_params, timeout=10):
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

    base64_test_strings = []
    with open(sys.path[0]+"/base64_test_strings.txt","r") as f:
        for line in f:
            if line[0] =="#":
                continue
            else:
                base64_test_strings.append(line.strip())
    
    mock_inputs_1 = {
        "ocr_artifact_id": 123,
        "ocr_attachment_id": None,
        "ocr_incident_id": 123,
        "ocr_task_id": 123,
        "ocr_confidence_threshold": 49,
        "ocr_language":"eng",
        "ocr_base64": None
    }

    mock_inputs_2 = {
        "ocr_artifact_id": None,
        "ocr_attachment_id": None,
        "ocr_incident_id": 123,
        "ocr_task_id": None,
        "ocr_base64": base64_test_strings[0],
        "ocr_confidence_threshold":80,
        "ocr_language": "eng"
    }

    mock_inputs_3 = {
        "ocr_artifact_id": 111,
        "ocr_attachment_id": 123,
        "ocr_incident_id": 123,
        "ocr_task_id": 123,
        "ocr_confidence_threshold": 49,
        "ocr_language":"eng",
        "ocr_base64": "fakeBase64" 
    }

    mock_inputs_4 = {
        "ocr_artifact_id": None,
        "ocr_attachment_id": None,
        "ocr_incident_id": 123,
        "ocr_task_id": None,
        "ocr_base64": base64_test_strings[1],
        "ocr_confidence_threshold":90,
        "ocr_language": "eng"
    }
    
    @patch("pytesseract.image_to_data")
    @pytest.mark.parametrize("mock_inputs", [(mock_inputs_3)])
    def test_double_input(self, mock_response, circuits_app,mock_inputs):
        # tests how the app handles getting both Base64 string and an artifact
        with pytest.raises(BaseFunctionError):
            results = call_fn_ocr_function(circuits_app, mock_inputs)
    
    def side_effect_1(img_rbg,output_type,config):
        # pytest mocked side_effect, which returns a dataframe similar to what tesseract would return
        path = sys.path[2] + "/SO_output.csv"
        bug = sys.path
        df = pd.read_csv(path)
        return df
    
    @pytest.mark.parametrize("mock_inputs", [(mock_inputs_4)])
    @patch.object(pytesseract,"image_to_data",side_effect = side_effect_1)
    def test_confidence_threshold(self, mock_request, circuits_app, mock_inputs):
        # tests to make sure that setting a confidence threshold returns only what is above that threshold
        result = call_fn_ocr_function(circuits_app,mock_inputs) 
        for res in result["content"]:
            assert float(res["confidence"]) >= mock_inputs["ocr_confidence_threshold"]

    @pytest.mark.parametrize("mock_inputs", [(mock_inputs_2)])
    @patch.object(pytesseract,"image_to_data",side_effect = side_effect_1)
    def test_df_processing(self,mock_request, circuits_app,mock_inputs):
        # tests the dataframe parsing lines of the app
        result = call_fn_ocr_function(circuits_app, mock_inputs)
        texts = result["content"]
        assert texts[0]["text"].split("\n")[0].strip() == "Python Script to convert Image into Byte array"
        assert texts[1]["text"].split("\n")[0].strip() == "lam writing a Python script where | want to do bulk photo upload. | want to read an Image and"

    @pytest.mark.livetest
    def test_basic_ocr(self):
        # tests that the OCR is functional
        path = sys.path[0] + "/../doc/screenshots/SO_title.png" 
        img = cv2.imread(path, cv2.IMREAD_COLOR) # What is the correct path?
        img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) # open-cv (cv2) defaults to BGR colors, we convert just in case
        lang = 'eng'
        text = pytesseract.image_to_string(img_rgb, config=f"-l {lang} --psm 1")
        assert text.split("\n")[0].strip() == "Python Script to convert Image into Byte array"
    
    @pytest.mark.livetest
    def test_basic_ocr_rotated(self):
        # tests that tesseract can correctly handle rotation
        path = sys.path[0] + "/../doc/screenshots/SO_title.png" 
        img = cv2.imread(path, cv2.IMREAD_COLOR) # What is the correct path?
        img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) # open-cv (cv2) defaults to BGR colors, we convert just in case
        lang = 'eng'
        text = pytesseract.image_to_string(img_rgb, config=f"-l {lang} --psm 1")
        assert text.split("\n")[0].strip() == "Python Script to convert Image into Byte array"
    
    @pytest.mark.livetest
    @pytest.mark.parametrize("mock_inputs", [(mock_inputs_2)])
    def test_reading_from_base64(self, circuits_app, mock_inputs):
       # tests reading directly from a base64 string
       result = call_fn_ocr_function(circuits_app, mock_inputs) 
       assert result["content"][0]["text"] == "Description" 
    
