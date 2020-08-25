#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

from collections import OrderedDict
from fn_spamhaus_query.util.spamhaus_helper import make_api_call, format_dict, spamhaus_call_error
from shared_mock_data import MockedResponse
from resilient_lib import RequestsCommon, IntegrationError
from mock import patch
import pytest


def test_make_api_call():
    with patch("fn_spamhaus_query.components.fn_spamhaus_query_submit_artifact.RequestsCommon.execute_call_v2") as mock_get:

        make_api_call(
            base_url="https://www.example.com/",
            api_key="ABCDEF",
            search_resource="info",
            qry="123",
            rc=RequestsCommon({}, {})
        )

        mock_get.assert_called_with(
            method="get",
            url="https://www.example.com/info/123",
            headers={"Authorization": "Bearer ABCDEF"},
            callback=spamhaus_call_error
        )


def test_format_dict():
    formatted_dict = format_dict(OrderedDict([("key1", "value1"), ("key2", "value2")]))
    actual_result = """\n-----------------\nkey1: value1\nkey2: value2\n-----------------\n"""

    assert formatted_dict == actual_result


def test_spamhaus_call_error_bad_code():
    with pytest.raises(IntegrationError, match=r"Call to Spamhaus API failed. Reason: Bad Request"):
        spamhaus_call_error(MockedResponse(status_code=401, reason="Bad Request"))
