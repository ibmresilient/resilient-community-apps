# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from sn_test_helper import *

PACKAGE_NAME = "fn_service_now"
FUNCTION_NAME = "sn_utilities_add_attachment_to_servicenow_record"

# Get mock config data
config_data = get_mock_config_data()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = SNResilientMock

def call_sn_utilities_add_attachment_to_servicenow_record_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("sn_utilities_add_attachment_to_servicenow_record", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("sn_utilities_add_attachment_to_servicenow_record_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestSnUtilitiesAddAttachmentToServicenowRecord:
    """ Tests for the sn_utilities_add_attachment_to_servicenow_record function"""

    inputs = {
      "attachment_id": 1,
      "incident_id": 1001,
      "task_id": 2002
    }

    output = {
      "inputs": inputs,
      "success": True,
      "res_id": "RES-1001-2002",
      "sn_ref_id": "INC123456",
      "attachment_name": u"Mock Attachment Name",
      "sn_attachment_sys_id": "c1ea807ddb82230044ccd426ca961937"
    }

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("inputs, expected_results", [(inputs, output)])
    def test_success(self, circuits_app, inputs, expected_results):
        """ Test calling with sample values for the parameters """

        mock_response = {'attachment_id': 'c1ea807ddb82230044ccd426ca961937', 'sn_ref_id': 'INC0010459'}

        ResilientHelper.sn_POST = MagicMock(return_value=mock_response)

        results = call_sn_utilities_add_attachment_to_servicenow_record_function(circuits_app, inputs)
        assert(expected_results == results)