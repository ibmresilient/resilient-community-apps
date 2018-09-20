# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

import logging
import simplejson as json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_slack.lib.resilient_common import validate_fields
import slack_common
import tempfile
import datetime
import os

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
            slack_utils = slack_common.SlackUtils(api_token)

            # get the channel history in json format
            # find the channel
            slack_utils.find_channel_by_name(slack_channel_name)
            yield StatusMessage("Found channel #{} with id {}".format(slack_channel_name, slack_utils.get_channel_id()))

            # load history
            messages = slack_utils.get_channel_history(None)

            # Saving conversation history to a text file
            yield StatusMessage("Saving conversation history to a text file.")
            new_attachment = slack_utils.save_conversation_history_as_attachment(messages, self.rest_client(),
                                                                                 incident_id, task_id)

            # If the attachment succeeded in POSTing, print message, return result
            if new_attachment is not None:
                yield StatusMessage('Chat log was uploaded as an attachment for {}'.format(new_attachment['id']))
                #yield FunctionResult({'attachment_id': new_attachment['id']})

            # Else, raise an error
            else:
                yield StatusMessage('Failed creating attachment')
                raise FunctionError(u'Failed creating attachment')


            # # notify the channel that we are going to archive
            # sc.api_call("chat.postMessage", channel="#" + channel_name,
            #             text="This channel has been set to be archived from Resilient")
            #
            # # set the channel to archive
            # sc.api_call("channels.archive", channel=channel_id)

            yield StatusMessage("Integration has completed")

            results = {}  # FIXME create a Note in the postprocess script?

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            LOG.error(err)
            yield FunctionError()
