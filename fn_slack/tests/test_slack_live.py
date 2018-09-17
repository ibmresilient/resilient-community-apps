# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
from fn_slack.components.slack_common import *
import pytest
import simplejson as json
try:
    from unittest.mock import patch
except:
    from mock import patch

def_username = "Resilient"
slack_test_channel = "test-channel"


class TestSlack:
    """ Tests for the fn_slack function"""

    # pipenv run python -m unittest discover tests
    # url = None

    # def setUp(self):
    #     self.resoptions = {
    #         'host': 'localhost',
    #         'port': '443',
    #     }
    #

    #TODO - add ok = "False" api call results! - errors patch - side_effect

    @patch('fn_slack.components.slack_common.SlackClient.api_call')
    def test_find_channel_by_name(self, mocked_api_call):
        mocked_api_call.return_value = {
            "ok": True,
            "channels": [
                {
                    "id": "C012AB3CD",
                    "name": "general"
                },
                {
                    "id": "C061EG9T2",
                    "name": "random"
                },
                {
                    "id": "C0EAQDV4Z",
                    "name": "test-channel"
                }]
        }
        slack_utils = SlackUtils("fake_api_key")
        slack_utils.find_channel_by_name(slack_test_channel)
        assert (slack_utils.get_channel().get("name") == slack_test_channel)

    @patch('fn_slack.components.slack_common.SlackClient.api_call')
    def test_slack_create_channel(self, mocked_api_call):
        mocked_api_call.return_value = {
            "ok": True,
            "channel":
                {
                    "id": "C0EAQDV4Z",
                    "name": "test-channel"
                }
        }
        slack_utils = SlackUtils("fake_api_key")
        slack_utils.slack_create_channel(slack_test_channel, False)
        assert (slack_utils.get_channel().get("name") == slack_test_channel)

    @patch('fn_slack.components.slack_common.SlackClient.api_call')
    @pytest.mark.parametrize("test_input,expected", [
        ("test-channel-public", False),
        ("test-channel-private", True)
    ])
    def test_is_channel_private(self, mocked_api_call, test_input, expected):
        mocked_api_call.return_value = {
            "ok": True,
            "channels": [
                {
                    "id": "C0EAQDV4Z",
                    "name": "test-channel-public",
                    "is_channel": True,
                    "is_private": False

                },
                {
                    "id": "C0EAQDV4X",
                    "name": "test-channel-private",
                    "is_channel": False,
                    "is_private": True

                }
            ]
        }
        slack_utils = SlackUtils("fake_api_key")
        slack_utils.find_channel_by_name(test_input)
        assert (slack_utils.is_channel_private() == expected)

    # def test_lookup_user_by_email(self):
    #     id_user = self.slack_utils._lookup_user_by_email(slack_test_single_user_email)
    #     self.assertEqual(id_user, slack_test_single_user_id)
    #
    # def test_find_user_ids(self):
    #     user_id_list = self.slack_utils.find_user_ids(slack_test_user_emails)
    #     self.assertEqual(user_id_list, slack_test_user_ids) #FIXME UCNC5K34J != [u'UCNC5K34J'] list!
    #
    # def test_invite_users_to_channel(self):
    #     results = self.slack_utils.invite_users_to_channel(slack_test_user_ids)
    #     self.assertEqual(results.get("ok"), True)
    #
    #     # invite the same users again
    #     results = self.slack_utils.invite_users_to_channel(slack_test_user_ids)
    #     self.assertTrue(results.get("ok") and results.get("error") == "already_in_channel")

    def test_build_boolean(self):
        result = build_boolean("1")
        assert result == 'True'

        result = build_boolean("yes")
        assert result == 'True'

        result = build_boolean("true")
        assert result == 'True'

        result = build_boolean("TRUE")
        assert result == 'True'

        result = build_boolean(1)
        assert result == 'True'

        result = build_boolean(0)
        assert result == 'False'

        result = build_boolean(55)
        assert result == 'False'

        result = build_boolean("no")
        assert result == 'False'

        result = build_boolean("0")
        assert result == 'False'

        result = build_boolean("false")
        assert result == 'False'

        result = build_boolean("FALSE")
        assert result == 'False'
  #
  #   def test_build_payload(self):
  #       dataDict = self._buildDataDetails()
  #       payload = build_payload(dataDict, self.resoptions)
  #
  #       self.assertIsNotNone(payload)
  #       self.assertRegexpMatches(payload, 'Resilient URL')
  #
  #   def test_slack_post_message(self):
  #       """
  #       channel=slack_channel,
  #       text=payload,
  #       as_user=slack_as_user,
  #       username=slack_user_id if slack_user_id else def_username,
  #       reply_broadcast=slack_reply_broadcast,
  #       parse=slack_parse,
  #       mrkdown=slack_markdown,
  #       thread_ts=slack_thread_id
  #       def slack_post_message(self, resoptions, slack_details, slack_as_user, slack_username, slack_reply_broadcast,
  #                          slack_parse, slack_markdown, slack_thread_id, def_username):
  #       """
  #       dataDict = self._buildDataDetails()
  #       results = self.slack_utils.slack_post_message(self.resoptions, json.dumps(dataDict), True, None, True,
  #                                                     "none", True, None, def_username)
  #       self.assertTrue(results['ok'], True)
  #
  #       # send the reply
  #       thread_id = results['ts']
  #       results = self.slack_utils.slack_post_message(self.resoptions, json.dumps(dataDict), True, None, True,
  #                                                     "none", True, thread_id, def_username)
  #       self.assertTrue(results['ok'], True)
  #       self.assertEqual(thread_id, results['message']['thread_ts'])
  #
  #   def _buildDataDetails(self):
  #       return {
  # "Resilient Incident": {"type": "string", "data": "title here" },
  # "Resilient URL": {"type": "incident", "data": "1234" },
  # "Description": {"type": "richtext", "data": "<div>data<div>" },
  # "Confirmed": {"type": "boolean", "data": "true" },
  # "Create Date": {"type": "datetime", "data": 1525356259000 },
  # "Start Date": {"type": "datetime", "data": 1525356259000 },
  # "Severity": {"type": "string", "data": "low" },
  # "NIST Vectors": {"type": "string", "data": "[Email, Malware]" },
  # "Incident Types": {"type": "string", "data": "[Phishing]" }
  #       }
  #
  #   def test_get_permalink(self):
  #       results = self.slack_utils.get_permalink()
  #       self.assertTrue(results['ok'], True)
