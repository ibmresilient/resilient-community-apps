# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_cisco_enforcement"
FUNCTION_NAME = "event"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_event_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("event", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("event_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestEvent:
    """ Tests for the event function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("99ff12cf-f002-418a-ba75-2ff96137b522, c8aef649-7963-4e67-a811-f6505ba2e206, da7267dc-e822-45fa-8d18-297fbcbd2787, 545cc8ab-8bc7-487d-b395-213736518c07, c5239fd4-21af-469a-9ae6-c45aa9784c4b, be3abf5f-7b65-4c5f-8ac6-442535b39c03, be5d67ad-96e3-47c2-975e-7a6080b829ca, d4e05190-1492-49e4-813d-f583726c50ae, ed3dd357-0bd7-4698-970a-d31599159dbd, 85487e13-cdab-45c6-b012-4ee01cfa19ee, dc7a8e54-8a3b-406e-b34b-48f430c97544, 4bde1794-0705-43f9-9d7b-860eb83c9958, 3ed0b3ce-f6b0-4ddc-b724-5d6d5b96d7b0, ae997d8b-f8e6-41a3-b1d6-1b96a12d9cbe, 27aecdca-a858-4ff5-bbf4-c18d20ee90a9, e0bcee28-1db2-44c0-b20e-b1bf6f54feef, 022ccdd5-4303-4949-a2fb-472d7163c7ba, 152ee7fe-7dc9-4118-a02f-2c62d0be027a, expected_results", [
        ("text", "text", 1518367008000, 1518367008000, "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", {"value": "xyz"}),
        ("text", "text", 1518367008000, 1518367008000, "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", "text", {"value": "xyz"})
    ])
    def test_success(self, circuits_app, 99ff12cf-f002-418a-ba75-2ff96137b522, c8aef649-7963-4e67-a811-f6505ba2e206, da7267dc-e822-45fa-8d18-297fbcbd2787, 545cc8ab-8bc7-487d-b395-213736518c07, c5239fd4-21af-469a-9ae6-c45aa9784c4b, be3abf5f-7b65-4c5f-8ac6-442535b39c03, be5d67ad-96e3-47c2-975e-7a6080b829ca, d4e05190-1492-49e4-813d-f583726c50ae, ed3dd357-0bd7-4698-970a-d31599159dbd, 85487e13-cdab-45c6-b012-4ee01cfa19ee, dc7a8e54-8a3b-406e-b34b-48f430c97544, 4bde1794-0705-43f9-9d7b-860eb83c9958, 3ed0b3ce-f6b0-4ddc-b724-5d6d5b96d7b0, ae997d8b-f8e6-41a3-b1d6-1b96a12d9cbe, 27aecdca-a858-4ff5-bbf4-c18d20ee90a9, e0bcee28-1db2-44c0-b20e-b1bf6f54feef, 022ccdd5-4303-4949-a2fb-472d7163c7ba, 152ee7fe-7dc9-4118-a02f-2c62d0be027a, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "99ff12cf-f002-418a-ba75-2ff96137b522": 99ff12cf-f002-418a-ba75-2ff96137b522,
            "c8aef649-7963-4e67-a811-f6505ba2e206": c8aef649-7963-4e67-a811-f6505ba2e206,
            "da7267dc-e822-45fa-8d18-297fbcbd2787": da7267dc-e822-45fa-8d18-297fbcbd2787,
            "545cc8ab-8bc7-487d-b395-213736518c07": 545cc8ab-8bc7-487d-b395-213736518c07,
            "c5239fd4-21af-469a-9ae6-c45aa9784c4b": c5239fd4-21af-469a-9ae6-c45aa9784c4b,
            "be3abf5f-7b65-4c5f-8ac6-442535b39c03": be3abf5f-7b65-4c5f-8ac6-442535b39c03,
            "be5d67ad-96e3-47c2-975e-7a6080b829ca": be5d67ad-96e3-47c2-975e-7a6080b829ca,
            "d4e05190-1492-49e4-813d-f583726c50ae": d4e05190-1492-49e4-813d-f583726c50ae,
            "ed3dd357-0bd7-4698-970a-d31599159dbd": ed3dd357-0bd7-4698-970a-d31599159dbd,
            "85487e13-cdab-45c6-b012-4ee01cfa19ee": 85487e13-cdab-45c6-b012-4ee01cfa19ee,
            "dc7a8e54-8a3b-406e-b34b-48f430c97544": dc7a8e54-8a3b-406e-b34b-48f430c97544,
            "4bde1794-0705-43f9-9d7b-860eb83c9958": 4bde1794-0705-43f9-9d7b-860eb83c9958,
            "3ed0b3ce-f6b0-4ddc-b724-5d6d5b96d7b0": 3ed0b3ce-f6b0-4ddc-b724-5d6d5b96d7b0,
            "ae997d8b-f8e6-41a3-b1d6-1b96a12d9cbe": ae997d8b-f8e6-41a3-b1d6-1b96a12d9cbe,
            "27aecdca-a858-4ff5-bbf4-c18d20ee90a9": 27aecdca-a858-4ff5-bbf4-c18d20ee90a9,
            "e0bcee28-1db2-44c0-b20e-b1bf6f54feef": e0bcee28-1db2-44c0-b20e-b1bf6f54feef,
            "022ccdd5-4303-4949-a2fb-472d7163c7ba": 022ccdd5-4303-4949-a2fb-472d7163c7ba,
            "152ee7fe-7dc9-4118-a02f-2c62d0be027a": 152ee7fe-7dc9-4118-a02f-2c62d0be027a
        }
        results = call_event_function(circuits_app, function_params)
        assert(expected_results == results)