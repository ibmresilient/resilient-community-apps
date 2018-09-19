# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

import logging
import simplejson as json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_slack.lib.resilient_common import validate_fields
import slack_common
import csv
import datetime

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

            # Get the function parameters:
            slack_channel_name = kwargs.get("slack_channel")  # text

            LOG.debug("slack_channel: %s", slack_channel_name)

            # configuration specific slack parameters
            api_token = self.options['api_token']

            slack_utils = slack_common.SlackUtils(api_token)
            res_client = self.rest_client()

            # get the channel history in json format
            # find the channel
            slack_utils.find_channel_by_name(slack_channel_name)
            yield StatusMessage("Found channel #{} with id {}".format(slack_channel_name, slack_utils.get_channel_id()))

            results = slack_utils.get_channel_history()
            if results.get("ok"): #FIXME pagination!!!
                yield StatusMessage("Channel history accessed.")
            else:
                yield FunctionError("Getting channel history failed: " + json.dumps(results))

            # create a csv file for us to put the JSON from slack in
            file_name = "slack_msg_export_" + slack_channel_name + ".csv"
            with open(file_name, mode='w') as slack_csv_file:
                csv_writer = csv.writer(slack_csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

                yield StatusMessage("Archiving conversation history to CSV")
                # For each msg in the history, parse
                for message in results.get("messages"):
                    # get the username
                    if message.get("type") == "message":
                        subtype = message.get("subtype")
                        if subtype == "bot_message":
                            username = message["username"] #FIXME is it really username, cannot find this in Slack API doc
                        else:
                            username = slack_utils.get_user_info(message.get("user")).get("name")

                        # get the timestamp
                        msg_ts = datetime.datetime.utcfromtimestamp(float(message.get("ts")))
                        msg_time = msg_ts.strftime("%Y-%m-%d %H:%M:%S")

                        # get the text message
                        msg_text = message.get("text")
                    else:
                        yield StatusMessage("Skipping message as not message.")

                    # write that message output to the csv file
                    csv_row = [msg_time.encode('utf-8'), msg_text.encode('utf-8'), username.encode('utf-8')]
                    csv_writer.writerow(csv_row)

            # # Save csv as an attachment - FIXME use utils for saving attachments!
            # yield StatusMessage("Chat log has been uploaded for " + str(inc_id))
            # res_client.post_attachment('/incidents/' + str(inc_id) + '/attachments', f_name)

            # clean up after myself and delete the chatlog
            # os.remove(f_name)

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
