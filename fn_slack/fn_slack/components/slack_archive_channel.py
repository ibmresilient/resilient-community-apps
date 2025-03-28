# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Function implementation to Slack.
This function exports conversation history to a text file,
saves it as an Attachment in Resilient and archives Slack channel.
"""

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import RequestsCommon
from fn_slack.lib.slack_common import *

LOG = logging.getLogger(__name__)
SLACK_SECTION_HDR = "fn_slack"

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'slack_close_channel"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get(SLACK_SECTION_HDR, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get(SLACK_SECTION_HDR, {})

    @function("slack_archive_channel")
    def _slack_archive_channel_function(self, event, *args, **kwargs):
        """Function: Function exports conversation history from Slack channel to a text file,
            saves the text file as an Attachment and archives the Slack channel. """
        try:
            validate_fields(['api_token', 'username'], self.options)
            validate_fields(['incident_id'], kwargs)

            # Get the function parameters:
            incident_id = kwargs.get('incident_id')  # number (required)
            task_id = kwargs.get('task_id')  # number (optional)
            channel_id = kwargs.get('slack_channel_id') # test (optional)

            LOG.info('incident_id: %s', incident_id)
            LOG.info('task_id: %s', task_id)
            LOG.info('channel_id: %s', channel_id)

            # configuration specific slack parameters
            api_token = self.options['api_token']
            def_username = self.options['username']

            # get proxies if they exist
            rc = RequestsCommon(opts=self.opts, function_opts=self.options)

            # Initialize SlackClient
            slack_utils = SlackUtils(api_token, proxies=rc.get_proxies())
            # Initialize Resilient API object
            res_client = self.rest_client()

            # Use the incident/task associated channel (the default channel).
            res_associated_channel_name = slack_channel_name_datatable_lookup(res_client, incident_id, task_id)
            LOG.debug("slack_channel name is associated with Incident or Task: %s", res_associated_channel_name)

            # Channel name validation - At this point channel needs to be defined
            if res_associated_channel_name is None:
                raise FunctionError("There is no slack_channel name associated with Incident or Task available to be archived")

            if not channel_id:
                channel = slack_utils.find_channel(res_associated_channel_name)
                channel_id = channel.get("id")
                channel_name = channel.get("name")
            else:
                channel = slack_utils.check_channel_id(channel_id)
                channel_name= channel.get("name")

            if channel is None:
                raise FunctionError(
                    u"There is no private or public channel named {} in your workspace".format(res_associated_channel_name))

            if slack_utils.is_channel_archived():
                raise FunctionError(
                    u"Channel {} is already marked as archived".format(res_associated_channel_name))
            else:
                yield StatusMessage(
                    u"Found channel #{} with id {}".format(res_associated_channel_name, channel_id))

            # notify the channel that we are going to archive
            text = u"Slack channel {} has been set to be archived from Resilient.".format(res_associated_channel_name)
            results_msg_posted = slack_utils.slack_post_message(None, text, None, None, None, def_username, channel_id)
            if results_msg_posted.get("ok"):
                yield StatusMessage("Message warning 'Channel is set to be archived' was added to Slack.")
            else:
                raise FunctionError(u"Posting message for archiving channel failed: " + json.dumps(results_msg_posted))

            # get the channel history
            messages = slack_utils.get_channel_complete_history(channel_id)

            template_file = self.options.get('template_file', None)

            # Saving conversation history to a text file and post it as attachment
            new_attachment = slack_utils.save_conversation_history_as_attachment(res_client, messages, incident_id,
                                                                                task_id, channel_name, template_file=template_file)
            if new_attachment is not None:
                yield StatusMessage("Channel's chat history was uploaded as an Attachment")
            else:
                raise FunctionError("Failed creating an Attachment")

            # Archive channel
            archive_results = slack_utils.archive_channel(channel_id)
            if archive_results.get("ok"):
                yield StatusMessage(u"Channel {} has been archived".format(res_associated_channel_name))
            else:
                raise FunctionError(u"Archiving channel failed: " + json.dumps(archive_results))

            results = {"channel": res_associated_channel_name}
            LOG.info(results)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            LOG.error(err)
            yield FunctionError()
