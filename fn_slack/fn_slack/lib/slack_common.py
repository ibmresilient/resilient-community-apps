# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
import logging
import json
try:
    from json import JSONDecodeError
except:
    JSONDecodeError = ValueError

from fn_slack.lib.errors import IntegrationError
from fn_slack.lib.resilient_common import *
from slackclient import SlackClient
from six import string_types
import tempfile
import datetime
import resilient_circuits.template_functions as template_functions
from os.path import join, pardir
import os
import time

LOG = logging.getLogger(__name__)

# Template files for Slack
ARCHIVE_TEMPLATE_PATH = "data/templates/template_archive_slack.jinja2"
# API name of Slack conversations datatable
DATA_TABLE_API_NAME = "slack_conversations_db"
# Prefix for generating res_id which is either RES-1001 for incidents or RES-1001-2002 for tasks
RES_PREFIX = "RES"


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
        if self.get_channel() is not None:
            return self.get_channel().get("id")
        else:
            return None

    def get_channel_name(self):
        """
        Return channel_name.
        :return: channel_name
        """
        if self.get_channel() is not None:
            return self.get_channel().get("name")
        else:
            return None

    def slack_post_message(self, resoptions, slack_text, slack_as_user, slack_username, slack_markdown, def_username):
        """
        Process the slack post
        :param resoptions: app.config resilient section
        :param slack_text: json structure for how to structure the payload to slack
        See slack API for the use of these variables
        :param slack_as_user:
        :param slack_username:
        :param slack_markdown:
        :param def_username - name to use for who posted the message
        :return: JSON result
        """
        try:
            payload = convert_slack_details_to_payload(slack_text, resoptions)
        except JSONDecodeError: # if slack_text isn't in JSON format then just post it as is - we need to post to Slack from other methods, like right before archiving channel
            payload = slack_text

        # start processing
        results = self.slack_client.api_call(
            "chat.postMessage",
            channel=self.get_channel_id(),
            text=payload,
            as_user=slack_as_user,
            username=slack_username if slack_username else def_username,
            parse="full",  # In full parse mode, Slack will linkify URLs, channel names (starting with a '#') and usernames (starting with an '@').
            link_names=1,  # Find and link channel names by mentioning users with their user ID '<@U123>'. On by default.
            mrkdown=slack_markdown
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
            channel=self.get_channel_id(),
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

        for ch in all_channels:
            if ch.get("name") == slack_channel_name:
                self.channel = ch
                break

    def _slack_find_channels(self, cursor=None):
        """
        Method returns a list of all public or private channels in a workspace.
        Using Conversations API to access anything channel-like (private, public, direct, etc)

        Supports pagination. Cursor-based pagination will make it easier to
        incrementally collect information. To begin pagination, specify a limit value under 1000.
        Slack recommends no more than 200 results at a time. Paginate only until channel is found.
        :return: list of channels
        """
        has_more_results = True
        while has_more_results:
            results = self.slack_client.api_call(
                "conversations.list",
                exclude_archived=False,  # we need to load archived channels
                types="public_channel,private_channel",
                limit=100,
                cursor=cursor
            )
            LOG.debug(results)

            has_more_results, cursor = self._get_next_cursor_for_next_page(results)
            for ch in results.get("channels"):  # yield the first page, paginate only until channel is found!
                yield ch

    def lookup_user_by_email(self, user_email):
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

        return results

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

    def is_channel_archived(self):
        """
        Verify if channel is archived.
        :return: True if channel is archived
        """
        if self.channel and self.channel.get("is_archived"):
            return True

        else:
            return False

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
            channel=self.get_channel_id(),
            message_ts=thread_id
        )
        LOG.debug(results)

        if results.get("ok"):
            return results.get("permalink")

        else:
            raise ValueError("Slack error response: " + results.get("error", ""))

    def _get_channel_parent_message_history(self, cursor=None):
        """
        Method returns the thread's parent message IDs ("ts") from a conversation. Supports pagination.
        Need to call "conversations.history" method with no latest or oldest arguments,
        and then continue paging using the cursor. Cursor-based pagination will make it easier to
        incrementally collect information. To begin pagination, specify a limit value under 1000.
        Slack recommends no more than 200 results at a time.

        "conversations.history" method returns only parent messages, save all parent messages ts IDs and call
        "conversations.replies" function to load complete message history.
        :return: list of 'ts' timestamps - thread's parent message.
        """
        message_ts_list = []
        has_more_results = True
        while has_more_results:
            results = self.slack_client.api_call(
                "conversations.history",
                channel=self.get_channel_id(),
                limit=200,
                cursor=cursor
            )
            LOG.debug(results)

            has_more_results, cursor = self._get_next_cursor_for_next_page(results)
            message_ts_list.extend([msg.get("ts") for msg in results.get("messages")])

        return message_ts_list

    @staticmethod
    def _get_next_cursor_for_next_page(results):
        """
        Cursor-based pagination will make it easier to incrementally collect information.
        :param results
        :return:
        """
        has_more_results = True
        cursor = None

        if results.get("ok"):
            response_metadata = results.get("response_metadata")
            if response_metadata:  # more pages
                cursor = response_metadata.get("next_cursor")
                if not cursor:
                    # we've reached the last page
                    has_more_results = False
            else:
                # we've reached the last page
                has_more_results = False

            return has_more_results, cursor
        else:
            raise ValueError("Slack error response: " + results.get("error", ""))

    def get_channel_complete_history(self, cursor=None):
        """
        Method will return the entire history for a conversation. Supports pagination.
        Cursor-based pagination will make it easier to
        incrementally collect information. To begin pagination, specify a limit value under 1000.
        Slack recommends no more than 200 results at a time.

        Do not use "conversations.history" here use "conversations.replies" instead, "conversations.replies" method
        returns an entire thread (a message plus all the messages in reply to it),
        while "conversations.history" method returns only parent messages.
        :return: JSON result
        """
        # Get a list of thread's parent message "ts" which are the timestamp of an existing parent
        # message with 0 or more replies. If there are no replies then just the single parent message
        # referenced by "ts" will return - it is just an ordinary message.
        message_ts_list = self._get_channel_parent_message_history()

        history = []

        for msg_ts in message_ts_list:
            has_more_results = True
            while has_more_results:
                results = self.slack_client.api_call(
                    "conversations.replies",
                    channel=self.get_channel_id(),
                    ts=msg_ts,
                    limit=20,
                    cursor=cursor
                )
                LOG.debug(results)

                has_more_results, cursor = self._get_next_cursor_for_next_page(results)
                history.extend(results.get("messages"))

        return history

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

    def save_conversation_history_as_attachment(self, res_client, messages, incident_id, task_id):
        """
        Method saves conversation history to a text file and posts it as an attachment.
        :param messages list of message dict
        :param res_client Resilient API
        :param incident_id
        :param task_id
        :return:
        """
        archive_template = get_template_file_path(ARCHIVE_TEMPLATE_PATH)

        with tempfile.NamedTemporaryFile(mode="w+t", delete=False) as temp_file:
            try:
                # For each msg in the history, parse
                for message in messages:
                    if message.get("type") == "message":

                        # 1 get the username
                        subtype = message.get("subtype")
                        if subtype == "bot_message":
                            username = message["username"]  # Bot's name is stored in "username" property
                        else:
                            username = self.get_user_info(message.get("user")).get("name")

                        # 2 were there any replies - only parent messages can have replies
                        reply_count = message.get("reply_count")
                        is_msg_parent = reply_count is not None

                        # 3 get the timestamp
                        msg_ts = datetime.datetime.utcfromtimestamp(float(message.get("ts")))
                        msg_time = msg_ts.strftime("%Y-%m-%d %H:%M:%S")

                        # 4 get the text message
                        text = message.get("text")

                        # 5 write in a temp file
                        data = data_for_template(username, reply_count, msg_time, text, is_msg_parent)
                        output_data = map_values(archive_template, data)
                        temp_file.write(output_data.encode('utf-8'))

                temp_file.close()

                new_attachment = self._post_attachment_to_resilient(res_client, incident_id, task_id, temp_file)

            except Exception as ex:
                raise ex

            finally:
                os.unlink(temp_file.name)

        return new_attachment

    def _post_attachment_to_resilient(self, res_client, incident_id, task_id, temp_file):
        """
        Function posts an attachment to Resilient.
        :param res_client:
        :param incident_id:
        :param task_id:
        :param temp_file:
        :return:
        """
        # Create POST uri
        # ..for a task, if task_id is defined
        if task_id:
            attachment_uri = '/tasks/{}/attachments'.format(task_id)
        # ...else for an attachment
        else:
            attachment_uri = '/incidents/{}/attachments'.format(incident_id)

        # POST the new attachment
        attachment_name = "slack_msg_export_channel_" + self.get_channel_name() + ".txt"
        new_attachment = res_client.post_attachment(attachment_uri, temp_file.name, filename=attachment_name,
                                                    mimetype='text/plain')
        return new_attachment

    def archive_channel(self):
        """
        Function sets the channel to archive.
        :return:
        """
        # results = self.slack_client.api_call(
        #     "conversations.archive",
        #     channel=self.get_channel_id()
        # )
        # LOG.debug(results)
        # return results
        return {"ok": True} # FIXME at the moment it's turned off for easier testing

    def get_channel_type(self):
        """
        Return channels status as str.
        :return:
        """
        if self.is_channel_private():
            return "Private"
        else:
            return "Public"

    def create_row_in_datatable(self, res_client, incident_id, task_id, thread_id):
        """
        Create a row in Resilient datatable.
        :param res_client:
        :param incident_id:
        :param task_id:
        :param thread_id:
        :return:
        """
        # Get current time (*1000 as API does not accept int)
        now = int(time.time() * 1000)

        # Create res_id
        res_id = generate_res_id(incident_id, task_id)

        # generate a permalink URL to join this conversation
        conversation_url = self.get_permalink(thread_id)

        # Generate cells for the datatable
        cells = {
            "cells": {
                "slack_db_time": {"value": now},
                "slack_db_res_id": {"value": res_id},
                "slack_db_channel": {"value": self.get_channel_name()},
                "slack_db_channel_type": {"value": self.get_channel_type()},
                "slack_db_permalink": {"value": """<a href="{0}">Link</a>""".format(conversation_url)}
            }
        }

        # Generate uri to POST datatable row
        uri = "/incidents/{0}/table_data/{1}/row_data?handle_format=names".format(incident_id, DATA_TABLE_API_NAME)

        try:
            # POST row
            add_row_response = res_client.post(uri, cells)
        except Exception as exe:
            raise exe

        return add_row_response


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


