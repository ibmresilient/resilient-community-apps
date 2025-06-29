# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from .mock_attachment import AttachmentMock
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_soar_utils"
FUNCTION_NAME = "soar_utils_get_contact_info"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the SOAR REST API (uncomment to connect to a real appliance)
# resilient_mock = "pytest_resilient_circuits.BasicResilientMock"
resilient_mock = AttachmentMock

def call_utilities_get_contact_info(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("soar_utils_get_contact_info", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("soar_utils_get_contact_info_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value

class TestSoarUtilsGetContactInfo:
    """ Tests for the utilities_get_contact_info function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("incident_id, task_id, expected_results", [
        (2095, None, {'owner': {'owner_type': 'unknown', 'owner_info': None}, 'members': []})
    ])

    def test_success(self, circuits_app, incident_id, task_id, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = {
            "incident_id": incident_id,
            "task_id": task_id
        }
        results = call_utilities_get_contact_info(circuits_app, function_params)
        assert(expected_results == results)
