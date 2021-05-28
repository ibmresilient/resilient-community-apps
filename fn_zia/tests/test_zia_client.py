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

    """ Test zia_client.allowlist_action"""
    @patch("fn_zia.lib.auth.RequestsCommon", side_effect=mocked_requests)
    @pytest.mark.parametrize("allowlisturls, action, expected_result", [
        ("192.168.1.1", "ADD_TO_LIST", {"whitelistUrls": ["goodhost.com"]}),
        ("goodhost.com, 192.168.1.1", "REMOVE_FROM_LIST", {"whitelistUrls": []})
    ])
    def test_allowlist_action(self, mock_post, allowlisturls, action, expected_result):
        opts = {}
        zia_client = ZiaClient(opts, get_fn_opts())
        result = zia_client.allowlist_action(allowlisturls, action)
        assert(result == expected_result)

    """ Test zia_client.get_allowlist_urls"""
    @patch("fn_zia.lib.auth.RequestsCommon", side_effect=mocked_requests)
    @pytest.mark.parametrize("expected_result", [
        ({"whitelistUrls": ["goodhost.com", "192.168.1.1"]})
    ])
    def test_get_allowlist_urls(self, mock_post, expected_result):
        opts = {}
        zia_client = ZiaClient(opts, get_fn_opts())
        result = zia_client.get_allowlist_urls()
        assert(result == expected_result)

    """ Test zia_client.get_url_categories"""
    @patch("fn_zia.lib.auth.RequestsCommon", side_effect=mocked_requests)
    @pytest.mark.parametrize("custom_only, category_id, expected_result", [
        ("true", "CUSTOM_01", [{'id': 'CUSTOM_01', 'configuredName': 'TEST_CAT_1', 'superCategory': 'USER_DEFINED',
                                'keywords': ['test'], 'keywordsRetainingParentCategory': [], 'urls': ['testhost.com'],
                                'dbCategorizedUrls': [], 'customCategory': True, 'editable': True, 'type': 'URL_CATEGORY',
                                'val': 128, 'customUrlsCount': 1, 'urlsRetainingParentCategoryCount': 0}]),
        ("true", None, [{'id': 'CUSTOM_02', 'configuredName': 'TEST_CAT_2', 'superCategory': 'USER_DEFINED',
                         'keywords': ['test2'], 'keywordsRetainingParentCategory': [],
                         'urls': ['testhost2.com, 192.168.1.1'], 'dbCategorizedUrls': [], 'customCategory': True,
                         'editable': True, 'type': 'URL_CATEGORY', 'val': 128, 'customUrlsCount': 2,
                         'urlsRetainingParentCategoryCount': 0}])
    ])
    def test_get_url_categories(self, mock_post, custom_only, category_id, expected_result):
        opts = {}
        zia_client = ZiaClient(opts, get_fn_opts())
        result = zia_client.get_url_categories(custom_only, category_id)
        assert(result == expected_result)

    """ Test zia_client.category_action"""
    @patch("fn_zia.lib.auth.RequestsCommon", side_effect=mocked_requests)
    @pytest.mark.parametrize("category_id, configured_name, urls, action, expected_result", [
        ("CUSTOM_01", "TEST_CAT_1", "192.168.1.2, 192.168.1.3", "ADD_TO_LIST",
         {'id': 'CUSTOM_01', 'configuredName': 'TEST_CAT_1', 'keywordsRetainingParentCategory': [],
          'urls': ['1.1.1.1', 'testhost.com', '192.168.1.1', '192.168.1.2', '192.168.1.3'], 'dbCategorizedUrls': [],
          'customCategory': True, 'editable': True, 'description': 'CUSTOM_01_DESC', 'type': 'URL_CATEGORY', 'val': 128,
          'customUrlsCount': 2, 'urlsRetainingParentCategoryCount': 0}),
    ])
    def test_category_action(self, mock_post, category_id, configured_name, urls, action, expected_result):
        opts = {}
        zia_client = ZiaClient(opts, get_fn_opts())
        result = zia_client.category_action(category_id, configured_name, urls, action)
        assert(result == expected_result)

    mock_inputs_1 = {
        "custom_category": "true",
        "super_category": "USER_DEFINED",
        "urls": "testhost.com",
        "keywords": "test1",
        "configured_name": "TEST_CAT_1"
    }

    expected_results_1 = {'id': 'CUSTOM_01', 'configuredName': 'true', 'superCategory': ['test1'],
                          'keywords': ['testhost.com'], 'keywordsRetainingParentCategory': [],
                          'urls': ['TEST_CAT_1'], 'dbCategorizedUrls': [], 'customCategory': True, 'editable': True,
                          'type': 'USER_DEFINED', 'val': 130, 'customUrlsCount': 2, 'urlsRetainingParentCategoryCount': 0}


    mock_inputs_2 = {
        "custom_category": "true",
        "super_category": "USER_DEFINED",
        "urls": "testhost.com 192.168.1.1",
        "keywords": "test1 test2",
        "configured_name": "TEST_CAT_2"
    }
    expected_results_2 = {'id': 'CUSTOM_01', 'configuredName': 'true', 'superCategory': ['test1', 'test2'],
                          'keywords': ['testhost.com', '192.168.1.1'], 'keywordsRetainingParentCategory': [],
                          'urls': ['TEST_CAT_2'], 'dbCategorizedUrls': [], 'customCategory': True, 'editable': True,
                          'type': 'USER_DEFINED', 'val': 130, 'customUrlsCount': 2,
                          'urlsRetainingParentCategoryCount': 0}

    """ Test zia_client.add_url_category"""
    @patch("fn_zia.lib.auth.RequestsCommon", side_effect=mocked_requests)
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1),
        (mock_inputs_2, expected_results_2)
    ])
    def test_add_url_category(self, mock_post, mock_inputs, expected_results):
        opts = {}
        zia_client = ZiaClient(opts, get_fn_opts())
        result = zia_client.add_url_category(**mock_inputs)
        assert(result == expected_results)

    mock_inputs_1 = {
        "zia_urls": "host.com"
    }

    expected_results_1 = [{"url": "host.com", "urlClassifications": ["PROFESSIONAL_SERVICES"],
                           "urlClassificationsWithSecurityAlert": []}]

    mock_inputs_2 = {
        "zia_urls": "host.com, viruses.org"
    }

    expected_results_2 = [{"url": "host.com", "urlClassifications": ["PROFESSIONAL_SERVICES"],
                           "urlClassificationsWithSecurityAlert": []},
                          {"url": "viruses.org", "urlClassifications": ["MISCELLANEOUS_OR_UNKNOWN"],
                           "urlClassificationsWithSecurityAlert": []}]

    """ Test zia_client.url_lookup"""
    @patch("fn_zia.lib.auth.RequestsCommon", side_effect=mocked_requests)
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1),
        (mock_inputs_2, expected_results_2)
    ])
    def test_url_lookup(self, mock_post, mock_inputs, expected_results):
        opts = {}
        zia_client = ZiaClient(opts, get_fn_opts())
        result = zia_client.url_lookup(mock_inputs["zia_urls"])
        assert(result == expected_results)


    """ Test zia_client.activate"""
    @patch("fn_zia.lib.auth.RequestsCommon", side_effect=mocked_requests)
    @pytest.mark.parametrize("zia_activate, expected_result", [
        (True, {"status": "Activated"}),
        (False, {"status": "Not_selected"})
    ])
    def test_activate(self, mock_post, zia_activate, expected_result):
        opts = {}
        zia_client = ZiaClient(opts, get_fn_opts())
        result = zia_client.activate(zia_activate)
        assert(result == expected_result)

    mock_inputs_1 = {
        "zia_full_report": True,
        "zia_md5": "542a09dbd513bf75e29572922ce0687e"
    }

    expected_results_1 = "Full Details"

    mock_inputs_2 = {
        "zia_full_report": False,
        "zia_md5": "542a09dbd513bf75e29572922ce0687e"
    }

    expected_results_2 = "Summary"

    """ Test zia_client.get_sandbox_report"""
    @patch("fn_zia.lib.auth.RequestsCommon", side_effect=mocked_requests)
    @pytest.mark.parametrize("mock_inputs, expected_result", [
        (mock_inputs_1, expected_results_1),
        (mock_inputs_2, expected_results_2)
    ])
    def test_get_sandbox_report(self, mock_post, mock_inputs, expected_result):
        opts = {}
        zia_client = ZiaClient(opts, get_fn_opts())
        result = zia_client.get_sandbox_report(mock_inputs["zia_md5"], mock_inputs["zia_full_report"])
        assert (expected_result in result)