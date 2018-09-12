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
import simplejson as json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_slack.lib.resilient_common import validate_fields
import slack_common


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'slack_post_message"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_slack", {})
        self.resoptions = opts.get("resilient", {})
        self.log = logging.getLogger(__name__)

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

        The remaining input fields are passed to the slack api call to control the message post. Refer to the slack api documentated
        on how to use the parameters
        """
        try:
            # validate input
            validate_fields(['slack_channel', 'slack_details', 'slack_reply_broadcast'], kwargs)
            validate_fields(['api_token', 'username'], self.options)

            # Get the function parameters:
            slack_channel = kwargs.get("slack_channel")  # text
            slack_is_private = kwargs.get("slack_is_channel_private")  # Boolean
            slack_participant_emails = kwargs.get("slack_participant_emails")  # text
            slack_details = kwargs.get("slack_details")  # text
            slack_thread_id = kwargs.get("slack_thread_id")  # text
            slack_user_id = kwargs.get("slack_user_id")  # text
            slack_reply_broadcast = kwargs.get("slack_reply_broadcast") # Boolean
            slack_mrkdown = kwargs.get("slack_mrkdwn")  # Boolean
            slack_parse = kwargs.get("slack_parse")  # Boolean
            slack_link_names = kwargs.get("slack_link_names")   # Boolean
            slack_as_user = kwargs.get("slack_as_user")   # Boolean

            self.log.debug("slack_channel: %s", slack_channel)
            self.log.debug("slack_details: %s", slack_details)
            self.log.debug("slack_is_private: %s", slack_details)
            self.log.debug("slack_participant_emails: %s", slack_participant_emails)
            self.log.debug("slack_thread_id: %s", slack_thread_id)
            self.log.debug("slack_reply_broadcast: %s", slack_reply_broadcast)
            self.log.debug("slack_parse: %s", slack_parse)
            self.log.debug("slack_mrkdwn: %s", slack_mrkdown)
            self.log.debug("slack_link_names: %s", slack_link_names)
            self.log.debug("slack_as_user: %s", slack_as_user)
            self.log.debug("slack_user_id: %s", slack_user_id)

            # configuration specific slack parameters
            api_token = self.options['api_token']
            def_username = self.options['username']

            # find or create a new channel
            slack_client = slack_common.SlackUtils(api_token)
            slack_id_channel = None

            if not slack_client.find_channel_by_name(slack_channel):
                # rewrite the slack_channel name just in case Slack validation modifies the submitted channel name
                slack_channel, slack_id_channel = slack_client.slack_create_channel(slack_channel, slack_is_private)

            # find id channel, based on the channel name
            if not slack_id_channel:
                slack_id_channel = slack_client.find_id_channel_by_name(slack_channel)

            # find user id based on their emails
            user_id_list = slack_client.find_user_ids(slack_participant_emails)

            # invite users to a channel
            results_users_added = slack_client.invite_users_to_channel(slack_id_channel, user_id_list)

            if "ok" in results_users_added and results_users_added.get("ok"):
                yield StatusMessage("Users invited to #{} channel".format(slack_channel))
            elif "ok" in results_users_added and not results_users_added.get("ok") \
                    and results_users_added.get("error") == "already_in_channel":
                yield StatusMessage("Invited user is already in #{} channel".format(slack_channel))
            else:
                yield FunctionError("Invite users failed: " + json.dumps(results_users_added))

            # post message to the channel
            results_msg_posted = slack_client.slack_post_message(self.resoptions, slack_details, slack_channel,
                                                                 slack_as_user, slack_user_id, slack_reply_broadcast,
                                                                 slack_parse, slack_link_names, slack_mrkdown,
                                                                 slack_thread_id, def_username)

            if "ok" in results_msg_posted and results_msg_posted.get("ok"):
                yield StatusMessage("Message added to slack")
            else:
                yield FunctionError("Message add failed: "+json.dumps(results_msg_posted))

            # Produce a FunctionResult with the results
            yield FunctionResult(results_msg_posted)
        except Exception as err:
            self.log.error(err)
            yield FunctionError()

