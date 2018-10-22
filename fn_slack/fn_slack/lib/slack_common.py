# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
import logging
import json
from fn_slack.lib.errors import IntegrationError
from fn_slack.lib.resilient_common import *
from slackclient import SlackClient
from six import string_types
import tempfile
import resilient_circuits.template_functions as template_functions
from os.path import join, pardir
import os
import time
import collections
import re

LOG = logging.getLogger(__name__)

# Template files for Slack
ARCHIVE_TEMPLATE_PATH = "data/templates/template_archive_slack.jinja2"
# API name of Slack conversations datatable
DATA_TABLE_API_NAME = "slack_conversations_db"
# Prefix for generating res_id which is either RES-1001 for incidents or RES-1001-2002 for tasks
RES_PREFIX = "RES"


class SlackUtils(object):

    def __init__(self, api_token):
        self.slack_client = SlackClient(api_token)
        self.channel = None
        self.warnings = []

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

    def get_warnings(self):
        """
        Return instance variable warnings.
        :return: warnings
        """
        return self.warnings

    def add_warning(self, warn):
        """
        Add warn to warnings.
        :param warn:
        :return:
        """
        if warn:
            self.warnings.append(warn)

    def find_or_create_channel(self, input_channel_name, slack_is_private, res_client, incident_id, task_id):
        """
        If channel_name is NOT specified in the function input, method will perform a lookup
        for associated channel_name in Slack Conversations Datatable. If there is an Incident or Task associated
        slack_channel, method will use found channel name for either searching for an existing Slack channel in
        Slack Workspace (api call) or create a new Slack channel (api call).
        If channel_name is specified in the function input, method will search for an existing Slack channel in
        Slack Workspace (api call) or create a new Slack channel (api call) with the specified channel_name.
        If channel_name is specified and there is also the associated channel fond, method will ignore the associated
        one and post to the input one.
        :param input_channel_name:
        :param slack_is_private:
        :param res_client:
        :param incident_id:
        :param task_id:
        :return: Method returns a channel_name.
        """
        # If user doesn't specify a channel name, use the incident/task associated channel (the default channel).
        res_associated_channel_name = slack_channel_name_datatable_lookup(res_client, incident_id, task_id)
        LOG.debug("slack_channel name associated with Incident or Task: %s", res_associated_channel_name)

        # Channel name validation - Channel name needs to be defined
        if input_channel_name is None and res_associated_channel_name is None:
            raise IntegrationError("There is no slack_channel name associated with Incident or Task available "
                                   "to post messages in")

        # Pick the right channel to post in
        slack_channel_name = None

        if input_channel_name is None and res_associated_channel_name:
            # if there wasn't channel specified in the activity prompt,
            # post to the_channel associated with the Incident or Task
            slack_channel_name = res_associated_channel_name

        elif input_channel_name:
            # if there was channel specified in the activity prompt,
            # post to to this one and ignore the associated one
            slack_channel_name = input_channel_name

            if res_associated_channel_name:
                # If the associated channel exists yield a StatusMessage
                self.add_warning("This Incident or Task has an association with Slack channel #{}, your message "
                                 "was posted in a different channel #{}".format(res_associated_channel_name,
                                                                                input_channel_name))

        # find the channel in Slack Workspace
        self.find_channel_by_name(slack_channel_name)

        # validation for channels existing in Slack Workspace
        if self.get_channel():
            self.add_warning("Channel #{} was found in your Workspace".format(slack_channel_name))

            # validate if your fun input param 'slack_is_private' matches channel's type, if not stop the workflow
            if slack_is_private and not self.is_channel_private():
                raise IntegrationError("You've indicated the channel you are posting to should be private. "
                                       "The existing channel #{} you are posting to is a public channel. "
                                       "To post to this channel change the input parameter "
                                       "'slack_is_channel_private' to 'No'.".format(slack_channel_name))
            elif slack_is_private is False and self.is_channel_private():
                raise IntegrationError("You've indicated the channel you are posting to should be public. "
                                       "The existing channel #{} you are posting to is a private channel. "
                                       "To post to this channel change the input parameter "
                                       "'slack_is_channel_private' to 'Yes'.".format(slack_channel_name))
            elif self.is_channel_archived():
                raise IntegrationError("Channel {} is archived".format(slack_channel_name))

        # create a new channel
        else:
            # validate slack_is_private is defined, check for None only, False is ok
            if slack_is_private is None:
                raise ValueError("Required field 'slack_is_private' is missing or empty")

            self.slack_create_channel(slack_channel_name, slack_is_private)

            # rewrite slack_channel_name just in case Slack validation modifies the submitted channel name
            slack_channel_name = self.get_channel_name()
            self.add_warning("Channel #{} was created in your Workspace".format(slack_channel_name))

        return slack_channel_name, res_associated_channel_name is not None

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
        attachment_json = None
        payload = None
        try:
            attachment_json = convert_slack_details_to_payload(slack_text, resoptions)
        except ValueError: # if slack_text isn't in JSON format then just post it as is - we need to post to Slack in a non JSON format from other functions, like right before archiving channel
            payload = slack_text

        results = self.slack_client.api_call(
            "chat.postMessage",
            channel=self.get_channel_id(),
            as_user=slack_as_user,
            username=slack_username if slack_username else def_username,  # FIXME! Username to be deprecated! Slack apps and their bot users should not use the username field when authoring a message. The username is part of your app's configuration and will not always be settable at runtime.
            parse="none",  # Slack will not perform any processing on the message, it will keep all markup formatting '<'
            link_names=1,  # Slack will linkify URLs, channel names (starting with a '#') and usernames (starting with an '@')
            mrkdown=slack_markdown,
            attachments=attachment_json,
            text=payload
        )
        LOG.debug(results)

        if results.get("ok"):
            self.add_warning("Message added to Slack")
            return results
        else:
            raise IntegrationError("Message add failed: " + json.dumps(results))

    def slack_post_attachment(self, attachment_content, attachment_data, slack_text):
        """
        Function uploads file to your slack_channel.
        :param attachment_content:
        :param attachment_data:
        :param slack_text
        :return:
        """
        attachment = attachment_data.get("attachment")
        if attachment:
            file_name = attachment.get("name") if attachment else None
            file_type = attachment.get("content_type") if attachment else None
            incident_id = attachment.get("inc_id") if attachment else None
            artifact_type = attachment.get("type") if attachment else None
        else:
            file_name = attachment_data.get("name")
            file_type = attachment_data.get("content_type")
            incident_id = attachment_data.get("inc_id")
            artifact_type = attachment_data.get("type")

        results = self.slack_client.api_call(
            "files.upload",
            channels=self.get_channel_id(),
            file=attachment_content,
            filename=file_name,
            filetype=file_type,
            title="Incident id {} {} attachment {}".format(incident_id, artifact_type, file_name),
            initial_comment=slack_text
        )
        LOG.debug(results)

        if results.get("ok"):
            self.add_warning("Attachment uploaded to Slack")
            return results
        else:
            raise IntegrationError("File upload failed: " + json.dumps(results))

    def find_user_ids_based_on_email(self, slack_participant_emails):
        """
        Find user ids based on their emails.
        :param slack_participant_emails:
        :return: user_id_list
        """
        # Find user ids based on their emails
        user_id_list = []

        emails = [email.strip() for email in slack_participant_emails.split(",") if email.strip()]  # making sure to exclude '  ' or ''
        for email in emails:
            results_user_id = self.lookup_user_by_email(email)

            if results_user_id.get("ok") and results_user_id.get("user"):
                user_id_list.append(results_user_id.get("user").get("id"))
            elif not results_user_id.get("ok") and results_user_id.get("error", "") == "users_not_found":
                self.add_warning("User {} s not a member of your workspace".format(email))
            else:
                raise IntegrationError("Invite users failed: " + json.dumps(results_user_id))

        return user_id_list

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

        if results.get("ok"):
            self.add_warning("Users invited to channel #{}".format(self.get_channel_name()))
        elif not results.get("ok") and results.get("error") == "already_in_channel":
            self.add_warning("Invited user is already in #{} channel".format(self.get_channel_name()))
        else:
            raise IntegrationError("Invite users failed: " + json.dumps(results))

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

            if not results.get("ok"):
                raise IntegrationError("Slack error response: " + results.get("error", ""))

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
            raise IntegrationError("Slack error response: " + results.get("error", ""))

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
            raise IntegrationError("Slack error response: " + results.get("error", ""))

    def get_ts_from_file_upload_results(self, file_upload_results):
        """
        Extract ts from file.upload json results.
        :param file_upload_results:
        :return:
        """
        file_ts = None
        file_data = file_upload_results.get("file")
        if file_data:
            shares = file_data.get("shares")
            if shares:
                channel_upload_data = None

                if shares.get("private"):
                    channel_upload_data = shares.get("private").get(self.get_channel_id())
                elif shares.get("public"):
                    channel_upload_data = shares.get("public").get(self.get_channel_id())
                else:
                    return channel_upload_data  # no other type supported

                first_data_entry = channel_upload_data[0]
                if first_data_entry:
                    file_ts = first_data_entry.get("ts")

        return file_ts

    def _get_channel_parent_message_history(self, cursor=None):
        """
        Method returns only parent messages from a conversation.

        "conversations.history" function supports pagination. Need to call "conversations.history" method with no
        latest or oldest arguments, and then continue paging using the cursor. Cursor-based pagination will
        make it easier to incrementally collect information. To begin pagination, specify a limit value under 1000.
        Slack recommends no more than 200 results at a time.
        :return: list of parent messages
        """
        parent_messages_list = []
        has_more_results = True
        while has_more_results:
            results = self.slack_client.api_call(
                "conversations.history",
                channel=self.get_channel_id(),
                limit=200,
                cursor=cursor
            )
            LOG.debug(results)

            if not results.get("ok"):
                raise IntegrationError("Slack error response: " + results.get("error", ""))

            has_more_results, cursor = self._get_next_cursor_for_next_page(results)
            parent_messages_list.extend(results.get("messages"))

        return parent_messages_list

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
            raise IntegrationError("Slack error response: " + results.get("error", ""))

    def get_channel_complete_history(self):
        """
        Method will return the entire conversation history, parent messages (with attachments) and their threads.

        "conversations.history" returns all parent messages (including Slack attachments!). Based on all parent messages
        timestamp IDs we call "conversations.replies" function to load their threads (without Slack attachments). If
        there are no replies then the single parent message referenced by "ts" will return.

        "conversations.history" function returns only parent messages but "conversations.replies"
        function returns the entire thread (the parent message plus all the thread replies), need to be careful not to
        duplicate messages.

        History loads from the newest to the oldest.
        :return: JSON result
        """
        parent_messages_list = self._get_channel_parent_message_history()

        history = []

        for parent_msg in parent_messages_list:
            history.append(parent_msg)  # always append the parent

            # if parent doesn't have replies skip to the next one
            if not parent_msg.get("replies"):
                continue

            # load the thread
            thread_messages_list = self._get_channel_thread_message_history(parent_msg.get("ts"))
            for msg in thread_messages_list:
                # exclude parent msg by comparing "ts" and "thread_ts"
                if msg.get("ts") != msg.get("thread_ts"):
                    # append parent's replies only
                    history.append(msg)

        return history

    def _get_channel_thread_message_history(self, msg_ts, cursor=None):
        """
        Method returns the entire thread (the parent message plus all the thread replies).

        "conversations.replies" function supports pagination. Cursor-based pagination will make it easier to
        incrementally collect information. To begin pagination, specify a limit value under 1000.
        Slack recommends no more than 200 results at a time.
        :return: list of entire thread (parent plus reply) messages
        """
        thread_messages_list = []
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

            if not results.get("ok"):
                raise IntegrationError("Slack error response: " + results.get("error", ""))

            has_more_results, cursor = self._get_next_cursor_for_next_page(results)
            thread_messages_list.extend(results.get("messages"))

        return thread_messages_list

    def get_user_display_name(self, user_id):
        """
        This method returns user's display name.
        If you want to maintain a mapping of display names and user IDs, look for the display_name
        listed under profile.
        :param user_id:
        :return: user display name or None if there isn't one
        """
        display_name = None

        user = self._get_user_info(user_id)
        if user.get("profile"):
            display_name = user.get("profile").get("display_name")

        if not display_name:
            return user.get("name")

        return display_name

    def _get_user_info(self, user_id):
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
            raise IntegrationError("Slack error response: " + results.get("error", ""))

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
                number = 1
                for message in messages:
                    if message.get("type") == "message":

                        # 1 get the username
                        subtype = message.get("subtype")
                        if subtype == "bot_message":
                            username = message["username"]  # Bot's name is stored in "username" property
                            # FIXME! Bot's username to be deprecated
                        else:
                            username = self.get_user_display_name(message.get("user"))

                        # 2 does msg have replies
                        # files, parent msg and threads behave differently
                        # if there was a reply on the thread it will include "reply_count" property
                        # but not all parent msg have "reply_count" property
                        # we can establish whether this is a parent or a child msg by comparing "ts" and "thread_ts"
                        ts = message.get("ts")
                        thread_ts = message.get("thread_ts")

                        is_msg_parent = False
                        if thread_ts is None or thread_ts == ts:
                            is_msg_parent = True

                        reply_count = message.get("reply_count")

                        # 3 get the timestamp
                        msg_time = readable_datetime(float(message.get("ts")), False)

                        # 4 get the text message
                        text, pretext = "", ""
                        attachments = message.get("attachments")
                        if not attachments:
                            text = message.get("text")
                        else:
                            at = attachments[0]
                            pretext = at.get("pretext") if at else ""
                            text = at.get("text") if at else ""

                        file_permalink, file_name = "", ""
                        file_uploads = message.get("files")
                        if file_uploads:
                            f = file_uploads[0]  # only one in the list
                            file_permalink = f.get("permalink") if f else ""
                            file_name = f.get("name") if f else ""

                        # 4 write in a temp file
                        data = data_for_template(number, username, reply_count, msg_time, pretext, text, file_permalink, file_name, is_msg_parent)
                        output_data = map_values(archive_template, data)

                        temp_file.write(output_data.encode('utf-8'))
                        number += 1

                temp_file.close()
                new_attachment = self._post_attachment_to_resilient(res_client, incident_id, task_id, temp_file)

            except ValueError as err:
                raise err
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
        try:
            new_attachment = res_client.post_attachment(attachment_uri, temp_file.name, filename=attachment_name, mimetype='text/plain')
        except Exception as ex:
            raise ValueError("Failed to post the {} attachment: {}".format(attachment_name, ex))

        return new_attachment

    def archive_channel(self):
        """
        Function sets the channel to archive.
        :return:
        """
        results = self.slack_client.api_call(
            "conversations.archive",
            channel=self.get_channel_id()
        )
        LOG.debug(results)
        return results
        #return {"ok": True}  # TODO archiving turned off for easier testing

    def get_channel_type(self):
        """
        Return channels status as str.
        :return:
        """
        if self.is_channel_private():
            return "Private"
        else:
            return "Public"

    def create_row_in_datatable(self, res_client, incident_id, task_id, conversation_url):
        """
        Create an association, a 1 to 1 connection, between res_id and slack_channel_id -a  row in Resilient datatable.
        :param res_client:
        :param incident_id:
        :param task_id:
        :param conversation_url:
        :return:
        """
        # Get current time (*1000 as API does not accept int)
        now = int(time.time() * 1000)

        # Create res_id
        res_id = generate_res_id(incident_id, task_id)

        # URL might not always be available
        permalink = """<a href="{0}">Link</a>""".format(conversation_url) if conversation_url else "N/A"

        # Generate cells for the datatable
        cells = {
            "cells": {
                "slack_db_time": {"value": now},
                "slack_db_res_id": {"value": res_id},
                "slack_db_channel": {"value": self.get_channel_name()},
                "slack_db_channel_type": {"value": self.get_channel_type()},
                "slack_db_permalink": {"value": permalink}
            }
        }

        # Generate uri to POST datatable row
        uri = "/incidents/{0}/table_data/{1}/row_data?handle_format=names".format(incident_id, DATA_TABLE_API_NAME)

        try:
            # POST row
            res_client.post(uri, cells)
            self.add_warning("Row was added to {} datatable".format(DATA_TABLE_API_NAME))
        except Exception as ex:
            raise ValueError("Failed to add row to {} datatable: {}".format(DATA_TABLE_API_NAME, ex))

    def get_file_attachment_data(self, res_client, incident_id, artifact_id, task_id, attachment_id):
        """
        Call the Resilient REST API to get the specific attachment content, type and title.
        :param res_client:
        :param incident_id:
        :param artifact_id:
        :param task_id:
        :param attachment_id:
        :return:
        """

        if incident_id and artifact_id:
            content_uri = "/incidents/{}/artifacts/{}/contents".format(incident_id, artifact_id)
            data_uri = "/incidents/{}/artifacts/{}".format(incident_id, artifact_id)
        elif attachment_id:
            if task_id:
                content_uri = "/tasks/{}/attachments/{}/contents".format(task_id, attachment_id)
                data_uri = "/tasks/{}/attachments/{}".format(task_id, attachment_id)
            elif incident_id:
                content_uri = "/incidents/{}/attachments/{}/contents".format(incident_id, attachment_id)
                data_uri = "/incidents/{}/attachments/{}".format(incident_id, attachment_id)
            else:
                raise ValueError("task_id or incident_id must be specified with attachment")
        else:
            raise ValueError("artifact or attachment or incident id must be specified")

        try:
            # Get the attachment content and data
            content = res_client.get_content(content_uri)
            attachment_data = res_client.get(data_uri)
            self.add_warning("Attachment file retrieved")
            return content, attachment_data
        except Exception as ex:
            raise ValueError("Failed to get attachment from Resilient: {}".format(ex))


