# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Test oauth-utils helper functions"""
import hashlib
import os
from time import sleep

import pytest
from mock import mock, patch
from threading import Event
from oauth_utils.bin.flask_app import FlaskApp
from oauth_utils.lib.oauth2flow import OAuth2Flow
from .mock_data.mock_artifacts import mocked_oauth2

CSRF_TOKEN = hashlib.sha256(os.urandom(64)).hexdigest()

"""
Suites of tests to test the OAuth-utils Flask app functions
"""
def assert_attribs_in(json_obj, *attribs):
    for attrib in attribs:
        assert hasattr(json_obj, attrib)

class TestFlaskApp:
    """Test Flask app functions"""

    """Test test_instantiation function"""
    @pytest.mark.parametrize("expected_result", [
        ("oauth_utils.bin.flask_app.FlaskApp object at")
    ])
    def test_instantiation(self, expected_result):
        expected_attribs = ["app", "csrf_token", "start", "stop", "stop_event", "thread"]
        stop_event = Event()
        flask_app = FlaskApp(CSRF_TOKEN, stop_event, None)
        assert(expected_result in repr(flask_app))
        assert_attribs_in(flask_app, *expected_attribs)
        assert flask_app.stop_event == stop_event

    """Test start function"""
    @pytest.mark.parametrize("status, query_string, data", [
        (500, {}, "Internal Server Error"),
        (200, {"state": CSRF_TOKEN,
               "code": "4/0AX4XfWjgvQx7XPaQJf4qkwuJtUNBOc3WHgWsBU3qTojAZukH7JT8l33Qpcu6R4lWF8qDgw",
               "scope": "https://mail.google.com/"}, '<span id="app_id">abca1234</span>')
    ])
    def test_start(self, monkeypatch, status, query_string, data):
        def mock_auth(auth_code=None):
            return "abca1234"
        stop_event = Event()
        fn_opts = {}
        monkeypatch.setattr(os, '_exit', mock.MagicMock())
        oauth2 = OAuth2Flow(fn_opts, CSRF_TOKEN)
        monkeypatch.setattr(oauth2, 'authenticate', mock_auth)
        flask_app = FlaskApp(CSRF_TOKEN, stop_event, None)
        flask_app.start(oauth2, stop_event)
        with flask_app.app.test_client() as test_client:
            response = test_client.get("/callback", query_string=query_string)
            assert response.status_code == status
            assert data in response.data.decode('utf-8')
        flask_app.stop()

    """Test stop function"""
    def test_stop(self):
        stop_event = Event()
        fn_opts = {}
        oauth2 = OAuth2Flow(fn_opts, CSRF_TOKEN)
        flask_app = FlaskApp(CSRF_TOKEN, stop_event, None)
        flask_app.start(oauth2, stop_event)
        assert flask_app.thread.is_alive() == True
        flask_app.stop()
        sleep(1)
        assert flask_app.thread.is_alive() == False
