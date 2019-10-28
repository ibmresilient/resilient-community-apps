# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import os
import pytest
import sys
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

if sys.version_info.major == 3:
    from unittest.mock import Mock, patch
else:
    from mock import Mock, patch

"""
pytest --resilient_app_config=/<path>/<to>/app.config tests/test_fn_log_capture.py
"""

PACKAGE_NAME = "fn_log_capture"
FUNCTION_NAME = "fn_log_capture"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def call_fn_log_capture_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_log_capture", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_log_capture_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnLogCapture:
    """ Tests for the fn_log_capture function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None



    @pytest.mark.parametrize("log_capture_maxlen, log_capture_date, log_capture_date_option, log_min_level, "
                             "incident_id", [
        (None, 1571684880000, None, "Debug", 123),
        (None, None, "before", "Debug", 123),
        (5, 1571684880000, None, "Debug", 123)
    ])
    @patch('fn_log_capture.components.funct_fn_log_capture.get_log_file_data')
    @patch('fn_log_capture.components.funct_fn_log_capture.write_file_attachment')
    def test_failure(self, mock_write_file_attachment, mock_get_log_file, circuits_app,
                     log_capture_maxlen, log_capture_date, log_capture_date_option,
                     log_min_level, incident_id):
        """ Test calling with sample values for the parameters """
        function_params = {
            "log_capture_maxlen": log_capture_maxlen,
            "log_capture_date": log_capture_date,
            "log_capture_date_option": log_capture_date_option,
            "log_min_level": log_min_level,
            "incident_id": incident_id
        }

        setup_get_log_file(mock_get_log_file)
        mock_write_file_attachment.return_value = {}

        with pytest.raises(Exception):
            results = call_fn_log_capture_function(circuits_app, function_params)

def setup_get_log_file(mock_function):
    log_dir = os.path.dirname(os.path.realpath(__file__))
    log_file = os.path.join(log_dir, "data", "sample.log")

    with open(log_file, "rb") as f:
        mock_function.return_value = f.readlines()