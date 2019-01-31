# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest

from fn_icdx.util.helper import ICDXHelper

class TestIcdxUtilitiesHelper:
    """ Tests for the helper class"""

    @pytest.mark.parametrize("input_dict", [
        (({},{},{})),
        (({'Malware SHA-256 Hash': u'E1B8TEST', 'File Path': u'c:\\workarea\\TEST', 'File Name': u'TEST'}, {}, {'Malware MD5 Hash': u'C1B07TEST'})),
        (({'Malware SHA-256 Hash': u'E1B8TEST', 'File Path': u'c:\\workarea\\TEST', 'File Name': u'TEST'}, None))
    ])
    def test_dictionary_merge(self, input_dict):
        """ Test that the dictionary merge function works as expected.
        The function should return a dictionary
        If 1 or all inputs or None or empty it should not affect the return type"""
        helper = ICDXHelper({})
        result = helper.merge_dicts(input_dict)

        assert(isinstance(result, dict))

    @pytest.mark.parametrize("input_dict", [
        (({}, {}, {})),
        (({},None, {})),
        (({}, None))
    ])
    def test_dictionary_merge_failure(self, input_dict):
        """ Test that the dictionary merge function handles empty inputs.
        The function should return a dictionary
        If 1 or all inputs or None or empty it should not affect the return type
        But if all inputs are None or empty the return should be False-y i.e empty dict"""
        helper = ICDXHelper({})
        result = helper.merge_dicts(input_dict)

        assert (isinstance(result, dict))
        assert(bool(result) == False)

    @pytest.mark.parametrize("search_result", [
        ({"name": "Test","file":{'sha2': u'E1B8TEST', 'path': u'c:\\workarea\\TEST', 'name': u'TEST', 'md5': u'C1B07TEST'}}),
        ({"name": "Test","file":{'sha2': u'E1B8TEST', 'path': u'c:\\workarea\\TEST'}}),
    ])
    def test_file_artifact_parse_success(self, search_result):
        """ Test that the file artifact function works as expected
        The function should return a dictionary
        With a known good input the return should be Truth-y (has elements)
        """
        helper = ICDXHelper({})
        result = helper.parse_for_file_artifacts(search_result)

        assert (isinstance(result, dict))
        assert (bool(result))

    @pytest.mark.parametrize("search_result", [
        ({"name": "Test"}),
        ({"name": "Test", "file": {}}),
    ])
    def test_file_artifact_parse_failure(self, search_result):
        helper = ICDXHelper({})
        result = helper.parse_for_file_artifacts(search_result)

        assert (not result)
        assert (bool(result) is False)

    @pytest.mark.parametrize("search_result", [
        ({"name": "Test",
          "connection": {'dst_ip':'192.168.1.1', 'dst_mac':'mac', 'dst_name':'test_conn', 'dst_port':80}}),
        ({"name": "Test", "connection": {'src_ip':'10.1.1.1', 'src_mac':'mac2', 'src_name':'test_conn2', 'src_port':8080}}),
    ])
    def test_network_artifact_parse_success(self, search_result):
        """ Test that the file artifact function works as expected
        The function should return a dictionary
        With a known good input the return should be Truth-y (has elements)
        """
        helper = ICDXHelper({})
        result = helper.parse_for_network_artifacts(search_result)

        assert (isinstance(result, dict))
        assert (bool(result))

    @pytest.mark.parametrize("search_result", [
        ({"name": "Test"}),
        ({"name": "Test", "connection": {}}),
    ])
    def test_network_artifact_parse_failure(self, search_result):
        helper = ICDXHelper({})
        result = helper.parse_for_network_artifacts(search_result)

        assert (not result)
        assert (bool(result) is False)

    @pytest.mark.parametrize("search_result", [
        ({"name": "Test",
          "email": {'header_subject': u'Important updates', 'header_from': u'testuser2', 'header_to': u'testuser2'}}),
        ({"name": "Test", "email": {'header_subject': u'New version of software', 'header_from': u'testuser'}}),
    ])
    def test_email_artifact_parse_success(self, search_result):
        """ Test that the file artifact function works as expected
        The function should return a dictionary
        With a known good input the return should be Truth-y (has elements)
        """
        helper = ICDXHelper({})
        result = helper.parse_for_email_artifacts(search_result)

        assert (isinstance(result, dict))
        assert (bool(result))

    @pytest.mark.parametrize("search_result", [
        ({"name": "Test"}),
        ({"name": "Test", "email": {}}),
    ])
    def test_email_artifact_parse_failure(self, search_result):
        helper = ICDXHelper({})
        result = helper.parse_for_email_artifacts(search_result)

        assert (not result)
        assert (bool(result) is False)

    @pytest.mark.parametrize("search_result", [
        ({"name": "Test with email object ",
          "connection": {'dst_ip': '10.1.1.1', 'dst_mac': 'mac', 'dst_name': 'test_conn', 'dst_port': 80}, 'email' :{'sender_ip':'127.0.0.1'}}),
        ({"name": "Test with email object 2",
          "connection": {'src_ip': '10.1.1.1', 'src_mac': 'mac2', 'src_name': 'test_conn2', 'src_port': 8080},'email' :{'sender_ip':'127.0.0.1'}}),
    ])
    def test_multi_artifact_parse_success(self, search_result):
        """ Test that the file artifact function works as expected
        The function should return a dictionary
        With a known good input the return should be Truth-y (has elements)
        """
        helper = ICDXHelper({})
        result = helper.search_for_artifact_data(search_result)
        assert (isinstance(result, dict))
        assert (result is not None)
        assert '10.1.1.1' in result['IP Address']
        if 'email object' in search_result['name']:
            assert '127.0.0.1' in result['IP Address']




