# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use, line-too-long
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from fn_cve_search.util.selftest import selftest_function

class TestCVESearch:

    opts = {
        "fn_cve_search": {
            "max_results_display": 50,
            "cve_base_url": "https://cve.circl.lu/api"
        }
    }

    @pytest.mark.livetest
    def test_cs_device_id_not_defined(self):
        result = selftest_function(TestCVESearch.opts)
        assert (result['state'] == "Success")
