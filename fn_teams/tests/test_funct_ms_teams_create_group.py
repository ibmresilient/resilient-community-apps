# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from multiprocessing.sharedctypes import Value
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_teams"
FUNCTION_NAME = "ms_teams_create_group"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_ms_teams_create_group_function(circuits, function_params, timeout=5):
    evt = SubmitTestFunction("ms_teams_create_group", function_params)
    circuits.manager.fire(evt)
    exception_event = circuits.watcher.wait("exception", parent=None, timeout=timeout)

    if exception_event is not False:
        exception = exception_event.args[1]
        raise exception

    else:
        event = circuits.watcher.wait("ms_teams_create_group_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestMsTeamsCreateGroup:
    """ Tests for the ms_teams_create_group function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None
        
    @pytest.mark.livetest
    def test_success(self, circuits_app):
        """ Test calling with sample values for the parameters """

        results = call_ms_teams_create_group_function(circuits_app, {})
        assert(results.get("success"))
