# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Test helper functions"""
import pytest
from fn_cisco_amp4ep.lib.helpers import *

"""
Suites of tests to test the Umbrella Investigate Helper functions
"""

class Func(object):
    def __init__(self, options={}):
        self.options = options

class TestAmpHelpersValidateParamsGood:
    """Test validate_params function"""

    @pytest.mark.parametrize("amp_limit, expected_results", [
        (50, None)
    ])
    def test_validate_params_limit(self, amp_limit, expected_results):
        params = {
            "limit": amp_limit
        }
        results = validate_params(params)
        assert (expected_results == results)

    @pytest.mark.parametrize("amp_offset, expected_results", [
        (100, None)
    ])
    def test_validate_params_offset(self, amp_offset, expected_results):
        params = {
            "offset": amp_offset
        }
        results = validate_params(params)
        assert (expected_results == results)

    @pytest.mark.parametrize("amp_conn_guid, expected_results", [
        ("abcd1234-a123-123a-123a-123456abcdef", None)
    ])
    def test_validate_params_conn_guid(self, amp_conn_guid, expected_results):
        params = {
            "conn_guid": amp_conn_guid
        }
        results = validate_params(params)
        assert (expected_results == results)

    @pytest.mark.parametrize("amp_internal_ip, expected_results", [
        ("192.4.87.123", None)
    ])
    def test_validate_params_internal_ip(self, amp_internal_ip, expected_results):
        params = {
            "internal_ip": amp_internal_ip
        }
        results = validate_params(params)
        assert (expected_results == results)

    @pytest.mark.parametrize("amp_external_ip, expected_results", [
        ("111.209.122.63", None)
    ])
    def test_validate_params_external_ip(self, amp_external_ip, expected_results):
        params = {
            "external_ip": amp_external_ip
        }
        results = validate_params(params)
        assert (expected_results == results)


class TestAmpHelpersValidateParamsErr:
    """Test validate_params function"""

    @pytest.mark.parametrize("amp_limit, expected_results", [
        ("anyoldtext", "Invalid value 'anyoldtext' for function parameter 'limit'.")
    ])
    def test_validate_params_limit(self, amp_limit, expected_results):
        params = {
            "limit": amp_limit
        }
        with pytest.raises(ValueError) as e:
            validate_params(params)
        assert expected_results == str(e.value)

    @pytest.mark.parametrize("amp_offset, expected_results", [
        ("anyoldtext", "Invalid value 'anyoldtext' for function parameter 'offset'.")
    ])
    def test_validate_params_offset(self, amp_offset, expected_results):
        params = {
            "offset": amp_offset
        }
        with pytest.raises(ValueError) as e:
            validate_params(params)
        assert expected_results == str(e.value)

    @pytest.mark.parametrize("amp_conn_guid, expected_results", [
        ("anyoldtext", "Invalid value 'anyoldtext' for function parameter 'conn_guid'.")
    ])
    def test_validate_params_conn_guid(self, amp_conn_guid, expected_results):
        params = {
            "conn_guid": amp_conn_guid
        }
        with pytest.raises(ValueError) as e:
            validate_params(params)
        assert expected_results == str(e.value)

    @pytest.mark.parametrize("amp_internal_ip, expected_results", [
        ("anyoldtext", "Invalid value 'anyoldtext' for function parameter 'internal_ip'.")
    ])
    def test_validate_params_internal_ip(self, amp_internal_ip, expected_results):
        params = {
            "internal_ip": amp_internal_ip
        }
        with pytest.raises(ValueError) as e:
            validate_params(params)
        assert expected_results == str(e.value)

    @pytest.mark.parametrize("amp_external_ip, expected_results", [
        ("anyoldtext", "Invalid value 'anyoldtext' for function parameter 'external_ip'.")
    ])
    def test_validate_params_external_ip(self, amp_external_ip, expected_results):
        params = {
            "external_ip": amp_external_ip
        }
        with pytest.raises(ValueError) as e:
            validate_params(params)
        assert expected_results == str(e.value)

class TestAmpHelpersValidateOptsErr:
    """Test validate_opts function"""


    @pytest.mark.parametrize("api_version, client_id, api_token, expected_results", [
        ("v1", "01234abcde56789efghi", "abcd1234-a123-123a-123a-123456abcdef",
         "Mandatory config setting 'base_url' not set."),
    ])
    def test_validate_opts_base_url_Not_set(self, api_version, client_id, api_token, expected_results):
        func = Func({
            "api_version": api_version,
            "client_id": client_id,
            "api_token": api_token,
        })
        with pytest.raises(Exception) as e:
            validate_opts(func)
        assert expected_results == str(e.value)

    @pytest.mark.parametrize("base_url, client_id, api_token, expected_results", [
        ("https://api.amp.cisco.com/", "01234abcde56789efghi", "abcd1234-a123-123a-123a-123456abcdef",
         "Mandatory config setting 'api_version' not set."),
    ])
    def test_validate_opts_api_version_Not_set(self, base_url, client_id, api_token, expected_results):
        func = Func({
            "base_url": base_url,
            "client_id": client_id,
            "api_token": api_token,
        })
        with pytest.raises(Exception) as e:
            validate_opts(func)
        assert expected_results == str(e.value)

    @pytest.mark.parametrize("base_url, api_version, api_token, expected_results", [
        ("https://api.amp.cisco.com/", "v1", "abcd1234-a123-123a-123a-123456abcdef",
         "Mandatory config setting 'client_id' not set."),
    ])
    def test_validate_opts_client_id_Not_set(self, base_url, api_version, api_token, expected_results):
        func = Func({
            "base_url": base_url,
            "api_version": api_version,
            "api_token": api_token,
        })
        with pytest.raises(Exception) as e:
            validate_opts(func)
        assert expected_results == str(e.value)

    @pytest.mark.parametrize("base_url, api_version, client_id, expected_results", [
        ("https://api.amp.cisco.com/", "v1", "01234abcde56789efedc",
         "Mandatory config setting 'api_token' not set."),
    ])
    def test_validate_opts_api_token_Not_set(self, base_url, api_version, client_id, expected_results):
        func = Func({
            "base_url": base_url,
            "api_version": api_version,
            "client_id": client_id,
        })
        with pytest.raises(Exception) as e:
            validate_opts(func)
        assert expected_results == str(e.value)

    @pytest.mark.parametrize("base_url, api_version, client_id, api_token, expected_results", [
        (None, None, None, None, "Invalid format for config setting 'base_url'."),
        ("https://api.amp.cisco.com/", None, None, None, "Invalid format for config setting 'api_version'."),
        ("https://api.amp.cisco.com/", "v1", None, None, "Invalid format for config setting 'client_id'."),
        ("https://api.amp.cisco.com/", "v1", "01234abcde56789efedc", None, "Invalid format for config setting 'api_token'."),
    ])
    def test_validate_opts_Invalid(self, base_url, api_version, client_id, api_token, expected_results):
        func = Func({
            "base_url": base_url,
            "api_version": api_version,
            "client_id": client_id,
            "api_token": api_token,
        })
        with pytest.raises(Exception) as e:
            validate_opts(func)
        assert expected_results == str(e.value)

class TestAmpHelpersIsNone:
    """Test init_env function"""

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
        assert expected_results == results