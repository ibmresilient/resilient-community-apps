# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Test Sep client  class."""
from __future__ import print_function
from mock import patch
import pytest
from fn_zia.lib.auth import *
from  mock_artifacts import mocked_requests

"""
Suite of tests to test Zia client class
"""

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def get_fn_opts():
    return dict({
        "zia_api_base_url": "https://ziaserver/api/v1",
        "zia_username": "ziauser",
        "zia_password": "ziapass",
        "zia_api_key": "abCDeFIJkl0M"
    })


class TestZia:
    """ Test auth using mocked data.  """

    """ Test auth._set_jsession_header"""
    @patch("fn_zia.lib.auth.RequestsCommon", side_effect=mocked_requests)
    @pytest.mark.parametrize("expected_result", [
        ("JSESSIONID=971F40D46FE1A27AB4E2783BA77A1C76")
    ])
    def test_set_jsession_header(self, mock_req, expected_result):
        opts = {}
        auth = Auth(opts, get_fn_opts())
        auth._set_jsession_header()
        assert(auth._jsession_id == expected_result)
        assert(auth._headers["cookie"] == expected_result)

    """ Test auth._obfuscate_api_key"""
    @patch("fn_zia.lib.auth.RequestsCommon", side_effect=mocked_requests)
    @pytest.mark.parametrize("timestamp, expected_result", [
        ("1620836100899", "baakllCJCIIM")
    ])
    def test_obfuscate_api_key(self, mock_req, timestamp, expected_result):
        opts = {}
        auth = Auth(opts, get_fn_opts())
        auth._timestamp = timestamp
        auth._obfuscate_api_key()
        assert(auth._obf_api_key == expected_result)

    """ Test auth._obfuscate_api_key_with_with_new_timestamp"""
    @patch("fn_zia.lib.auth.RequestsCommon", side_effect=mocked_requests)
    @pytest.mark.parametrize("timestamp, expected_result", [
        ("1620837564418", "FIeebke0eeCM")
    ])
    def test_obfuscate_api_key_with_new_timestamp(self, mock_req, timestamp, expected_result):
        opts = {}
        auth = Auth(opts, get_fn_opts())
        auth._timestamp = timestamp
        auth._obfuscate_api_key(timestamp)
        assert(auth._obf_api_key == expected_result)

    """ Test auth._parse_jsessionid"""
    @patch("fn_zia.lib.auth.RequestsCommon", side_effect=mocked_requests)
    @pytest.mark.parametrize("set_cookie, expected_result", [
        ("JSESSIONID=6C42F97B950DE134775BCAC65F16F614; Path=/; Secure; HttpOnly",
         "JSESSIONID=6C42F97B950DE134775BCAC65F16F614"),
        ("TextJSESSIONID=6C42F97B950DE134775BCAC65F16F614Moretext",
        "JSESSIONID=6C42F97B950DE134775BCAC65F16F614")
    ])
    def test_obfuscate_parse_jsessionid(self, mock_req, set_cookie, expected_result):
        opts = {}
        auth = Auth(opts, get_fn_opts())
        result = auth._parse_jsessionid(set_cookie)
        assert(result==expected_result)

    """ Test auth._parse_jsessionid_missing_id"""
    @patch("fn_zia.lib.auth.RequestsCommon", side_effect=mocked_requests)
    @pytest.mark.parametrize("set_cookie, expected_result", [
        ("JSESSIONID=6C42F97B950D; Path=/; Secure; HttpOnly",
         "The 'JSESSIONID' parameter is missing from the authenticate response."),
        ("SESSIONID=6C42F97B950DE134775BCAC65F16F614; Path=/; Secure; HttpOnly",
         "The 'JSESSIONID' parameter is missing from the authenticate response.")

    ])
    def test_obfuscate_parse_jsessionid_missing_id(self, mock_req, set_cookie, expected_result):
        opts = {}
        auth = Auth(opts, get_fn_opts())
        with pytest.raises(ValueError) as e:
            auth._parse_jsessionid(set_cookie)
        assert str(e.value) == expected_result