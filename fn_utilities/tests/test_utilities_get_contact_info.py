# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock_attachment import AttachmentMock
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_utilities"
FUNCTION_NAME = "utilities_get_contact_info"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
# resilient_mock = "pytest_resilient_circuits.BasicResilientMock"
resilient_mock = AttachmentMock


def call_utilities_get_contact_info(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("utilities_get_contact_info", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("utilities_get_contact_info_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestUtilitiesStringToAttachment:
    """ Tests for the utilities_get_contact_info function"""

    @pytest.mark.parametrize("incident_id, task_id, expected_results", [
        (2095, None, {'owner': None, 'members': []})
    ])

    def test_success(self, circuits_app, incident_id, task_id, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = {
            "incident_id": incident_id,
            "task_id": task_id
        }
        results = call_utilities_get_contact_info(circuits_app, function_params)
        assert(expected_results == results)