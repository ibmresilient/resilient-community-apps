# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""
from unittest.mock import patch

import pytest
from resilient_circuits import FunctionResult, SubmitTestFunction
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_lib import IntegrationError

PACKAGE_NAME = "fn_darktrace"
FUNCTION_NAME = "darktrace_get_devices"

# Read the default configuration-data section from the package
config_data = """[fn_darktrace]
api_key=abcd-efgh
api_secret=1234-abcd-56789-efgh
darktrace_base_url=https://fake.cloud.darktrace.com
"""

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_darktrace_get_devices_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("darktrace_get_devices", function_params)

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
        event = circuits.watcher.wait("darktrace_get_devices_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestDarktraceGetDevices:
    """ Tests for the darktrace_get_devices function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "darktrace_incident_group_id": "1234-abcd-5678-efgh"
    }

    expected_results_1 = {
        "devices": "some device details",
        "base_device_url": "https://fake.cloud.darktrace.com/#device/"
    }

    expected_results_2 = {
        "devices": "details details",
        "base_device_url": "https://fake.cloud.darktrace.com/#device/"
    }

    @patch("fn_darktrace.components.funct_darktrace_list_similar_devices.AppCommon.get_incident_groups")
    @patch("fn_darktrace.components.funct_darktrace_list_similar_devices.AppCommon.get_devices")
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1),
        (mock_inputs_1, expected_results_2)
    ])
    def test_success(self, patch_get_devices, patch_get_incident_group, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        patch_get_incident_group.return_value = [{"devices": [1,2,3,4]}]
        patch_get_devices.return_value = expected_results.get("devices")

        results = call_darktrace_get_devices_function(circuits_app, mock_inputs)
        assert(expected_results == results.get("content"))
        patch_get_incident_group.assert_called_with({"groupid": mock_inputs.get("darktrace_incident_group_id")})
        patch_get_devices.assert_called_with({"did": "1,2,3,4,", "includetags": "true"})


    incident_group_results_1 = [ # test failure of too many 
        {"devices": [1,2,3,4]},
        {"devices": [5,6,7,8,9]}
    ]
    incident_group_results_2 = [ ]# test failure of not enough

    @patch("fn_darktrace.components.funct_darktrace_list_similar_devices.AppCommon.get_incident_groups")
    @pytest.mark.parametrize("mock_inputs, incident_group_results", [
        (mock_inputs_1, incident_group_results_1),
        (mock_inputs_1, incident_group_results_2)
    ])
    def test_failure(self, patch_get_incident_group, circuits_app, mock_inputs, incident_group_results, caplog):
        

        patch_get_incident_group.return_value = incident_group_results

        with pytest.raises(IntegrationError):
            call_darktrace_get_devices_function(circuits_app, mock_inputs)

        assert "Multiple groups found" in caplog.text or "No groups found" in caplog.text