def convert_slack_details_to_payload(slack_text, resoptions):
    """
    Method converts json format to python dict and creates a payload for the post message.
    :param slack_text:
    :param resoptions:
    :return:
    """
    try:
        data = json.loads(slack_text.replace("\\n", ""), strict=False)  # cleanup for json.loads
        payload = build_payload(data, resoptions)
        LOG.debug(payload)
        return payload
    except JSONDecodeError:
        raise JSONDecodeError


def get_template_file_path(path):
    """
    Get template file path.
    :param path:
    :return:
    """
    current_path = os.path.dirname(os.path.realpath(__file__))
    template_file_path = join(current_path, pardir, path)
    return template_file_path


def map_values(template_file, message_dict):
    """
    Map values from jinja template.
    :param template_file:
    :param message_dict:
    :return:
    """
    with open(template_file, 'r') as template:

        LOG.debug("Message in dict form: {}".format(message_dict))

        template = template.read()
        output_data = template_functions.render(template, message_dict)

        return output_data


def data_for_template(username, reply_count, msg_time, msg_text, is_msg_parent):
    """
    Prepare the dictionary of substitution values for jinja template
    :param username:
    :param reply_count:
    :param msg_time:
    :param msg_text:
    :param is_msg_parent
    :return:
    """
    data = {
        "username": username,
        "reply_count": reply_count,
        "msg_time": msg_time,
        "msg_text": msg_text,
        "is_msg_parent": is_msg_parent
    }
    return data


