# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
import pytest
from mock import Mock
from test_helper import get_mock_config_data
from fn_crowdstrike_falcon.util.cs_helper import CrowdStrikeHelper

PACKAGE_NAME = "fn_crowdstrike_falcon"
FUNCTION_NAME = "fn_cs_falcon_get_devices_ioc_ran_on"

config_data = get_mock_config_data()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_cs_falcon_get_devices_ioc_ran_on_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_cs_falcon_get_devices_ioc_ran_on", function_params)
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
        event = circuits.watcher.wait("fn_cs_falcon_get_devices_ioc_ran_on_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestFnCsFalconGetDevicesIocRanOn:
    """ Tests for the fn_cs_falcon_get_devices_ioc_ran_on function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs = {
        "cs_ioc_type": None,
        "cs_ioc_value": "something",
        "cs_return_limit": "something"
    }

    @pytest.mark.parametrize("inputs", [(mock_inputs)])
    def test_cs_ioc_type_not_defined(self, circuits_app, inputs):
        """ test_cs_ioc_type_not_defined """
        with pytest.raises(ValueError) as err:
            call_fn_cs_falcon_get_devices_ioc_ran_on_function(circuits_app, inputs)
        assert err.value.args[0] == "'cs_ioc_type' is a mandatory function input"

    mock_inputs = {
        "cs_ioc_type": "something",
        "cs_ioc_value": None,
        "cs_return_limit": "something"
    }

    @pytest.mark.parametrize("inputs", [(mock_inputs)])
    def test_cs_ioc_value_not_defined(self, circuits_app, inputs):
        """ test_cs_ioc_value_not_defined """
        with pytest.raises(ValueError) as err:
            call_fn_cs_falcon_get_devices_ioc_ran_on_function(circuits_app, inputs)
        assert err.value.args[0] == "'cs_ioc_value' is a mandatory function input"

    mock_inputs = {
        "cs_ioc_type": "mock_unsupported_type",
        "cs_ioc_value": "abc"
    }

    @pytest.mark.parametrize("inputs", [(mock_inputs)])
    def test_unsupported_artifact_type(self, circuits_app, inputs):
        """ test_unsupported_artifact_type """
        with pytest.raises(ValueError) as err:
            call_fn_cs_falcon_get_devices_ioc_ran_on_function(circuits_app, inputs)
        assert "mock_unsupported_type is not a supported IOC type. Supported types are" in err.value.args[0]

    mock_inputs = {
        "cs_ioc_type": "DNS Name",
        "cs_ioc_value": "localhost"
    }

    mock_output = {
        'inputs': {'cs_ioc_type': 'DNS Name', 'cs_ioc_value': 'localhost', 'cs_return_limit': None},
        'success': False,
        'reason': "IOC DNS Name:localhost not found on any CrowdStrike Device."
    }

    @pytest.mark.parametrize("inputs, expected_results", [(mock_inputs, mock_output)])
    def test_get_device_ioc_ran_on_response_error(self, circuits_app, inputs, expected_results):
        """ test_get_device_ioc_ran_on_response_error """

        mock_response_1 = {
            "error": True,
            "err_msg": "Resource Not Found"
        }

        CrowdStrikeHelper.cs_api_request = Mock()
        CrowdStrikeHelper.cs_api_request.side_effect = [mock_response_1]

        results = call_fn_cs_falcon_get_devices_ioc_ran_on_function(circuits_app, inputs)

        assert expected_results.get("inputs") == results.get("inputs")
        assert expected_results.get("success") == results.get("success")
