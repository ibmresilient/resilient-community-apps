# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Test Sep client  class."""
from __future__ import print_function
from mock import patch
import pytest
from fn_sep.lib.sep_client import *
from  mock_artifacts import mocked_request
from fn_sep.lib.helpers import transform_kwargs
import xml.etree.ElementTree as ET
"""
Suite of tests to test Symantec SEP client class
"""

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def get_config():
    return dict({
        "base_path":    "/sepm/api/v1",
        "auth_path":    "/sepm/api/v1/identity/authenticate",
        "host":         "192.168.1.2",
        "port":         "8446",
        "username":     "admin",
        "password":     "password",
        "domain":       "Default"
    })

def setup_test_xml():
    test_xml = dedent(u"""\
        <?xml version="1.0" encoding="UTF-8"?>
        <EOC creator="Resilient" version="1.0" id="id">
            <DataSource name="name" id="id" version="version"/>
            <ScanType>QUICK_SCAN</ScanType>

            <Threat category="" type="" severity="" time="">
                <Description>Just a test.</Description>
                <Attacker/>
            </Threat>
            <Activity>
                <OS id="0" name="name" version="version">
                    <Process/>
                    <Files>
                        <File name="C:\\temp\\eicar.zip" action="create">
                            <Hash name="SHA256" value="131f95c51cc819465fa1797f6ccacf9d494aaaff46fa3eac73ae63ffbdfd8267"/>
                        </File>
                        <File name="C:\\temp\\eicar.zip" action="create">
                            <Hash name="SHA1" value=""/>
                        </File>
                        <File name="C:\\temp\\eicar.zip" action="create">
                            <Hash name="MD5" value=""/>
                        </File>
                    </Files>
                    <Registry/>
                    <Network/>
                </OS>
            </Activity>
        </EOC>""")

    return test_xml

