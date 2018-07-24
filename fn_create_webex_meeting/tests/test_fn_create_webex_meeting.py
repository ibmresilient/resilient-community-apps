# -*- coding: utf-8 -*-

# (c) Copyright IBM Corp. 2018. All Rights Reserved.
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function

import mock
from fn_create_webex_meeting.lib.cisco_api import WebexAPI

partial_data = {"timezone": True, "createmeeting": True}


def mocked_requests_post(url, data=None, **kwargs):
    global partial_data

    class MockResponse:
        def __init__(self, text, status_code):
            self.text = text
            self.status_code = status_code

    if "site.LstTimeZone" in str(data) and partial_data["timezone"] == True:
        print("Mocking timezone")
        content = ""
        with open('data/timezone_info.txt', 'r') as timezone_info_file:
            content = timezone_info_file.read()

        return MockResponse(content, 200)

    if "java:com.webex.service.binding.meeting.CreateMeeting" in str(data) and partial_data["createmeeting"] == True:
        print("Mocking createmeeting")
        content = ""
        with open('data/meeting_request.txt', 'r') as meeting_request_file:
            content = meeting_request_file.read()

        return MockResponse(content, 200)

    return MockResponse("", 200)


def run_cisco_api_create_meeting():
    opts = dict()
    opts["webex_site_url"] = ""  # Fill with the full site url, i.e abc.webex.com
    opts["email"] = ""  # Fill with user email
    opts["password"] = ""  # Fill with user password
    opts["sitename"] = ""  # Fill with sitename, i.e abc
    opts["timezone"] = "-04:00"  # Fill with a timezone, i.e GMT-04:00

    webex_meeting_name = "Test Meeting"  # text
    webex_meeting_password = "Test Password"  # text
    webex_meeting_agenda = "Test Agenda"  # text

    opts["meeting_password"] = webex_meeting_password
    opts["meeting_name"] = webex_meeting_name
    opts["meeting_agenda"] = webex_meeting_agenda

    common = WebexAPI(opts)

    result = common.create_meeting()

    return result


class TestCreateWebexMeeting:
    """ Tests for the fn_create_webex_meeting function"""

    @mock.patch('requests.post', side_effect=mocked_requests_post)
    def test_success(self, request):
        """ Test calling with sample values for the parameters """
        result = run_cisco_api_create_meeting()

        assert result["status"] == "SUCCESS"

    @mock.patch('requests.post', side_effect=mocked_requests_post)
    def test_partial_data(self, request):
        """Simulate invalid response from the Cisco WebEx API"""
        global partial_data
        partial_data["timezone"] = False

        try:
            run_cisco_api_create_meeting()
            assert False
        except Exception:
            pass

        partial_data["timezone"] = True
        partial_data["createmeeting"] = False

        try:
            run_cisco_api_create_meeting()
            assert False
        except Exception:
            pass

        assert True
