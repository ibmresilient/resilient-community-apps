# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Test helper functions"""
import pytest
from fn_clamav.lib.helpers import *
from  mock_artifacts import mocked_res_client
"""
Suites of tests to test the fn_clamav Helper functions
"""

class Func(object):
    def __init__(self, options={}):
        self.options = options

class TestClamavHelpersValidateParamsGood:
    """Test validate_params function"""

    @pytest.mark.parametrize("incident_id, expected_results", [
        (50, None)
    ])
    def test_validate_params_incident_id(self, incident_id, expected_results):
        params = {
            "incident_id": incident_id
        }
        results = validate_params(params, ['incident_id'])
        assert (expected_results == results)

    @pytest.mark.parametrize("artifact_id, expected_results", [
        (50, None)
    ])
    def test_validate_params_artifact_id(self, artifact_id, expected_results):
        params = {
            "artifact_id": artifact_id
        }
        results = validate_params(params, [])
        assert (expected_results == results)

    @pytest.mark.parametrize("task_id, expected_results", [
        (50, None)
    ])
    def test_validate_params_task_id(self, task_id, expected_results):
        params = {
            "task_id": task_id
        }
        results = validate_params(params, [])
        assert (expected_results == results)

    @pytest.mark.parametrize("attachment_id, expected_results", [
        (50, None)
    ])
    def test_validate_params_attachment_id(self, attachment_id, expected_results):
        params = {
            "incident_id": attachment_id
        }
        results = validate_params(params, [])
        assert (expected_results == results)

class TestClamavHelpersValidateParamsErr:
    """Test validate_params function"""

    @pytest.mark.parametrize("incident_id, artifact_id, task_id, attachment_id, expected_results", [
        ("anyoldtext", 25, 2251251, 10, "Invalid value 'anyoldtext' for function parameter 'incident_id'."),
        (2095, "anyoldtext", 2251251, 10, "Invalid value 'anyoldtext' for function parameter 'artifact_id'."),
        (2095, 25, "anyoldtext", 10, "Invalid value 'anyoldtext' for function parameter 'task_id'."),
        (2095, 25, 2251251, "anyoldtext", "Invalid value 'anyoldtext' for function parameter 'attachment_id'.")
    ])
    def test_validate_params_incident_id(self, incident_id, artifact_id, task_id, attachment_id, expected_results):
        params = {
            "incident_id": incident_id,
            "artifact_id": artifact_id,
            "task_id": task_id,
            "attachment_id": attachment_id
        }
        with pytest.raises(ValueError) as e:
            validate_params(params, ['incident_id'])
        assert expected_results == str(e.value)

class TestClamavHelpersValidateOptsErr:
    """Test validate_opts function"""


    @pytest.mark.parametrize("port, timeout, expected_results", [
        (3310, 500,
         "Mandatory config setting 'host' not set."),
    ])
    def test_validate_opts_host_Not_set(self, port, timeout, expected_results):
        func = Func({
            "port": port,
            "timeout": timeout
        })
        with pytest.raises(Exception) as e:
            validate_opts(func)
        assert expected_results == str(e.value)

    @pytest.mark.parametrize("host, timeout, expected_results", [
        ("localhost", 500,
         "Mandatory config setting 'port' not set."),
    ])
    def test_validate_opts_port_Not_set(self, host, timeout, expected_results):
        func = Func({
            "host": host,
            "timeout": timeout
        })
        with pytest.raises(Exception) as e:
            validate_opts(func)
        assert expected_results == str(e.value)

    @pytest.mark.parametrize("host, port, expected_results", [
        ("localhost", 500,
         "Mandatory config setting 'timeout' not set."),
    ])
    def test_validate_opts_timeout_Not_set(self, host, port, expected_results):
        func = Func({
            "host": host,
            "port": port
        })
        with pytest.raises(Exception) as e:
            validate_opts(func)
        assert expected_results == str(e.value)

    @pytest.mark.parametrize("host, port, timeout, expected_results", [
        (None, None, None, "Invalid format for config setting 'host'."),
        ("*()&", None, None, "Invalid format for config setting 'host'."),
        ("localhost", None, None, "Invalid format for config setting 'port'."),
        ("localhost", 3310, None, "Invalid format for config setting 'timeout'."),
    ])
    def test_validate_opts_Invalid(self, host, port, timeout, expected_results):
        func = Func({
            "host": host,
            "port": port,
            "timeout": timeout
        })
        with pytest.raises(Exception) as e:
            validate_opts(func)
        assert expected_results == str(e.value)

class TestClamavHelpersIsNone:
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

class Test_Clamav_get_file_attachment:
    """ Test for the get_file_attachment function"""

    @pytest.mark.parametrize("incident_id, artifact_id, task_id, attachment_id, expected_results_1, expected_results_2", [
        (2095, None, None, 25, "incident_eicar.txt", b"X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"),
        (2095, 10, None, None, "artifact_eicar.txt", b"X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"),
        (2095, None, 2251251, 25, "task_eicar.txt", b"X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*")
    ])
    def test_get_file_attachment(self, incident_id, artifact_id, task_id, attachment_id, expected_results_1, expected_results_2):
        """ Test get_file_attachment using mocked data.  """

        results = get_file_attachment(mocked_res_client(), incident_id, artifact_id, task_id, attachment_id)

        data_content = results["content"]
        file_name = results["filename"]
        assert expected_results_1 == file_name
        assert expected_results_2 == data_content
