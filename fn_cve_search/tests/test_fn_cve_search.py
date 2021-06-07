# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use, line-too-long
"""Tests using pytest_resilient_circuits"""

import pytest
from fn_cve_search.util import cve
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

    def test_get_gm_epoch_time_stamp(self):
        assert cve.get_gm_epoch_time_stamp("2018-09-11") == 1536624000000
