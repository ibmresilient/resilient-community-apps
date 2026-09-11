# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
from fn_mcafee_esm.components.mcafee_esm_case_polling import ds_to_millis


class TestMcAfeeCasePolling:

    def test_ds_to_millis_good(self):
        ts = ds_to_millis("05/17/2017 17:07:59")

        assert 1495040879000 == ts

    def test_ds_to_millis_bad_format(self):
        ts = ds_to_millis("2017-05-17 17:07:59")

        assert None is ts

    def test_ds_to_millis_bad_length(self):
        val = "05/17/2017T17:07:59.832Z"
        try:
            ts = ds_to_millis(val)
        except ValueError as e:
            assert e.args[0] == "Invalid timestamp length %s" % val


