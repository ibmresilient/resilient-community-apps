#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

from collections import OrderedDict
from fn_ip_void.util.ipvoid_helper import get_request_info, make_api_call, format_dict
from resilient_lib import RequestsCommon
from mock import patch


def test_request_info():
    req_info = get_request_info("https://www.example.com", None, "selftest", True)

    assert type(req_info) is tuple
    assert req_info[0] == "https://www.example.com/iprep/v1/pay-as-you-go/"
    assert req_info[1] == {"stats": True}


def test_make_api_call():
    with patch("fn_ip_void.components.fn_ip_void_request.RequestsCommon.execute_call_v2") as mock_get:

        make_api_call(
            base_url="https://www.example.com",
            sub_url=None,
            query_type="selftest",
            value=True,
            api_key="12345",
            rc=RequestsCommon({}, {})
        )

        mock_get.assert_called_with(
            method="get",
            url="https://www.example.com/iprep/v1/pay-as-you-go/",
            params={"key": "12345", "stats": True}
        )


def test_format_dict():
    formatted_dict = format_dict(OrderedDict([("key1", "value1"), ("key2", "value2")]))
    actual_result = """\n-----------------\nkey1: value1\nkey2: value2\n-----------------\n"""

    assert formatted_dict == actual_result
