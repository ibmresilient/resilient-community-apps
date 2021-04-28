# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

import pytest
from fn_pagerduty.lib import resilient_common


def test_merge_two_dicts():
    a = {"k1": "v1"}
    b = {"k2": "v2"}

    expected_result = {
        "k1": "v1",
        "k2": "v2"
    }

    result = resilient_common.merge_two_dicts(a, b)

    for e in expected_result:
        assert e in result
