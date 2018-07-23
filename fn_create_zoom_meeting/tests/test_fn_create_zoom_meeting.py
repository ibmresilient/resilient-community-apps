# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import mock
from fn_create_zoom_meeting.components.zoom_common import ZoomCommon

partial_response = {"meetings": True, "page_number": True}

def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.text = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if "page_number=" in args[0] and partial_response["page_number"]:
        content = ""
        with open('data/users_request.txt', 'r') as meeting_request_file:
            content = meeting_request_file.read()

        return MockResponse(content, 200)

    return MockResponse(None, 404)


def mocked_requests_post(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.text = json_data
            self.content = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if "meetings" in args[0] and partial_response["meetings"]:
        content = ""
        with open('data/create_meeting.txt', 'r') as meeting_request_file:
            content = meeting_request_file.read()

        return MockResponse(content, 200)

    return MockResponse(None, 404)


def run_zoom_common_create_meeting():
    zoom_api_key = "P4NSEjFtQl-uI9KPyk_jBg"  # Fill with zoom api key
    zoom_api_secret = "eDLSPQUrZYcBdRRsFkjeG0M5dZLD0yLyL89u"  # Fill with zoom api secret

    zoom_host_email = "x"
    zoom_agenda = "test"
    zoom_record_meeting = False
    zoom_topic = "test"
    zoom_password = ""

    common = ZoomCommon(zoom_api_key, zoom_api_secret)

    result = common.create_meeting(zoom_host_email, zoom_agenda, zoom_record_meeting, zoom_topic, zoom_password)

    return result


class TestFnCreateZoomMeeting:
    """ Tests for the fn_create_zoom_meeting function"""

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    @mock.patch('requests.post', side_effect=mocked_requests_post)
    def test_success(self, get, post):
        """ Test calling with sample values """
        result = run_zoom_common_create_meeting()
        assert result["host_url"] is not None

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    @mock.patch('requests.post', side_effect=mocked_requests_post)
    def test_partial(self, get, post):
        """ Test calling with partial data """

        partial_response["meetings"] = False
        partial_response["page_number"] = False

        try:
            run_zoom_common_create_meeting()
            assert False
        except Exception:
            pass

        partial_response["meetings"] = True

        try:
            run_zoom_common_create_meeting()
            assert False
        except Exception:
            assert True
