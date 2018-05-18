# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from mock import Mock, patch
import requests
import sys
import os.path
from fn_mcafee_atd.util.helper import submit_file, check_atd_status, get_atd_report, create_report_file, remove_dir, \
    check_status_code, _get_atd_session_headers, _check_url_ending, submit_url
sys.path.append("../fn_mcafee_atd/util")
sys.path.append("fn_mcafee_atd/util")

PACKAGE_NAME = "fn_mcafee_atd"
FUNCTION_NAME = "mcafee_atd_analyze_file"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


# def call_mcafee_atd_analyze_file_function(circuits, function_params, timeout=10):
#     # Fire a message to the function
#     evt = SubmitTestFunction("mcafee_atd_analyze_file", function_params)
#     circuits.manager.fire(evt)
#     event = circuits.watcher.wait("mcafee_atd_analyze_file_result", parent=evt, timeout=timeout)
#     assert event
#     assert isinstance(event.kwargs["result"], FunctionResult)
#     pytest.wait_for(event, "complete", True)
#     return event.kwargs["result"].value


class MockClass:
    def __init__(self):
        self.atd_username = TestMcafeeAtdAnalyzeFile.fake_username
        self.atd_password = TestMcafeeAtdAnalyzeFile.fake_username
        self.atd_url = TestMcafeeAtdAnalyzeFile.fake_url
        self.trust_cert = TestMcafeeAtdAnalyzeFile.verify
        self.vm_profile_list = "1"
        self.filePriority = "add_to_q"
        return


