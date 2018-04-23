# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import datetime
import logging
import json

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_slack.lib.errors import IntegrationError
from fn_slack.lib.resilient_common import clean_html, build_incident_url, build_resilient_url
from slackclient import SlackClient
from six import string_types

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'slack_post_message"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_slack", {})
        self.resoptions = opts.get("resilient", {})
        self.log = logging.getLogger(__name__)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_slack", {})
        self.resoptions = opts.get("resilient", {})

    @function("slack_post_message")
    def _slack_post_message_function(self, event, *args, **kwargs):
        """Function: Create a Slack message based on an incident. All summary and detail information about an Incident are presented"""
        try:
            # Get the function parameters:
            slack_channel = kwargs.get("slack_channel")  # text
            slack_details = kwargs.get("slack_details")  # text
            slack_thread_id = kwargs.get("slack_thread_id")  # text
            slack_reply_broadcast = self.get_select_param(kwargs.get("slack_reply_broadcast"))

            self.log.info("slack_channel: %s", slack_channel)
            self.log.info("slack_details: %s", slack_details)
            self.log.info("slack_thread_id: %s", slack_thread_id)
            self.log.info("slack_reply_broadcast: %s", slack_reply_broadcast)

            data = json.loads(slack_details)

            # configuration specific parameters
            api_token = self.options['api_token']
            as_user = self.options['username']

            sl = SlackClient(api_token)

            for key,val in data.items():
                self.log.info("%s %s", key, val)

            payload = self._build_payload(data)

            self.log.info(payload)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")
            results = sl.api_call(
                "chat.postMessage",
                channel=slack_channel,
                text=payload,
                as_user="false",
                username=as_user,
                reply_broadcast=slack_reply_broadcast
            )

            self.log.info(results) # todo

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()

    def _build_payload(self, dataDict):
        """
        build the payload string based on the different types of data created
        :param dataDict:
        :return: payload string
        """
        payload = ""

        for key, valDict in dataDict.items():
            if len(payload) > 0:
                payload += "\n"

            if valDict['type'] == 'string':
                payload += '{}: {}'.format(key, valDict['data'])

            elif valDict['type'] == 'incident':
                payload += '{}: {}'.format(key, self._buildIncident(valDict['data']))

            elif valDict['type'] == 'richtext':
                payload += '{}: {}'.format(key, clean_html(valDict['data']).strip())

            elif valDict['type'] == 'datetime':
                payload += '{}: {}'.format(key, self._buildTimeStamp(valDict['data']))

            elif valDict['type'] == 'boolean':
                payload += '{}: {}'.format(key, self._buildBoolean(valDict['data'], true_value='Yes', false_value='No'))

            else:
                raise IntegrationError("Invalid type: %s", key)

        return payload

    def _buildIncident(self, id):
        return build_incident_url(build_resilient_url(self.resoptions['host'], self.resoptions['port']), id)

    def _buildTimeStamp(self, ts):
        return datetime.datetime.utcfromtimestamp(ts/1000).strftime('%Y-%m-%dT%H:%M:%SZ')

    def _buildBoolean(self, value, true_value="True", false_value="False"):
        if isinstance(value, string_types):
            return true_value if value.lower() in ('1', 'yes', 'true') else false_value
        if isinstance(value, int):
            return true_value if value == 1 else false_value

        return false_value
