# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
from fn_slack.lib.slack_common import *
import pytest
try:
    from unittest.mock import patch
except:
    from mock import patch

def_username = "Resilient"
slack_test_channel = "test-channel"


class TestSlack(object):
    """ Tests for the fn_slack function"""

    @patch('fn_slack.lib.slack_common.SlackClient.api_call')
    def test_find_channel_by_name(self, mocked_api_call):
        """ Test find Slack channel by name"""
        print("Test find Slack channel by name\n")

        mocked_api_call.side_effect = [
            {
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
                        "name": "test-channel2"
                    }],
                "response_metadata":
                    {
                    "next_cursor": "aW1f"
                    }
            },
            {
                "ok": True,
                "channels": [
                    {
                        "id": "C012AB3CR",
                        "name": "test-channel"
                    }],
                "response_metadata":
                    {
                        "next_cursor": None
                    }
            }]
        slack_utils = SlackUtils("fake_api_key")
        slack_utils.find_channel_by_name(slack_test_channel)

        assert slack_utils.get_channel_name() == slack_test_channel

    @patch('fn_slack.lib.slack_common.SlackClient.api_call')
    def test_find_channel_by_name_error(self, mocked_api_call):
        """ Test find Slack channel by name error"""
        print("Test find Slack channel by name error\n")

        mocked_api_call.return_value = {
                "ok": False
            }

        try:
            slack_utils = SlackUtils("fake_api_key")
            slack_utils.find_channel_by_name(slack_test_channel)
            assert False
        except ValueError:
            assert True

    @patch('fn_slack.lib.slack_common.SlackClient.api_call')
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
        assert slack_utils.get_channel_name() == slack_test_channel

    @patch('fn_slack.lib.slack_common.SlackClient.api_call')
    def test_slack_create_channel_error(self, mocked_api_call):
        """ Test find Slack channel by name error"""
        print("TTest create Slack channel error\n")

        mocked_api_call.return_value = {
            "ok": False,
        }

        try:
            slack_utils = SlackUtils("fake_api_key")
            slack_utils.slack_create_channel(slack_test_channel, False)
            assert False
        except ValueError:
            assert True

    @pytest.mark.parametrize("channel,expected_channel_id", [
        ({"id": "C0EAQDV4Z", "name": "test-channel"}, 'C0EAQDV4Z'),
        (None, None)
    ])
    def test_get_channel_id(self, channel, expected_channel_id):
        """ Test get channel id"""
        print("Test get channel id\n")

        slack_utils = SlackUtils("fake_api_key")
        slack_utils.set_channel(channel)

        assert slack_utils.get_channel_id() == expected_channel_id

    @pytest.mark.parametrize("channel,expected_channel_name", [
        ({"id": "C0EAQDV4Z", "name": "test-channel"}, 'test-channel'),
        (None, None)
    ])
    def test_get_channel_name(self, channel, expected_channel_name):
        """ Test get channel id"""
        print("Test get channel id\n")

        slack_utils = SlackUtils("fake_api_key")
        slack_utils.set_channel(channel)

        assert slack_utils.get_channel_name() == expected_channel_name

    @pytest.mark.parametrize("is_channel,is_private,expected", [
        (True, False, False),  # public channel
        (False, True, True)  # private channel
    ])
    def test_is_channel_private(self, is_channel, is_private, expected):
        """ Test is Slack channel private"""
        print("Test is Slack channel private - {}\n".format(expected))

        # Setup channel first
        mocked_channel = {
            "id": "C0EAQDV4Z",
            "name": "test-channel",
            "is_channel": is_channel,
            "is_private": is_private
        }
        slack_utils = SlackUtils("fake_api_key")
        slack_utils.set_channel(mocked_channel)

        assert slack_utils.is_channel_private() == expected

    @pytest.mark.parametrize("is_archived,expected", [
        (True, True),  # archived channel
        (False, False)  # non archived channel
    ])
    def test_is_channel_archived(self, is_archived, expected):
        """ Test is Slack channel archived"""
        print("Test is Slack channel archived\n")

        # Setup channel first
        mocked_channel = {
            "id": "C0EAQDV4Z",
            "name": "test-channel",
            "is_archived": is_archived
        }
        slack_utils = SlackUtils("fake_api_key")
        slack_utils.set_channel(mocked_channel)

        assert slack_utils.is_channel_archived() == expected

    @pytest.mark.parametrize("user_ids,expected", [
        ("a@a.com, b@b.com", ['W012A3CDE', 'W012A3CDE']),
        ("b@b.com", ['W012A3CDE']),
        ("b@b.com, ", ['W012A3CDE']),
        (" ", [])
    ])
    @patch('fn_slack.lib.slack_common.SlackClient.api_call')
    def test_find_user_ids(self, mocked_api_call, user_ids, expected):
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

        user_id_list = slack_utils.find_user_ids(user_ids)
        assert user_id_list == expected

    @patch('fn_slack.lib.slack_common.SlackClient.api_call')
    def test_find_user_ids_error(self, mocked_api_call):
        """ Test find Slack user id by email error"""
        print("Test find Slack user id by email error\n")

        mocked_api_call.return_value = {
            "ok": False
        }

        try:
            slack_utils = SlackUtils("fake_api_key")
            slack_utils.find_user_ids("b@b.com")
            assert False
        except ValueError:
            assert True

    @pytest.mark.parametrize("user_ids_list,expected_ids", [
        (["W1234567890", "U2345678901", "U3456789012"], "W1234567890,U2345678901,U3456789012"),
        (["W1234567890"], "W1234567890")
    ])
    @patch('fn_slack.lib.slack_common.SlackClient.api_call')
    def test_invite_users_to_channel(self, mocked_api_call, user_ids_list, expected_ids):
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
        results = slack_utils.invite_users_to_channel(user_ids_list)
        mocked_api_call.assert_called_with(
            "conversations.invite",
            channel="C0EAQDV4Z",
            users=expected_ids
        )
        assert results.get("ok") is True

    @patch('fn_slack.lib.slack_common.SlackClient.api_call')
    def test_invite_users_to_channel_error_pass(self, mocked_api_call):
        """ Test invite Slack users to a channel - already in channel error"""
        print("Test invite Slack users to a channel - already in channel error\n")

        # Setup channel first
        mocked_channel = {
            "id": "C0EAQDV4Z",
            "name": "test-channel"
        }
        slack_utils = SlackUtils("fake_api_key")
        slack_utils.set_channel(mocked_channel)

        # Test inviting users to a channel error
        mocked_api_call.return_value = {
            "ok": False,
            "error": "already_in_channel"
        }
        results = slack_utils.invite_users_to_channel(["W1234567890"])
        if not results.get("ok") and results.get("error") == "already_in_channel":
            assert True
        else:
            assert False

    @patch('fn_slack.lib.slack_common.SlackClient.api_call')
    def test_invite_users_to_channel_error(self, mocked_api_call):
        """ Test invite Slack users to a channel error"""
        print("Test invite Slack users to a channel error\n")

        # Setup channel first
        mocked_channel = {
            "id": "C0EAQDV4Z",
            "name": "test-channel"
        }
        slack_utils = SlackUtils("fake_api_key")
        slack_utils.set_channel(mocked_channel)

        # Test inviting users to a channel error
        mocked_api_call.return_value = {
            "ok": False,
            "error": "something_else"
        }
        results = slack_utils.invite_users_to_channel(["W1234567890"])
        if not results.get("ok") and results.get("error") == "already_in_channel":
            assert False
        else:
            assert True

    @pytest.mark.parametrize("input,output", [
        ("1", "True"),
        ("yes", "True"),
        ("true", "True"),
        ("TRUE", "True"),
        (1, "True"),
        (0, "False"),
        (55, "False"),
        ("no", "False"),
        ("0", "False"),
        ("false", "False"),
        ("FALSE", "False"),
        ({}, "False")
    ])
    def test_build_boolean(self, input, output):
        """ Test build boolean method"""
        print("Test build boolean method\n")

        result = build_boolean(input)
        assert result == output

    def test_build_payload(self):
        """ Test build payload method"""
        print("Test build payload method\n")

        dataDict = self._buildDataDetails()
        resoptions = {'host': 'localhost', 'port': '443'}
        payload = build_payload(dataDict, resoptions)

        assert payload is not None
        assert 'Resilient URL' in payload

    def test_build_payload_error(self):
        """ Test build payload method error"""
        print("Test build payload method error\n")

        dataDict = {"Something else": {"type": "list", "data": "[a,b,c]"}}
        try:
            build_payload(dataDict, {})
            assert False
        except IntegrationError:
            assert True

    @patch('fn_slack.lib.slack_common.SlackClient.api_call')
    def test_slack_post_message(self, mocked_api_call):
        """ Test post and reply Slack message"""
        print("Test post and reply Slack message\n")

        # Setup channel first
        mocked_channel = {
            "id": "C1H9RESGL",
            "name": "test-channel"
        }
        slack_utils = SlackUtils("fake_api_key")
        slack_utils.set_channel(mocked_channel)

        # 1 - Test sending a message with a non json payload
        mocked_api_call.return_value = {
            "ok": True,
            "channel": "C1H9RESGL",
            "ts": "1536873835.000100"
        }

        payload = "testing"
        results = slack_utils.slack_post_message(None, payload, True, None, True, "none", True, None, def_username)
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
                "thread_ts": "1536873835.000100"  # this is the one that needs to match it's parent for threading
            },
            "ts": "1537293614.000100"
        }

        results2 = slack_utils.slack_post_message(None, payload, True, None, True, "none", True, thread_id, def_username)
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

        # 3 - Test sending a reply with json payload

        # create slack_details for the post_message
        resoptions = {
            'host': 'localhost',
            'port': '443',
         }
        slack_details = json.dumps(self._buildDataDetails())
        results3 = slack_utils.slack_post_message(resoptions, slack_details, True, None, True, "none", True, None,
                                                  def_username)

        # covert slack_details to payload - to compare what was assert_called_with
        payload = convert_slack_details_to_payload(slack_details, resoptions)

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
        assert results3.get("ok") is True

    @patch('fn_slack.lib.slack_common.SlackClient.api_call')
    def test_slack_post_message_error(self, mocked_api_call):
        """ Test post and reply Slack message error"""
        print("Test post and reply Slack message error\n")

        # Setup channel first
        mocked_channel = {
            "id": "C1H9RESGL",
            "name": "test-channel"
        }
        slack_utils = SlackUtils("fake_api_key")
        slack_utils.set_channel(mocked_channel)

        # Test inviting users to a channel error
        mocked_api_call.return_value = {
            "ok": False
        }
        results = slack_utils.slack_post_message(None, "testing", True, None, True, "none", True, None,
                                                 def_username)
        assert results.get("ok") is False

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

    @patch('fn_slack.lib.slack_common.SlackClient.api_call')
    def test_get_permalink(self, mocked_api_call):
        """ Test get a permalink"""
        print("Test get a permalink\n")

        # Setup channel first
        mocked_channel = {
            "id": "C0EAQDV4Z",
            "name": "test-channel"
        }
        slack_utils = SlackUtils("fake_api_key")
        slack_utils.set_channel(mocked_channel)

        mocked_api_call.return_value = {
            "ok": True,
            "channel": "C0EAQDV4Z",
            "permalink": "https://ghostbusters.slack.com/archives/C0EAQDV4Z/p135854651500008"
        }
        permalink = slack_utils.get_permalink("fake_thread_id")
        assert permalink == "https://ghostbusters.slack.com/archives/C0EAQDV4Z/p135854651500008"

    @patch('fn_slack.lib.slack_common.SlackClient.api_call')
    def test_get_permalink_error(self, mocked_api_call):
        """ Test get a permalink error"""
        print("Test get a permalink error\n")

        # Setup channel first
        mocked_channel = {
            "id": "C0EAQDV4Z",
            "name": "test-channel"
        }
        slack_utils = SlackUtils("fake_api_key")
        slack_utils.set_channel(mocked_channel)

        mocked_api_call.return_value = {
            "ok": False
        }
        try:
            slack_utils.get_permalink("fake_thread_id")
            assert False
        except ValueError:
            assert True

    @patch('fn_slack.lib.slack_common.SlackClient.api_call')
    def test_archive_channel(self, mocked_api_call):
        """ Test archive channel"""
        print("TTest archive channel\n")

        # Setup channel first
        mocked_channel = {
            "id": "C0EAQDV4Z",
            "name": "test-channel"
        }
        slack_utils = SlackUtils("fake_api_key")
        slack_utils.set_channel(mocked_channel)

        mocked_api_call.return_value = {
            "ok": True
        }
        results = slack_utils.archive_channel()

        assert results.get("ok") is True

    # @patch('fn_slack.lib.slack_common.SlackClient.api_call')
    # def test_archive_channel_error(self, mocked_api_call):
    #     """ Test archive channel error"""
    #     print("TTest archive channel error\n")
    #
    #     # Setup channel first
    #     mocked_channel = {
    #         "id": "C0EAQDV4Z",
    #         "name": "test-channel"
    #     }
    #     slack_utils = SlackUtils("fake_api_key")
    #     slack_utils.set_channel(mocked_channel)
    #
    #     mocked_api_call.return_value = {
    #         "ok": False
    #     }
    #     results = slack_utils.archive_channel()
    #
    #     assert results.get("ok") is False

    @patch('fn_slack.lib.slack_common.SlackClient.api_call')
    def test_get_user_info(self, mocked_api_call):
        """ Test get user info"""
        print("Test get user info\n")

        mocked_api_call.return_value = {
            "ok": True,
            "user": {
                    "id": "W012A3CDE",
                    "name": "spengler"
                }
        }
        slack_utils = SlackUtils("fake_api_key")
        user = slack_utils.get_user_info("W012A3CDE")
        mocked_api_call.assert_called_with(  # checks the last call to a method, check for b@b.com email
            "users.info",
            user="W012A3CDE"
        )
        assert user.get("id") == 'W012A3CDE'

    @patch('fn_slack.lib.slack_common.SlackClient.api_call')
    def test_get_user_info_error(self, mocked_api_call):
        """ Test get user info error"""
        print("Test get user info error\n")

        mocked_api_call.return_value = {
            "ok": False
        }
        try:
            slack_utils = SlackUtils("fake_api_key")
            slack_utils.get_user_info("W012A3CDE")
            assert False
        except ValueError:
            assert True

    @pytest.mark.parametrize("results,expected_has_more,expected_cursor", [
        ({"ok": True, "response_metadata": {"next_cursor": "bmV4d"}}, True, "bmV4d"),
        ({"ok": True, "response_metadata": {"next_cursor": None}}, False, None),
        ({"ok": True}, False, None)
    ])
    def test_get_next_cursor_for_next_page(self, results, expected_has_more, expected_cursor):
        """ Test get next cursor for next page"""
        print("Test get next cursor for next page\n")

        slack_utils = SlackUtils("fake_api_key")
        has_more_results, cursor = slack_utils._get_next_cursor_for_next_page(results)
        assert has_more_results == expected_has_more
        assert cursor == expected_cursor

    def test_get_next_cursor_for_next_page_error(self):
        """ Test get next cursor for next page error"""
        print("Test get next cursor for next page error\n")

        results = {
            "ok": False
        }
        try:
            slack_utils = SlackUtils("fake_api_key")
            slack_utils._get_next_cursor_for_next_page(results)
            assert False
        except ValueError:
            assert True

    @patch('fn_slack.lib.slack_common.SlackClient.api_call')
    def test_get_channel_parent_message_history(self, mocked_api_call):
        """ Test get channel parent msg history"""
        print("Test get channel parent msg history\n")

        mocked_api_call.side_effect = [
            {
                "ok": True,
                "messages": [
                    {
                        "ts": "1"
                    },
                    {
                        "ts": "2"
                    }],
                "response_metadata": {
                    "next_cursor": "bmV4d"
                }
            },
            {
                "ok": True,
                "messages": [
                    {
                        "ts": "3"
                    },
                    {
                        "ts": "4"
                    }],
                "response_metadata": {
                    "next_cursor": None
                }
            }]
        slack_utils = SlackUtils("fake_api_key")
        message_ts_list = slack_utils._get_channel_parent_message_history()
        assert message_ts_list == ["1", "2", "3", "4"]

    @patch('fn_slack.lib.slack_common.SlackUtils._get_channel_parent_message_history')
    @patch('fn_slack.lib.slack_common.SlackClient.api_call')
    def test_get_channel_complete_history(self, mocked_api_call, mocked_msg_history_list):
        """ Test get complete history"""
        print("Test get complete history\n")

        mocked_api_call.side_effect = [
            {
                "ok": True,
                "messages": [
                    {
                        "text": "one"
                    },
                    {
                        "text": "two"
                    }],
                "response_metadata": {
                    "next_cursor": "bmV4d"
                }
            },
            {
                "ok": True,
                "messages": [
                    {
                        "text": "three"
                    }],
                "response_metadata": {
                    "next_cursor": None
                }
            }]

        mocked_msg_history_list.return_value = ["ts1"]

        slack_utils = SlackUtils("fake_api_key")
        history = slack_utils.get_channel_complete_history()
        assert history == [{'text': 'one'}, {'text': 'two'}, {'text': 'three'}]