class TestMcafeeAtdAnalyzeFile:
    # Test Data

    fake_host = "mcafee_atd_url.com"
    fake_port = 8888
    fake_url = "https://" + fake_host + ":" + str(fake_port)
    fake_username = "Username"
    fake_password = "MyPassword"
    verify = True
    sim_session_headers = {
        "Accept": "application/vnd.ve.v1.0+json",
        "VE-SDK-API": "c2Vzc2lvbl9rZXk6MQ=="
    }


    # Util function to generate simulated requests response
    def _generateResponse(self, content, status):
        class simResponse:
            def __init__(self, content, status):
                self.status_code = status
                self.content = content

            def json(self):
                return self.content

        return simResponse(content, status)

    @patch("requests.get")
    def test_helper_get_atd_session_headers(self, mocked_requests_get):
        sim_content = {
            "results": {
                "session": "session_key",
                "userId": "1"
            }
        }
        mocked_requests_get.return_value = self._generateResponse(sim_content, 200)
        creds = MockClass()

        atd_session_headers = _get_atd_session_headers(creds)

        # Assert headers returned are correct
        assert atd_session_headers == self.sim_session_headers

    @patch("requests.get")
    def test_helper_check_status_code_good(self, mocked_requests_get):
        mocked_requests_get.return_value = self._generateResponse(None, 200)

        status = check_status_code(mocked_requests_get.return_value)
        # Assert status does not return an error
        assert status is None

    @patch("requests.get")
    def test_helper_check_status_code_bad(self, mocked_requests_get):
        try:
            mocked_requests_get.return_value = self._generateResponse(None, 404)

            check_status_code(mocked_requests_get.return_value)
        # Assert status does return an error
        except ValueError:
            assert True

    def test_helper_check_url_ending_file(self):
        url = "https://www.google.com/file.exe"
        submit_type = _check_url_ending(url)

        # Assert submit type is 3
        assert submit_type is '3'

    def test_helper_check_url_ending_not_file(self):
        url = "https://www.google.com/news"
        submit_type = _check_url_ending(url)

        # Assert submit type is 1
        assert submit_type is '1'

    @patch("requests.get")
    @patch("requests.post")
    def test_file_upload(self, mocked_requests_post, mocked_requests_get):
        sim_post_content = {}
        sim_get_content = {
            "results": {
                "session": "session_key",
                "userId": "1"
            }
        }
        f = "This is file contents"
        mocked_requests_post.return_value = self._generateResponse(sim_post_content, 200)
        mocked_requests_get.return_value = self._generateResponse(sim_get_content, 200)
        creds = MockClass()

        file_upload = submit_file(creds, f, "a_new_file.txt")

        # Verify call was successful
        assert file_upload.status_code == 200

    @patch("requests.get")
    @patch("requests.post")
    def test_url_upload(self, mocked_requests_post, mocked_requests_get):
        sim_post_content = {}
        sim_get_content = {
            "results": {
                "session": "session_key",
                "userId": "1"
            }
        }
        mocked_requests_post.return_value = self._generateResponse(sim_post_content, 200)
        mocked_requests_get.return_value = self._generateResponse(sim_get_content, 200)
        creds = MockClass()

        url_upload = submit_url(creds, url="https://www.badurl.com")

        # Verify call was successful
        assert url_upload.status_code == 200

        url_file_upload = submit_url(creds, "3", "https://www.badurl.com/file.exe")
        # Verify call was successful
        assert url_file_upload.status_code == 200

    @patch("requests.get")
    def test_check_atd_status(self, mocked_requests_get):
        sim_get_content1 = {
            "results": {
                "session": "session_key",
                "userId": "1"
            }
        }
        sim_get_content2 = {
            "results": {
                "istate": 4,
                "status": "Analysis is complete"
            }
        }
        mocked_requests_get.side_effect = [self._generateResponse(sim_get_content1, 200),
                                           self._generateResponse(sim_get_content2, 200)]
        creds = MockClass()

        r = check_atd_status(creds, '1')
        # Assert analysis is not complete
        assert r is False

        sim_get_content2["results"]["istate"] = 3
        mocked_requests_get.side_effect = [self._generateResponse(sim_get_content1, 200),
                                           self._generateResponse(sim_get_content2, 200)]
        r = check_atd_status(creds, '1')
        # Assert analysis is not complete
        assert r is False

        sim_get_content2["results"]["istate"] = 2
        mocked_requests_get.side_effect = [self._generateResponse(sim_get_content1, 200),
                                           self._generateResponse(sim_get_content2, 200)]
        r = check_atd_status(creds, '1')
        # Assert analysis is complete
        assert r is True

        sim_get_content2["results"]["istate"] = 1
        mocked_requests_get.side_effect = [self._generateResponse(sim_get_content1, 200),
                                           self._generateResponse(sim_get_content2, 200)]
        r = check_atd_status(creds, '1')
        # Assert analysis is complete
        assert r is True

    def test_create_and_delete_file(self):
        name = "file name"
        type = "pdf"
        res = create_report_file(name, type)

        # Assert file name and directory and location are returned
        assert res["report_file_name"] == "{}_report.{}".format(name, type)
        assert res.get("report_file") is not None
        assert res.get("tmp_dir") is not None

        # Assert file exists
        assert os.path.isfile(res.get("report_file")) is True

        remove_dir(res.get("tmp_dir"))
        # Assert file is removed
        assert os.path.isdir(res.get("tmp_dir")) is False

    @patch("requests.get")
    def test_get_atd_report(self, mocked_requests_get):
        name = "file name"
        type = "pdf"
        f = create_report_file(name, type)
        try:
            sim_get_content1 = {
                "results": {
                    "session": "session_key",
                    "userId": "1"
                }
            }
            sim_get_content2 = "This is the report result"
            generated_report = self._generateResponse(sim_get_content2, 200)
            creds = MockClass()
            mocked_requests_get.side_effect = [self._generateResponse(sim_get_content1, 200),
                                               generated_report]
            res = get_atd_report(creds, '1', '', f.get("report_file"))

            # Assert JSON report is returned
            assert res == generated_report.content

            # Assert file is empty
            with open(f.get("report_file"), 'r') as r:
                content = r.read()
                assert content == ""

            mocked_requests_get.side_effect = [self._generateResponse(sim_get_content1, 200),
                                               generated_report,
                                               generated_report]
            res = get_atd_report(creds, '1', "pdf", f.get("report_file"))

            # Assert JSON report is returned
            assert res == generated_report.content

            # Assert file contents is as expected
            with open(f.get("report_file"), 'r') as r:
                content = r.read()
                assert content == generated_report.content

        finally:
            remove_dir(f.get("tmp_dir"))







    # """ Tests for the mcafee_atd_analyze_file function"""
    #
    # def test_function_definition(self):
    #     """ Test that the package provides customization_data that defines the function """
    #     func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
    #     assert func is not None
    #
    # @pytest.mark.parametrize("incident_id, artifact_id, expected_results", [
    #     (123, 123, {"value": "xyz"}),
    #     (123, 123, {"value": "xyz"})
    # ])
    # def test_success(self, circuits_app, incident_id, artifact_id, expected_results):
    #     """ Test calling with sample values for the parameters """
    #     function_params = {
    #         "incident_id": incident_id,
    #         "artifact_id": artifact_id
    #     }
    #     results = call_mcafee_atd_analyze_file_function(circuits_app, function_params)
    #     assert(expected_results == results)