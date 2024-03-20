# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from unittest.mock import patch

import pytest
from resilient_circuits import FunctionResult, SubmitTestFunction
from resilient_circuits.util import get_function_definition

PACKAGE_NAME = "fn_darktrace"
FUNCTION_NAME = "darktrace_add_device_tags"

config_data = """[fn_darktrace]
api_key=abcd-efgh
api_secret=1234-abcd-56789-efgh
darktrace_base_url=https://fake.cloud.darktrace.com
"""

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_darktrace_add_device_tags_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("darktrace_add_device_tags", function_params)

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
        event = circuits.watcher.wait("darktrace_add_device_tags_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestDarktraceAddDeviceTags:
    """ Tests for the darktrace_add_device_tags function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "darktrace_device_tags": "test1, test2",
        "darktrace_device_id": "1"
    }

    expected_results_1 = {"all_tags": ["test1","test2"],
                          "added_tags": ["test1","test2"],
                          "error_tags": []
                         }

    mock_inputs_2 = {
        "darktrace_device_tags": "test",
        "darktrace_device_id": "<a href='x.com' target='_blank'>1</a>"
    }

    expected_results_2 = {"all_tags": ["test"],
                          "added_tags": ["test"],
                          "error_tags": []
                         }

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1),
        (mock_inputs_2, expected_results_2)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        with patch("fn_darktrace.components.funct_darktrace_add_device_tags.AppCommon.add_tag_to_device") as patch_add_tags:
            with patch("fn_darktrace.components.funct_darktrace_add_device_tags.AppCommon.get_devices") as patch_get_devices:
                # on test success, we'll just force it to return a successfully with an empty dict
                patch_add_tags.return_value = {}
                # fill in the appropriate expected return format from "get_devices"
                patch_get_devices.return_value = {"tags": [{"name": tag} for tag in expected_results.get("all_tags")]}

                results = call_darktrace_add_device_tags_function(circuits_app, mock_inputs)
                assert(expected_results == results.get("content"))
                patch_add_tags.assert_called()



    mock_inputs_3 = {
        "darktrace_device_tags": "test1,already exists",
        "darktrace_device_id": "6"
    }

    expected_results_3 = {"all_tags": ["test1","already exists"],
                          "added_tags": ["test1"],
                          "error_tags": ["already exists"]
                         }

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_3, expected_results_3)
    ])
    def test_failure(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        with patch("fn_darktrace.components.funct_darktrace_add_device_tags.AppCommon.add_tag_to_device") as patch_add_tags:
            with patch("fn_darktrace.components.funct_darktrace_add_device_tags.AppCommon.get_devices") as patch_get_devices:

                # make it so that the patch returns a good result the first time, and fails the second time
                patch_add_tags.side_effect = [{}, {"tags": "DATANOTFOUND ERROR"}]
                # fill in the appropriate expected return format from "get_devices"
                patch_get_devices.return_value = {"tags": [{"name": tag} for tag in expected_results.get("all_tags")]}

                results = call_darktrace_add_device_tags_function(circuits_app, mock_inputs)
                assert(expected_results == results.get("content"))
                patch_add_tags.assert_called()
