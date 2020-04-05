# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import json
import os
import pytest
from datetime import datetime
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from mock import patch, Mock
from fn_twilio.components.twilio_send_sms import FunctionComponent

PACKAGE_NAME = "fn_twilio"
FUNCTION_NAME = "twilio_send_sms"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_twilio_send_sms_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("twilio_send_sms", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("twilio_send_sms_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestTwilioSendSms:
    """ Tests for the twilio_send_sms function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("twilio_sms_destination, twilio_sms_message, result_file, expected_results", 
    [
        ("19788354530", "hello world", "hello_world.json", 
           {"success": True, "twilio_status": [{"status": "queued", "phone_number": "+19788354530", "error_message": None, "message_body": "hello world"}]}),
        ("9788354530", "hello world", "bad_response.json", 
           {"success": False, "twilio_status": [{"status": False, "phone_number": "+9788354530", "error_message": "Unable to create record: The 'To' number +9788354530 is not a valid phone number.", "message_body": None}]})
    ])
    @patch.object(FunctionComponent, 'create_message')
    def test_success(self, mock_method, circuits_app, twilio_sms_destination, twilio_sms_message, 
                     result_file, expected_results):
        """ Test calling with sample values for the parameters """
        mock_method.return_value = read_mock_payload(result_file)

        function_params = { 
            "twilio_sms_destination": twilio_sms_destination,
            "twilio_sms_message": twilio_sms_message
        }
        results = call_twilio_send_sms_function(circuits_app, function_params)
        assert(expected_results['success'] == results['success'])
        assert(results.get('twilio_status'))
        for key in expected_results['twilio_status'][0].keys():
            assert(expected_results['twilio_status'][0][key] == results['twilio_status'][0][key])

def read_mock_payload(file_name):
    test_dir = os.path.dirname(__file__)
    file_path = os.path.join(test_dir, "mock_data/{}".format(file_name))
    with open(file_path) as f:
        result = json.load(f)
        return Message(result)

class Message:
    def __init__(self, message_json):
        self.messaging_service_sid = message_json.get('messaging_service_sid')
        self.date_created = datetime.strptime(message_json.get('date_created'), "%a, %d %b %Y %X %z")
        self.body = message_json.get('body')
        self.direction = message_json.get('direction')
        self.status = message_json.get('status')
        self.error_code = message_json.get('error_code')
        self.error_message = message_json.get('error_message')


    """[summary]
    message = self.create_message(client, message, src_address, phone_number)

            entry = {
                "phone_number": phone_number,
                "messaging_service_sid": message.messaging_service_sid,
                "date_created": str(message.date_created),
                "date_created_ts": get_ts_from_datetime(message.date_created),
                "direction": message.direction,
                "message_body": message.body,
                "status": message.status,
                "error_message": None
            }

            if message.error_code is None:
                entry['success'] = True
                self.log.info('Sent to {0}'.format(phone_number))
            else:
                entry['success'] = False
                entry["error_message"]: message.error_message
                self.log.error('Failed to send to {0} [{1}]'.format(phone_number, message.error_message))
    """