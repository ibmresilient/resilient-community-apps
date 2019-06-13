# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Test requests functionality."""
from __future__ import print_function
from mock import patch
import pytest
from fn_sep.lib.requests_sep import *
from mock_artifacts import mocked_request_session, get_test_zip
"""
Suites of tests to test the Symantec SEP requests functions
"""
FUNCTION_PARAMS  = {}

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def get_req_data(req_name):
    req_data = {
        "get": ({
            "method": "get",
            "url": 'https://192.168.1.2:8446/sepm/api/v1/computers',
            "verify_flag": False,
            "headers": {'content-type': 'application/json',
                        'Authorization': 'Bearer abcd1234-a123-123a-123a-123456abcdef'},
            "params": {'sort': None, 'lastUpdate': None, 'computerName': u'TESTHOST', 'pageIndex': None,
                        'pageSize': None, 'os': None, 'domain': None, 'order': None}
        }),
        "patch": ({
            "method": "patch",
            "url": 'https://192.168.1.2:8446/sepm/api/v1/computers',
            "verify_flag": False,
            "headers": {'content-type': 'application/json',
                        'Authorization': 'Bearer abcd1234-a123-123a-123a-123456abcdef'},
            "data": [{"group": {"id": "8E20F39B0946C25D118925C2E28C2D59"}, "hardwareKey": "DC7D24D6465566D2941F35BC8D17801E"}]
         }),
        "post": ({
            "method": "post",
            "url": 'https://192.168.1.2:8446/sepm/api/v1/command-queue/files',
            "verify_flag": False,
            "headers": {'content-type': 'application/json',
                        'Authorization': 'Bearer abcd1234-a123-123a-123a-123456abcdef'},
            "params": {'sha1': None, 'source': None, 'computer_ids': [u'D41BA16E0946C25D40C83823C500518B'],
                     'sha256': u'abc4fd780b47e8d4e5661d4c3881d114e8631e84a686e3bb8aad85d4af20454a',
                     'file_path': u'C:\\temp\\test.txt', 'md5': None}
        }),
        "put": ({
            "method": "put",
            "url": 'https://192.168.1.2:8446/sepm/api/v1/groups/7E4BB200A9FE9DC526EDABFB1EE261B8/system-lockdown/fingerprints/2012E43F25AE42A9A826866518866226',
            "verify_flag": False,
            "headers": {'content-type': 'application/json',
                        'Authorization': 'Bearer abcd1234-a123-123a-123a-123456abcdef'},
            "data": '{"fingerprint_id": "2012D32F25AE42A9A826866518866226", "group_id": "7E4BB119A9FE9DC526EDABFB1EE261B8"}'
        }),
        "delete": ({
            "method": "delete",
            "url": 'https://192.168.1.2:8446/sepm/api/v1/policy-objects/fingerprints/2012E43F25AE42A9A826866518866226',
            "verify_flag": False,
            "headers": {'content-type': 'application/json',
                        'Authorization': 'Bearer abcd1234-a123-123a-123a-123456abcdef'}
        }),
        "get_content": ({
            "method": "get",
            "url": 'https://192.168.1.2:8446/sepm/api/v1/command-queue/file/BGD3A9A9A9FE9DC54EBE8CB410E3898C/content',
            "verify_flag": False,
            "headers": {'content-type': 'application/json; charset=UTF-8', 'Accept-Encoding': 'gzip, deflate, compress',
                        'Authorization': 'Bearer bd68a651-2602-4ac1-ad21-74112a13d20b'}
        }),
    }
    return req_data[req_name]

def get_config():
    return dict({
        "base_path":    "/sepm/api/v1",
        "auth_path":    "/sepm/api/v1/identity/authenticate",
        "host":         "192.168.1.2",
        "port":         "8446",
        "username":     "admin",
        "password":     "password",
        "domain":       "Default",
        "results_limit": 6
    })

