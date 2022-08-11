# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""
import json
import time
import pytest
import datetime

from mock import patch
from resilient_lib import RequestsCommon
from resilient_circuits.util import get_config_data
from resilient_circuits.action_message import FunctionError_ as FunctionError
from fn_webex.lib.cisco_meetings import WebexMeetings
from fn_webex.lib.cisco_authentication import WebexAuthentication

PACKAGE_NAME = "fn_webex"
FUNCTION_NAME = "webex_create_meeting"

config_data = get_config_data(PACKAGE_NAME)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def mocked_requests_post(method, url, data=None, headers=None, proxies=None):
    class MockResponse:
        def __init__(self, text, status_code):
            self.text = text
            self.status_code = status_code

        def json(self):
            return json.loads(self.text)

    response = None
    if data and not isinstance(data, dict):
        data = json.loads(data)
    if url == "":        
        response = MockResponse(text="", status_code=404)
    elif url != "" and data.get("start") == "" and data.get("end") == "" and data.get("title") == "":
        response = None
    elif url != "" and data.get("start") != "" and data.get("end") != "" and data.get("title") != "":
        response = MockResponse(text="done", status_code=200)
    if headers and headers.get("bearerID") == "":
        response = MockResponse(text="Invalid bearerID", status_code=401)

    if "client_secret" in data:
        if data.get("client_secret") == "":
            response = MockResponse(text='''{"access_token" : ""}''', status_code=200)
        else:
            response = MockResponse(text='''{"access_token" : "ID1234"}''', status_code=200)
    return response

class LOG:
    def __init__(self):
        pass

    def info(self, msg):
        print("[INFO]", msg)
    
    def warn(self, msg):
        print("[WARN]", msg)
    
    def error(self, msg):
        print("[ERROR]", msg)
    
class TestFnCreateMeeting:

    requiredParameters = {
            "rc"           : RequestsCommon(),
            "start"        : round((datetime.datetime.now() + datetime.timedelta(minutes=45)).timestamp()) * 1000,
            "end"          : round((datetime.datetime.now() + datetime.timedelta(minutes=95)).timestamp()) * 1000,
            "siteURL"      : "http://www.example.com",
            "tokenURL"     : "http://www.example.com",
            "bearerID"     : "1234",
            "timzone"      : "gmt 05:30",
            "clientID"     : "client123",
            "clientSecret" : "Secret123",
            "refreshToken" : "token1234",
            "scope"        : "scope1 scope2 scope3",
            "logger"       : LOG()
        }
    optionalParameters = {
            "siteURL"     : "",
            "hostEmail"   : "",
            "title"       : "pytest",
            "password"    : "abcd123",
            "agenda"      : "pytest",
            "sendEmail"   : "",
        }

    @patch('resilient_lib.RequestsCommon.execute', side_effect=mocked_requests_post)
    @patch('resilient_lib.RequestsCommon.execute', side_effect=mocked_requests_post)
    def test_call_create_meeting(self, mock, mock2):

        requiredParameters = self.requiredParameters.copy()
        optionalParameters = self.optionalParameters.copy()
        requiredParameters["siteURL"] = ""
        authenticator = WebexAuthentication(requiredParameters)
        requiredParameters["header"] = authenticator.Authenticate()
        webex = WebexMeetings(requiredParameters, optionalParameters)
        with pytest.raises(FunctionError) as err:
            webex.create_meeting()
        
        requiredParameters = self.requiredParameters.copy()
        optionalParameters = self.optionalParameters.copy()
        requiredParameters["start"] = 0
        requiredParameters["end"]   = 0
        optionalParameters["title"] = ""
        webex = WebexMeetings(requiredParameters, optionalParameters)
        with pytest.raises(ValueError) as err:
            webex.create_meeting()

        requiredParameters = self.requiredParameters.copy()
        optionalParameters = self.optionalParameters.copy()
        requiredParameters["clientSecret"] = ""
        with pytest.raises(ValueError) as err:
            authenticator = WebexAuthentication(requiredParameters)
            requiredParameters["header"] = authenticator.Authenticate()

        requiredParameters = self.requiredParameters.copy()
        optionalParameters = self.optionalParameters.copy()
        webex = WebexMeetings(requiredParameters, optionalParameters)
        authenticator = WebexAuthentication(self.requiredParameters)
        self.requiredParameters["header"] = authenticator.Authenticate()
        webex.create_meeting()


class TestWebexMeetings:
    requiredParameters = {
            "rc"                          : RequestsCommon(),
            "start"                       : round((datetime.datetime.now() + datetime.timedelta(minutes=45)).timestamp()) * 1000,
            "end"                         : round((datetime.datetime.now() + datetime.timedelta(minutes=95)).timestamp()) * 1000,
            "url"                         : "http://www.example.com",
            "tokenURL"                    : "http://www.example.com",
            "bearerID"                    : "1234",
            "timzone"                     : "gmt 05:30",
            "clientID"                    : "client123",
            "clientSecret"                : "secret123",
            "refreshToken"                : "token1234",
            "scope"                       : "scope1 scope2 scope3"
        }
    optionalParameters = {
            "siteURL"                     : "",
            "hostEmail"                   : "",
            "title"                       : "pytest",
            "password"                    : "abcd123",
            "agenda"                      : "pytest",
            "sendEmail"                   : "",
        }
    webex = WebexMeetings(requiredParameters, optionalParameters)
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        ("GMT 05:30" , "+0530"), ("GMT +05:30", "+0530"), ("GMT -05:30", "-0530"),
        ("UTC -05:30", "-0530"), ("GMT 0530"  , "+0530"), (" GMT 0530 ", "+0530"),
        ("0530"      , "+0530"),( " -05:30  " , "-0530")])
    def test_get_timeZones(self, mock_inputs, expected_results):
        with pytest.raises(ValueError) as err:
            self.webex.get_timeZones("GMT 05:£30")
        with pytest.raises(ValueError) as err:
            self.webex.get_timeZones("IST 05:30")
        assert(self.webex.get_timeZones(mock_inputs), expected_results)
        assert(self.webex.get_timeZones(None), time.strftime("%z", time.localtime()))


    def test_check_time(self):
        start_time = round((datetime.datetime.now() + datetime.timedelta(minutes=45)).timestamp()) * 1000
        end_time = round((datetime.datetime.now() + datetime.timedelta(minutes=5)).timestamp()) * 1000
        with pytest.raises(ValueError) as err:
            self.webex.check_time("+0000", start_time, end_time)

        start_time = round((datetime.datetime.now() - datetime.timedelta(minutes=45)).timestamp()) * 1000
        end_time = round((datetime.datetime.now() - datetime.timedelta(minutes=5)).timestamp()) * 1000
        with pytest.raises(ValueError) as err:
            self.webex.check_time("+0000", start_time, end_time)

        start_time = self.requiredParameters.get("start")
        end_time = self.requiredParameters.get("end")
        self.webex.check_time("+0000", start_time, end_time)