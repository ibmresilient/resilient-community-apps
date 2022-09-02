# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from multiprocessing.sharedctypes import Value
import pytest
from mock import patch
import json
from resilient_lib import RequestsCommon
from fn_webex.lib.cisco_interface import WebexInterface
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import FunctionResult

PACKAGE_NAME = "fn_webex"
FUNCTION_NAME = "webex_create_room"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

class LOG:
    def __init__(self):
        pass

    def info(self, msg):
        print("[INFO]", msg)
    
    def warn(self, msg):
        print("[WARN]", msg)
    
    def error(self, msg):
        print("[ERROR]", msg)
    
    def debug(self, msg):
        print("[ERROR]", msg)


class mocked_restClient:
    def __init__(self):
        pass

    def get(self, request):
        if "incident" in request:
            return {'members': [16, 17, 18, 21], 'vers': 12} 
        elif "group" in request:
            return [{'id': 3, 'members': [19, 20]}]

    def post(self, request,  payload):
        if "users" in request:
            return {"data" : [
                        {'id':  1, 'display_name': 'Admin User', 'status': 'A', 'email': 'admin@example.com'}, 
                        {'id': 16, 'display_name': 'Resilient Sysadmin', 'status': 'A', 'email': 'soar1@example.ie'},
                        {'id': 17, 'display_name': 'soar2 Sysadmin', 'status': 'A', 'email': 'soar2@example.ie'},
                        {'id': 18, 'display_name': 'soar3 Sysadmin', 'status': 'A', 'email': 'soar3@example.ie'}, 
                        {'id': 19, 'display_name': 'soar4 Sysadmin', 'status': 'A', 'email': 'soar4@example.ie'},
                        {'id': 20, 'display_name': 'soar5 Sysadmin', 'status': 'A', 'email': 'soar5@example.ie'}
                    ]}


def mocked_requestCommon(method, url, data=None, headers=None, proxies=None, callback=None):
    class MockResponse:
        def __init__(self, text, status_code):
            self.text = text
            self.status_code = status_code

        def json(self):
            return json.loads(self.text)
    response = None
    if url == "https://webexapis.com/v1/rooms/":
        response = MockResponse('{"items": [{"id": "Y123", "title": "UnittestRoom", "created": "2022-08-11T18:24:46.655Z","isPublic": "false"}, {"id": "Y234", "title": "UnittestRoom", "created": "2022-08-11T18:24:46.655Z","isPublic": "false"}, {"id": "Y345", "title": "UnittestRoom", "created": "2022-08-11T18:24:46.655Z","isPublic": "false"}]}', 200)

    elif url == "https://webexapis.com/v1/memberships":
        response = None

    elif url == "https://webexapis.com/v1/rooms/{}/meetingInfo".format("Y123"):
        response = MockResponse('''{"items": [{"id": "Y123", "title": "UnittestRoom", "created": "2022-08-11T18:24:46.655Z","isPublic": "false"}]}''', status_code=200)

    else:
        raise ValueError(url)
    if callback:
        return callback(response)
    return response


def call_webex_create_room_function():
    requiredParameters = {
            "rc"         : RequestsCommon(),
            "incidentId" : 1234,
            "header"     : None,
            "logger"     : LOG(),
            "resclient"  : mocked_restClient(),
            "addAllMembers" : True,
            "roomName"   : "UnittestRoom",
            "roomId"     : "Y123",
            "entityURL"  : "https://webexapis.com/v1/rooms/",
            "entityId"   : "roomId",
            "entityName" : "roomName",
            "membershipUrl" : "https://webexapis.com/v1/memberships",
            'additionalAttendee' : "sara@example.com, hannah@example.com, harsha@example.com"
        }

    webex = WebexInterface(requiredParameters)
    webex.find_operation()
    webex.generate_member_list()
    webex.retrieve_entity()
    webex.add_membership()
    response = webex.get_entity_details()
    return FunctionResult(response, success=True)


class TestWebexCreateRoom:
    """ Tests for the webex_create_room function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('resilient_lib.RequestsCommon.execute', side_effect=mocked_requestCommon)
    def test_success(self, mock):
        """ Test calling with sample values for the parameters """
        expected = {
            'items': [{
                'id': 'Y123', 
                'title': 'UnittestRoom',
                'created': '2022-08-11T18:24:46.655Z', 'isPublic': 'false'
                }],
            'attendees': 'soar1@example.ie, soar2@example.ie, soar3@example.ie, sara@example.com, hannah@example.com, harsha@example.com',
            'status': True, 
            'roomName': 'UnittestRoom'}
        results = call_webex_create_room_function()

        assert(results.value["status"], True)
        assert(results.value, expected)