def build_payload(ordered_data_dict):
    """
    Build the payload string based on the different types of data created.
    :param ordered_data_dict:
    :return: payload string
    """
    payload = ""

    for key, value in ordered_data_dict.items():

        input_type = value.get("type")
        input_data = value.get("data")

        if input_type == 'string' and input_data:
            payload += "\n"
            matches = re.findall(r"u'(.*?)'", input_data)  # extract data from u'[u\\'Malware\\', u\\'Lost PC / laptop / tablet\\']'
            if matches:
                data = ", ".join(matches)
                payload += u'*{}*: {}'.format(key, data)
            else:
                payload += u'*{}*: {}'.format(key, input_data)

        elif input_type == 'richtext' and input_data:
            cleaned_data = clean_html(input_data)
            if len(cleaned_data) > 0:
                payload += "\n"
                payload += u'*{}*: {}'.format(key, cleaned_data)

        elif input_type == 'datetime' and input_data:
            payload += "\n"
            payload += '*{}*: `<!date^{}^{{date_num}} {{time_secs}}|{}>`'.format(key, input_data/1000, readable_datetime(input_data), True)  # send epoch in seconds to Slack

        elif input_type == 'boolean' and input_data:
            payload += "\n"
            payload += '*{}*: {}'.format(key, build_boolean(input_data, true_value='Yes', false_value='No'))

        elif input_data:
            raise IntegrationError("Invalid type: " + input_type)

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
        # slack_text.replace("\\n", "") - cleanup for json.loads
        # object_pairs_hook=OrderedDict - JSON object decoded with an ordered list of pairs
        # strict=False - control characters will be allowed inside strings
        ordered_data = json.loads(slack_text.replace("\\n", ""), object_pairs_hook=collections.OrderedDict, strict=False)
        LOG.debug(ordered_data)

        resilient_url_dict = ordered_data.pop("Resilient URL", None)  # get the "Resilient URL" and delete it from the dict
        url = None
        if resilient_url_dict and resilient_url_dict.get("type") == "incident" and resilient_url_dict.get("data"):
            url = build_incident_url(build_resilient_url(resoptions['host'], resoptions['port']), resilient_url_dict.get("data"))

        additional_text_dict = ordered_data.pop("Additional Text", None)  # get the "Additional Text" and delete it from the dict
        pretext = None
        if additional_text_dict and additional_text_dict.get("type") == "string" and additional_text_dict.get("data"):
            pretext = additional_text_dict.get("data")

        type_data_dict = ordered_data.pop("Type of data", None)  # get the "Type of data" and delete it from the dict
        type_data = None
        if type_data_dict and type_data_dict.get("type") == "string" and type_data_dict.get("data"):
            type_data = type_data_dict.get("data")

        payload = build_payload(ordered_data)
        LOG.debug(payload)

        attachment_json = [
                {
                    "pretext": pretext,
                    "fallback": "Resilient {}".format(type_data),
                    "title": "Resilient {}".format(type_data),
                    "title_link": url,
                    "text": payload,
                    "color": "#36a64f"
                }
            ]
        return attachment_json
    except ValueError:
        raise ValueError


