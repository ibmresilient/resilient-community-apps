# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_playbook_utils"
FUNCTION_NAME = "pb_export_playbook"
SAMPLE_PLAYBOOK = "Sample Playbook"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
#resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

PLAYBOOK_B64 = """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"""


def call_function(circuits, function_name, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction(function_name, function_params)

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
        event = circuits.watcher.wait(f"{function_name}_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestPbExportPlaybook:
    """ Tests for the pb_export_playbook function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None


    mock_import_inputs_1 = { 
        "pbm_body": PLAYBOOK_B64,
        "pbm_base64_content": True
    }

    @pytest.mark.livetest
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_import_inputs_1, None)
    ])
    def test_import_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_function(circuits_app, "pb_import_playbook", mock_inputs)
        assert(results.get("success"))

    mock_export_inputs_1 = {
        "pbm_id": None,
        "pbm_name": "Sample Playbook"
    }

    expected_export_results_2 = {"value": "xyz"}

    @pytest.mark.livetest
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_export_inputs_1, None)
    ])
    def test_export_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_function(circuits_app, "pb_export_playbook", mock_inputs)
        assert(results.get("success"))

    mock_get_inputs_1 = {
        "pbm_type": "enabled",
        "pbm_name_contains": None
    }

    mock_get_inputs_2 = {
        "pbm_type": "draft",
        "pbm_name_contains": "nothing should match"
    }

    @pytest.mark.livetest
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_get_inputs_1, None),
        (mock_get_inputs_2, {}),
    ])
    def test_get_playbooks_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_function(circuits_app, "pb_get_playbooks", mock_inputs)
        assert(results)
        if expected_results:
            assert(results['content'] == expected_results)