def slack_channel_name_datatable_lookup(res_client, incident_id, task_id=None):
    """
    Function loads Resilient datatable and looks for the slack_channel name associated with your incident or task.
    :param res_client:
    :param incident_id:
    :param task_id:
    :return:
    """
    datatable = ConversationsDatatable(res_client, incident_id)
    datatable.get_data()
    return datatable.get_slack_channel_name(incident_id, task_id)


class ConversationsDatatable():
    """ Object for the Slack conversations datatable"""

    def __init__(self, res_client, incident_id):
        self.res_client = res_client
        self.incident_id = incident_id
        self.api_name = DATA_TABLE_API_NAME
        self.data = None
        self.rows = None

    def get_data(self):
        uri = "/incidents/{0}/table_data/{1}?handle_format=names".format(self.incident_id, self.api_name)
        try:
            self.data = self.res_client.get(uri)
            self.rows = self.data["rows"]
        except Exception as ex:
            raise ValueError("Failed to get {} datatable: ".format(DATA_TABLE_API_NAME) + ex)

    def get_slack_channel_name(self, incident_id, task_id=None):
        """
        Returns a res_associated_channel_name
        :param incident_id:
        :param task_id:
        :return:
        """
        id = [RES_PREFIX, str(incident_id)]

        if task_id is not None:
            id.append(str(task_id))

        res_id_to_search = "-".join(id)

        for row in self.rows:
            cells = row["cells"]
            slack_db_res_id = cells.get("slack_db_res_id")
            res_id = slack_db_res_id.get("value") if slack_db_res_id else None
            if res_id is None:
                raise ValueError("{} datatable is missing 'slack_db_res_id' column.".format(DATA_TABLE_API_NAME))

            if res_id_to_search == res_id:
                slack_db_channel = cells.get("slack_db_channel")
                if slack_db_channel:
                    return slack_db_channel.get("value")
        return None


def generate_res_id(incident_id, task_id=None):
    """If incident_id and task_id are valid, returns "RES-1001-2002"
      Else if task_id is None, returns "RES-1001" """

    res_id = [RES_PREFIX, str(incident_id)]
    if task_id is not None:
        res_id.append(str(task_id))
    return "-".join(res_id)
