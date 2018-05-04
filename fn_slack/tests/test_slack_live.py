# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
from fn_slack.components.slack_common import *
import logging
import os
import unittest
import simplejson as json

api_token = os.environ['TEST_RESILIENT_SLACK_API_TOKEN']
def_username = "Resilient"
slack_channel = "test-this-channel"

class TestSlack(unittest.TestCase):
    # pipenv run python -m unittest discover tests
    url = None

    def setUp(self):
        self.resoptions = {
            'host': 'localhost',
            'port': '443',
        }
        self.log = logging.getLogger(__name__)

    def tearDown(self):
        pass

    def test1_build_payload(self):
        dataDict = self._buildDataDetails()

        payload = build_payload(dataDict, self.resoptions)
        #self.log.info(payload)

        self.assertIsNotNone(payload)
        self.assertRegexpMatches(payload, 'Resilient URL')

    def test2_post(self):
        """
        channel=slack_channel,
        text=payload,
        as_user=slack_as_user,
        username=slack_user_id if slack_user_id else def_username,
        reply_broadcast=slack_reply_broadcast,
        parse=slack_parse,
        link_names=slack_link_names,
        mrkdown=slack_markdown,
        thread_ts=slack_thread_id
        def slack_post_message(log, resoptions, slack_details, slack_channel, slack_as_user, slack_user_id, slack_reply_broadcast,
                       slack_parse, slack_link_names, slack_markdown, slack_thread_id, api_token, def_username):
        """
        dataDict = self._buildDataDetails()

        results = slack_post_message(self.log, self.resoptions, json.dumps(dataDict), slack_channel, True, False, True,
                                     True, True, True, None, api_token, def_username)

        self.assertTrue(results['ok'], results)

        # send the reply
        thread_id = results['ts']
        results = slack_post_message(self.log, self.resoptions, json.dumps(dataDict), slack_channel, True, False, True,
                                     True, True, True, thread_id, api_token, def_username)

        self.assertTrue(results['ok'], results)
        self.assertEqual(thread_id, results['message']['thread_ts'])

    def _buildDataDetails(self):
        return {
  "Resilient Incident": {"type": "string", "data": "title here" },
  "Resilient URL": {"type": "incident", "data": "1234" },
  "Description": {"type": "richtext", "data": "<div>data<div>" },
  "Confirmed": {"type": "boolean", "data": "true" },
  "Create Date": {"type": "datetime", "data": 1525356259000 },
  "Start Date": {"type": "datetime", "data": 1525356259000 },
  "Severity": {"type": "string", "data": "low" },
  "NIST Vectors": {"type": "string", "data": "[Email, Malware]" },
  "Incident Types": {"type": "string", "data": "[Phishing]" }
        }