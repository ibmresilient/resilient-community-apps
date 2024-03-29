# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Function implementation to Slack.
This function creates a Slack message based on a Resilient Incident, it's Tasks, Notes and Artifacts.

Many of the features of posting a Slack message are under customer control including:
- Creating private or public channels
- Inviting users to conversations
- Preserving embedded links
- Posting messages from Incidents, Notes, Artifacts and Tasks displaying authorship
- Slack user ID <@U345GHIJKL> and channel ID #C012ABCDE references
"""

from fn_slack.lib.slack_common import *
from resilient_circuits import (FunctionError, FunctionResult,
                                ResilientComponent, StatusMessage, function,
                                handler)
from resilient_lib import RequestsCommon

LOG = logging.getLogger(__name__)
SLACK_SECTION_HDR = "fn_slack"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'slack_post_message"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get(SLACK_SECTION_HDR, {})
        self.resoptions = opts.get("resilient", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get(SLACK_SECTION_HDR, {})
        self.resoptions = opts.get("resilient", {})

    @function("slack_post_message")
    def _slack_post_message_function(self, event, *args, **kwargs):
        """Function: Create a Slack message based on an Incident, Task, Note or an Artifact data.
        All the fields to send to Slack are sent in slack_text. A json structure is used to know how to interpret field
        meanings. A structure can look like this with conversions based on the 'type' key/value pair:

        {
          "Additional Text": {{"type": "string", "data": "My text message to post in Slack" }},
          "Resilient URL": {{"type": "incident", "data": 123 }},
          "Type of data": {{"type": "string", "data": "Incident" }},
          "Incident name": {"type": "string", "data": "plain text here"},
          "Description": {"type": "richtext", "data": "<div>text here</div>"},
          "Date Occurred": {"type": "boolean", "data": "1"},
          "Date Occurred": {"type": "datetime", "data": 158949393}
          ...
        }

        If channel_name is NOT specified as the function input, method will perform a lookup
        for associated channel_name in Slack Conversations Datatable. If there is an Incident or Task associated
        slack_channel, method will use found channel name and search for an existing channel in
        Slack Workspace (api call).

        If channel_name is specified as the function input, method will search for an existing channel in
        Slack Workspace (api call) or create a new Slack channel (api call), if it doesn't exist yet, with the
        specified channel_name.
        If channel_name is specified and there is also the associated channel found, method will ignore the associated
        one and post to the input one.

        Default settings for posting messages are:
        - parse="none", Slack will not perform any processing on the message, it will keep all markup formatting '<'
        - link_names=1, Slack will linkify URLs, channel names (starting with a '#') and username ids (starting with an '<@ user_id >')
                        Example of text to post in Slack: "Hey user <@UCNC5K34J> check out #random"
                        TODO Using link_names when posting messages to be deprecated
        Threading isn't supported (reply_broadcast and thread_ts are None).

        The remaining input fields are passed to the Slack api call to control the message post.
        Refer to the slack api documentation on how to use the parameters.
        """
        try:
            # validate input
            validate_fields(['incident_id', 'slack_text'], kwargs)
            validate_fields(['api_token', 'username'], self.options)

            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number (required)
            task_id = kwargs.get("task_id")  # number (optional)
            input_channel_name = kwargs.get("slack_channel")  # text (optional)
            slack_is_private = kwargs.get("slack_is_channel_private")  # Boolean (optional)
            slack_participant_emails = kwargs.get("slack_participant_emails")  # text (optional)
            slack_text = kwargs.get("slack_text")  # text (required)
            slack_mrkdown = kwargs.get("slack_mrkdwn")  # Boolean (optional)
            slack_as_user = kwargs.get("slack_as_user")   # Boolean (optional)
            slack_username = kwargs.get("slack_username")  # text (optional)
            channel_id = kwargs.get("slack_channel_id") # text (optional)

            LOG.debug("incident_id: %s", incident_id)
            LOG.debug("task_id: %s", task_id)
            LOG.debug("slack_channel: %s", input_channel_name)
            LOG.debug("slack_text: %s", slack_text)
            LOG.debug("slack_is_private: %s", slack_is_private)
            LOG.debug("slack_participant_emails: %s", slack_participant_emails)
            LOG.debug("slack_mrkdwn: %s", slack_mrkdown)
            LOG.debug("slack_as_user: %s", slack_as_user)
            LOG.debug("slack_username: %s", slack_username)
            LOG.debug("channel_id: %s", channel_id)


            # configuration specific slack parameters
            api_token = self.options['api_token']
            def_username = self.options['username']

            # get proxies if they exist
            rc = RequestsCommon(opts=self.opts, function_opts=self.options)

            # Initialize SlackClient
            slack_utils = SlackUtils(api_token, proxies=rc.get_proxies())
            # Initialize Resilient API object
            res_client = self.rest_client()

            # Find or create a channel
            slack_channel_name, has_association_in_slack_db = slack_utils.find_or_create_channel(
                input_channel_name, slack_is_private, res_client, incident_id, task_id, channel_id)

            # Add users to the channel
            if slack_participant_emails:
                # Find user ids based on their emails
                user_id_list = slack_utils.find_user_ids_based_on_email(slack_participant_emails)

                # invite users to a channel
                if user_id_list:
                    slack_utils.invite_users_to_channel(user_id_list, channel_id)

            # Post a message
            results_msg_posted = slack_utils.slack_post_message(self.resoptions, slack_text, slack_as_user,
                                                                slack_username, slack_mrkdown, def_username, channel_id)

            # Generate a permalink URL to join this conversation
            conversation_url = slack_utils.get_permalink(results_msg_posted.get("ts"), channel_id)

            # Create an association if there isn't one
            if has_association_in_slack_db is False:
                slack_utils.create_row_in_datatable(res_client, incident_id, task_id, conversation_url)

            users_list = slack_utils.get_channel_users_list(channel_id)
            user_info = slack_utils.get_users_info(users_list)

            # Yield Status Messages
            for warn in slack_utils.get_warnings():
                yield StatusMessage(warn)


            results = {
                        "channel": slack_channel_name,
                        "url": conversation_url,
                        "user_info" : user_info
                    }

            LOG.info(results)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            LOG.error(err)
            yield FunctionError()
