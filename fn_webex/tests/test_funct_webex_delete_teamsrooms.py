# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from mock import patch
import json
from resilient_lib import RequestsCommon
from fn_webex.lib.cisco_interface import WebexInterface
from resilient_circuits.util import get_config_data, get_function_definition

PACKAGE_NAME = "fn_webex"
FUNCTION_NAME = "webex_delete_teamsrooms"

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
        print("[DEBUG]", msg)


def mocked_requestCommon(method, url, data=None, headers=None, proxies=None, callback=None):
    class MockResponse:
        def __init__(self, text, status_code):
            self.text = text
            self.status_code = status_code

        def json(self):
            return json.loads(self.text)

    if "rooms" in url:
        assert(url, "https://www.example.com/v1/rooms/room123")
    else:
        assert(url, "https://www.example.com/v1/teams/room123")

    response = MockResponse("", status_code=204)

    if callback:
        response = callback(response)
    return response


def call_webex_delete_entity_function(requiredParameters):
    webex = WebexInterface(requiredParameters)
    response = webex.deleteEntity()
    return response


class TestWebexDeleteEntity:
    """ Tests for the webex_create_room function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('resilient_lib.RequestsCommon.execute', side_effect=mocked_requestCommon)
    def test_success(self, mock):
        """ Test calling with sample values for the parameters """
        requiredParameters = {
            "rc"         : RequestsCommon(),
            "incidentId" : 1234,
            "header"     : None,
            "resclient"  : None,
            "logger"     : LOG(),
            "baseURL"    : "https://www.example.com"
        }

        expected = {'status_code': 204,
         'message': 'API call successful! No content returned'}
        
        requiredParameters["entityName"] = "room"
        requiredParameters["entityId"] = "room123"
        response = call_webex_delete_entity_function(requiredParameters)
        
        assert(response.success, True)
        assert(response.value, expected)
