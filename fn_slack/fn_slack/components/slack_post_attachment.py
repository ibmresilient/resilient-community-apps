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
        """Function: Function uploads Incident, Task or Artifact attachment to Slack channel.
            FIXME - You can upload files as bot user with Bot User Token!"""
        try:
            validate_fields(['api_token'], self.options)
            validate_fields(['incident_id', 'attachment_id'], kwargs)

            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number (required)
            task_id = kwargs.get("task_id")  # number (optional)
            artifact_id = kwargs.get("artifact_id")  # number (optional)
            attachment_id = kwargs.get("attachment_id")  # number (required)
            input_channel_name = kwargs.get("slack_channel")  # text (optional)
            slack_is_private = kwargs.get("slack_is_channel_private")  # Boolean (optional)
            slack_participant_emails = kwargs.get("slack_participant_emails")  # text (optional)
            slack_text = kwargs.get("slack_text")  # text (optional)

            LOG.info("incident_id: %s", incident_id)
            LOG.info("task_id: %s", task_id)
            LOG.info("artifact_id: %s", artifact_id)
            LOG.info("attachment_id: %s", attachment_id)
            LOG.debug("slack_channel: %s", input_channel_name)
            LOG.debug("slack_text: %s", slack_text)
            LOG.debug("slack_is_private: %s", slack_is_private)
            LOG.debug("slack_participant_emails: %s", slack_participant_emails)

            # configuration specific slack parameters
            api_token = self.options['api_token']

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

            # Get the the attachment from Incident or Task
            attachment_content, attachment_data = get_file_attachment_data(res_client, incident_id, artifact_id, task_id, attachment_id)
            yield StatusMessage("Attachment file retrieved")

            # Upload file to Slack
            results = slack_utils.slack_post_attachment(attachment_content, attachment_data)

            if results.get("ok"):
                yield StatusMessage("Attachment uploaded to Slack")
            else:
                raise FunctionError("File upload failed: " + json.dumps(results))

            # find ts from file upload
            file_ts = slack_utils.get_ts_from_file_upload_results(results)

            # generate a permalink URL to join this conversation
            conversation_url = slack_utils.get_permalink(file_ts)

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
