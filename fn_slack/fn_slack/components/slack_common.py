# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
import logging
import simplejson as json
from fn_slack.lib.errors import IntegrationError
from fn_slack.lib.resilient_common import clean_html, build_incident_url, build_resilient_url, build_timestamp
from slackclient import SlackClient
from six import string_types
import tempfile
import datetime
import os

LOG = logging.getLogger(__name__)


class SlackUtils(object):

    slack_client = None
    channel = None

    def __init__(self, api_token):
        self.slack_client = SlackClient(api_token)

    def get_channel(self):
        """
        Return instance variable channel.
        :return: channel
        """
        return self.channel

    def set_channel(self, channel):
        """
        Set channel.
        :param channel:
        :return:
        """
        self.channel = channel

    def get_channel_id(self):
        """
        Return channel_id.
        :return: channel_id
        """
        return self.channel.get("id")

    def get_channel_name(self):
        """
        Return channel_name.
        :return: channel_name
        """
        return self.channel.get("name")

    def get_slack_client(self):
        """
        Return instance variable slack_client.
        :return: slack_client
        """
        return self.slack_client

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
                self.channel = channel

    def find_user_ids(self, emails):
        """
        Method will lookup users by email and return a list od user ids.
        :param emails: comma-delimited string
        :return: list of user ids
        """
        list_emails = emails.split(",")
        user_id_list = [self._lookup_user_by_email(email.strip()) for email in list_emails if email.strip()] # making sure to exclude ' ' or ''
        return user_id_list

    def _lookup_user_by_email(self, user_email):
        """
        Retrieve a single user by looking them up by their registered email address.
        :param user_email: An email address belonging to a user in the workspace
        :return: id_user
        """
        results = self.slack_client.api_call(
            "users.lookupByEmail",
            email=user_email
        )
        LOG.debug(results)

        user_data = results.get("user")
        if results.get("ok") and user_data:
            return user_data.get("id")

        else:
            raise ValueError("Slack error response: " + results.get("error", ""))

    def is_channel_private(self):
        """
        Verify if channel is private.
        channel.get("is_channel") is True & channel.get("is_private") is False -> public channel
        channel.get("is_channel") is False & channel.get("is_private") is True -> private channel
        :return: True if channel is private else False
        """
        if self.channel and not self.channel.get("is_channel") and self.channel.get("is_private"):
            return True

        else:
            return False

    def _slack_find_channels(self):
        """
        Method returns a list of all public or private channels in a workspace.
        # FIXME max 100 channels returned, look into cursor!
        :return: list of channels
        """
        # Using Conversations API to access anything channel-like (private, public, direct, etc)

        results = self.slack_client.api_call(
            "conversations.list",
            exclude_archived=True,
            types="public_channel,private_channel"
        )
        LOG.debug(results)

        if results.get("ok"):
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

        if results.get("ok"):
            self.channel = results.get("channel")

        else:
            raise ValueError("Slack error response: " + results.get("error", ""))

    def get_permalink(self, thread_id):
        """
        Retrieve a permalink URL for a specific extant message
        :param thread_id: A message's ts value, uniquely identifying it within a channel
        :return: permalink
        """
        results = self.slack_client.api_call(
            "chat.getPermalink",
            channel=self.channel.get("id"),
            message_ts=thread_id
        )
        LOG.debug(results)

        if results.get("ok"):
            return results.get("permalink")

        else:
            raise ValueError("Slack error response: " + results.get("error", ""))

    def get_channel_history(self, cursor=None):
        """
        Method return the entire history for a conversation. Need to call the method with no latest or oldest arguments,
        and then continue paging using the cursor. Cursor-based pagination will make it easier to
        incrementally collect information. To begin pagination, specify a limit value under 1000.
        Slack recommends no more than 200 results at a time.
        :return: JSON result
        """
        messages = []
        has_more_results = True
        while has_more_results:
            results = self.slack_client.api_call(
                "conversations.history",
                channel=self.channel.get("id"),
                limit=200,
                cursor=cursor
            )

            LOG.debug(results)

            if results.get("ok"):
                response_metadata = results.get("response_metadata")
                if results.get("has_more") and response_metadata:  # more pages
                    cursor = response_metadata.get("next_cursor")
                    # we've reached the last page
                    # not sure this extra step is needed, since we already check for "has_more" flag
                    # Slack pagination documentation isn't clear on this
                    if not cursor:
                        has_more_results = False
                else:  # final page
                    has_more_results = False
                messages.extend(results.get("messages"))

            else:
                raise ValueError("Slack error response: " + results.get("error", ""))

        return messages

    def get_user_info(self, user_id):
        """
        This method returns information about a member of a workspace.
        :param user_id:
        :return: user dict
        """
        results = self.slack_client.api_call(
            "users.info",
            user=user_id
        )
        LOG.debug(results)

        if results.get("ok"):
            return results.get("user")

        else:
            raise ValueError("Slack error response: " + results.get("error", ""))

    def save_conversation_history_as_attachment(self, messages, client, incident_id, task_id):
        """
        Method saves conversation history to a text file and posts it as an attachment.
        :param messages list of message dict
        :param client Resilient API
        :param incident_id
        :param task_id
        :return:
        """
        new_attachment = None
        with tempfile.NamedTemporaryFile(mode="w+t", delete=False) as temp_file:
            try:
                # For each msg in the history, parse
                for message in messages:
                    # get the username
                    if message.get("type") == "message":
                        subtype = message.get("subtype")
                        if subtype == "bot_message":
                            username = message["username"]  # Bot's name is stored in "username" property
                        else:
                            username = self.get_user_info(message.get("user")).get("name")

                        # get the timestamp
                        msg_ts = datetime.datetime.utcfromtimestamp(float(message.get("ts")))
                        msg_time = msg_ts.strftime("%Y-%m-%d %H:%M:%S")

                        # get the text message
                        msg_text = message.get("text")

                    # write to a temp file
                    temp_file.write(username.encode('utf-8') + " - " + msg_time.encode('utf-8') + ": " +
                                    msg_text.encode('utf-8') + "\n")
                    temp_file.write("\n")  # Add a new blank line

                temp_file.close()

                # Create POST uri
                # ..for a task, if task_id is defined
                if task_id:
                    attachment_uri = '/tasks/{}/attachments'.format(task_id)
                # ...else for an attachment
                else:
                    attachment_uri = '/incidents/{}/attachments'.format(incident_id)

                # POST the new attachment
                attachment_name = "slack_msg_export_" + self.get_channel_name() + ".txt"
                new_attachment = client.post_attachment(attachment_uri, temp_file.name, filename=attachment_name,
                                                        mimetype='text/plain')
            finally:
                os.unlink(temp_file.name)

        return new_attachment


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
