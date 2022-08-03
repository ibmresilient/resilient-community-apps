# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""Test helper functions"""

from __future__ import print_function
import pytest
from fn_bigfix.util.helpers import validate_opts, create_attachment
from tests.mock_artifacts import mocked_res_client

"""Suite of tests to test Helper functions"""

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

class Func(object):
    def __init__(self, options={}):
        self.options = options

class TestHelpersValidatOpts:
    """Tests for the omit_params function"""

    @pytest.mark.parametrize("bigfix_url, bigfix_port, bigfix_user, bigfix_pass, bigfix_hunt_results_limit, "
                             "bigfix_polling_interval, bigfix_polling_timeout, bigfix_endpoints_wait, expected_results", [
        ("", "", "", "", "", "", "", "", "Mandatory config setting 'bigfix_url' not set."),
        ("https://bigfix-url.com", "", "", "", "", "", "", "", "Mandatory config setting 'bigfix_port' not set."),
        ("https://bigfix-url.com", "12345", "", "", "", "", "", "", "Mandatory config setting 'bigfix_user' not set."),
        ("https://bigfix-url.com", "12345", "BigFixAdmin", "", "", "", "", "", "Mandatory config setting 'bigfix_pass' not set."),
        ("https://bigfix-url.com", "12345", "BigFixAdmin", "MyPassword", "", "", "", "", "Mandatory config setting 'bigfix_hunt_results_limit' not set."),
        ("https://bigfix-url.com", "12345", "BigFixAdmin", "MyPassword", "30", "", "", "", "Mandatory config setting 'bigfix_polling_interval' not set."),
        ("https://bigfix-url.com", "12345", "BigFixAdmin", "MyPassword", "30", "1800", "", "", "Mandatory config setting 'bigfix_polling_timeout' not set."),
        ("https://bigfix-url.com", "12345", "BigFixAdmin", "MyPassword", "30", "1800", "200", "", "Mandatory config setting 'bigfix_endpoints_wait' not set.")
    ])
    def test_validate_opts_missing_token(self, bigfix_url, bigfix_port, bigfix_user, bigfix_pass, bigfix_hunt_results_limit,
                                         bigfix_polling_interval, bigfix_polling_timeout, bigfix_endpoints_wait, expected_results):
        func = Func({
            "bigfix_url": bigfix_url,
            "bigfix_port": bigfix_port,
            "bigfix_user": bigfix_user,
            "bigfix_pass": bigfix_pass,
            "bigfix_hunt_results_limit": bigfix_hunt_results_limit,
            "bigfix_polling_interval": bigfix_polling_interval,
            "bigfix_polling_timeout": bigfix_polling_timeout,
            "bigfix_endpoints_wait": bigfix_endpoints_wait,
        })
        with pytest.raises(Exception) as e:
            validate_opts(func)
        assert str(e.value) == expected_results

class TestHelpersCreateAttachment:
    """ Tests for the create_attachment function"""

    @pytest.mark.parametrize("file_name, file_content, params", [
        ("test_file.xml", 'My test data', {"incident_id": 12345})
    ])
    def test_create_attachment(self, file_name, file_content, params):
        """ Test create_attachment using mocked data. """
        keys = ["name", "inc_id"]

        results = create_attachment(mocked_res_client("post_attachment", file_name, params["incident_id"]), file_name, file_content, params)
        assert_keys_in(results, *keys)
        assert results["name"] == file_name
        assert results["inc_id"] == params["incident_id"]
