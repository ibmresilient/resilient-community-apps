# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_slack.lib.slack_common import *
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
        """Function: Function exports conversation history from Slack channel to a text file,
            saves the text file as an attachment and archives the Slack channel. """

        try:
            validate_fields(['api_token', 'username'], self.options)
            validate_fields(['incident_id'], kwargs)

            # Get the function parameters:
            incident_id = kwargs.get('incident_id')  # number (required)
            task_id = kwargs.get('task_id')  # number (optional)

            LOG.info('incident_id: %s', incident_id)
            LOG.info('task_id: %s', task_id)

            # configuration specific slack parameters
            api_token = self.options['api_token']
            def_username = self.options['username']

            # Initialize SlackClient
            slack_utils = SlackUtils(api_token)
            # Initialize Resilient API object
            res_client = self.rest_client()

            # Use the incident/task associated channel (the default channel).
            res_associated_channel_name = slack_channel_name_datatable_lookup(res_client, incident_id, task_id)
            LOG.debug("slack_channel name is associated with Incident or Task: %s", res_associated_channel_name)

            # Channel name validation - At this point channel needs to be defined
            if res_associated_channel_name is None:
                raise FunctionError("There is no slack_channel name associated with Incident or Task available to be archived")

            slack_utils.find_channel_by_name(res_associated_channel_name)
            if slack_utils.get_channel() is None:
                raise FunctionError(
                    "There is no private or public channel named {} in your workspace".format(res_associated_channel_name))

            if slack_utils.is_channel_archived():
                raise FunctionError(
                    "Channel {} is already marked as archived".format(res_associated_channel_name))
            else:
                yield StatusMessage(
                    "Found channel #{} with id {}".format(res_associated_channel_name, slack_utils.get_channel_id()))

            # notify the channel that we are going to archive
            text = "This channel has been set to be archived from Resilient."
            results_msg_posted = slack_utils.slack_post_message(None, text, None, None, None, def_username)
            if results_msg_posted.get("ok"):
                yield StatusMessage("Message warning 'Channel is set to be archived' was added to Slack.")
            else:
                raise FunctionError("Posting message for archiving channel failed: " + json.dumps(results_msg_posted))

            # get the channel history
            messages = slack_utils.get_channel_complete_history()

            # Saving conversation history to a text file and post it as attachment
            yield StatusMessage("Saving conversation history to a text file")
            new_attachment = slack_utils.save_conversation_history_as_attachment(res_client, messages, incident_id, task_id)
            if new_attachment is not None:
                yield StatusMessage("Channel's chat history was uploaded as an attachment")
            else:
                raise FunctionError("Failed creating an attachment")

            # Archive channel
            archive_results = slack_utils.archive_channel()
            if archive_results.get("ok"):
                yield StatusMessage("Channel {} has been archived".format(res_associated_channel_name))
            else:
                raise FunctionError("Archiving channel failed: " + json.dumps(archive_results))

            results = {"channel": res_associated_channel_name}
            LOG.info(results)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            LOG.error(err)
            yield FunctionError()