def get_template_file_path(path):
    """
    Get template file path.
    :param path:
    :return:
    """
    if not isinstance(path, string_types):
        raise ValueError("Variable 'path' type must be a string {}".format(path))

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


def data_for_template(number, username, reply_count, msg_time, msg_pretext, msg_text, file_permalink, file_name, is_msg_parent):
    """
    Prepare the dictionary of substitution values for jinja template
    :param number
    :param username:
    :param reply_count:
    :param msg_time:
    :param msg_pretext:
    :param msg_text:
    :param file_permalink:
    :param file_name:
    :param is_msg_parent:
    :return:
    """
    data = {
        "number": number,
        "username": username,
        "reply_count": reply_count,
        "msg_time": msg_time,
        "msg_pretext": msg_pretext,
        "msg_text": msg_text,
        "file_permalink": file_permalink,
        "file_name": file_name,
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
    try:
        datatable = ConversationsDatatable(res_client, incident_id)
        datatable.get_data()
        return datatable.get_slack_channel_name(incident_id, task_id)
    except ValueError as err:
        raise err


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
            self.rows = self.data.get("rows")
        except Exception as ex:
            raise ValueError("Failed to get {} datatable: {}".format(DATA_TABLE_API_NAME, ex))

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
            cells = row.get("cells")
            slack_db_res_id = cells.get("slack_db_res_id")
            res_id = slack_db_res_id.get("value") if slack_db_res_id else None
            if res_id is None:
                raise ValueError("{} datatable is missing 'slack_db_res_id' column".format(DATA_TABLE_API_NAME))

            if res_id_to_search == res_id:
                slack_db_channel = cells.get("slack_db_channel")
                if slack_db_channel:
                    return slack_db_channel.get("value")
        return None


def generate_res_id(incident_id, task_id=None):
    """
    If incident_id and task_id are valid, returns "RES-1001-2002"
    Else if task_id is None, returns "RES-1001"
    :param incident_id:
    :param task_id:
    :return:
    """
    res_id = [RES_PREFIX, str(incident_id)]
    if task_id is not None:
        res_id.append(str(task_id))
    return "-".join(res_id)
