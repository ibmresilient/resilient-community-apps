# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
from fn_slack.lib.slack_common import *
import pytest
try:
    from unittest.mock import patch, Mock
except:
    from mock import patch, Mock

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
        except IntegrationError:
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
        except IntegrationError:
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

    @pytest.mark.parametrize("user_email_list,expected_list_ids", [
        ("a@a.com, b@b.com, ", ["W012A3CDE", "W012A3CDE"]),
        ("", [])
    ])
    @patch('fn_slack.lib.slack_common.SlackClient.api_call')
    def test_find_user_ids_based_on_email(self, mocked_api_call, user_email_list, expected_list_ids):
        """ Test find user ids on email"""
        print("Test find user ids on email\n")

        mocked_api_call.return_value = {
            "ok": True,
            "user": {
                "id": "W012A3CDE"
            }
        }
        slack_utils = SlackUtils("fake_api_key")

        results = slack_utils.find_user_ids_based_on_email(user_email_list)
        assert results == expected_list_ids

    @patch('fn_slack.lib.slack_common.SlackClient.api_call')
    def test_find_user_ids_based_on_email_error_pass(self, mocked_api_call):
        """ Test find Slack user id by email error pass"""
        print("Test find Slack user id by email error pass\n")

        mocked_api_call.return_value = {
            "ok": False,
            "error": "users_not_found"
        }

        slack_utils = SlackUtils("fake_api_key")
        try:
            slack_utils.find_user_ids_based_on_email("b@b.com")
            assert True
        except IntegrationError:
            assert False

    @patch('fn_slack.lib.slack_common.SlackClient.api_call')
    def test_find_user_ids_based_on_email_error(self, mocked_api_call):
        """ Test find Slack user id by email error"""
        print("Test find Slack user id by email error\n")

        mocked_api_call.return_value = {
            "ok": False,
            "error": "something_else"
        }

        slack_utils = SlackUtils("fake_api_key")
        try:
            slack_utils.find_user_ids_based_on_email("b@b.com")
            assert False
        except IntegrationError:
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
        try:
            slack_utils.invite_users_to_channel(user_ids_list)
            mocked_api_call.assert_called_with(
                "conversations.invite",
                channel="C0EAQDV4Z",
                users=expected_ids
            )
            assert True
        except IntegrationError:
            assert False

    @patch('fn_slack.lib.slack_common.SlackClient.api_call')
    def test_invite_users_to_channel_error_pass(self, mocked_api_call):
        """ Test invite Slack users to a channel - already in channel error pass"""
        print("Test invite Slack users to a channel - already in channel error pass\n")

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
        try:
            slack_utils.invite_users_to_channel(["W1234567890"])
            assert True
        except IntegrationError:
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
        try:
            slack_utils.invite_users_to_channel(["W1234567890"])
            assert False
        except IntegrationError:
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

    def test_build_payload_error(self):
        """ Test build payload method error"""
        print("Test build payload method error\n")

        dataDict = {"Something else": {"type": "list", "data": "[a,b,c]"}}
        try:
            build_payload(dataDict)
            assert False
        except IntegrationError:
            assert True

    @patch('fn_slack.lib.slack_common.SlackClient.api_call')
    def test_slack_post_message_no_attachment(self, mocked_api_call):
        """ Test post and reply Slack message without attachment
        # 1 - Test sending a message with a non json payload"""
        print("Test post and reply Slack message without attachment\n")

        # Setup channel first
        mocked_channel = {
            "id": "C1H9RESGL",
            "name": "test-channel"
        }
        slack_utils = SlackUtils("fake_api_key")
        slack_utils.set_channel(mocked_channel)

        mocked_api_call.return_value = {
            "ok": True,
            "channel": "C1H9RESGL"
        }

        payload = "testing"
        results = slack_utils.slack_post_message(None, payload, True, None, True, def_username)
        mocked_api_call.assert_called_with(
            "chat.postMessage",
            channel="C1H9RESGL",
            as_user=True,
            username=def_username,
            parse="none",
            link_names=1,
            mrkdown=True,
            text=payload,
            attachments=None
        )
        assert results.get("ok") is True

    @patch('fn_slack.lib.slack_common.SlackClient.api_call')
    def test_slack_post_message_attachment(self, mocked_api_call):
        """ Test post and reply Slack message with attachment
        2 - Test sending a reply with json payload"""
        print("Test post and reply Slack message with attachment\n")

        # Setup channel first
        mocked_channel = {
            "id": "C1H9RESGL",
            "name": "test-channel"
        }
        slack_utils = SlackUtils("fake_api_key")
        slack_utils.set_channel(mocked_channel)

        mocked_api_call.return_value = {
            "ok": True,
            "channel": "C1H9RESGL"
        }

        # create slack_details for the post_message
        resoptions = {
            'host': 'localhost',
            'port': '443',
         }
        slack_details = json.dumps(self._buildDataDetails())
        results = slack_utils.slack_post_message(resoptions, slack_details, True, None, True, def_username)

        # covert slack_details to payload - to compare what was assert_called_with
        attachment_json = convert_slack_details_to_payload(slack_details, resoptions)

        mocked_api_call.assert_called_with(
            "chat.postMessage",
            channel="C1H9RESGL",
            as_user=True,
            username=def_username,
            parse="none",
            link_names=1,
            mrkdown=True,
            attachments=attachment_json,
            text=None
        )
        assert results.get("ok") is True

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
        try:
            slack_utils.slack_post_message(None, "testing", True, None, True, def_username)
            assert False
        except IntegrationError:
            assert True

    def _buildDataDetails(self):
        """ Mock Data Details """
        return {
            "Additional Text": {"type": "string", "data": "Hey this is my message"},
            "Resilient URL": {"type": "incident", "data": "1234"},
            "Type of data": {"type": "string", "data": "Artifact"},
            "Resilient Incident": {"type": "string", "data": "title here"},
            "Description": {"type": "richtext", "data": "<div>data<div>"},
            "Confirmed": {"type": "boolean", "data": "true"},
            "Create Date": {"type": "datetime", "data": 1525356259000},
            "Start Date": {"type": "datetime", "data": 1525356259000},
            "Severity": {"type": "string", "data": "low"},
            "NIST Vectors": {"type": "string", "data": "[Email, Malware]"},
            "Incident Types": {"type": "string", "data": "u'[u\\'Malware\\', u\\'Lost PC / laptop / tablet\\']'"}
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
        except IntegrationError:
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
                    "name": "spengler",
                    "profile": {
                        "display_name": "Egon Spengler"
                    }
                }
        }
        slack_utils = SlackUtils("fake_api_key")
        display_name = slack_utils.get_user_display_name("W012A3CDE")
        mocked_api_call.assert_called_with(  # checks the last call to a method, check for b@b.com email
            "users.info",
            user="W012A3CDE"
        )
        assert display_name == "Egon Spengler"

    @patch('fn_slack.lib.slack_common.SlackClient.api_call')
    def test_get_user_info_no_display_name(self, mocked_api_call):
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
        display_name = slack_utils.get_user_display_name("W012A3CDE")
        mocked_api_call.assert_called_with(  # checks the last call to a method, check for b@b.com email
            "users.info",
            user="W012A3CDE"
        )
        assert display_name == "spengler"

    @patch('fn_slack.lib.slack_common.SlackClient.api_call')
    def test_get_user_info_error(self, mocked_api_call):
        """ Test get user info error"""
        print("Test get user info error\n")

        mocked_api_call.return_value = {
            "ok": False
        }
        try:
            slack_utils = SlackUtils("fake_api_key")
            slack_utils.get_user_display_name("W012A3CDE")
            assert False
        except IntegrationError:
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
        except IntegrationError:
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
                        "text": "one",
                        "ts": "1"
                    },
                    {
                        "text": "two",
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
                        "text": "three",
                        "ts": "3"
                    },
                    {
                        "text": "four",
                        "ts": "4"
                    }],
                "response_metadata": {
                    "next_cursor": None
                }
            }]
        slack_utils = SlackUtils("fake_api_key")
        message_ts_list = slack_utils._get_channel_parent_message_history()
        assert message_ts_list == [{'text': 'one', "ts": "1"}, {'text': 'two', "ts": "2"}, {'text': 'three', "ts": "3"}, {'text': 'four', "ts": "4"}]

    @patch('fn_slack.lib.slack_common.SlackClient.api_call')
    def test_get_channel_parent_message_history_error(self, mocked_api_call):
        """ Test get channel parent msg history error"""
        print("Test get channel parent msg history error\n")

        mocked_api_call.side_effect = [
            {
                "ok": False
            }]

        slack_utils = SlackUtils("fake_api_key")
        try:
            slack_utils._get_channel_parent_message_history()
            assert False
        except IntegrationError:
            assert True

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
                        "text": "parent_one",
                        "thread_ts": "111",
                        "ts": "111"
                    },
                    {
                        "text": "reply_one",
                        "thread_ts": "111",
                        "ts": "112"
                    }],
                "response_metadata": {
                    "next_cursor": "bmV4d"
                }
            },
            {
                "ok": True,
                "messages": [
                    {
                        "text": "reply_two",
                        "thread_ts": "111",
                        "ts": "113"
                    }],
                "response_metadata": {
                    "next_cursor": None
                }
            }]

        mocked_msg_history_list.return_value = [{'text': 'parent_one', "replies": [{"mock": "mock"}]}, {'text': 'parent_two'}]

        slack_utils = SlackUtils("fake_api_key")
        history = slack_utils.get_channel_complete_history()
        assert history == [{'text': 'parent_one', "replies": [{"mock": "mock"}]},
                           {'text': 'reply_one', "thread_ts": "111", "ts": "112"},
                           {"text": "reply_two", "thread_ts": "111", "ts": "113"},
                           {'text': 'parent_two'}]

    @patch('fn_slack.lib.slack_common.SlackUtils._get_channel_parent_message_history')
    @patch('fn_slack.lib.slack_common.SlackClient.api_call')
    def test_get_channel_complete_history_error(self, mocked_api_call, mocked_msg_history_list):
        """ Test get complete history error """
        print("Test get complete history error\n")

        mocked_api_call.side_effect = [
            {
                "ok": False
            }]

        mocked_msg_history_list.return_value = [{'text': 'parent_one', "replies": [{"mock": "mock"}]},
                                                {'text': 'parent_two'}]

        slack_utils = SlackUtils("fake_api_key")
        try:
            slack_utils.get_channel_complete_history()
            assert False
        except IntegrationError:
            assert True

    @pytest.mark.parametrize("is_channel,is_private,expected", [
        (True, False, "Public"),  # public channel
        (False, True, "Private")  # private channel
    ])
    def test_get_channel_type(self, is_channel, is_private, expected):
        """ Test get channel type as str"""
        print("Test get channel type as str - {}\n".format(expected))

        # Setup channel first
        mocked_channel = {
            "id": "C0EAQDV4Z",
            "name": "test-channel",
            "is_channel": is_channel,
            "is_private": is_private
        }
        slack_utils = SlackUtils("fake_api_key")
        slack_utils.set_channel(mocked_channel)

        assert slack_utils.get_channel_type() == expected

    def test_get_template_file_path(self):
        """ Test get template file path"""
        print("Test get template file path\n")

        path = get_template_file_path("test")

        assert "test" in path

    def test_get_template_file_path_error(self):
        """ Test get template file path error"""
        print("Test get template file path error\n")

        try:
            get_template_file_path(123)
            assert False
        except ValueError:
            assert True

    def test_data_for_template(self):
        """ Test data for template"""
        print("Test data for template\n")

        data = data_for_template("number", "username", "reply_count", "msg_time", "msg_pretext", "msg_text",
                                 "file_permalink", "file_name", True)

        expected_data = {
            "number": "number",
            "username": "username",
            "reply_count": "reply_count",
            "msg_time": "msg_time",
            "msg_pretext": "msg_pretext",
            "msg_text": "msg_text",
            "file_permalink": "file_permalink",
            "file_name": "file_name",
            "is_msg_parent": True
        }

        assert data == expected_data

    @pytest.mark.parametrize("incident_id,task_id,res_id", [
        (1001, None, "RES-1001"),
        (1001, 2002, "RES-1001-2002")
    ])
    def test_generate_res_id(self, incident_id, task_id, res_id):
        """ Test generate res id"""
        print("Test generate res id\n")

        assert generate_res_id(incident_id, task_id) == res_id

    @pytest.mark.parametrize("incident_id,task_id,expected_channel_name", [
        (2095, None, "test-incident-channel"),
        (2095, 2251214, "test-task-channel")
    ])
    def test_slack_channel_name_datatable_lookup(self, incident_id, task_id, expected_channel_name):
        """ Test slack channel name datatable lookup"""
        print("Test slack channel name datatable lookup\n")

        mocked_res_client = Mock()
        mocked_res_client.get.return_value = {u'rows': [
            {u'cells': {
                u'slack_db_res_id': {u'row_id': 14, u'id': u'slack_db_res_id', u'value': u'RES-2095'},
                u'slack_db_channel': {u'row_id': 14, u'id': u'slack_db_channel', u'value': u'test-incident-channel'}}},

            {u'cells': {
              u'slack_db_res_id': {u'row_id': 15, u'id': u'slack_db_res_id', u'value': u'RES-2095-2251214'},
              u'slack_db_channel': {u'row_id': 15, u'id': u'slack_db_channel', u'value': u'test-task-channel'}}}
        ]}

        result = slack_channel_name_datatable_lookup(mocked_res_client, 2095, 2251214)
        return result == expected_channel_name

    def test_slack_channel_name_datatable_lookup_data_error(self):
        """ Test slack channel name datatable lookup data error"""
        print("Test slack channel name datatable lookup data error\n")

        mocked_res_client = Mock()
        mocked_res_client.get.side_effect = Exception

        try:
            slack_channel_name_datatable_lookup(mocked_res_client, 2095, 2251214)
            assert False
        except ValueError:
            assert True

    def test_slack_channel_name_datatable_lookup_no_res_id_error(self):
        """ Test slack channel name datatable lookup no res id error"""
        print("Test slack channel name datatable lookup no res id error\n")

        mocked_res_client = Mock()
        mocked_res_client.get.return_value = {u'rows': [
            {u'cells': {
                u'slack_db_channel': {u'row_id': 14, u'id': u'slack_db_channel', u'value': u'test-incident-channel'}}}]}

        try:
            slack_channel_name_datatable_lookup(mocked_res_client, 2095, 2251214)
            assert False
        except ValueError:
            assert True

    def test_slack_channel_name_datatable_lookup_return_none(self):
        """ Test slack channel name datatable lookup return none"""
        print("Test slack channel name datatable lookup return none\n")

        mocked_res_client = Mock()
        mocked_res_client.get.return_value = {u'rows': [
            {u'cells': {
                u'slack_db_res_id': {u'row_id': 14, u'id': u'slack_db_res_id', u'value': u'RES-2095'},
                u'slack_db_channel': {u'row_id': 14, u'id': u'slack_db_channel', u'value': u'test-incident-channel'}}}
        ]}

        result = slack_channel_name_datatable_lookup(mocked_res_client, 2095, 2251214)
        assert result is None

    @patch('fn_slack.lib.slack_common.SlackUtils.get_permalink')
    def test_create_row_in_datatable(self, mocked_permalink):
        """ Test slack create row in datatable"""
        print("Test slack create row in datatable\n")

        slack_utils = SlackUtils("fake_api_key")
        mocked_res_client = Mock()
        mocked_res_client.post.return_value = True
        mocked_permalink.return_value = "mocked_permalink"
        try:
            slack_utils.create_row_in_datatable(mocked_res_client, 2095, 2251214, "fake_thread_id")
            assert True
        except ValueError:
            assert False

    @patch('fn_slack.lib.slack_common.SlackUtils.get_permalink')
    def test_create_row_in_datatable_error(self, mocked_permalink):
        """ Test slack create row in datatable error"""
        print("Test slack create row in datatable error\n")

        slack_utils = SlackUtils("fake_api_key")
        mocked_res_client = Mock()
        mocked_res_client.post.side_effect = Exception
        mocked_permalink.return_value = "mocked_permalink"
        try:
            slack_utils.create_row_in_datatable(mocked_res_client, 2095, 2251214, "fake_thread_id")
            assert False
        except ValueError:
            assert True

    @pytest.mark.parametrize("incident_id,task_id", [
        (2095, None),
        (2095, 2251214)
    ])
    def test_post_attachment_to_resilient(self, incident_id, task_id):
        """ Test post attachment to resilient"""
        print("Test post attachment to resilient\n")

        # Setup channel first
        mocked_channel = {
            "name": "test-channel"
        }
        slack_utils = SlackUtils("fake_api_key")
        slack_utils.set_channel(mocked_channel)

        mocked_res_client = Mock()
        mocked_res_client.post_attachment.return_value = True

        mocked_temp_file = Mock()
        mocked_temp_file.name.return_value = "Name"

        try:
            slack_utils._post_attachment_to_resilient(mocked_res_client, incident_id, task_id, mocked_temp_file)
            assert True
        except ValueError:
            assert False

    def test_post_attachment_to_resilient_error(self):
        """ Test post attachment to resilient error"""
        print("Test post attachment to resilient error\n")

        # Setup channel first
        mocked_channel = {
            "name": "test-channel"
        }
        slack_utils = SlackUtils("fake_api_key")
        slack_utils.set_channel(mocked_channel)

        mocked_res_client = Mock()
        mocked_res_client.post_attachment.side_effect = Exception

        mocked_temp_file = Mock()
        mocked_temp_file.name.return_value = "Name"

        try:
            slack_utils._post_attachment_to_resilient(mocked_res_client, 2095, 2251214, mocked_temp_file)
            assert False
        except ValueError:
            assert True

    @pytest.mark.parametrize("type_channel,file_ts_result", [
        ("private", "1532"),
        ("public", "1532"),
        ("other", None)
    ])
    def test_get_ts_from_file_upload_results(self, type_channel, file_ts_result):
        """ Test get timestamp from file.upload json results"""
        print("Test get timestamp from file.upload json results\n")

        # Setup channel first
        mocked_channel = {
            "id": "C0EAQDV4Z",
            "name": "test-channel"
        }
        slack_utils = SlackUtils("fake_api_key")
        slack_utils.set_channel(mocked_channel)

        file_upload_results = {
            "ok": True,
            "file": {
                "shares": {
                    type_channel: {"C0EAQDV4Z": [{"ts": "1532"}]}
                }
            }
        }

        file_ts = slack_utils.get_ts_from_file_upload_results(file_upload_results)
        assert file_ts == file_ts_result

    @pytest.mark.parametrize("attachment_data", [
        {"attachment": {"name": "n", "content_type": "ct", "inc_id": "id", "type": "tp"}},  # attachment
        {"name": "n", "content_type": "ct", "inc_id": "id", "type": "tp"}  # artifact attachment
    ])
    @patch('fn_slack.lib.slack_common.SlackClient.api_call')
    def test_slack_post_attachment(self, mocked_api_call, attachment_data):
        """ Test Slack post attachment - file upload"""
        print("Test Slack post attachment - file upload\n")

        mocked_api_call.side_effect = [
            {
                "ok": True
            }]

        slack_utils = SlackUtils("fake_api_key")
        try:
            slack_utils.slack_post_attachment("attachment_content", attachment_data, "text")
            assert True
        except IntegrationError:
            assert False

    @patch('fn_slack.lib.slack_common.SlackClient.api_call')
    def test_slack_post_attachment_error(self, mocked_api_call):
        """ Test Slack post attachment - file upload error"""
        print("Test Slack post attachment - file upload error\n")

        mocked_api_call.side_effect = [
            {
                "ok": False
            }]

        slack_utils = SlackUtils("fake_api_key")
        try:
            slack_utils.slack_post_attachment("attachment_content", {}, "text")
            assert False
        except IntegrationError:
            assert True

    def test_get_warnings(self):
        """ Test get warnings"""
        print("Test get warnings\n")
        slack_utils = SlackUtils("fake_api_key")
        assert isinstance(slack_utils.get_warnings(), list)

    @pytest.mark.parametrize("input_channel_name,channel_name_db_lookup_return,chosen_channel", [
        (None, "test-channel-return", "test-channel-return"),
        ("test-channel", "test-channel-return", "test-channel")
    ])
    @patch('fn_slack.lib.slack_common.slack_channel_name_datatable_lookup')
    def test_find_the_proper_channel_name(self, mocked_channel_name_db_lookup, input_channel_name,
                                          channel_name_db_lookup_return, chosen_channel):
        """ Test find the proper channel name"""
        print("Test find the proper channel name\n")

        slack_utils = SlackUtils("fake_api_key")

        mocked_channel_name_db_lookup.return_value = channel_name_db_lookup_return

        slack_channel_name, res_associated_channel_name = slack_utils._find_the_proper_channel_name(
            input_channel_name, "res_client", "incident_id", "task_id")

        assert slack_channel_name == chosen_channel
        assert res_associated_channel_name == channel_name_db_lookup_return

    @patch('fn_slack.lib.slack_common.slack_channel_name_datatable_lookup')
    def test_find_the_proper_channel_name_error(self, mocked_channel_name_db_lookup):
        """ Test find the proper channel name error"""
        print("Test find the proper channel name error\n")
        slack_utils = SlackUtils("fake_api_key")
        mocked_channel_name_db_lookup.return_value = None
        try:
            slack_utils._find_the_proper_channel_name(None, "res_client", "incident_id", "task_id")
            assert False
        except IntegrationError:
            assert True

    @pytest.mark.parametrize("slack_is_private,is_channel,is_private,is_archived", [
        (True, True, False, False),  # slack_is_private is True & channel is public
        (False, False, True, False),  # slack_is_private is False & channel is private
        (True, False, True, True)  # slack_is_private is True & channel is private but channel is archived
    ])
    @patch('fn_slack.lib.slack_common.SlackUtils._find_the_proper_channel_name')
    @patch('fn_slack.lib.slack_common.SlackUtils.find_channel_by_name')
    def test_find_or_create_channel_error(self, mocked_found_channel, mocked_channel_name, slack_is_private, is_channel, is_private, is_archived):
        """ Test find or create channel error"""
        print("Test find or create channel error\n")
        mocked_found_channel.return_value = True  # do nothing
        mocked_channel_name.return_value = ("test-channel", "res_associated_channel_name")
        mocked_channel = {
            "id": "C0EAQDV4Z",
            "name": "test-channel",
            "is_channel": is_channel,
            "is_private": is_private,
            "is_archived": is_archived
        }
        slack_utils = SlackUtils("fake_api_key")
        slack_utils.set_channel(mocked_channel)
        try:
            slack_utils.find_or_create_channel("test-channel", slack_is_private, "res_client", "incident_id", "task_id")
            assert False
        except IntegrationError:
            assert True

    @patch('fn_slack.lib.slack_common.SlackUtils._find_the_proper_channel_name')
    @patch('fn_slack.lib.slack_common.SlackUtils.find_channel_by_name')
    @patch('fn_slack.lib.slack_common.SlackUtils.slack_create_channel')
    @patch('fn_slack.lib.slack_common.SlackUtils.get_channel_name')
    def test_find_or_create_channel(self, mocked_returned_channel_name, mocked_created_channel, mocked_found_channel,
                                    mocked_channel_name):
        """ Test find or create channel"""
        print("Test find or create channel\n")
        mocked_found_channel.return_value = True  # do nothing
        mocked_channel_name.return_value = ("test-channel", "res_associated_channel_name")
        mocked_created_channel.return_value = True  # do nothing
        mocked_returned_channel_name.return_value = "edited-test-channel" # Slack validation can modify the submitted channel name

        slack_utils = SlackUtils("fake_api_key")
        slack_channel_name, has_association_in_slack_db = slack_utils.find_or_create_channel(
            "test-channel", True, "res_client", "incident_id", "task_id")

        assert slack_channel_name == "edited-test-channel"
        assert has_association_in_slack_db is True

    @patch('fn_slack.lib.slack_common.SlackUtils._find_the_proper_channel_name')
    @patch('fn_slack.lib.slack_common.SlackUtils.find_channel_by_name')
    @patch('fn_slack.lib.slack_common.SlackUtils.slack_create_channel')
    def test_find_or_create_channel_is_private_error(self, mocked_created_channel, mocked_found_channel, mocked_channel_name):
        """ Test find or create channel - is private error"""
        print("Test find or create channel - is private error\n")
        mocked_found_channel.return_value = True  # do nothing
        mocked_channel_name.return_value = ("test-channel", "res_associated_channel_name")
        mocked_created_channel.return_value = True  # do nothing

        slack_utils = SlackUtils("fake_api_key")
        try:
            slack_utils.find_or_create_channel("test-channel", None, "res_client", "incident_id", "task_id")
            assert False
        except ValueError:
            assert True

    @pytest.mark.parametrize("message,expected_output_data", [
        ({"type": "message", "subtype": "bot_message", "username": "username", "ts": "1531195200",
         "thread_ts": "1531195200", "reply_count": 3, "text": "Non attachment text",
          "files": [{"permalink": "permalink", "name": "name"}]},
         {'username': "username", 'msg_time': '2018-07-10 04:00:00', 'reply_count': 3, 'msg_text': 'Non attachment text',
          'msg_pretext': None, 'file_name': 'File name name', 'file_permalink': 'File url permalink',
          'is_msg_parent': True, 'number': 'number'}),  # this is a file upload and is_parent is True
        ({"type": "message", "subtype": "not_bot_message", "username": "username", "ts": "1531195200",
          "thread_ts": "1531195201", "reply_count": 3, "text": None,
          "attachments": [{"pretext": "pretext", "text": "Attachment text"}]},
         {'username': "mocked_user_display_name", 'msg_time': '2018-07-10 04:00:00', 'reply_count': 3, 'msg_text': 'Attachment text',
          'msg_pretext': 'pretext', 'file_name': None, 'file_permalink': None,
          'is_msg_parent': False, 'number': 'number'})  # this is an Slack attachment and is_parent is False and it's not a bot message
    ])
    @patch('fn_slack.lib.slack_common.SlackUtils.get_user_display_name')
    def test_parse_message_data(self, mocked_user_display_name, message, expected_output_data):
        """ Test parse message data"""
        print("Test parse message data\n")
        slack_utils = SlackUtils("fake_api_key")
        mocked_user_display_name.return_value = "mocked_user_display_name"
        data = slack_utils._parse_message_data(message, "number")
        assert data == expected_output_data
