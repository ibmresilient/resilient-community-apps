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

    # TODO - add ok = "False" api call results! - errors patch - side_effect

    @patch('fn_slack.components.slack_common.SlackClient.api_call')
    def test_find_channel_by_name(self, mocked_api_call):
        """ Test find Slack channel by name"""
        print("Test find Slack channel by name\n")

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
        mocked_api_call.assert_called_with(
            "conversations.list",
            exclude_archived=True,
            types="public_channel,private_channel"
        )
        assert (slack_utils.get_channel().get("name") == slack_test_channel)

    @patch('fn_slack.components.slack_common.SlackClient.api_call')
    def test_find_channel_by_name_error(self, mocked_api_call):
        """ Test find Slack channel by name error"""
        print("Test find Slack channel by name error\n")

        mocked_api_call.return_value = {
                "ok": False,
            }

        try:
            slack_utils = SlackUtils("fake_api_key")
            slack_utils.find_channel_by_name(slack_test_channel)
            assert False
        except ValueError:
            assert True

    @patch('fn_slack.components.slack_common.SlackClient.api_call')
    def test_slack_create_channel(self, mocked_api_call):
        """ Test create Slack channel"""
        print("Test create Slack channel\n")

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
        mocked_api_call.assert_called_with(
            "conversations.create",
            name=slack_test_channel,
            is_private=False
        )
        assert (slack_utils.get_channel().get("name") == slack_test_channel)

    @patch('fn_slack.components.slack_common.SlackClient.api_call')
    @pytest.mark.parametrize("test_input,expected", [
        ("test-channel-public", False),
        ("test-channel-private", True)
    ])
    def test_is_channel_private(self, mocked_api_call, test_input, expected):
        """ Test is Slack channel private"""
        print("Test is Slack channel private - {}\n".format(expected))

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
        mocked_api_call.assert_called_with(
            "conversations.list",
            exclude_archived=True,
            types="public_channel,private_channel"
        )
        assert (slack_utils.is_channel_private() == expected)

    @patch('fn_slack.components.slack_common.SlackClient.api_call')
    def test_find_user_ids(self, mocked_api_call):
        """ Test find Slack user id by email"""
        print("Test find Slack user id by email\n")

        mocked_api_call.return_value = {
            "ok": True,
            "user": {
                    "id": "W012A3CDE",
                    "team_id": "T012AB3C4",
                    "name": "spengler"
                }
        }
        slack_utils = SlackUtils("fake_api_key")
        user_id_list = slack_utils.find_user_ids("a@a.com, b@b.com") #FIXME test multiple times to test split and strip
        mocked_api_call.assert_called_with( # checks the last call to a method, check for b@b.com email
            "users.lookupByEmail",
            email="b@b.com"
        )
        assert user_id_list == ['W012A3CDE', 'W012A3CDE']

    @patch('fn_slack.components.slack_common.SlackClient.api_call')
    def test_invite_users_to_channel(self, mocked_api_call):
        """ Test invite Slack users to a channel"""
        print("Test invite Slack users to a channel\n")

        # Setup channel first
        mocked_channel = {
            "id": "C0EAQDV4Z",
            "name": "test-channel"
        }
        slack_utils = SlackUtils("fake_api_key")
        slack_utils.set_channel(mocked_channel)

        # Test inviting users to a channel
        mocked_api_call.return_value = {
            "ok": True,
            "channel":
                {
                    "id": "C0EAQDV4Z",
                    "name": "test-channel"
                }
        }
        results = slack_utils.invite_users_to_channel(["W1234567890", "U2345678901", "U3456789012"])
        mocked_api_call.assert_called_with(
            "conversations.invite",
            channel="C0EAQDV4Z",
            users="W1234567890,U2345678901,U3456789012"
        )
        assert results.get("ok") is True

        # invite the same users again
        #self.assertTrue(results.get("ok") and results.get("error") == "already_in_channel")

    def test_build_boolean(self):
        """ Test build boolean method"""
        print("Test build boolean method\n")

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

    def test_build_payload(self):
        """ Test build payload method"""
        print("Test build payload method\n")

        dataDict = self._buildDataDetails()
        resoptions = {
                    'host': 'localhost',
                    'port': '443',
                }
        payload = build_payload(dataDict, resoptions)

        assert payload is not None
        assert 'Resilient URL' in payload

    @patch('fn_slack.components.slack_common.SlackUtils.slack_create_channel')
    @patch('fn_slack.components.slack_common.SlackClient.api_call')
    def test_slack_post_message(self, mocked_api_call, mocked_create_channel):
        """ Test post and reply Slack message"""
        print("Test post and reply Slack message\n")

        # Setup channel first
        mocked_create_channel.return_value = {
                    "id": "C1H9RESGL",
                    "name": "test-channel"
                    }
        slack_utils = SlackUtils("fake_api_key")
        channel = slack_utils.slack_create_channel(slack_test_channel, False)
        slack_utils.set_channel(channel)

        # 1 - Test sending a message
        mocked_api_call.return_value = {
            "ok": True,
            "channel": "C1H9RESGL",
            "message": {
                "text": "Here's a message for you",
                "ts": "1536873835.000100"
            },
            "ts": "1536873835.000100"
        }

        # create slack_details for the post_message
        resoptions = {
            'host': 'localhost',
            'port': '443',
        }
        dataDict = self._buildDataDetails()
        slack_details = json.dumps(dataDict)

        results = slack_utils.slack_post_message(resoptions, slack_details, True, None, True, "none", True, None,
                                                 def_username)

        # covert slack_details to string - create payload to compare with for assert_called_with
        data = json.loads(slack_details.replace("\\n", ""), strict=False)  # cleanup for json.loads
        payload = build_payload(data, resoptions)

        mocked_api_call.assert_called_with(
            "chat.postMessage",
            channel="C1H9RESGL",
            text=payload,
            as_user=True,
            username=def_username,
            reply_broadcast=True,
            parse="none",
            link_names=1,
            mrkdown=True,
            thread_ts=None
        )
        assert results.get("ok") is True

        # 2 - Test sending a reply with thread_id
        thread_id = results.get("ts")

        mocked_api_call.return_value = {
            "ok": True,
            "channel": "C1H9RESGL",
            "message": {
                "text": "Here's a message for you",
                "ts": "1537293614.000100",
                "thread_ts": "1536873835.000100" # this is the one that needs to match it's parent for threading
            },
            "ts": "1537293614.000100"
        }

        results2 = slack_utils.slack_post_message(resoptions, slack_details, True, None, True, "none", True, thread_id,
                                                  def_username)
        mocked_api_call.assert_called_with(
            "chat.postMessage",
            channel="C1H9RESGL",
            text=payload,
            as_user=True,
            username=def_username,
            reply_broadcast=True,
            parse="none",
            link_names=1,
            mrkdown=True,
            thread_ts=thread_id
        )
        assert results2.get("ok") is True
        assert results2.get("message").get("thread_ts") == thread_id

    def _buildDataDetails(self):
        """ Mock Data Details """
        return {
  "Resilient Incident": {"type": "string", "data": "title here" },
  "Resilient URL": {"type": "incident", "data": "1234" },
  "Description": {"type": "richtext", "data": "<div>data<div>" },
  "Confirmed": {"type": "boolean", "data": "true" },
  "Create Date": {"type": "datetime", "data": 1525356259000 },
  "Start Date": {"type": "datetime", "data": 1525356259000 },
  "Severity": {"type": "string", "data": "low" },
  "NIST Vectors": {"type": "string", "data": "[Email, Malware]" },
  "Incident Types": {"type": "string", "data": "[Phishing]" }
        }

    @patch('fn_slack.components.slack_common.SlackUtils.slack_create_channel')
    @patch('fn_slack.components.slack_common.SlackClient.api_call')
    def test_get_permalink(self, mocked_api_call, mocked_create_channel):
        """ Test get a permalink"""
        print("Test get a permalink\n")

        mocked_create_channel.return_value = {
                    "id": "C0EAQDV4Z",
                    "name": "test-channel"
                }
        slack_utils = SlackUtils("fake_api_key")
        channel = slack_utils.slack_create_channel(slack_test_channel, False)
        slack_utils.set_channel(channel)

        mocked_api_call.return_value = {
            "ok": True,
            "channel": "C0EAQDV4Z",
            "permalink": "https://ghostbusters.slack.com/archives/C0EAQDV4Z/p135854651500008"
        }
        permalink = slack_utils.get_permalink("fake_thread_id")
        assert permalink == "https://ghostbusters.slack.com/archives/C0EAQDV4Z/p135854651500008"
