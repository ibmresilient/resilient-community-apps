# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use, line-too-long
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
import pytest
from mock import Mock
from test_helper import get_mock_config_data, get_mock_contain_device_results_content
from fn_crowdstrike_falcon.util.cs_helper import CrowdStrikeHelper

PACKAGE_NAME = "fn_crowdstrike_falcon"
FUNCTION_NAME = "fn_cs_falcon_device_actions"

config_data = get_mock_config_data()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_cs_falcon_device_actions_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("fn_cs_falcon_device_actions", function_params)

    # Add the workflow_instance_id
    evt.kwargs.get("message").update({
        "workflow_instance": {
            "workflow_instance_id": 123
        }
    })

    # Fire a message to the function
    circuits.manager.fire(evt)

    # circuits will fire an "exception" event if an exception is raised in the FunctionComponent
    # return this exception if it is raised
    exception_event = circuits.watcher.wait("exception", parent=None, timeout=timeout)

    if exception_event is not False:
        exception = exception_event.args[1].args[1]
        raise exception

    # else return the FunctionComponent's results
    else:
        event = circuits.watcher.wait("fn_cs_falcon_device_actions_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value

class TestFnCsFalconDeviceActions:
    """ Tests for the fn_cs_falcon_device_actions function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs = {
        "cs_device_id": None,
        "cs_action_name": None
    }

    @pytest.mark.parametrize("inputs", [(mock_inputs)])
    def test_cs_device_id_not_defined(self, circuits_app, inputs):
        """ test cs_device_id not defined """
        with pytest.raises(ValueError) as err:
            call_fn_cs_falcon_device_actions_function(circuits_app, inputs)

        assert err.value.args[0] == "'cs_device_id' is a mandatory function input"

    mock_inputs = {
        "cs_device_id": "xxxxxx",
        "cs_action_name": "contain"
    }

    @pytest.mark.parametrize("inputs", [(mock_inputs)])
    def test_first_POST_fails(self, circuits_app, inputs):
        """ test_first_POST_fails """

        mock_response_1 = {
            "error": True,
            "err_msg": "an unknown error occurred"
        }

        CrowdStrikeHelper.cs_api_request = Mock()
        CrowdStrikeHelper.cs_api_request.side_effect = [mock_response_1]

        with pytest.raises(ValueError) as err:
            call_fn_cs_falcon_device_actions_function(circuits_app, inputs)

        assert err.value.args[0] == "> Failed to contain device xxxxxx. an unknown error occurred"
        assert CrowdStrikeHelper.cs_api_request.call_count == 1

    @pytest.mark.parametrize("inputs", [(mock_inputs)])
    def test_invalid_bearer_token(self, circuits_app, inputs):
        """ test_invalid_bearer_token """

        mock_response_1 = {
            "error": True,
            "err_msg": "invalid bearer token"
        }

        mock_response_2 = {
            "error": True,
            "err_msg": "mock error message"
        }

        CrowdStrikeHelper.cs_api_request = Mock()
        CrowdStrikeHelper.cs_api_request.side_effect = [mock_response_1, mock_response_2]

        CrowdStrikeHelper.get_oauth2_token = Mock()
        CrowdStrikeHelper.get_oauth2_token.side_effect = ["MOCKTOKEN"]

        with pytest.raises(ValueError) as err:
            call_fn_cs_falcon_device_actions_function(circuits_app, inputs)

        assert err.value.args[0] == "> Failed to contain device xxxxxx. mock error message"
        assert CrowdStrikeHelper.cs_api_request.call_count == 2

    mock_output = {
        'inputs': {'cs_device_id': 'xxxxxx', 'cs_action_name': 'contain'},
        'success': True,
        'content': get_mock_contain_device_results_content()
    }

    @pytest.mark.parametrize("inputs, expected_results", [(mock_inputs, mock_output)])
    def test_contain_device(self, circuits_app, inputs, expected_results):
        """ test_contain_device """

        mock_response_1 = {
            "meta": "xxxxxx",
            "resources": [{
                "id": "xxxxxx"
            }]
        }

        mock_response_2 = {
            "status": "contained"
        }

        CrowdStrikeHelper.cs_api_request = Mock()
        CrowdStrikeHelper.cs_api_request.side_effect = [mock_response_1]

        CrowdStrikeHelper.get_device_status = Mock()
        CrowdStrikeHelper.get_device_status.side_effect = [mock_response_2]

        results = call_fn_cs_falcon_device_actions_function(circuits_app, inputs)

        assert CrowdStrikeHelper.cs_api_request.call_count == 1
        assert CrowdStrikeHelper.get_device_status.call_count == 1
        assert expected_results.get("inputs") == results.get("inputs")
        assert expected_results.get("success") == results.get("success")
        assert expected_results.get("content") == results.get("content")
