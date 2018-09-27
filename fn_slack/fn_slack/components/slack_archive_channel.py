# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_slack.lib.resilient_common import validate_fields
from fn_slack.lib.slack_common import SlackUtils
import json

LOG = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'slack_close_channel"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_slack", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_slack", {})

    @function("slack_archive_channel")
    def _slack_archive_channel_function(self, event, *args, **kwargs):
        """Function: Function exports conversation history from given Slack channel to a csv file,
        saves the csv file as an attachment and archives the Slack channel. """

        try:
            validate_fields(['api_token'], self.options)
            validate_fields(['incident_id'], kwargs)

            # Get the function parameters:
            slack_channel_name = kwargs.get("slack_channel")  # text
            incident_id = kwargs.get('incident_id')  # number (required)
            task_id = kwargs.get('task_id')  # number (optional)

            LOG.debug("slack_channel: %s", slack_channel_name)
            LOG.info('incident_id: %s', incident_id)
            LOG.info('task_id: %s', task_id)

            # configuration specific slack parameters
            api_token = self.options['api_token']
            def_username = self.options['username']

            # find the channel
            slack_utils = SlackUtils(api_token)
            slack_utils.find_channel_by_name(slack_channel_name)
            if slack_utils.get_channel() is None:
                yield FunctionError(
                    "There is no private or public channel named {} in your workspace. ".format(slack_channel_name))

            if slack_utils.is_channel_archived():
                yield FunctionError(
                    "Channel {} is already marked as archived.".format(slack_channel_name))
            else:
                yield StatusMessage(
                    "Found channel #{} with id {}".format(slack_channel_name, slack_utils.get_channel_id()))

            # notify the channel that we are going to archive
            text = "This channel has been set to be archived from Resilient."
            results_msg_posted = slack_utils.slack_post_message(None, text, None, None, True, None, None, None, def_username)
            if results_msg_posted.get("ok"):
                yield StatusMessage("Message warning 'Channel is set to be archived' was added to Slack.")
            else:
                yield FunctionError("Posting message for archiving channel failed: " + json.dumps(results_msg_posted))

            # get the channel history
            messages = slack_utils.get_channel_complete_history()

            # Saving conversation history to a text file and post it as attachment
            yield StatusMessage("Saving conversation history to a text file.")
            new_attachment = slack_utils.save_conversation_history_as_attachment(messages, self.rest_client(),
                                                                                 incident_id, task_id)
            if new_attachment is not None:
                yield StatusMessage("Channel's chat history was uploaded as an attachment.")
            else:
                yield FunctionError("Failed creating an attachment.")

            # Archive channel
            results = slack_utils.archive_channel()
            if results.get("ok"):
                yield StatusMessage("Channel {} has been archived.".format(slack_channel_name))
            else:
                yield FunctionError("Archiving channel failed: " + json.dumps(results))

            results = {"channel": slack_channel_name}

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            LOG.error(err)
            yield FunctionError()
