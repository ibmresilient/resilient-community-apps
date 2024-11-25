# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_ioc_parser_v2"
FUNCTION_NAME = "func_ioc_parser_v2"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_func_ioc_parser_v2_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("func_ioc_parser_v2", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("func_ioc_parser_v2_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFuncIocParserV2:
    """ Tests for the func_ioc_parser_v2 function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None
