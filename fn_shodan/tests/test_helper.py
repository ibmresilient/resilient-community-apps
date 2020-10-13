#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

from collections import OrderedDict
from fn_shodan.util.helper import handle_error, make_api_call, format_dict


def test_handle_error():
    assert handle_error("mock reason") == {"err": True, "reason": "mock reason"}
    assert handle_error("mock reason") != {"err": True}
    assert handle_error("mock reason") != {"reason": "mock reason"}


def test_format_dict():
    formatted_dict = format_dict(OrderedDict([("key1", "value1"), ("key2", "value2")]))
    actual_result = """\n-----------------\nkey1: value1\nkey2: value2\n-----------------\n"""

    assert formatted_dict == actual_result
