# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
import time
from io import StringIO
from xml.sax.handler import ContentHandler
from xml.sax import make_parser
from fn_playbook_maker.components.funct_make_playbook import make_playbook_info, MakeTemplates
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_playbook_maker"
FUNCTION_NAME = "make_playbook"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
#resilient_mock = "pytest_resilient_circuits.BasicResilientMock"
test_inputs = {
            'pbm_playbook_name': 'test name',
            'pbm_app_name': None,
            'pbm_activation_type': 'Manual',
            'pbm_playbook_type': 'incident',
            'pbm_function_names': 'funct_1',
            'pbm_activation_fields': True,
            'pbm_add_to_same_playbook': None
        }
test_inputs_function_info = [
    {
        "function_name": 'funct_1',
        "fields": [
            {
                "blank_option": False,
                "name": "input_field",
                "input_type": "text",
                "required": True,
                "text": "Input Field",
                "tooltip": "some tip. special \" & <something>",
                "rich_text": False,
                "values": []
            }
        ]
    }
]

test_inputs_multiple_functions = {
            'pbm_playbook_name': 'test name with quote \"',
            'pbm_app_name': None,
            'pbm_activation_type': 'Manual',
            'pbm_playbook_type': 'incident',
            'pbm_function_names': 'funct_1,funct2',
            'pbm_activation_fields': True,
            'pbm_add_to_same_playbook': None
        }
test_inputs_multiple_functions_function_info = [
    {
        "function_name": 'funct_1',
        "fields": [
            {
                "blank_option": False,
                "name": "input_field",
                "input_type": "text",
                "required": True,
                "text": "Input Field quote \"",
                "tooltip": "some tip with quote \"",
                "rich_text": False,
                "values": []
            }
        ]
    },
    {
        "function_name": 'funct_2',
        "fields": [
            {
                "blank_option": False,
                "name": "input_field2",
                "input_type": "text",
                "required": True,
                "text": "Input Field",
                "tooltip": "some tip",
                "rich_text": False,
                "values": []
            }
        ]
    }
]

def call_make_playbook_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("make_playbook", function_params)

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
        event = circuits.watcher.wait("make_playbook_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestMakePlaybook:
    """ Tests for the make_playbook function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    def test_make_payload_info(self):
        payload_info = make_playbook_info(test_inputs, test_inputs_function_info)

        assert(payload_info.get('inputs'))
        assert(payload_info.get('playbook_info'))
        assert(payload_info.get('functions'))

        assert(payload_info['inputs'].get('pbm_playbook_name') == test_inputs['pbm_playbook_name'])

        assert(payload_info['functions'][0].get('function_name') == test_inputs_function_info[0]['function_name'])
        assert(payload_info['functions'][0].get('script_uuid'))

        assert(payload_info['playbook_info'].get('playbook_name').startswith(test_inputs['pbm_playbook_name']))
        assert(payload_info['playbook_info'].get('playbook_name_api_name') and ' ' not in payload_info['playbook_info'].get('playbook_name_api_name'))
        assert(str(payload_info['playbook_info'].get('uuid_uuid')) in payload_info['playbook_info'].get('playbook_display_name'))

    def test_make_payload_xml(self):
        templates = MakeTemplates()
        parser = make_parser(  )
        parser.setContentHandler(ContentHandler(  ))

        playbook_payload = make_playbook_info(test_inputs, test_inputs_function_info)
        playbook_xml = templates.make_playbook_xml(playbook_payload)
        parser.parse(StringIO(playbook_xml))

    def test_make_playbook_json(self):
        templates = MakeTemplates()
        playbook_payload = make_playbook_info(test_inputs, test_inputs_function_info)
        templates.make_playbook_json(playbook_payload)
        playbook_json = templates.make_playbook_json(playbook_payload)
        assert(playbook_json['playbook_json'][0].get('fields_type',{}).get('fields'))
        assert(playbook_json['playbook_json'][0].get('manual_settings',{}).get('view_items'))

    def test_make_playbook_json_mulitple_functions(self):
        templates = MakeTemplates()
        playbook_payload = make_playbook_info(test_inputs_multiple_functions, test_inputs_multiple_functions_function_info)
        templates.make_playbook_json(playbook_payload)
        playbook_json = templates.make_playbook_json(playbook_payload)
        assert(len(playbook_json['playbook_json'][0].get('fields_type',{}).get('fields')) == 2)
        assert(len(playbook_json['playbook_json'][0].get('manual_settings',{}).get('view_items')) == 2)
        assert(len(playbook_json['playbook_json'][0].get('local_scripts')) == 2)

    mock_inputs_1 = {
        "pbm_app_name": "fn_scheduler",
        "pbm_function_names": None,
        "pdm_activation_fields": True,
        "pbm_playbook_type": "incident",
        "pbm_activation_type": "Manual",
        "pbm_playbook_name": "test app_"+str(int(time.time()))
    }

    expected_results_1 = {"value": "xyz"}

    mock_inputs_2 = {
        "pbm_app_name": None,
        "pbm_function_names": "create_a_scheduled_rule, list_scheduled_rules",
        "pdm_activation_fields": False,
        "pbm_playbook_type": "artifact",
        "pbm_activation_type": "Automatic",
        "pbm_playbook_name": "test function_"+str(int(time.time()))
    }

    expected_results_2 = {"value": "xyz"}

    @pytest.mark.skip
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_2, expected_results_2)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_make_playbook_function(circuits_app, mock_inputs)
        assert(expected_results == results)
