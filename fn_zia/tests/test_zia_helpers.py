# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Test helper functions"""
import pytest
from fn_zia.lib.helpers import *
from .mock_artifacts import get_url_categories_base, get_allowlist_urls, get_blocklist_urls
"""
Suites of tests to test the ZIA Helper functions
"""


class TestZIAHelpers:
    """Test helper functions"""

    """Test is_regex function"""
    @pytest.mark.parametrize("regex_pattern, expected_results", [
        ("(CAT_|CAT_2).*", True),
        ("goodhost.com", True),
        ("+++", False)
    ])
    def test_is_regex(self, regex_pattern, expected_results):
        assert is_regex(regex_pattern) == expected_results

    """Test filter_by_category function"""
    mock_inputs_1 = {
        "name_filter": None,
    }

    expected_results_1 = {'categories': [{'id': 'CUSTOM_01', 'configuredName': 'TEST_CAT_1', 'superCategory': 'USER_DEFINED',
                                          'keywords': ['test'], 'keywordsRetainingParentCategory': [],
                                          'urls': ['testhost.com'], 'dbCategorizedUrls': [], 'customCategory': True,
                                          'editable': True, 'type': 'URL_CATEGORY', 'val': 128, 'customUrlsCount': 1,
                                          'urlsRetainingParentCategoryCount': 0},
                                         {'id': 'CUSTOM_02', 'configuredName': 'TEST_CAT_2', 'superCategory': 'USER_DEFINED',
                                          'keywords': ['test2'], 'keywordsRetainingParentCategory': [],
                                          'urls': ['testhost2.com', '192.168.1.1'], 'dbCategorizedUrls': [], 'customCategory': True,
                                          'editable': True, 'type': 'URL_CATEGORY', 'val': 128, 'customUrlsCount': 2,
                                          'urlsRetainingParentCategoryCount': 0}],
                          'category_counts': {'total': 2, 'filtered': 2}
                          }


    mock_inputs_2 = {
        "name_filter": "CAT_1",
    }
    expected_results_2 = {'categories': [{'id': 'CUSTOM_01', 'configuredName': 'TEST_CAT_1', 'superCategory': 'USER_DEFINED',
                                          'keywords': ['test'], 'keywordsRetainingParentCategory': [],
                                          'urls': ['testhost.com'], 'dbCategorizedUrls': [], 'customCategory': True,
                                          'editable': True, 'type': 'URL_CATEGORY', 'val': 128, 'customUrlsCount': 1,
                                          'urlsRetainingParentCategoryCount': 0}],
                          'category_counts': {'total': 2, 'filtered': 1}
                          }

    mock_inputs_3 = {
        "name_filter": ".*",
    }
    expected_results_3 = {'categories': [{'id': 'CUSTOM_01', 'configuredName': 'TEST_CAT_1', 'superCategory': 'USER_DEFINED',
                                          'keywords': ['test'], 'keywordsRetainingParentCategory': [],
                                          'urls': ['testhost.com'], 'dbCategorizedUrls': [], 'customCategory': True,
                                          'editable': True, 'type': 'URL_CATEGORY', 'val': 128, 'customUrlsCount': 1,
                                          'urlsRetainingParentCategoryCount': 0},
                                         {'id': 'CUSTOM_02', 'configuredName': 'TEST_CAT_2', 'superCategory': 'USER_DEFINED',
                                          'keywords': ['test2'], 'keywordsRetainingParentCategory': [],
                                          'urls': ['testhost2.com', '192.168.1.1'], 'dbCategorizedUrls': [], 'customCategory': True,
                                          'editable': True, 'type': 'URL_CATEGORY', 'val': 128, 'customUrlsCount': 2,
                                          'urlsRetainingParentCategoryCount': 0}],
                          'category_counts': {'total': 2, 'filtered': 2}
                          }

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1),
        (mock_inputs_2, expected_results_2),
        (mock_inputs_3, expected_results_3)
    ])
    def test_filter_by_category(self, mock_inputs, expected_results):
        input = {
            "categories": get_url_categories_base()
        }
        results = filter_by_category(input, name_filter=mock_inputs["name_filter"])
        assert results == expected_results

    """Test filter_by_url function"""
    mock_inputs_1 = {
        "response": get_url_categories_base()[1],
        "url_filter": None,
        "url_type": "urls"
    }

    expected_results_1 = {'id': 'CUSTOM_02', 'configuredName': 'TEST_CAT_2', 'superCategory': 'USER_DEFINED',
                          'keywords': ['test2'], 'keywordsRetainingParentCategory': [],
                          'urls': ['testhost2.com', '192.168.1.1'], 'dbCategorizedUrls': [], 'customCategory': True,
                          'editable': True, 'type': 'URL_CATEGORY', 'val': 128, 'customUrlsCount': 2,
                          'urlsRetainingParentCategoryCount': 0,
                          'url_counts': {'total': 2, 'filtered': 2}
                          }
    mock_inputs_2 = {
        "response": get_url_categories_base()[1],
        "url_filter": "testhost2",
        "url_type": "urls"
    }

    expected_results_2 = {'id': 'CUSTOM_02', 'configuredName': 'TEST_CAT_2', 'superCategory': 'USER_DEFINED',
                          'keywords': ['test2'], 'keywordsRetainingParentCategory': [],
                          'urls': ['testhost2.com'], 'dbCategorizedUrls': [], 'customCategory': True,
                          'editable': True, 'type': 'URL_CATEGORY', 'val': 128, 'customUrlsCount': 2,
                          'urlsRetainingParentCategoryCount': 0,
                          'url_counts': {'total': 2, 'filtered': 1}
                          }

    mock_inputs_3 = {
        "response": get_allowlist_urls(),
        "url_filter": "good",
        "url_type":  "whitelistUrls"
    }
    expected_results_3 = {'whitelistUrls': ['goodhost.com'], 'url_counts': {'total': 2, 'filtered': 1}}

    mock_inputs_4 = {
        "response": get_blocklist_urls(),
        "url_filter": "bad",
        "url_type":  "blacklistUrls"
    }
    expected_results_4 = {'blacklistUrls': ['badhost.com'], 'url_counts': {'total': 2, 'filtered': 1}}

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1),
        (mock_inputs_2, expected_results_2),
        (mock_inputs_3, expected_results_3),
        (mock_inputs_4, expected_results_4),
    ])
    def test_filter_by_url(self, mock_inputs, expected_results):

        results = filter_by_url(mock_inputs["response"], url_filter=mock_inputs["url_filter"],
                                url_type=mock_inputs["url_type"])
        assert results == expected_results