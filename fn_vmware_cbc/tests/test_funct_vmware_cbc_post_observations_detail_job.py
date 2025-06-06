# -*- coding: utf-8 -*-
# Generated with resilient-sdk v52.0.0.0.927
"""Tests using pytest_resilient_circuits"""

import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_vmware_cbc"
FUNCTION_NAME = "vmware_cbc_post_observations_detail_job"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_vmware_cbc_post_observations_detail_job_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("vmware_cbc_post_observations_detail_job", function_params)

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
        event = circuits.watcher.wait("vmware_cbc_post_observations_detail_job_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestVmwareCbcPostObservationsDetailJob:
    """ Tests for the vmware_cbc_post_observations_detail_job function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "observations ={ 'alert_id': '3680c6ba-c645-6779-3976-f9ed69326ca1' }"
    }

    expected_results_1 =   {"content": {"results": [{"alert_category": ["THREAT"],"alert_id": ["3680c6ba-c645-6779-3976-f9ed69326ca1"]}]}}

    @pytest.mark.livetest
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_vmware_cbc_post_observations_detail_job_function(circuits_app, mock_inputs)
        assert(expected_results.get("content") == results.get("content"))
