#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

from collections import OrderedDict
from fn_api_void.lib.apivoid_helper import build_request_url, make_apivoid_api_call
from resilient_lib import RequestsCommon
from mock import patch


def test_build_request_url():
    request_url = build_request_url("https://www.example.com", None, "selftest", "12345", True)

    assert request_url == "https://www.example.com/sitetrust/v1/pay-as-you-go/?key=12345&stats=True"


def test_make_api_call():
    with patch("fn_api_void.components.funct_fn_api_void_request.RequestsCommon.execute_call_v2") as mock_get:

        make_apivoid_api_call(
            base_url="https://www.example.com",
            sub_url=None,
            query_type="selftest",
            value=True,
            api_key="12345",
            rc=RequestsCommon({}, {})
        )

        mock_get.assert_called_with(
            method="get",
            url="https://www.example.com/sitetrust/v1/pay-as-you-go/?key=12345&stats=True"
        )
