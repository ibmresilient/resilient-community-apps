# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

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

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_slack", {})
        self.resoptions = opts.get("resilient", {})

    @function("slack_post_attachment")
    def _slack_post_attachment(self, event, *args, **kwargs):
        """Function:
        """
        try:
            validate_fields(['api_token'], self.options)
            validate_fields(['incident_id', 'attachment_id'], kwargs)

            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number (required)
            task_id = kwargs.get("task_id")  # number (optional)
            artifact_id = kwargs.get("artifact_id")  # number (optional)
            attachment_id = kwargs.get("attachment_id")  # number (required)

            LOG.info("incident_id: %s", incident_id)
            LOG.info("task_id: %s", task_id)
            LOG.info("artifact_id: %s", artifact_id)
            LOG.info("attachment_id: %s", attachment_id)

            # configuration specific slack parameters
            api_token = self.options['api_token']

            # Initialize SlackClient
            slack_utils = SlackUtils(api_token)
            # Initialize Resilient API object
            res_client = self.rest_client()

            # Use the incident/task associated channel (the default channel).
            res_associated_channel_name = slack_channel_name_datatable_lookup(res_client, incident_id, task_id)
            LOG.debug("slack_channel name associated with Incident: %s", res_associated_channel_name)

            # Channel name validation - At this point channel needs to be defined
            if res_associated_channel_name is None:
                raise FunctionError("There is no slack_channel name associated with Incident or Task. There is no channel available to post attachments in.")

            slack_utils.find_channel_by_name(res_associated_channel_name)
            if slack_utils.get_channel() is None:
                raise FunctionError(
                    "There is no private or public channel named {} in your workspace. ".format(
                        res_associated_channel_name))

            if slack_utils.is_channel_archived():
                raise FunctionError(
                    "Channel {} is already marked as archived.".format(res_associated_channel_name))
            else:
                yield StatusMessage(
                    "Found channel #{} with id {}".format(res_associated_channel_name, slack_utils.get_channel_id()))

            # Get the the attachment from Incident or Task
            attachment_content, attachment_data = get_file_attachment_data(res_client, incident_id, artifact_id, task_id, attachment_id)
            yield StatusMessage("Attachment file retrieved.")

            # Upload file to Slack
            results = slack_utils.slack_post_attachment(attachment_content, attachment_data)

            if results.get("ok"):
                yield StatusMessage("Attachment uploaded to Slack.")
            else:
                raise FunctionError("File upload failed: " + json.dumps(results))

            results = {"channel": res_associated_channel_name,
                       "channel_id": results.get("channel")}

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            LOG.error(err)
            yield FunctionError()
