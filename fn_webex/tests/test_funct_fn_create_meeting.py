# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""
from multiprocessing.sharedctypes import Value
import json
import time
import pytest

from mock import patch
from pyclbr import Function
from resilient_lib import RequestsCommon
from fn_webex.lib.cisco_api import WebexAPI
from resilient_circuits.action_message import FunctionError_ as FunctionError
from resilient_circuits.util import get_config_data, get_function_definition


PACKAGE_NAME = "fn_webex"
FUNCTION_NAME = "fn_create_meeting"

config_data = get_config_data(PACKAGE_NAME)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def mocked_requests_post(method, url, data=None, headers=None, proxies=None):
    class MockResponse:
        def __init__(self, text, status_code):
            self.text = text
            self.status_code = status_code

    response = None
    if data:
        data = json.loads(data)
    if url == "":        
        response = MockResponse(text="", status_code=404)
    elif url != "" and data.get("start") == "" and data.get("end") == "" and data.get("title") == "":
        response = None
    elif url != "" and data.get("start") != "" and data.get("end") != "" and data.get("title") != "":
        response = MockResponse(text="done", status_code=200)
    if headers.get("bearerID") == "":
        response = MockResponse(text="Invalid bearerID", status_code=401)
    return response


class TestFnCreateMeeting:

    requiredParameters = {
            "rc"                          : RequestsCommon(),
            "start"                       : 1657973238000,
            "end"                         : 1657975870000,
            "url"                         : "http://www.example.com",
            "bearerID"                    : "1234",
            "timzone"                     : "gmt 05:30"
        }
    optionalParameters = {
            "siteURL"                     : "",
            "hostEmail"                   : "",
            "title"                       : "pytest",
            "password"                    : "abcd123",
            "agenda"                      : "pytest",
            "sendEmail"                   : "",
        }

    @patch('resilient_lib.RequestsCommon.execute_call_v2', side_effect=mocked_requests_post)
    @patch('resilient_lib.RequestsCommon.execute_call_v2', side_effect=mocked_requests_post)
    def test_call_create_meeting(self, mock, mock2):

        requiredParameters = self.requiredParameters.copy()
        optionalParameters = self.optionalParameters.copy()
        requiredParameters["url"] = ""
        webex = WebexAPI(requiredParameters, optionalParameters)
        with pytest.raises(FunctionError) as err:
            webex.create_meeting()
        
        requiredParameters = self.requiredParameters.copy()
        optionalParameters = self.optionalParameters.copy()
        requiredParameters["start"] = 0
        requiredParameters["end"]   = 0
        optionalParameters["title"] = ""
        webex = WebexAPI(requiredParameters, optionalParameters)
        with pytest.raises(FunctionError) as err:
            webex.create_meeting()

        requiredParameters = self.requiredParameters.copy()
        optionalParameters = self.optionalParameters.copy()
        requiredParameters["bearerID"] = ""
        with pytest.raises(ValueError) as err:
            webex = WebexAPI(requiredParameters, optionalParameters)

        requiredParameters = self.requiredParameters.copy()
        optionalParameters = self.optionalParameters.copy()
        webex = WebexAPI(requiredParameters, optionalParameters)
        webex.create_meeting()


class TestWebexApi:
    requiredParameters = {
            "rc"                          : RequestsCommon(),
            "start"                       : 1657973238000,
            "end"                         : 1657975870000,
            "url"                         : "",
            "bearerID"                    : "NGM3OGJiMzgtM2E5Yi00OTNlLWE5NDgtYmZkNTVjODQ4NzJiNDFmMWVlODUtZDBi_P0A1_f688574e-8402-4b53-864e-e725f4468887",
            "timzone"                     : "gmt 05:30"
        }
    optionalParameters = {
            "siteURL"                     : "",
            "hostEmail"                   : "",
            "title"                       : "pytest",
            "password"                    : "abcd123",
            "agenda"                      : "pytest",
            "sendEmail"                   : "",
        }
    webex = WebexAPI(requiredParameters, optionalParameters)
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        ("GMT 05:30" , "+0530"), ("GMT +05:30", "+0530"), ("GMT -05:30", "-0530"),
        ("UTC -05:30", "-0530"), ("GMT 0530"  , "+0530"), (" GMT 0530 ", "+0530"),
        ("0530"      , "+0530"),( " -05:30  " , "-0530")])
    def test_get_timeZones(self, mock_inputs, expected_results):
        assert(self.webex.get_timeZones(mock_inputs) == expected_results)

        assert(self.webex.get_timeZones(None) == time.strftime("%z", time.localtime()))
        try:
            self.webex.get_timeZones("GMT 05:£30")
        except ValueError as msg:
            print(msg)
        try:
            self.webex.get_timeZones("IST 05:30")
        except ValueError as msg:
            print(msg)


    @pytest.mark.parametrize("mock_inputs, expected_results", [
        ("ID123" , {"Bearer ID123" : "application/json"}), 
    ])
    def test_generate_header(self, mock_inputs, expected_results):
        assert(isinstance(self.webex.generate_header(mock_inputs), dict))
        assert(self.webex.generate_header(mock_inputs), expected_results)

        with pytest.raises(ValueError) as err:
            self.webex.generate_header(None), expected_results


