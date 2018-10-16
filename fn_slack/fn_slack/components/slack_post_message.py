# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Function implementation to Slack.
This function creates a Slack message based on a Resilient incident, it's tasks, notes and artifacts.

Many of the features of posting a Slack message are under customer control including:
- Creating private or public channels
- Inviting users to conversations
- posting messages displaying authorship
"""

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_slack.lib.slack_common import *
import warnings

LOG = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'slack_post_message"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_slack", {})
        self.resoptions = opts.get("resilient", {})

        self._init()

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_slack", {})
        self.resoptions = opts.get("resilient", {})

        self._init()

    def _init(self):
        # validate app.config
        validate_fields(['api_token', 'username'], self.options)

    @function("slack_post_message")
    def _slack_post_message_function(self, event, *args, **kwargs):
        """Function: Create a Slack message based on an incident, task, note or an artifact data.
        All the fields to send to slack are sent in slack_text. A json structure is used to know how to interpret field meanings. A
        structure can look like this with conversions based on the 'type' key/value pair
        {
          "Resilient Incident": {"type": "string", "data": "plain text here"},
          "Resilient URL": {"type": "incident", "data": "123"},
          "Description": {"type": "richtext", "data": "<div>text here</div>"},
          "Confirmed": {"type": "boolean", "data": "1"},
          "Start Date": {"type": "datetime", "data": 158949393}
        }

        Default settings for posting messages are:
        - parse="full", full parse mode, Slack will linkify URLs, channel names (starting with a '#') and usernames (starting with an '@').
        - link_names=1, find and link channel names by mentioning users with their user ID '<@U123>'. On by default.
                        FIXME! Soon to be deprecated!
                        Slack apps and their bot users should not use the username field when authoring a message.
                        The username is part of your app's configuration and will not always be settable at runtime.

        Threading isn't supported (reply_broadcast and thread_ts are None).

        The remaining input fields are passed to the slack api call to control the message post.
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

            LOG.debug("incident_id: %s", incident_id)
            LOG.debug("task_id: %s", task_id)
            LOG.debug("slack_channel: %s", input_channel_name)
            LOG.debug("slack_text: %s", slack_text)
            LOG.debug("slack_is_private: %s", slack_is_private)
            LOG.debug("slack_participant_emails: %s", slack_participant_emails)
            LOG.debug("slack_mrkdwn: %s", slack_mrkdown)
            LOG.debug("slack_as_user: %s", slack_as_user)
            LOG.debug("slack_username: %s", slack_username)

            # configuration specific slack parameters
            api_token = self.options['api_token']
            def_username = self.options['username']

            # Initialize SlackClient
            slack_utils = SlackUtils(api_token)
            # Initialize Resilient API object
            res_client = self.rest_client()

            with warnings.catch_warnings(record=True) as warning_messages:
                warnings.simplefilter("always", UserWarning)
                # Find or create a channel
                # ------------------------
                slack_channel_name, has_association_in_slack_db = \
                    slack_utils.find_or_create_channel(input_channel_name, slack_is_private, res_client, incident_id,
                                                       task_id)
                # Check the warning message and yield StatusMessage.
                for w in warning_messages:
                    usr_msg = w.message
                    if usr_msg and usr_msg.message:
                        yield StatusMessage(usr_msg.message)

            user_id_list = None
            with warnings.catch_warnings(record=True) as warning_messages:
                warnings.simplefilter("always", UserWarning)
                # Find user ids based on their emails
                # -----------------------------------
                if slack_participant_emails:
                    user_id_list = slack_utils.find_user_ids_based_on_email(slack_participant_emails)
                    # Check the warning message and yield StatusMessage.
                    for w in warning_messages:
                        usr_msg = w.message
                        if usr_msg and usr_msg.message:
                            yield StatusMessage(usr_msg.message)

            if user_id_list:
                with warnings.catch_warnings(record=True) as warning_messages:
                    warnings.simplefilter("always", UserWarning)
                    # Add users to the channel
                    # ------------------------
                    slack_utils.invite_users_to_channel(user_id_list)
                    # Check the warning message and yield StatusMessage.
                    for w in warning_messages:
                        usr_msg = w.message
                        if usr_msg and usr_msg.message:
                            yield StatusMessage(usr_msg.message)

            results_msg_posted = slack_utils.slack_post_message(self.resoptions, slack_text, slack_as_user,
                                                                slack_username, slack_mrkdown, def_username)
            if results_msg_posted.get("ok"):
                yield StatusMessage("Message added to Slack.")
            else:
                raise FunctionError("Message add failed: " + json.dumps(results_msg_posted))

            # generate a permalink URL to join this conversation
            conversation_url = slack_utils.get_permalink(results_msg_posted.get("ts"))

            if has_association_in_slack_db is False:
                with warnings.catch_warnings(record=True) as warning_messages:
                    warnings.simplefilter("always", UserWarning)
                    # Create an association if there isn't one
                    # ----------------------------------------
                    slack_utils.create_row_in_datatable(res_client, incident_id, task_id, conversation_url)
                    # Check the warning message and yield StatusMessage.
                    for w in warning_messages:
                        usr_msg = w.message
                        if usr_msg and usr_msg.message:
                            yield StatusMessage(usr_msg.message)

            results = {"channel": slack_channel_name,
                       "url": conversation_url}

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            LOG.error(err)
            yield FunctionError()