class TestSEPRequests:

    """Test get_unzipped_contents function"""
    @pytest.mark.parametrize("zip,  expected_results", [
        (get_test_zip(),  ["10", "^oy~*nk~k"]),
    ])
    def test_unzip(self, zip, expected_results):
        req_sep = RequestsSep(get_config(), FUNCTION_PARAMS)
        (key, content) = req_sep.get_unzipped_contents(zip)
        assert expected_results[0] == key
        assert expected_results[1] == content

    """Test decrypt_xor function"""
    @pytest.mark.parametrize("xored_data, key, expected_results", [
        ("^oy~*nk~k", "10" , "Test data"),
    ])
    def test_decrypt_xor(self, xored_data, key, expected_results):
        req_sep = RequestsSep(get_config(), FUNCTION_PARAMS)
        results = req_sep.decrypt_xor(xored_data, key)
        assert expected_results == results

    """Test get method function"""
    @patch('fn_sep.lib.requests_sep.request', side_effect=mocked_request_session)
    @pytest.mark.parametrize("req_data, expected_results", [
        (get_req_data("get"), (2))
    ])
    def test_get_method(self, mock_get, req_data, expected_results):

        keys = ["content", "firstPage", "lastPage", "number", "numberOfElements", "size", "sort", "totalElements",
                  "totalPages"]

        req_sep = RequestsSep(get_config(), FUNCTION_PARAMS)
        method = req_data.pop("method")
        url = req_data.pop("url")
        results = req_sep.execute_call(method, url, **req_data)
        assert_keys_in(results, *keys)
        assert expected_results == len(results["content"])

    """Test patch method function"""
    @patch('fn_sep.lib.requests_sep.request', side_effect=mocked_request_session)
    @pytest.mark.parametrize("req_data, expected_results", [
        (get_req_data("patch"), [200, "OK"])
    ])
    def test_patch_method(self, mock_patch, req_data, expected_results):

        keys = ["responseCode", "responseMessage"]

        req_sep = RequestsSep(get_config(), FUNCTION_PARAMS)
        method = req_data.pop("method")
        url = req_data.pop("url")
        results = req_sep.execute_call(method, url, **req_data)
        assert_keys_in(results[0], *keys)
        assert expected_results[0] == int(results[0]["responseCode"])
        assert expected_results[1] == results[0]["responseMessage"]

    """Test post method function"""
    @patch('fn_sep.lib.requests_sep.request', side_effect=mocked_request_session)
    @pytest.mark.parametrize("req_data, expected_results", [
        (get_req_data("post"), "171969C124D54C069D7018914AA02184")
    ])
    def test_post_method(self, mock_post, req_data, expected_results):

        req_sep = RequestsSep(get_config(), FUNCTION_PARAMS)
        method = req_data.pop("method")
        url = req_data.pop("url")
        results = req_sep.execute_call(method, url, **req_data)
        assert expected_results == results["commandID"]

    """Test put method function"""
    @patch('fn_sep.lib.requests_sep.request', side_effect=mocked_request_session)
    @pytest.mark.parametrize("req_data, expected_results", [
        (get_req_data("put"), "")
    ])
    def test_put_method(self, mock_post, req_data, expected_results):
        keys = ["responseCode", "responseMessage"]

        req_sep = RequestsSep(get_config(), FUNCTION_PARAMS)
        method = req_data.pop("method")
        url = req_data.pop("url")
        results = req_sep.execute_call(method, url, **req_data)
        assert expected_results == results

    """Test delete method function"""
    @patch('fn_sep.lib.requests_sep.request', side_effect=mocked_request_session)
    @pytest.mark.parametrize("req_data, expected_results", [
        (get_req_data("delete"), "")
    ])
    def test_delete_method(self, mock_post, req_data, expected_results):
        keys = ["responseCode", ""]

        req_sep = RequestsSep(get_config(), FUNCTION_PARAMS)
        method = req_data.pop("method")
        url = req_data.pop("url")
        results = req_sep.execute_call(method, url, **req_data)
        assert expected_results == results

    """Test get content function"""
    @patch('fn_sep.lib.requests_sep.request', side_effect=mocked_request_session)
    @pytest.mark.parametrize("req_data, expected_results", [
        (get_req_data("get_content"), "Test data")
    ])
    def test_get_content(self, mock_post, req_data, expected_results):
        keys = ["responseCode", ""]

        req_sep = RequestsSep(get_config(), FUNCTION_PARAMS)
        method = req_data.pop("method")
        url = req_data.pop("url")
        results = req_sep.execute_call(method, url, **req_data)
        assert expected_results == results



