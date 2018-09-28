# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Function implementation to Slack.
This function creates a Slack message based on a Resilient incident and it's notes. Threaded replies are possible based on a retained Slack thread_id.
Many of the features of posting a Slack message are under customer control including:
- threaded replies
- preserving embedded links
- Slack markdown capability
- posting messages displaying authorship
"""

import logging
import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_slack.lib.resilient_common import validate_fields
from fn_slack.lib.slack_common import SlackUtils

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
        """Function: Create a Slack message based on an incident. Threaded replies are possible based on a retained slack thread_id.
        All the fields to send to slack are sent in slack_details. A json structure is used to know how to interpret field meanings. A
        structure can look like this with conversions based on the 'type' key/value pair
        {
          "Resilient Incident": {"type": "string", "data": "plain text here"},
          "Resilient URL": {"type": "incident", "data": "123"},
          "Description": {"type": "richtext", "data": "<div>text here</div>"},
          "Confirmed": {"type": "boolean", "data": "1"},
          "Start Date": {"type": "datetime", "data": 158949393}
        }

        The remaining input fields are passed to the slack api call to control the message post.
        Refer to the slack api documentation on how to use the parameters.
        """
        try:
            # validate input
            validate_fields(['slack_channel', 'slack_details', 'slack_reply_broadcast'], kwargs)
            validate_fields(['api_token', 'username'], self.options)

            # Get the function parameters:
            slack_channel_name = kwargs.get("slack_channel")  # text
            slack_is_private = kwargs.get("slack_is_channel_private")  # Boolean
            slack_participant_emails = kwargs.get("slack_participant_emails")  # text
            slack_details = kwargs.get("slack_details")  # text
            slack_reply_broadcast = kwargs.get("slack_reply_broadcast") # Boolean
            slack_mrkdown = kwargs.get("slack_mrkdwn")  # Boolean
            slack_parse = kwargs.get("slack_parse")  # Boolean
            slack_as_user = kwargs.get("slack_as_user")   # Boolean
            slack_username = kwargs.get("slack_username")  # text

            LOG.debug("slack_channel: %s", slack_channel_name)
            LOG.debug("slack_details: %s", slack_details)
            LOG.debug("slack_is_private: %s", slack_details)
            LOG.debug("slack_participant_emails: %s", slack_participant_emails)
            LOG.debug("slack_reply_broadcast: %s", slack_reply_broadcast)
            LOG.debug("slack_parse: %s", slack_parse)
            LOG.debug("slack_mrkdwn: %s", slack_mrkdown)
            LOG.debug("slack_as_user: %s", slack_as_user)
            LOG.debug("slack_username: %s", slack_username)

            # configuration specific slack parameters
            api_token = self.options['api_token']
            def_username = self.options['username']

            slack_utils = SlackUtils(api_token)
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

            results_msg_posted = slack_utils.slack_post_message(self.resoptions, slack_details, slack_as_user,
                                                                slack_username, slack_reply_broadcast, slack_parse,
                                                                slack_mrkdown, def_username)
            if results_msg_posted.get("ok"):
                yield StatusMessage("Message added to slack.")
            else:
                yield FunctionError("Message add failed: " + json.dumps(results_msg_posted))

            # generate a permalink URL to join this conversation
            conversation_url = slack_utils.get_permalink(results_msg_posted.get("ts"))

            results = {"channel": slack_channel_name,
                       "channel_id": results_msg_posted.get("channel"),
                       "conversation_url": conversation_url}

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            LOG.error(err)
            yield FunctionError()
