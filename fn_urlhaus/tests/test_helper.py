#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

from collections import OrderedDict
from fn_urlhaus.util.helper import make_api_call, format_dict
from resilient_lib import RequestsCommon
from mock import patch


def test_make_api_call_lookup():
    with patch("fn_urlhaus.components.funct_fn_urlhaus.RequestsCommon.execute_call_v2") as mock_get:

        make_api_call(
            call_type="lookup",
            base_url="https://www.example.com",
            artifact_type="URL",
            artifact_value="www.example.com",
            rc=RequestsCommon({}, {})
        )

        mock_get.assert_called_with(
            method="post",
            url="https://www.example.com/url",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={"url": "www.example.com"}
        )


def test_make_api_call_submission():
    with patch("fn_urlhaus.components.funct_fn_urlhaus.RequestsCommon.execute_call_v2") as mock_get:

        make_api_call(
            call_type="submission",
            base_url="https://www.example.com",
            api_key="ABCD1234",
            artifact_value="www.example.com",
            rc=RequestsCommon({}, {})
        )

        mock_get.assert_called_with(
            method="post",
            url="https://www.example.com",
            headers={"Content-Type": "application/json"},
            json={
                "token": "ABCD1234",
                "anonymous": "0",
                "submission": [{"url": "www.example.com", "threat": "malware_download"}]
            }
        )


def test_format_dict():
    formatted_dict = format_dict(OrderedDict([("key1", "value1"), ("key2", "value2")]))
    actual_result = """\n-----------------\nkey1: value1\nkey2: value2\n-----------------\n"""

    assert formatted_dict == actual_result
