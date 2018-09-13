# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
import logging
import simplejson as json
from fn_slack.lib.errors import IntegrationError
from fn_slack.lib.resilient_common import clean_html, build_incident_url, build_resilient_url, build_timestamp
from slackclient import SlackClient
from six import string_types

LOG = logging.getLogger(__name__)


class SlackUtils(object):

    slack_client = None
    channel = None

    def __init__(self, api_token, slack_channel_name):
        self.slack_client = SlackClient(api_token)
        self.channel = self.find_channel_by_name(slack_channel_name)

    def get_channel(self):
        """
        Return instance variable channel.
        :return: channel
        """
        return self.channel

    def set_channel(self, channel):
        """
        Set the instance variable channel.
        :param channel:
        """
        self.channel = channel

    def slack_post_message(self, resoptions, slack_details, slack_as_user, slack_username, slack_reply_broadcast,
                           slack_parse, slack_markdown, slack_thread_id, def_username):
        """
        Process the slack post
        :param resoptions: app.config resilient section
        :param slack_details: json structure for how to structure the payload to slack
        See slack API for the use of these variables
        :param slack_as_user:
        :param slack_username:
        :param slack_reply_broadcast:
        :param slack_parse:
        :param slack_markdown:
        :param slack_thread_id:
        :param def_username - name to use for who posted the message
        :return: JSON result
        """
        data = json.loads(slack_details.replace("\\n", ""), strict=False)  # cleanup for json.loads
        payload = build_payload(data, resoptions)
        LOG.debug(payload)

        # start processing
        results = self.slack_client.api_call(
            "chat.postMessage",
            channel=self.channel.get("id"),
            text=payload,
            as_user=slack_as_user,
            username=slack_username if slack_username else def_username,
            reply_broadcast=slack_reply_broadcast,
            parse=slack_parse,
            link_names=1, # Find and link channel names by mentioning users with their user ID '<@U123>'. On by default.
            mrkdown=slack_markdown,
            thread_ts=slack_thread_id
        )
        LOG.debug(results)

        return results

    def invite_users_to_channel(self, user_id_list):
        """
        Method invites 1-30 users to a public or private channel.
        :param user_id_list: A comma separated list of user IDs. Up to 30 users may be listed.
        :return: JSON result
        """
        users_id = ",".join(user_id_list)

        results = self.slack_client.api_call(
            "conversations.invite",
            channel=self.channel.get("id"),
            users=users_id
        )
        LOG.debug(results)

        return results

    def find_channel_by_name(self, slack_channel_name):
        """
        Method verifies if suggested slack channel already exists and returns the channel object.
        :param slack_channel_name: Name of the public or private channel
        :return: channel object
        """
        all_channels = self._slack_find_channels()

        for channel in all_channels:
            if slack_channel_name == channel.get("name"):
                return channel

        return None

    def find_user_ids(self, emails):
        """
        Method will lookup users by email and return a list od user ids.
        :param emails: comma-delimited string
        :return: list of user ids
        """
        list_emails = emails.split(",")
        user_id_list = [self._lookup_user_by_email(email.strip()) for email in list_emails]
        return user_id_list

    def _lookup_user_by_email(self, user_email):
        """
        Retrieve a single user by looking them up by their registered email address.
        :param user_email: An email address belonging to a user in the workspace
        :return:
        """
        results = self.slack_client.api_call(
            "users.lookupByEmail",
            email=user_email
        )
        LOG.debug(results)

        if all(key in results for key in ("ok", "user")) and results.get("ok"):
            return results.get("user").get("id")

        else:
            raise ValueError("Slack error response: " + results.get("error", ""))

    def is_channel_private(self):
        """
        Verify if channel is private.
        channel.get("is_channel") is True & channel.get("is_private") is False -> public channel
        channel.get("is_channel") is False & channel.get("is_private") is True -> private channel
        :return:
        """
        if self.channel and not self.channel.get("is_channel") and self.channel.get("is_private"):
            return True

        else:
            return False

    def _slack_find_channels(self):
        """
        Method returns a list of all public or private channels in a workspace.
        :return: list of channels
        """
        # Using Conversations API to access anything channel-like (private, public, direct, etc)

        results = self.slack_client.api_call(
            "conversations.list",
            exclude_archived=True,
            types="public_channel,private_channel"
        )
        LOG.debug(results)

        if "ok" in results and results.get("ok"):
            return results.get("channels")

        else:
            raise ValueError("Slack error response: " + results.get("error", ""))

    def slack_create_channel(self, slack_channel_name, is_private):
        """
        Method creates a public or private channel.
        Using Conversations API to access anything channel-like (private, public, direct, etc).
        Channel names can only contain lowercase letters, numbers, hyphens, and underscores, and must be
        21 characters or less. Slack validates the submitted channel name and modifies it to meet the above criteria.
        Since the channel name can get modified use channel_id instead.
        :param slack_channel_name: Name of the public or private channel to create
        :param is_private: Create a private channel instead of a public one
        :return: channel dict
        """
        results = self.slack_client.api_call(
            "conversations.create",
            name=slack_channel_name,
            is_private=is_private
        )
        LOG.debug(results)

        if all(key in results for key in ("ok", "channel")) and results.get("ok"):
            return results.get("channel")

        else:
            raise ValueError("Slack error response: " + results.get("error", ""))

    def get_permalink(self, thread_id):
        """
        Retrieve a permalink URL for a specific extant message
        :param thread_id: A message's ts value, uniquely identifying it within a channel
        :return:
        """
        results = self.slack_client.api_call(
            "chat.getPermalink",
            channel=self.channel.get("id"),
            message_ts=thread_id
        )
        LOG.debug(results)

        if all(key in results for key in ("ok", "permalink")) and results.get("ok"):
            return results.get("permalink")

        else:
            raise ValueError("Slack error response: " + results.get("error", ""))


def build_payload(dataDict, resoptions):
    """
    build the payload string based on the different types of data created
    :param dataDict:
    :return: payload string
    """
    payload = ""

    for key, valDict in dataDict.items():
        if len(payload) > 0:
            payload += "\n"

        if valDict['type'] == 'string' and valDict['data']:
            payload += '{}: {}'.format(key, valDict['data'])

        elif valDict['type'] == 'incident' and valDict['data']:
            payload += '{}: {}'.format(key, build_incident_url(build_resilient_url(resoptions['host'], resoptions['port']), valDict['data']))

        elif valDict['type'] == 'richtext' and valDict['data']:
            cleaned_data = clean_html(valDict['data'])
            if len(cleaned_data) > 0:
                payload += '{}: {}'.format(key, cleaned_data)

        elif valDict['type'] == 'datetime' and valDict['data'] and valDict['data'] != 0:
            payload += '{}: {}'.format(key, build_timestamp(valDict['data']))

        elif valDict['type'] == 'boolean' and valDict['data']:
            payload += '{}: {}'.format(key, build_boolean(valDict['data'], true_value='Yes', false_value='No'))

        elif valDict['data']:
            raise IntegrationError("Invalid type: "+ valDict['type'])

    return payload


def build_boolean(value, true_value="True", false_value="False"):
    """
    Builders for slack presentation. Convert internal boolean to displayable format.
    :param value: boolean
    :param true_value: value to use when boolean=True
    :param false_value: value to use when boolean=False
    :return: payload string
    """
    if isinstance(value, string_types):
        return true_value if value.lower() in ('1', 'yes', 'true') else false_value
    if isinstance(value, int):
        return true_value if value == 1 else false_value

    return false_value
