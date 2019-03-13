# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Test Bigfix client  class"""
from __future__ import print_function
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
import pytest
from fn_bigfix.lib.bigfix_client import *
from  mock_artifacts import mocked_requests, get_asset_properties

"""
Suite of tests to test BigFix client class
"""

def get_config():
    return dict({
        "bigfix_url": "https://bigfix-url.com",
        "bigfix_port": "12345",
        "bigfix_user": "BigFixAdmin",
        "bigfix_pass": "MyPassword",
        "bigfix_polling_interval": 30,
        "bigfix_polling_timeout":  600,
        "hunt_results_limit": 200
    })

class TestGetBfComputerProperties:
    """ Test bigfix_client.get_bf_computer_properties using mocked data.  """

    @patch('requests.get', side_effect=mocked_requests)
    @pytest.mark.parametrize("computer_id, expected_results", [
        (13550086, "Computer ID 13550086 Properties"),
        (12315195, "Computer ID 12315195 Properties")
    ])
    def test_get_bf_computer_properties(self, mock_get, computer_id, expected_results):

        bigfix_client = BigFixClient(get_config())
        response = bigfix_client.get_bf_computer_properties(computer_id)
        assert expected_results in response

class TestGetBfClientQuery:
    """ Test bigfix_client.get_bfclientquery using mocked data.  """

    @patch('requests.get', side_effect=mocked_requests)
    @pytest.mark.parametrize("query_id, expected_results", [
        (123, 2),
        (124, 4),
    ])
    def test_get_bfclientquery(self, mock_get, query_id, expected_results):
        """ Test create_attachment using mocked data.  """

        bigfix_client = BigFixClient(get_config())
        response = bigfix_client.get_bfclientquery(query_id)
        assert(expected_results == len(response))

class TestPostBfClientQuery:
    """ Test bigfix_client.post_bfclientquery using mocked data.  """

    @patch('requests.post', side_effect=mocked_requests)
    @pytest.mark.parametrize("query_id, expected_results", [
        ('exists file "/tmp/testfile.txt"', 142),
        ('exists process whose(name of it as lowercase = "besclient)', 144)
    ])
    def test_post_bfclientquery(self, mock_get, query_id, expected_results):
        """ Test create_attachment using mocked data.  """

        bigfix_client = BigFixClient(get_config())

        response = bigfix_client.post_bfclientquery(query_id)

class TestPostBfActionQuery:
    """ Test bigfix_client._post_bf_action_query using mocked data.  """

    @patch('requests.post', side_effect=mocked_requests)
    @pytest.mark.parametrize("query, computer_id, action_name, expected_results", [
        ('delete "/tmp/testfile.txt"', 13550086, "Delete File /tmp/testfile.txt", "142"),
            ('waithidden cmd.exe /c reg delete "HKLM\SOFTWARE\JP\JP2\com.jp.browsercore" /f', 12315195,
             "Delete Registry Key HKLM\SOFTWARE\JP\JP2\com.jp.browsercore", "143")
    ])
    def test_post_bf_action_query(self, mock_get, query, computer_id, action_name, expected_results):
        """ Test create_attachment using mocked data.  """

        bigfix_client = BigFixClient(get_config())

        status = bigfix_client._post_bf_action_query(query, computer_id, action_name)
        assert status == expected_results

    class TestProcessBfComputerQueryResponseToAttachment:
        """ Test bigfix_client._process_bf_computer_query_response_to_attachment using mocked data.  """

        @pytest.mark.parametrize(
            "response_text, title, expected_results",
            [
                (mocked_requests("/response_text", 13550086), "Computer ID 13550086 Properties", "Computer ID 13550086 Properties"),
                (mocked_requests("/response_text", 12315195), "Computer ID 12315195 Properties", "Computer ID 12315195 Properties"),
            ])
        def test_process_bf_computer_query_response_to_attachment(self, response_text, title, expected_results):
            """ Test create_attachment using mocked data.  """

            bigfix_client = BigFixClient(get_config())

            response = bigfix_client._process_bf_computer_query_response_to_attachment(response_text, title)

class TestGetBfActionStatus:
    """ Test bigfix_client.get_bf_action_status using mocked data.  """

    @patch('requests.get', side_effect=mocked_requests)
    @pytest.mark.parametrize(
        "action_id, expected_results",
        [
            (143, "The action executed successfully."),
            (144, "The Fixlet which this action addresses is not relevant on this machine."),
            (145, "The action failed.")
        ])

    def test_get_bf_action_status(self, mock_get, action_id, expected_results):
        """ Test create_attachment using mocked data.  """

        bigfix_client = BigFixClient(get_config())

        status = bigfix_client.get_bf_action_status(action_id)
        assert status == expected_results