# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
from resilient_circuits.action_message import FunctionError_
from mock import Mock, patch
import time
import os.path
from fn_mcafee_atd.util.helper import submit_file, check_atd_status, get_atd_report, create_report_file, remove_dir, \
    check_status_code, _get_atd_session_headers, submit_url, check_timeout, get_incident_id, check_config
from fn_mcafee_atd.components.mcafee_atd_analyze_file import _get_file


class MockClass:
    def __init__(self):
        self.mock = {
            "atd_username": TestMcafeeAtdAnalyzeFile.fake_username,
            "atd_password": TestMcafeeAtdAnalyzeFile.fake_password,
            "atd_url": TestMcafeeAtdAnalyzeFile.fake_url,
            "trust_cert": TestMcafeeAtdAnalyzeFile.verify,
            "filePriority": "add_to_q"
        }
        return

    def __setitem__(self, key, value):
        self.mock[key] = value


class MockCredsAfterCheck:
    def __init__(self):
        self.atd_username = TestMcafeeAtdAnalyzeFile.fake_username
        self.atd_password = TestMcafeeAtdAnalyzeFile.fake_password
        self.atd_url = TestMcafeeAtdAnalyzeFile.fake_url
        self.trust_cert = TestMcafeeAtdAnalyzeFile.verify
        self.filePriority = "add_to_q"
        self.timeout_mins = 30
        self.polling_interval = 60


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
        "VE-SDK-API": str.encode("c2Vzc2lvbl9rZXk6MQ==")
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

    def test_verify_config_no_section(self):
        mock_opts = {}
        try:
            check_config(mock_opts)
        except ValueError as e:
            assert  e.args[0] == "[fn_mcafee_atd] section is not set in the config file"

    def test_verify_config_no_atd_url(self):
        mock_opts = {
            "fn_mcafee_atd": MockClass().mock
        }
        del mock_opts["fn_mcafee_atd"]["atd_url"]
        try:
            check_config(mock_opts)
        except ValueError as e:
            assert e.args[0] == "atd_url is not set. You must set this value to run this function"

    def test_verify_config_no_atd_username(self):
        mock_opts = {
            "fn_mcafee_atd": MockClass().mock
        }
        del mock_opts["fn_mcafee_atd"]["atd_username"]
        try:
            check_config(mock_opts)
        except ValueError as e:
            assert e.args[0] == "atd_username is not set. You must set this value to run this function"

    def test_verify_config_no_atd_password(self):
        mock_opts = {
            "fn_mcafee_atd": MockClass().mock
        }
        del mock_opts["fn_mcafee_atd"]["atd_password"]
        try:
            check_config(mock_opts)
        except ValueError as e:
            assert e.args[0] == "atd_password is not set. You must set this value to run this function"

    def test_verify_config_valid(self):
        mock_opts = {
            "fn_mcafee_atd": MockClass().mock
        }
        mock_opts["fn_mcafee_atd"]["trust_cert"] = "True"
        actual_config = check_config(mock_opts)

        expected_config = mock_opts["fn_mcafee_atd"]
        expected_config["timeout_mins"] = 30
        expected_config["polling_interval"] = 60
        expected_config["trust_cert"] = True

        assert actual_config == expected_config

    def test_verify_config_default_url(self):
        mock_opts = {
            "fn_mcafee_atd": MockClass().mock
        }
        mock_opts["fn_mcafee_atd"]["atd_url"] = "<your_atd_url>"
        try:
            check_config(mock_opts)
        except ValueError as e:
            assert e.args[0] == "atd_url is still the default value, this must be changed to run this function"

    def test_verify_config_default_username(self):
        mock_opts = {
            "fn_mcafee_atd": MockClass().mock
        }
        mock_opts["fn_mcafee_atd"]["atd_username"] = "<your_atd_username>"
        try:
            check_config(mock_opts)
        except ValueError as e:
            assert e.args[0] == "atd_username is still the default value, this must be changed to run this function"

    def test_verify_config_default_password(self):
        mock_opts = {
            "fn_mcafee_atd": MockClass().mock
        }
        mock_opts["fn_mcafee_atd"]["atd_password"] = "<your_atd_password>"
        try:
            check_config(mock_opts)
        except ValueError as e:
            assert e.args[0] == "atd_password is still the default value, this must be changed to run this function"

    def test_verify_config_default_trust_cert(self):
        mock_opts = {
            "fn_mcafee_atd": MockClass().mock
        }
        mock_opts["fn_mcafee_atd"]["trust_cert"] = "[True|False]"
        try:
            check_config(mock_opts)
        except ValueError as e:
            assert e.args[0] == "trust_cert is not set correctly, please set to True or False to run this function"

    @patch("requests.get")
    def test_helper_get_atd_session_headers(self, mocked_requests_get):
        sim_content = {
            "results": {
                "session": "session_key",
                "userId": "1"
            }
        }
        mocked_requests_get.return_value = self._generateResponse(sim_content, 200)
        creds = MockCredsAfterCheck()

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
        creds = MockCredsAfterCheck()

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
        creds = MockCredsAfterCheck()

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
                "status": "Analysis is complete",
                "jobid": "1234"
            }
        }
        sim_get_content3 = {
            "severity": "1"
        }
        mocked_requests_get.side_effect = [self._generateResponse(sim_get_content1, 200),
                                           self._generateResponse(sim_get_content2, 200)]
        creds = MockCredsAfterCheck()

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
                                           self._generateResponse(sim_get_content2, 200),
                                           self._generateResponse(sim_get_content1, 200),
                                           self._generateResponse(sim_get_content3, 200)]
        r = check_atd_status(creds, '1')
        # Assert analysis is complete
        assert r is True

        sim_get_content2["results"]["istate"] = 1
        mocked_requests_get.side_effect = [self._generateResponse(sim_get_content1, 200),
                                           self._generateResponse(sim_get_content2, 200),
                                           self._generateResponse(sim_get_content1, 200),
                                           self._generateResponse(sim_get_content3, 200)]
        r = check_atd_status(creds, '1')
        # Assert analysis is complete
        assert r is True

    def test_create_and_delete_file(self):
        name = "file name"
        type = "pdf"
        res = create_report_file(name, type)

        # Assert file name and directory and location are returned
        assert res["report_file_name"] == "McAfeeATD_{}.{}".format(name, type)
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
            sim_get_content2 = str.encode("This is the report result")
            generated_report = self._generateResponse(sim_get_content2, 200)
            creds = MockCredsAfterCheck()
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
            res = get_atd_report(creds, '1', "pdf", f)

            # Assert JSON report is returned
            assert res == generated_report.content

            # Assert file contents is as expected
            with open(f.get("report_file"), 'r') as r:
                content = r.read()
                assert generated_report.content.decode("utf-8") == content

        finally:
            remove_dir(f.get("tmp_dir"))

    def test_check_timeout(self):
        start = time.time()
        # Assert does not time out early
        assert check_timeout(start, 1, 60) is True

        # Assert raises FunctionError if it times out
        start = time.time() - 30
        try:
            check_timeout(start, 1, 1)
        except FunctionError_ as e:
            assert e.args[0] == "Timeout limit reached"

    def test_get_incident_id(self):
        kw = {}

        # Assert error is thrown if incident_id is not provided
        try:
            get_incident_id(**kw)
        except FunctionError_ as e:
            assert e.args[0] == "incident_id is required"

        # Assert incident_id is returned if it exists
        kw["incident_id"] = "1"
        incident_id = get_incident_id(**kw)
        assert incident_id == "1"

    @patch("requests.get")
    def test_get_file(self, mocked_requests_get):
        kw = {}
        mocked_client = Mock()
        # Assert error is thrown if inputs are not set
        try:
            _get_file(mocked_client, **kw)
        except ValueError as e:
            assert e.args[0] == "Inputs not set correctly"

        # Assert file and file name are returned when downloading from artifact
        kw = {
            "incident_id": "1",
            "artifact_id": "123",
        }
        sim_get_content1 = {
            "attachment": {
                "name": "artifact_file"
            }
        }
        mocked_client.get.return_value = sim_get_content1
        mocked_client.get_content.return_value = "File Contents"
        expected_r = {
            "file": "File Contents",
            "file_name": sim_get_content1["attachment"]["name"]
        }

        response = _get_file(mocked_client, **kw)
        assert response == expected_r

        # Assert file and file name are returned when downloading from task attachment
        kw = {
            "incident_id": "1",
            "task_id": "456",
            "attachment_id": "789"
        }
        sim_get_content1 = {"name": "task_file"}
        mocked_client.get.return_value = sim_get_content1
        expected_r = {
            "file": "File Contents",
            "file_name": sim_get_content1["name"]
        }

        response = _get_file(mocked_client, **kw)
        assert response == expected_r

        # Assert file and file name are returned when downloading from incident attachment
        kw = {
            "incident_id": "1",
            "attachment_id": "789"
        }
        sim_get_content1 = {"name": "incident_file"}
        mocked_client.get.return_value = sim_get_content1
        expected_r = {
            "file": "File Contents",
            "file_name": sim_get_content1["name"]
        }

        response = _get_file(mocked_client, **kw)
        assert response == expected_r