class TestSEPClient:
    """ Test sep_client using mocked data.  """

    """ Test sep_client._get_token"""
    @patch("fn_sep.lib.sep_client.RequestsSep", side_effect=mocked_request)
    @pytest.mark.parametrize("expected_result", [
        ("abcd1234-a123-123a-123a-123456abcdef")
    ])
    def test_get_token(self, mock_post, expected_result):
        options = None
        function_params = None

        params = {
        }

        sep_client = Sepclient(get_config())
        response = sep_client._get_token()
        assert(response == expected_result)

    """ Test sep_client.get_version  """
    @patch("fn_sep.lib.sep_client.RequestsSep", side_effect=mocked_request)
    @pytest.mark.parametrize("expected_result_1, expected_result_2, expected_result_3", [
        ("14.2.1031.0100", "181118008", "1.0.0")
    ])
    def test_get_version(self, mock_get, expected_result_1, expected_result_2, expected_result_3):
        keys = ["version", "API_SEQUENCE", "API_VERSION"]

        params = {
        }

        sep_client = Sepclient(get_config())
        response = sep_client.get_version(**params)
        assert expected_result_1 == response[keys[0]]
        assert expected_result_2 == response[keys[1]]
        assert expected_result_3 == response[keys[2]]
        assert_keys_in(response, *keys)

    """ Test sep_client.get_domains  """
    @patch("fn_sep.lib.sep_client.RequestsSep", side_effect=mocked_request)
    @pytest.mark.parametrize("expected_result_1, expected_result_2, expected_result_3", [
        (2, "Default", "JP_test_Domain")
    ])
    def test_get_domains(self, mock_get, expected_result_1, expected_result_2, expected_result_3):

        params = {
        }

        sep_client = Sepclient(get_config())
        response = sep_client.get_domains(**params)
        assert expected_result_1 == len(response)
        assert expected_result_2 == response[0]["name"]
        assert expected_result_3 == response[1]["name"]

    """ Test sep_client.get_computers  """
    @patch("fn_sep.lib.sep_client.RequestsSep", side_effect=mocked_request)
    @pytest.mark.parametrize("expected_result", [
        (2)
    ])
    def test_get_computers(self, mock_get, expected_result):
        keys = ["content", "firstPage", "lastPage", "number", "numberOfElements", "size", "sort", "totalElements",
                  "totalPages"]

        params = {
        }

        sep_client = Sepclient(get_config())
        response = sep_client.get_computers(**params)
        assert_keys_in(response, *keys)
        assert expected_result == len(response["content"])

    """ Test sep_client.get_groups  """
    @patch("fn_sep.lib.sep_client.RequestsSep", side_effect=mocked_request)
    @pytest.mark.parametrize("expected_result", [
        (2)
    ])
    def test_get_groups(self, mock_get, expected_result):

        keys = ["content", "firstPage", "lastPage", "number", "numberOfElements", "size", "sort", "totalElements",
                  "totalPages"]


        params = {
        }
        sep_client = Sepclient(get_config())
        response = sep_client.get_groups(**params)
        assert_keys_in(response, *keys)
        assert expected_result == len(response["content"])

    """ Test sep_client.get_policies_summary  """
    @patch("fn_sep.lib.sep_client.RequestsSep", side_effect=mocked_request)
    @pytest.mark.parametrize("sep_domainid, sep_policy_type, expected_result", [
        ("908090000946C25D330E919313D23887", {'name': 'fw', 'id': 201}, 2)
    ])
    def test_get_policies_summary(self, mock_get, sep_domainid, sep_policy_type, expected_result):

        keys = ["content", "firstPage", "lastPage", "number", "numberOfElements", "size", "sort", "totalElements",
                  "totalPages"]

        test_kwargs = {
            "sep_domainid": sep_domainid,
            "sep_policy_type": sep_policy_type
        }
        params = transform_kwargs(test_kwargs)
        sep_client = Sepclient(get_config())
        response = sep_client.get_policies_summary(**params)
        assert_keys_in(response, *keys)
        assert expected_result == len(response["content"])

    """ Test sep_client.get_fingerprint_list """
    @patch("fn_sep.lib.sep_client.RequestsSep", side_effect=mocked_request)
    @pytest.mark.parametrize("sep_domainid, sep_fingerprintlist_id, sep_fingerprintlist_name, expected_result", [
        ("A9B4B7160946C25D24B6AA458EF5557F", "Blacklist", None, "582F9B6E0CC4C1DBBD772AAAF088CB3A")
    ])
    def test_get_fingerprint_list(self, mock_get, sep_domainid, sep_fingerprintlist_id, sep_fingerprintlist_name, expected_result):

        keys = ["data", "description", "groupIds", "hashType", "id", "name", "source"]

        test_kwargs = {
            "sep_domainid": sep_domainid,
            "sep_fingerprintlist_name": sep_fingerprintlist_name,
            "sep_fingerprintlist_id": sep_fingerprintlist_id
        }
        params = transform_kwargs(test_kwargs)
        sep_client = Sepclient(get_config())
        response = sep_client.get_fingerprint_list(**params)
        assert_keys_in(response, *keys)
        assert expected_result == response["data"][0]

    """ Test sep_client.delete_fingerprint_list """
    @patch("fn_sep.lib.sep_client.RequestsSep", side_effect=mocked_request)
    @pytest.mark.parametrize("sep_fingerprintlist_id, expected_results", [
        ("18113A4C9C1B449099084917D993BDE7", "")
    ])
    def test_delete_fingerprint_list(self, mock_get, sep_fingerprintlist_id, expected_results):

        test_kwargs = {
            "sep_fingerprintlist_id": sep_fingerprintlist_id,

        }
        params = transform_kwargs(test_kwargs)
        sep_client = Sepclient(get_config())
        response = sep_client.delete_fingerprint_list(**params)
        assert expected_results == response

    """ Test sep_client.add_fingerprint_list """
    @patch("fn_sep.lib.sep_client.RequestsSep", side_effect=mocked_request)
    @pytest.mark.parametrize("sep_fingerprintlist_name, sep_description, sep_domainid, sep_hash_value, expected_results", [
        ("Blacklist", "Hash of type Malware MD5 Hash", "A9B4B7160946C25D24B6AA458EF5557F", "582F9B6E0CC4C1DBBD772AAAF088CB3A",
         "B5F9985ED6C449A6905A0D570A5733FC")
    ])
    def test_add_fingerprint_list(self, mock_get, sep_fingerprintlist_name, sep_description, sep_domainid, sep_hash_value, expected_results):

        test_kwargs = {
            "sep_fingerprintlist_name": sep_fingerprintlist_name,
            "sep_description": sep_description,
            "sep_domainid": sep_domainid,
            "sep_hash_value": sep_hash_value
        }
        params = transform_kwargs(test_kwargs)
        sep_client = Sepclient(get_config())
        response = sep_client.add_fingerprint_list(**params)
        assert expected_results == response["id"]

    """ Test sep_client.update_fingerprint_list """
    @patch("fn_sep.lib.sep_client.RequestsSep", side_effect=mocked_request)
    @pytest.mark.parametrize("sep_fingerprintlist_name, sep_fingerprintlist_id, sep_description, sep_domainid, "
                             "sep_hash_value, expected_results", [
        ("Blacklist", "18113A4C9C1B449099084917D993BDE7", "Hash of type Malware MD5 Hash", "A9B4B7160946C25D24B6AA458EF5557F",
         "582F9B6E0CC4C1DBBD772AAAF088CB3A", "")
    ])
    def test_update_fingerprint_list(self, mock_get, sep_fingerprintlist_name, sep_fingerprintlist_id, sep_description,
                                     sep_domainid, sep_hash_value, expected_results):
        test_kwargs = {
            "sep_fingerprintlist_name": sep_fingerprintlist_name,
            "sep_fingerprintlist_id": sep_fingerprintlist_id,
            "sep_description": sep_description,
            "sep_domainid": sep_domainid,
            "sep_hash_value": sep_hash_value
        }
        params = transform_kwargs(test_kwargs)
        sep_client = Sepclient(get_config())
        response = sep_client.update_fingerprint_list(**params)
        assert expected_results == response

    """ Test sep_client.assign_fingerprint_list_to_group """
    @patch("fn_sep.lib.sep_client.RequestsSep", side_effect=mocked_request)
    @pytest.mark.parametrize("sep_groupid, sep_fingerprintlist_id, expected_results", [
        ("114BA13D0946C25D49CE7D3A846CBEDB", "7992BAC1C36E46FDBCD95F7E5A063AFB", "")
    ])
    def test_assign_fingerprint_list_to_group(self, mock_get, sep_groupid, sep_fingerprintlist_id, expected_results):
        test_kwargs = {
            "sep_groupid": sep_groupid,
            "sep_fingerprintlist_id": sep_fingerprintlist_id
        }
        params = transform_kwargs(test_kwargs)
        sep_client = Sepclient(get_config())
        response = sep_client.assign_fingerprint_list_to_group(**params)
        assert expected_results == response

    """ Test sep_client.upload_file """
    @patch("fn_sep.lib.sep_client.RequestsSep", side_effect=mocked_request)
    @pytest.mark.parametrize("sep_file_path, sep_computer_ids, sep_sha256, sep_sha1, sep_md5, sep_source, expected_results", [
        ("C:\temp\test_file.exe", "89AD1BBB0946C25D25E6C0984E971D8A",
         "bfe4fd780b47e8d4e5661d4c3881d114e8631e84a686e3bb8aad85d4af20454a", None, None, None, "171969C124D54C069D7018914AA02184")
    ])
    def test_upload_file(self, mock_get, sep_file_path, sep_computer_ids, sep_sha256, sep_sha1, sep_md5, sep_source, expected_results):
        test_kwargs = {
            "sep_file_path": sep_file_path,
            "sep_computer_ids": sep_computer_ids,
            "sep_sha256": sep_sha256,
            "sep_sha1": sep_sha1,
            "sep_md5": sep_md5,
            "sep_source": sep_source
        }
        params = transform_kwargs(test_kwargs)
        sep_client = Sepclient(get_config())
        response = sep_client.upload_file(**params)
        assert expected_results == response["commandID"]

    """ Test sep_client.get_command_status """
    @patch("fn_sep.lib.sep_client.RequestsSep", side_effect=mocked_request)
    @pytest.mark.parametrize("sep_incident_id, sep_commandid, sep_order, sep_pageindex, sep_pagesize, sep_sort, "
                             "sep_status_type, sep_matching_endpoint_ids, expected_results_1, expected_results_2", [
        (123, "3FEB081B2A144479A32980272C9C1E23", None, None, None, "text", "scan", False, 4, 1)
    ])
    def test_get_command_status(self, mock_get, sep_incident_id, sep_commandid, sep_order, sep_pageindex, sep_pagesize,
                                sep_sort, sep_status_type, sep_matching_endpoint_ids, expected_results_1,
                                expected_results_2):

        keys = ["content", "firstPage", "lastPage", "number", "numberOfElements", "size", "sort", "totalElements",
                  "totalPages"]

        test_kwargs = {
            "sep_incident_id": sep_incident_id,
            "sep_commandid": sep_commandid,
            "sep_order": sep_order,
            "sep_pageindex": sep_pageindex,
            "sep_pagesize": sep_pagesize,
            "sep_sort": sep_sort,
            "sep_status_type": sep_status_type,
            "sep_matching_endpoint_ids": sep_matching_endpoint_ids
        }
        params = transform_kwargs(test_kwargs)
        sep_client = Sepclient(get_config())
        response = sep_client.get_command_status(**params)
        content = response["content"]
        assert_keys_in(response, *keys)
        assert expected_results_1 == response["numberOfElements"]
        assert expected_results_1 == len(content)
        assert expected_results_2 == response["totalPages"]

    """ Test sep_client.get_file_content """
    @patch("fn_sep.lib.sep_client.RequestsSep", side_effect=mocked_request)
    @pytest.mark.parametrize("sep_file_id, expected_results", [
        ("A6954725A9FE9DC55AFCE85840A2483B", "SGkgdGhlcmU=")
    ])
    def test_get_file_content(self, mock_get, sep_file_id, expected_results):

        test_kwargs = {
            "sep_file_id": sep_file_id
        }
        params = transform_kwargs(test_kwargs)
        sep_client = Sepclient(get_config())
        response = sep_client.get_file_content(**params)
        assert expected_results == response

    """ Test sep_client.quarantine_endpoints """
    @patch("fn_sep.lib.sep_client.RequestsSep", side_effect=mocked_request)
    @pytest.mark.parametrize("sep_group_ids, sep_computer_ids, sep_undo, expected_results", [
        (None, "89AD1BBB0946C25D25E6C0984E971D8A", False, "09114E42730A479993DD6D94CF9CAA53")
    ])
    def test_quarantine_endpoints(self, mock_get, sep_group_ids, sep_computer_ids, sep_undo, expected_results):

        test_kwargs = {
            "sep_group_ids": sep_group_ids,
            "sep_computer_ids": sep_computer_ids,
            "sep_undo": sep_undo
        }
        params = transform_kwargs(test_kwargs)
        sep_client = Sepclient(get_config())
        response = sep_client.quarantine_endpoints(**params)
        assert expected_results == response["commandID_computer"]

    """ Test sep_client.scan_endpoints """
    @patch("fn_sep.lib.sep_client.RequestsSep", side_effect=mocked_request)
    @pytest.mark.parametrize("sep_group_ids, sep_computer_ids, sep_scan_type, sep_file_path, sep_sha256, sep_sha1, "
                             "sep_md5, sep_description, sep_scan_action, expected_results_1, expected_results_2", [
        (None, "236A7100A9FE9DC50A4F1AC2819C158E", 'QUICK_SCAN', "C:\\temp\\eicar.zip", None, None, None, "EOC scan",
         None, "0F0CBDD7EDFF4634B23FA11F5AB81FFC", "BB37F78894DB451B8E8921EC127667A3")
    ])
    def test_scan_endpoints(self, mock_get, sep_group_ids, sep_computer_ids, sep_scan_type, sep_file_path,
                     sep_sha256, sep_sha1, sep_md5, sep_description, sep_scan_action, expected_results_1, expected_results_2):

        test_kwargs = {
            "sep_group_ids": sep_group_ids,
            "sep_computer_ids": sep_computer_ids,
            "sep_scan_type": sep_scan_type,
            "sep_file_path": sep_file_path,
            "sep_sha256": sep_sha256,
            "sep_sha1": sep_sha1,
            "sep_md5": sep_md5,
            "sep_description": sep_description,
            "sep_scan_action": sep_scan_action
        }
        params = transform_kwargs(test_kwargs)
        sep_client = Sepclient(get_config())
        response = sep_client.scan_endpoints(**params)
        assert expected_results_1 == response["commandID_computer"]
        assert expected_results_2 == response["commandID_group"]

    """ Test sep_client.move_endpoint  """
    @patch("fn_sep.lib.sep_client.RequestsSep", side_effect=mocked_request)
    @pytest.mark.parametrize("sep_groupid, sep_hardwarekey, expected_results_1, expected_results_2", [
        ("7E4BB119A9FE9DC526EDABFB1EE261B8", "DC7D24D6465566D2941F35BC8D17801E", 200, "OK")
    ])
    def test_move_client(self, mock_get, sep_groupid, sep_hardwarekey, expected_results_1, expected_results_2):

        keys = ["responseCode","responseMessage"]

        test_kwargs = {
            "sep_groupid": sep_groupid,
            "sep_hardwarekey": sep_hardwarekey
        }
        params = transform_kwargs(test_kwargs)
        sep_client = Sepclient(get_config())
        response = sep_client.move_endpoint(**params)
        assert_keys_in(response[0], *keys)
        assert expected_results_1 == int(response[0]["responseCode"])
        assert expected_results_2 == response[0]["responseMessage"]

    """ Test sep_client.get_paginated_results  """
    @patch("fn_sep.lib.sep_client.RequestsSep", side_effect=mocked_request)
    @pytest.mark.parametrize("expected_results", [
        (2)
    ])
    def test_get_paginated_results(self, mock_get, expected_results):

        keys = ["content", "firstPage", "lastPage", "number", "numberOfElements", "size", "sort", "totalElements",
                  "totalPages"]
        test_kwargs = {
        }
        params = transform_kwargs(test_kwargs)
        sep_client = Sepclient(get_config())
        response = sep_client.get_paginated_results(sep_client.get_groups, **params)
        assert_keys_in(response, *keys)
        assert expected_results == len(response["content"])

    """ Test setup xml  """
    @patch("fn_sep.lib.sep_client.RequestsSep", side_effect=mocked_request)
    @pytest.mark.parametrize("scan_type, file_path, sha256, sha1, md5, description, scan_action, expected_results", [
        ("QUICK_SCAN", "C:\\temp\\eicar.zip", "131f95c51cc819465fa1797f6ccacf9d494aaaff46fa3eac73ae63ffbdfd8267", None,
         None, "Just a test.", None, setup_test_xml())
    ])
    def test_setup_xml(self, mock, scan_type, file_path, sha256, sha1, md5, description, scan_action, expected_results):

        sep_client = Sepclient(get_config())
        result = sep_client.setup_scan_xml(scan_type, file_path, sha256, sha1, md5, description, scan_action)
        test_results_parsed = ET.fromstring(expected_results.encode('utf8', 'ignore'))
        results_parsed = ET.fromstring(result.encode('utf8', 'ignore'))
        assert test_results_parsed.tag  ==  results_parsed.tag
        test_items_file = test_results_parsed.findall('Activity/OS/Files/File')
        result_items_file =  results_parsed.findall('Activity/OS/Files/File')
        for i in range(len(test_items_file)):
            assert test_items_file[i].attrib["name"] == result_items_file[i].attrib["name"]
        test_items_hash = test_results_parsed.findall('Activity/OS/Files/File/Hash')
        result_items_hash = results_parsed.findall('Activity/OS/Files/File/Hash')
        for i in range(len(test_items_hash)):
            assert test_items_hash[i].attrib["value"] == result_items_hash[i].attrib["value"]