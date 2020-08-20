#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

from fn_spamhaus_query.util.spamhaus_helper import make_api_call
from resilient_lib import RequestsCommon
from mock import patch


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
            headers={"Authorization": "Bearer ABCDEF"}
        )
