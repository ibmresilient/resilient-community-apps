# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Test Sep client  class."""
from __future__ import print_function
from mock import patch
import pytest
from fn_zia.lib.zia_client import *
from .mock_artifacts import mocked_requests

"""
Suite of tests to test Zia client class
"""
def assert_attribs_in(json_obj, *attribs):
    for attrib in attribs:
        assert hasattr(json_obj, attrib)

def get_fn_opts():
    return dict({
        "zia_api_base_url": "https://ziaserver/api/v1",
        "zia_username": "ziauser",
        "zia_password": "ziapass",
        "zia_api_key": "abCDeFIJkl0M"
    })

def get_headers():
    return dict({
        "content-type": "application/json",
        "cache-control": "no-cache",
        "User-Agent": "SOARCLIENT",
        "cookie": "JSESSIONID=971F40D46FE1A27AB4E2783BA77A1C76"
    })
    return test_xml

class TestZIAClient:
    """ Test zia_client test instantiation"""
    @patch("fn_zia.lib.auth.RequestsCommon", side_effect=mocked_requests)
    @pytest.mark.parametrize("expected_result", [
        ("fn_zia.lib.zia_client.ZiaClient object at")
    ])
    def test_instantiation(self, mock_post,expected_result):
        expected_attribs = ["_endpoints", "_headers", "_jessions_id", "_obf_api_key", "_req",
                            "_timestamp","api_base_url", "api_key", "password", "username",
                            "proxies"]
        opts = {}
        zia_client = ZiaClient(opts, get_fn_opts())
        assert(expected_result in repr(zia_client))
        assert_attribs_in(zia_client, *expected_attribs)

    ["payload", "finding", "data_tables"]
    """ Test zia_client._perform_method"""
    @patch("fn_zia.lib.auth.RequestsCommon", side_effect=mocked_requests)
    @pytest.mark.parametrize("opts, fn_opts, expected_result", [
        (None, None, "The 'opts' parameter is not set correctly."),
        (None, {}, "The 'opts' parameter is not set correctly."),
        ({}, None, "The 'fn_opts' parameter is not set correctly."),
    ])
    def test_missing_options(self, mock_post, opts, fn_opts, expected_result):
        with pytest.raises(ValueError) as e:
            zia_client = ZiaClient(opts, None)
        assert str(e.value) == expected_result

    """ Test zia_client._perform_method"""
    @patch("fn_zia.lib.auth.RequestsCommon", side_effect=mocked_requests)
    @pytest.mark.parametrize("method, uri, action, expected_result", [
        ("get", "https://ziaserver/api/v1/security/advanced",
         None, {"blacklistUrls": ["badhost.com", "192.168.12.2"]}),
        ("post", "https://ziaserver/api/v1/security/advanced/blacklistUrls?action={}",
         "ADD_TO_LIST", {"status": "OK"}),
        ("post", "https://ziaserver/api/v1/security/advanced/blacklistUrls?action={}",
         "REMOVE_FROM_LIST", {"status": "OK"})
    ])
    def test_perform_method(self, mock_post, method, uri, action, expected_result):
        opts = {}
        if action:
            uri = uri.format(action)
        zia_client = ZiaClient(opts, get_fn_opts())
        result = zia_client._perform_method(method, uri, headers=get_headers())
        assert(result == expected_result)

    """ Test zia_client.get_blocklist_urls"""
    @patch("fn_zia.lib.auth.RequestsCommon", side_effect=mocked_requests)
    @pytest.mark.parametrize("expected_result", [
        ({"blacklistUrls": ["badhost.com", "192.168.12.2"]})
    ])
    def test_get_blocklist_urls(self, mock_post, expected_result):
        opts = {}
        zia_client = ZiaClient(opts, get_fn_opts())
        result = zia_client.get_blocklist_urls()
        assert(result == expected_result)

    """ Test zia_client.blocklist_action"""
    @patch("fn_zia.lib.auth.RequestsCommon", side_effect=mocked_requests)
    @pytest.mark.parametrize("blocklisturls, action, expected_result", [
        ("badhost.com, 192.168.12.2", "ADD_TO_LIST", {"status": "OK"}),
        ("badhost.com, 192.168.12.2", "REMOVE_FROM_LIST", {"status": "OK"})
    ])
    def test_blocklist_action(self, mock_post,blocklisturls, action, expected_result):
        opts = {}
        zia_client = ZiaClient(opts, get_fn_opts())
        result = zia_client.blocklist_action(blocklisturls, action)
        assert(result == expected_result)