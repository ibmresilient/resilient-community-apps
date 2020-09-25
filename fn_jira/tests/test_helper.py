#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

from collections import OrderedDict
from fn_jira.util.helper import validate_app_configs, prepend_text, build_url_to_resilient, format_dict


def test_validate_app_configs():
    mock_app_configs = {
        "url": "www.example.com",
        "user": "exampleuser",
        "password": "examplepassword",
        "verify_cert": "true"
    }

    valid_app_configs = validate_app_configs(mock_app_configs)

    assert valid_app_configs.get("url") == "www.example.com"
    assert valid_app_configs.get("user") == "exampleuser"
    assert valid_app_configs.get("password") == "examplepassword"
    assert valid_app_configs.get("verify_cert") is True


def test_prepend_text():
    assert prepend_text("mock text") == "mock text"
    assert prepend_text(u"mock Ü Ý Þ ß à á text", "abc") == u"mock Ü Ý Þ ß à á text\n\nabc"


def test_build_url_to_resilient():
    assert build_url_to_resilient("www.example.com", "443", 1000) == "https://www.example.com:443/#incidents/1000"
    assert build_url_to_resilient("www.example.com", "443", 1000, 123) == "https://www.example.com:443/#incidents/1000?task_id=123"


def test_format_dict():
    formatted_dict = format_dict(OrderedDict([("key1", "value Ü Ý Þ ß1"), ("key2", "value2")]))
    actual_result = """\n-----------------\nkey1: value Ü Ý Þ ß1\nkey2: value2\n-----------------\n"""

    assert formatted_dict == actual_result
