# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Test helper functions"""
from __future__ import print_function
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
import pytest
from fn_bigfix.util.helpers import *
from  mock_artifacts import mocked_res_client, mocked_bigfix_client

"""
Suite of tests to test Helper functions
"""

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

class Func(object):
    def __init__(self, options={}):
        self.options = options

class TestHelpersValidateParams:
    """ Test for the validate_params function.  """

    @pytest.mark.parametrize("func_name, param_name, param_value, expected_results", [
        ("fn_bigfix_artifact", "artifact_id", None, "Required parameter 'artifact_id' not set."),
        ("fn_bigfix_artifact", "artifact_value", None, "Required parameter 'artifact_value' not set."),
        ("fn_bigfix_artifact", "artifact_type", None, "Required parameter 'artifact_type' not set."),
        ("fn_bigfix_artifact", "incident_id", None, "Required parameter 'incident_id' not set."),
        ("fn_bigfix_artifact", "incident_plan_status", None, "Required parameter 'incident_plan_status' not set."),
        ("fn_bigfix_remediation", "artifact_value", None, "Required parameter 'artifact_value' not set."),
        ("fn_bigfix_remediation", "artifact_type", None, "Required parameter 'artifact_type' not set."),
        ("fn_bigfix_remediation", "incident_id", None, "Required parameter 'incident_id' not set."),
        ("fn_bigfix_remediation", "asset_id", None, "Required parameter 'asset_id' not set."),
        ("fn_bigfix_assets", "incident_id", None, "Required parameter 'incident_id' not set."),
        ("fn_bigfix_assets", "asset_id", None, "Required parameter 'asset_id' not set."),
        ("fn_bigfix_assets", "asset_name", None, "Required parameter 'asset_name' not set."),
    ])
    def test_validate_params(self, func_name, param_name, param_value, expected_results):
        params = {
            param_name: param_value
        }
        with pytest.raises(ValueError) as e:
            validate_params(params, func_name)
        assert str(e.value) == expected_results


class TestHelpersValidatOpts:
    """Tests for the omit_params function"""


    @pytest.mark.parametrize("bigfix_url, bigfix_port, bigfix_user, bigfix_pass, hunt_results_limit, "
                             "bigfix_polling_interval, bigfix_polling_timeout, expected_results", [
        ("", "", "", "", "", "", "", "Mandatory config setting 'bigfix_url' not set."),
        ("https://bigfix-url.com", "", "", "", "", "", "", "Mandatory config setting 'bigfix_port' not set."),
        ("https://bigfix-url.com", "12345", "", "", "", "", "", "Mandatory config setting 'bigfix_user' not set."),
        ("https://bigfix-url.com", "12345", "BigFixAdmin", "", "", "", "", "Mandatory config setting 'bigfix_pass' not set."),
        ("https://bigfix-url.com", "12345", "BigFixAdmin", "MyPassword", "", "", "", "Mandatory config setting 'hunt_results_limit' not set."),
        ("https://bigfix-url.com", "12345", "BigFixAdmin", "MyPassword", "30", "", "", "Mandatory config setting 'bigfix_polling_interval' not set."),
        ("https://bigfix-url.com", "12345", "BigFixAdmin", "MyPassword", "30", "1800", "", "Mandatory config setting 'bigfix_polling_timeout' not set.")
    ])
    def test_validate_opts_missing_token(self, bigfix_url, bigfix_port, bigfix_user, bigfix_pass, hunt_results_limit,
                                         bigfix_polling_interval, bigfix_polling_timeout, expected_results):
        func = Func({
            "bigfix_url": bigfix_url,
            "bigfix_port": bigfix_port,
            "bigfix_user": bigfix_user,
            "bigfix_pass": bigfix_pass,
            "hunt_results_limit": hunt_results_limit,
            "bigfix_polling_interval": bigfix_polling_interval,
            "bigfix_polling_timeout": bigfix_polling_timeout,
        })
        with pytest.raises(Exception) as e:
            validate_opts(func)
        assert str(e.value) == expected_results

class TestHelpersIsNone:
    """Test for the init_env function"""

    @pytest.mark.parametrize("param_value, expected_results", [
        (None, True),
        ("None", True),
        ("NONE", True),
        ("none", True),
        ("", False),
        ("domain.com", False)
    ])
    def test_is_none(self, param_value, expected_results):
        param = None
        if (param_value == "Blank"):
            del param
        else:
            param = param_value
        results = is_none(param)
        assert results == expected_results

class TestHelpersCreateAttachment:
    """ Tests for the create_attachment function"""

    @pytest.mark.parametrize("file_name, file_content, params", [
        ("test_file.xml", 'My test data', {"incident_id": 12345})
    ])
    def test_create_attachment(self, file_name, file_content, params):
        """ Test create_attachment using mocked data.  """
        keys = ["name", "inc_id"]

        results = create_attachment(mocked_res_client("post_attachment", file_name, params["incident_id"]), file_name, file_content, params)
        assert_keys_in(results, *keys)
        assert results["name"] == file_name
        assert results["inc_id"] == params["incident_id"]