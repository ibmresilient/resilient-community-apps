# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Function implementation to Slack.
This function creates a Slack message based on a Resilient incident, it's tasks, notes and artifacts.

Many of the features of posting a Slack message are under customer control including:
- Creating private or public channels
- Inviting users to conversations
- Slack markdown capability
- posting messages displaying authorship
"""

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_slack.lib.slack_common import *

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
        """Function: Create a Slack message based on an incident, task, note or an artifact.
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

        Threading isn't supported (reply_broadcast and thread_ts are None).

        The remaining input fields are passed to the slack api call to control the message post.
        Refer to the slack api documentation on how to use the parameters.
        """
        try:
            # validate input
            validate_fields(['incident_id', 'slack_text'], kwargs)
            validate_fields(['api_token', 'username'], self.options)

            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            task_id = kwargs.get("task_id")  # number
            input_channel_name = kwargs.get("slack_channel")  # text
            slack_is_private = kwargs.get("slack_is_channel_private")  # Boolean
            slack_participant_emails = kwargs.get("slack_participant_emails")  # text
            slack_text = kwargs.get("slack_text")  # text
            slack_mrkdown = kwargs.get("slack_mrkdwn")  # Boolean
            slack_as_user = kwargs.get("slack_as_user")   # Boolean
            slack_username = kwargs.get("slack_username")  # text

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

            # If user doesn't specify a channel name, use the incident/task associated channel (the default channel).
            res_associated_channel_name = slack_channel_name_datatable_lookup(res_client, incident_id, task_id)
            LOG.debug("slack_channel name associated with Incident or Task: %s", res_associated_channel_name)

            # One more validation - channel needs to be defined
            if input_channel_name is None and res_associated_channel_name is None:
                yield FunctionError("Slack_channel name is missing or empty.")

            # Pick the right channel
            slack_channel_name = None
            if input_channel_name is None and res_associated_channel_name:
                slack_channel_name = res_associated_channel_name

            elif input_channel_name:
                if res_associated_channel_name:
                    yield StatusMessage("This incident/task has an association with Slack channel #{}, "
                                        "your message will be posted to a separate Slack channel #{}.".format(res_associated_channel_name, input_channel_name))
                slack_channel_name = input_channel_name

            # find or create a new channel
            slack_utils.find_channel_by_name(slack_channel_name)

            if slack_utils.get_channel():
                # validate if your input param 'slack_is_private' matches channel's type, if not stop the workflow
                if slack_is_private and not slack_utils.is_channel_private():
                    yield FunctionError("The existing channel #{} you are posting to is a public channel. "
                                        "To post to this channel please change the input parameter "
                                        "'slack_is_channel_private' "
                                        "to 'No' or create a new private channel.".format(slack_channel_name))
                elif not slack_is_private and slack_utils.is_channel_private():
                    yield FunctionError("The existing channel #{} you are posting to is a private channel. "
                                        "To post to this channel please change the input parameter "
                                        "'slack_is_channel_private' "
                                        "to 'Yes' or create a new public channel.".format(slack_channel_name))
                elif slack_utils.is_channel_archived():
                    yield FunctionError("Channel {} is archived.".format(slack_channel_name))
            else:
                # validate slack_is_private
                validate_fields(['slack_is_channel_private'], kwargs)

                # create a new channel
                slack_utils.slack_create_channel(slack_channel_name, slack_is_private)

                # rewrite slack_channel_name just in case Slack validation modifies the submitted channel name
                slack_channel_name = slack_utils.get_channel_name()

            if slack_participant_emails:
                # find user ids based on their emails
                user_id_list = []
                list_emails = slack_participant_emails.split(",")
                for email in list_emails:
                    email = email.strip()  # making sure to exclude ' ' or ''
                    if email:
                        results_user_id = slack_utils.lookup_user_by_email(email)

                        if results_user_id.get("ok") and results_user_id.get("user"):
                            user_id_list.append(results_user_id.get("user").get("id"))
                        elif not results_user_id.get("ok") and results_user_id.get("error", "") == "users_not_found":
                            yield StatusMessage("{} user is not a member of your workspace.".format(email))
                        else:
                            yield FunctionError("Invite users failed: " + json.dumps(results_user_id))

                if user_id_list:
                    # invite users to a channel
                    results_users_invited = slack_utils.invite_users_to_channel(user_id_list)

                    if results_users_invited.get("ok"):
                        yield StatusMessage("Users invited to #{} channel".format(slack_channel_name))
                    elif not results_users_invited.get("ok") and results_users_invited.get("error") == "already_in_channel":
                        yield StatusMessage("Invited user is already in #{} channel".format(slack_channel_name))
                    else:
                        yield FunctionError("Invite users failed: " + json.dumps(results_users_invited))

            results_msg_posted = slack_utils.slack_post_message(self.resoptions, slack_text, slack_as_user,
                                                                slack_username, slack_mrkdown, def_username)
            if results_msg_posted.get("ok"):
                yield StatusMessage("Message added to slack.")
            else:
                yield FunctionError("Message add failed: " + json.dumps(results_msg_posted))

            # Create a 1 to 1 connection between res_id and slack_channel_id if there isn't one
            if res_associated_channel_name is None:
                yield StatusMessage("Adding row to Slack conversations datatable")
                datatable_row = slack_utils.create_row_in_datatable(res_client, incident_id, task_id, results_msg_posted.get("ts"))
                if datatable_row is not None:
                    yield StatusMessage("Row was added to Slack conversations datatable")
                else:
                    yield FunctionError("Failed to add row to datatable.")

            results = {"channel": slack_channel_name,
                       "channel_id": results_msg_posted.get("channel")}

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            LOG.error(err)
            yield FunctionError()
