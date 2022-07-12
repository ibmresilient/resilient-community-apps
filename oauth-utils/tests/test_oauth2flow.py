# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Test oauth2flow  class."""
from __future__ import print_function

import hashlib
import os
from textwrap import dedent
from mock import patch
import pytest
from oauth_utils.lib.oauth2flow import *
from .mock_data.mock_artifacts import mocked_requests_post
"""
Suite of tests to test oauth2flow  class
"""
CSRF_TOKEN = hashlib.sha256(os.urandom(64)).hexdigest()

def assert_attribs_in(json_obj, *attribs):
    for attrib in attribs:
        assert hasattr(json_obj, attrib)

class TestOAuth2Flow:

    """ Test OAuth2Flow test instantiation"""
    @patch('requests.post', side_effect=mocked_requests_post)
    @pytest.mark.parametrize("scope, client_id, client_secret, token_url, auth_url, expected_result", [
        ("https://test.ibm.com/SMTP.Send", "1234567a-abc8-90d1-2efa3-123456789abcd", "ABCDEF-123456789abcd_2efa3",
         "https://test.ibm.com/oauth2/token", "https://test.ibm.com/oauth2/auth",
         "oauth_utils.lib.oauth2flow.OAuth2Flow object at"
         )
    ])
    def test_instantiation(self, mock_post, scope, client_id, client_secret, token_url, auth_url,  expected_result):
        expected_attribs = ["_auth_url", "_client_id", "_client_secret", "_redirect_uri", "_refresh_token",
                            "_scope", "_state", "_token_url", "authenticate", "get_authorization_url",
                            "validate_settings"]
        fn_opts  = {
            "scope": scope,
            "client_id": client_id,
            "client_secret": client_secret,
            "token_url": token_url,
            "auth_url": auth_url
        }
        oauth2 = OAuth2Flow(fn_opts, CSRF_TOKEN, None)
        assert(expected_result in repr(oauth2))
        assert_attribs_in(oauth2, *expected_attribs)

    """ Test OAuth2Flow missing fn_opts setting"""
    @patch('requests.post', side_effect=mocked_requests_post)
    @pytest.mark.parametrize("fn_opts, expected_result", [
        ({}, "'auth_url' is mandatory and is not set. You must set this value to run this function"),
        ({"auth_url": "a"}, "'token_url' is mandatory and is not set. You must set this value to run this function"),
        ({"auth_url": "a","token_url": "b"}, "'client_id' is mandatory and is not set. You must set this value to run this function"),
        ({"auth_url": "a","token_url": "b", "client_id": "c"}, "'client_secret' is mandatory and is not set. You must set this value to run this function"),
        ({"auth_url": "a","token_url": "b", "client_id": "c", "client_secret": "d"}, "'scope' is mandatory and is not set. You must set this value to run this function")
    ])
    def test_missing_options(self, mock_post, fn_opts, expected_result):
        oauth2 = OAuth2Flow(fn_opts, CSRF_TOKEN, None)
        with pytest.raises(ValueError) as e:
            oauth2.validate_settings(fn_opts)
        assert str(e.value) == expected_result

    """ Test OAuth2Flow missing fn_opts setting"""
    @patch('requests.post', side_effect=mocked_requests_post)
    @pytest.mark.parametrize("fn_opts, expected_result", [
        ({}, "Parameters 'auth_url, token_url, client_id, client_secret, scope' are required in the app.config and are not set. You must set these values to run this function."),
        ({"auth_url": "a"}, "Parameters 'token_url, client_id, client_secret, scope' are required in the app.config and are not set. You must set these values to run this function."),
        ({"auth_url": "a","token_url": "b"}, "Parameters 'client_id, client_secret, scope' are required in the app.config and are not set. You must set these values to run this function."),
        ({"auth_url": "a","token_url": "b", "client_id": "c"}, "Parameters 'client_secret, scope' are required in the app.config and are not set. You must set these values to run this function."),
        ({"auth_url": "a","token_url": "b", "client_id": "c", "client_secret": "d"}, "Parameter 'scope' is required in the app.config and is not set. You must set this value to run this function.")
    ])
    def test_missing_options(self, mock_post, fn_opts, expected_result):
        oauth2 = OAuth2Flow(fn_opts, CSRF_TOKEN, None)
        with pytest.raises(ValueError) as e:
            oauth2.validate_settings(fn_opts)
        assert str(e.value) == expected_result

    """ Test OAuth2Flow get_authorization_url"""
    @patch('requests.post', side_effect=mocked_requests_post)
    @pytest.mark.parametrize("port, scope, client_id, client_secret, token_url, auth_url, expected_result", [
        (None, "https://test.ibm.com/SMTP.Send", "1234567a-abc8-90d1-2efa3-123456789abcd", "ABCDEF-123456789abcd_2efa3",
         "https://test.ibm.com/oauth2/token", "https://test.ibm.com/oauth2/auth",
         "https://test.ibm.com/oauth2/auth?state={}&scope=https%3A%2F%2Ftest.ibm.com%2FSMTP.Send&client_id=1234567a-abc8-90d1-2efa3-123456789abcd&response_type=code&response_mode=query&redirect_uri=https%3A%2F%2Flocalhost%3A8080%2Fcallback".format(CSRF_TOKEN)
         ),
        (4000, "https://test.ibm.com/SMTP.Send", "1234567a-abc8-90d1-2efa3-123456789abcd", "ABCDEF-123456789abcd_2efa3",
         "https://test.ibm.com/oauth2/token", "https://test.ibm.com/oauth2/auth",
         "https://test.ibm.com/oauth2/auth?state={0}&scope=https%3A%2F%2Ftest.ibm.com%2FSMTP.Send&client_id=1234567a-abc8-90d1-2efa3-123456789abcd&response_type=code&response_mode=query&redirect_uri=https%3A%2F%2Flocalhost%3A{1}%2Fcallback".format(
             CSRF_TOKEN, 4000)
         )
    ])
    def test_authorization_url(self, mock_post, port, scope, client_id, client_secret, token_url, auth_url,  expected_result):
        fn_opts  = {
            "scope": scope,
            "client_id": client_id,
            "client_secret": client_secret,
            "token_url": token_url,
            "auth_url": auth_url
        }
        oauth2 = OAuth2Flow(fn_opts, CSRF_TOKEN, port)
        result = oauth2.get_authorization_url()
        assert str(result) == expected_result

    """ Test OAuth2Flow authenticate"""
    @patch('requests.post', side_effect=mocked_requests_post)
    @pytest.mark.parametrize("scope, client_id, client_secret, token_url, auth_url, expected_result", [
        ("https://test.ibm.com/SMTP.Send", "1234567a-abc8-90d1-2efa3-123456789abcd", "ABCDEF-123456789abcd_2efa3",
         "https://test.ibm.com/oauth2/token", "https://test.ibm.com/oauth2/auth",
         '1//07Gd6TUwZA_INCgYIARAAGAcSNwF'
         ),
    ])
    def test_authenticate(self, mock_post, scope, client_id, client_secret, token_url, auth_url,  expected_result):
        fn_opts = {
            "scope": scope,
            "client_id": client_id,
            "client_secret": client_secret,
            "token_url": token_url,
            "auth_url": auth_url
        }
        auth_code = "abcd1234"
        oauth2 = OAuth2Flow(fn_opts, CSRF_TOKEN, None)
        result = oauth2.authenticate(auth_code)
        assert str(result) == expected_result