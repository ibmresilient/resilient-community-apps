# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2026. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.2.1096
"""Tests using pytest_resilient_circuits"""

from unittest.mock import patch
import pytest
from fn_watsonx_analyst.util.FileParser import FileParser
from tests import helper
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_watsonx_analyst"
FUNCTION_NAME = "fn_watsonx_analyst_scan_artifact"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_watsonx_analyst_scan_artifact_function(
    circuits, function_params, timeout=5
):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("fn_watsonx_analyst_scan_artifact", function_params)

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
        event = circuits.watcher.wait(
            "fn_watsonx_analyst_scan_artifact_result", parent=evt, timeout=timeout
        )
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


@patch("fn_watsonx_analyst.util.rest.RestHelper.do_request", helper.mock_do_request)
class TestFnWatsonxScanArtifact:
    """Tests for the fn_watsonx_analyst_scan_artifact function"""

    cold_mem_limit = "40 MB"

    def test_function_definition(self):
        """Test that the package provides customization_data that defines the function"""
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "fn_watsonx_analyst_incident_id": 123,
        "fn_watsonx_analyst_artifact_id": 1411,
        "fn_watsonx_analyst_model_id": "mistralai/mistral-small-3-1-24b-instruct-2503",
        "fn_watsonx_analyst_system_prompt": "sample text",
    }

    expected_results_1 = (
        'Artifact name: runme2.sh\n\n<p style="display: inline">Lorem ipsum</p>'
    )

    mock_inputs_2 = {
        "fn_watsonx_analyst_incident_id": 123,
        "fn_watsonx_analyst_artifact_id": 1412,
        "fn_watsonx_analyst_model_id": "mistralai/mistral-small-3-1-24b-instruct-2503",
        "fn_watsonx_analyst_system_prompt": "sample text",
    }

    expected_results_2 = (
        "Artifact name: image.png\n\n" + FileParser.PARSED_CONTENT_EMPTY
    )

    mock_inputs_3 = {
        "fn_watsonx_analyst_incident_id": 123,
        "fn_watsonx_analyst_artifact_id": 1413,
        "fn_watsonx_analyst_model_id": "mistralai/mistral-small-3-1-24b-instruct-2503",
    }

    expected_results_3 = (
        'Artifact name: 128.210.157.251\n\n<p style="display: inline">Lorem ipsum</p>'
    )

    @pytest.mark.parametrize(
        "mock_inputs, expected_results",
        [(mock_inputs_1, expected_results_1), (mock_inputs_2, expected_results_2)],
    )
    @pytest.mark.limit_memory(cold_mem_limit)
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """Test calling with sample values for the parameters"""

        results = call_fn_watsonx_analyst_scan_artifact_function(
            circuits_app, mock_inputs
        )
        assert results["content"]["generated_text"].strip() == expected_results

    @pytest.mark.limit_memory(cold_mem_limit)
    def test_metadata_artifact(self, circuits_app):
        """Test scanning a metadata artifact (IP address)"""
        results = call_fn_watsonx_analyst_scan_artifact_function(
            circuits_app, self.mock_inputs_3
        )
        assert "Artifact name: 128.210.157.251" in results["content"]["generated_text"]
        assert results["success"] is True

    @pytest.mark.limit_memory(cold_mem_limit)
    def test_value_error_handling(self, circuits_app):
        """Test that ValueError is properly handled"""
        from unittest.mock import patch, MagicMock
        from fn_watsonx_analyst.components.funct_fn_watsonx_analyst_scan_artifact import scan_artifact_or_attachment
        
        # Mock to raise ValueError
        with patch('fn_watsonx_analyst.components.funct_fn_watsonx_analyst_scan_artifact.scan_artifact_or_attachment') as mock_scan:
            mock_scan.side_effect = ValueError("Test error message")
            
            mock_inputs = {
                "fn_watsonx_analyst_incident_id": 123,
                "fn_watsonx_analyst_artifact_id": 1411,
                "fn_watsonx_analyst_model_id": "mistralai/mistral-small-3-1-24b-instruct-2503",
            }
            
            with pytest.raises(Exception) as exc_info:
                call_fn_watsonx_analyst_scan_artifact_function(circuits_app, mock_inputs)
            
            # Verify the error was raised
            assert "Test error message" in str(exc_info.value) or "Unable to generate artifact summary" in str(exc_info.value)

    @pytest.mark.limit_memory(cold_mem_limit)
    def test_watsonx_api_exception_handling(self, circuits_app):
        """Test that WatsonxApiException is properly handled"""
        from unittest.mock import patch
        from fn_watsonx_analyst.util.errors import WatsonxApiException
        
        # Mock to raise WatsonxApiException
        with patch('fn_watsonx_analyst.components.funct_fn_watsonx_analyst_scan_artifact.scan_artifact_or_attachment') as mock_scan:
            mock_scan.side_effect = WatsonxApiException("API error occurred")
            
            mock_inputs = {
                "fn_watsonx_analyst_incident_id": 123,
                "fn_watsonx_analyst_artifact_id": 1411,
                "fn_watsonx_analyst_model_id": "mistralai/mistral-small-3-1-24b-instruct-2503",
            }
            
            with pytest.raises(Exception) as exc_info:
                call_fn_watsonx_analyst_scan_artifact_function(circuits_app, mock_inputs)
            
            # Verify the error was raised
            assert "API error occurred" in str(exc_info.value) or "Unable to generate artifact summary" in str(exc_info.value)

    @pytest.mark.limit_memory(cold_mem_limit)
    def test_generic_exception_handling(self, circuits_app):
        """Test that generic exceptions are properly handled"""
        from unittest.mock import patch
        
        # Mock to raise generic Exception
        with patch('fn_watsonx_analyst.components.funct_fn_watsonx_analyst_scan_artifact.scan_artifact_or_attachment') as mock_scan:
            mock_scan.side_effect = RuntimeError("Unexpected error")
            
            mock_inputs = {
                "fn_watsonx_analyst_incident_id": 123,
                "fn_watsonx_analyst_artifact_id": 1411,
                "fn_watsonx_analyst_model_id": "mistralai/mistral-small-3-1-24b-instruct-2503",
            }
            
            with pytest.raises(Exception) as exc_info:
                call_fn_watsonx_analyst_scan_artifact_function(circuits_app, mock_inputs)
            
            # Verify the error was raised
            assert "Unexpected error" in str(exc_info.value) or "Unable to generate artifact summary" in str(exc_info.value)

    def test_scan_artifact_or_attachment_missing_ids(self):
        """Test that ValueError is raised when both art_id and att_id are None"""
        from fn_watsonx_analyst.components.funct_fn_watsonx_analyst_scan_artifact import scan_artifact_or_attachment
        
        with pytest.raises(ValueError) as exc_info:
            scan_artifact_or_attachment(inc_id=123, art_id=None, att_id=None)
        
        assert "Either artifact or attachment ID must be provided" in str(exc_info.value)

    def test_scan_artifact_or_attachment_with_artifact(self):
        """Test scan_artifact_or_attachment with artifact ID"""
        from fn_watsonx_analyst.components.funct_fn_watsonx_analyst_scan_artifact import scan_artifact_or_attachment
        from unittest.mock import patch
        
        with patch('fn_watsonx_analyst.components.funct_fn_watsonx_analyst_scan_artifact._scan_artifact') as mock_scan:
            mock_scan.return_value = {"generated_text": "Test result", "success": True}
            
            result = scan_artifact_or_attachment(inc_id=123, art_id=1411, att_id=None)
            
            assert result["generated_text"] == "Test result"
            mock_scan.assert_called_once_with(123, 1411)

    def test_scan_artifact_or_attachment_with_attachment(self):
        """Test scan_artifact_or_attachment with attachment ID"""
        from fn_watsonx_analyst.components.funct_fn_watsonx_analyst_scan_artifact import scan_artifact_or_attachment
        from unittest.mock import patch
        
        with patch('fn_watsonx_analyst.components.funct_fn_watsonx_analyst_scan_artifact._scan_attachment') as mock_scan:
            mock_scan.return_value = {"generated_text": "Test attachment result", "success": True}
            
            result = scan_artifact_or_attachment(inc_id=123, art_id=None, att_id=456, task_id=789)
            
            assert result["generated_text"] == "Test attachment result"
            mock_scan.assert_called_once_with(123, 456, 789)
