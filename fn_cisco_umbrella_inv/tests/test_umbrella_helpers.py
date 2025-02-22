# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
"""Test helper functions"""
import pytest
from fn_cisco_umbrella_inv.util.helpers import *

"""
Suites of tests to test the Umbrella Investigate Helper functions
"""

class TestUmbrellaHelpersProcessParams:
    """Test process_params function"""

    @pytest.mark.parametrize("umbinv_resource, expected_results", [
        ("93.184.216.119", "93.184.216.119"),
        ("domain.com", "domain.com"),
        ("http://www.hoarafushionline.net/Fhabeys.exe", "http%3A%2F%2Fwww.hoarafushionline.net%2FFhabeys.exe"),
        ("domain.com", "domain.com")
    ])
    def test_process_params_resource(self, umbinv_resource, expected_results):
        process_result = {}
        params = {
            "resource": umbinv_resource
        }
        process_params(params, process_result)
        results = process_result["_res"]
        assert (expected_results == results)

    @pytest.mark.parametrize("umbinv_domain, expected_results", [
        ("domain.com", "domain.com")
    ])
    def test_process_params_domain_name(self, umbinv_domain, expected_results):
        process_result = {}
        params = {
            "domain": umbinv_domain
        }
        process_params(params, process_result)
        results = process_result["_domain"]
        assert (expected_results == results)

    @pytest.mark.parametrize("umbinv_ipaddr, expected_results", [
        ("93.184.216.119", "93.184.216.119")
    ])
    def test_process_params_ipaddr(self, umbinv_ipaddr, expected_results):
        process_result = {}
        params = {
            "ipaddr": umbinv_ipaddr
        }
        process_params(params, process_result)
        results = process_result["_ipaddr"]
        assert (expected_results == results)

    @pytest.mark.parametrize("umbinv_regex, expected_results", [
        ("paypal.*", "paypal.*")
    ])
    def test_process_params_regex(self, umbinv_regex, expected_results):
        process_result = {}
        params = {
            "regex": umbinv_regex
        }
        process_params(params, process_result)
        results = process_result["_regex"]
        assert (expected_results == results)

    @pytest.mark.parametrize("umbinv_resource, expected_results", [
        ("test@example.com", "test@example.com")
    ])
    def test_process_params_emails(self, umbinv_resource, expected_results):
        process_result = {}
        params = {
            "resource": umbinv_resource
        }
        process_params(params, process_result)
        results = process_result["_res"]
        assert (expected_results == results)

    @pytest.mark.parametrize("umbinv_resource, expected_results", [
        ("ns1.google.com", "ns1.google.com")
    ])
    def test_process_params_nameservers(self, umbinv_resource, expected_results):
        process_result = {}
        params = {
            "resource": umbinv_resource
        }
        process_params(params, process_result)
        results = process_result["_res"]
        assert (expected_results == results)

class TestUmbrellaHelpersValidateParams:
    """Test validate_params function"""

    @pytest.mark.parametrize("umbinv_resource, expected_results", [
        ("anyoldtext", "Invalid value for function parameter 'resource'.")
    ])
    def test_validate_params_resource(self, umbinv_resource, expected_results):
        params = {
            "resource": umbinv_resource
        }
        with pytest.raises(ValueError) as e:
            validate_params(params)
        assert str(e.value) == expected_results

    @pytest.mark.parametrize("umbinv_resource, expected_results", [
        ("anyoldtext", "Invalid value for function parameter 'resource'.")
    ])
    def test_validate_params_resource_any(self, umbinv_resource, expected_results):
        params = {
            "resource": umbinv_resource
        }
        with pytest.raises(ValueError) as e:
            validate_params(params)
        assert str(e.value) == expected_results

    @pytest.mark.parametrize("umbinv_resource, expected_results", [
        ("93.184.216.119.1", "Invalid value for function parameter 'resource'.")
    ])
    def test_validate_params_resource_ip(self, umbinv_resource, expected_results):
        params = {
            "resource": umbinv_resource
        }
        with pytest.raises(ValueError) as e:
            validate_params(params)
        assert str(e.value) == expected_results

    @pytest.mark.parametrize("umbinv_domain, expected_results", [
        ("domain.com.1", "Invalid value for function parameter 'domain'."),
        ("93.184.216.119", "Invalid value for function parameter 'domain'."),
        ("http://www.hoarafushionline.net/Fhabeys.exe", "Invalid value for function parameter 'domain'."),
        ("test@example.com", "Invalid value for function parameter 'domain'.")

    ])
    def test_validate_params_domain_name(self, umbinv_domain, expected_results):
        params = {
            "domain": umbinv_domain
        }
        with pytest.raises(ValueError) as e:
            validate_params(params)
        assert str(e.value) == expected_results

    @pytest.mark.parametrize("umbinv_ipaddr, expected_results", [
        ("domain.com", "Invalid value for function parameter 'ipaddr'."),
        ("93.184.216.119.1", "Invalid value for function parameter 'ipaddr'."),
        ("http://www.hoarafushionline.net/Fhabeys.exe", "Invalid value for function parameter 'ipaddr'."),
        ("test@example.com", "Invalid value for function parameter 'ipaddr'.")
    ])
    def test_validate_params_ip_address(self, umbinv_ipaddr, expected_results):
        params = {
            "ipaddr": umbinv_ipaddr
        }
        with pytest.raises(ValueError) as e:
            validate_params(params)
        assert str(e.value) == expected_results

    @pytest.mark.parametrize("umbinv_regex, expected_results", [
        ("&\()", "Invalid value for function parameter 'regex'.")
    ])
    def test_process_params_regex(self, umbinv_regex, expected_results):
        params = {
            "regex": umbinv_regex
        }
        with pytest.raises(ValueError) as e:
            validate_params(params)
        assert str(e.value) == expected_results

    @pytest.mark.parametrize("umbinv_resource, expected_results", [
        ("domain.com_", "Invalid value for function parameter 'resource'."),
        ("domain.com.1", "Invalid value for function parameter 'resource'."),
        ("93.184.216.119.21", "Invalid value for function parameter 'resource'."),
        ("http//www.hoarafushionline.net/Fhabeys.exe", "Invalid value for function parameter 'resource'."),
        ("test@@example.com.1", "Invalid value for function parameter 'resource'.")

    ])
    def test_validate_params_emails(self, umbinv_resource, expected_results):
        params = {
            "resource": umbinv_resource
        }
        with pytest.raises(ValueError) as e:
            validate_params(params)
        assert str(e.value) == expected_results


class TestUmbrellaHelpersOmitParams:
    """Test omit_params function"""

    @pytest.mark.parametrize("params, omit_list, expected_results", [
        ({'regex': 'aaa', 'param2': 'bbb', 'param3': 'bbb'}, "['regex']", {'param2': 'bbb', 'param3': 'bbb'}),
        ({'regex': 'aaa', 'param2': 'bbb', 'param3': 'bbb'}, "['regex','param2'", {'param3': 'bbb'}),
        ({'regex': 'aaa', 'param2': 'bbb', 'param3': 'bbb'}, "['param3'", {'regex': 'aaa', 'param2': 'bbb'})
    ])
    def test_omit_params(self, params, omit_list, expected_results):
        results =  omit_params(dict(params), omit_list)
        assert (expected_results == results)

class TestUmbrellaHelpersIsNone:
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
        results = str(param).lower() == "none"
        assert results == expected_results