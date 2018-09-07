# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from test_helper import get_test_config, get_default_test_config, generate_response, string_test_config
from fn_mcafee_esm.util.helper import check_config, check_status_code, get_authenticated_headers, merge_two_dicts
from fn_mcafee_esm.components.mcafee_esm_edit_case import case_edit_case_details
from fn_mcafee_esm.components.mcafee_esm_case_polling import is_case_incident, ds_to_millis


class TestMcAfeeCasePolling:

    def test_is_case_incident_yes(self):
        case = {
            'id': 1,
            'openTime': '07/25/2018 13:56:52',
            'statusId': {
                'value': 1
            },
            'severity': 10,
            'summary': 'Re-opened'
        }
        incident_list = [{'name': 'name1'},
                         {'name': 'name2'},
                         {'name': '1name'},]
        outcome = is_case_incident(case, incident_list)

        assert True is outcome

    def test_is_case_incident_no(self):
        case = {
            'id': 1,
            'openTime': '07/25/2018 13:56:52',
            'statusId': {
                'value': 1
            },
            'severity': 10,
            'summary': 'Re-opened'
        }
        incident_list = [{'name': 'name1'},
                         {'name': 'name2'},]
        outcome = is_case_incident(case, incident_list)

        assert False is outcome

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


