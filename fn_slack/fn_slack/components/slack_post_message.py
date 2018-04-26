# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import datetime
import logging
import simplejson as json

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_slack.lib.errors import IntegrationError
from fn_slack.lib.resilient_common import clean_html, build_incident_url, build_resilient_url, validateFields, groom
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

        self._init()

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_slack", {})
        self.resoptions = opts.get("resilient", {})

        self._init()

    def _init(self):
        # validate app.config
        validateFields(['api_token', 'username'], self.options)

    @function("slack_post_message")
    def _slack_post_message_function(self, event, *args, **kwargs):
        """Function: Create a Slack message based on an incident. All summary and detail information about an Incident are presented"""
        try:
            # validate input
            #validateFields(['slack_channel', 'slack_details', 'slack_reply_broadcast'], kwargs)

            # Get the function parameters:
            slack_channel = kwargs.get("slack_channel")  # text
            slack_details = kwargs.get("slack_details")  # text
            slack_thread_id = kwargs.get("slack_thread_id")  # text
            slack_user_id = kwargs.get("slack_user_id")  # text
            slack_reply_broadcast = self.get_select_param(kwargs.get("slack_reply_broadcast"))

            slack_markdown = self.get_select_param(kwargs.get("slack_markdwn"))  # select
            slack_parse = self.get_select_param(kwargs.get("slack_parse"))  # select
            slack_link_names = self.get_select_param(kwargs.get("slack_link_names"))   # select
            slack_as_user = self.get_select_param(kwargs.get("slack_as_user"))   # select

            self.log.info("slack_channel: %s", slack_channel)
            self.log.info("slack_details: %s", slack_details)
            self.log.info("slack_thread_id: %s", slack_thread_id)
            self.log.info("slack_reply_broadcast: %s", slack_reply_broadcast)
            self.log.info("slack_parse: %s", slack_parse) #todo
            self.log.info("slack_markdwn: %s", slack_markdown) #todo
            self.log.info("slack_link_names: %s", slack_link_names) #todo
            self.log.info("slack_as_user: %s", slack_as_user) #todo
            self.log.info("slack_user_id: %s", slack_user_id) #todo

            data = json.loads(slack_details.replace("\\n", ""), strict=False)  # cleanup for json.loads

            # configuration specific parameters
            api_token = self.options['api_token']
            def_username = self.options['username']

            sl = SlackClient(api_token)

            payload = self._build_payload(data)
            self.log.info(payload)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")
            results = sl.api_call(
                "chat.postMessage",
                channel=slack_channel,
                text=payload,
                as_user=slack_as_user,
                username=slack_user_id if slack_user_id else def_username,
                reply_broadcast=slack_reply_broadcast,
                parse=slack_parse,
                link_names=slack_link_names,
                mrkdown=slack_markdown,
                thread_ts=slack_thread_id
            )

            self.log.info(results)

            if 'ok' in results.keys() and results['ok']:
                yield StatusMessage("Message added to slack")
            else:
                yield FunctionError("Message add failed: "+json.dumps(results))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            self.log.error(err)
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

            if valDict['type'] == 'string' and valDict['data']:
                payload += '{}: {}'.format(key, valDict['data'])

            elif valDict['type'] == 'incident' and valDict['data']:
                payload += '{}: {}'.format(key, self._buildIncident(valDict['data']))

            elif valDict['type'] == 'richtext' and valDict['data']:
                payload += '{}: {}'.format(key, clean_html(valDict['data']))

            elif valDict['type'] == 'datetime' and valDict['data'] and valDict['data'] != 0:
                payload += '{}: {}'.format(key, self._buildTimeStamp(valDict['data']))

            elif valDict['type'] == 'boolean' and valDict['data']:
                payload += '{}: {}'.format(key, self._buildBoolean(valDict['data'], true_value='Yes', false_value='No'))

            elif valDict['data']:
                raise IntegrationError("Invalid type: "+ valDict['type'])

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

    def _buildRichText(self, data):
        return html2text.html2text(html.unescape(data))


