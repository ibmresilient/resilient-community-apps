# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
"""Function implementation"""

import logging
import pymsteams
import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, build_incident_url, build_resilient_url, ResultPayload, RequestsCommon, \
    MarkdownParser

SECTION_NAME = "fn_teams"
HEADERS = {"Content-Type":"application/json"}
TASK_FRAGMENT = "?task="
TIMEOUT = 60

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'teams_post_message"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get(SECTION_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get(SECTION_NAME, {})

    @function("teams_post_message")
    def _teams_post_message_function(self, event, *args, **kwargs):
        """Function: Post a message to a Microsoft Teams channel"""
        try:
            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            validate_fields(['incident_id', 'teams_channel', 'teams_payload'], kwargs)

            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            task_id = kwargs.get("task_id")  # number
            teams_channel = kwargs.get("teams_channel")  # text
            teams_payload = kwargs.get("teams_payload")  # text
            teams_mrkdown = kwargs.get("teams_mrkdown", False)  # boolean

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            log.info("task_id: %s", task_id)
            log.info("teams_channel: %s", teams_channel)
            log.info("teams_payload: %s", teams_payload)
            log.info("teams_mrkdown: %s", teams_mrkdown)

            yield StatusMessage("starting...")
            result_payload = ResultPayload(SECTION_NAME, **kwargs)

            # get the webhook for the channel
            webhook = self.options.get(teams_channel)
            if not webhook:
                raise ValueError("Unable to find channel: %s in app.config", teams_channel)

            request_common = RequestsCommon(self.opts)

            payload_json = json.loads(teams_payload.replace("\n", "").replace("None", "null"))

            proxies = request_common.get_proxies()
            card = pymsteams.connectorcard(webhook, http_proxy=proxies['http'] if proxies else None,
                                           https_proxy=proxies['https'] if proxies else None,
                                           http_timeout=TIMEOUT)

            self.build_conversation(card,
                                    incident_id, task_id, payload_json, teams_mrkdown)
            card.send()

            yield StatusMessage("done...")

            results = result_payload.done(True, None)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()


    def build_conversation(self, card,
                           incident_id, task_id, teams_payload, teams_mrkdow):
        """
        build the message card format used to post to teams webhooks
        :param card:
        :param incident_id:
        :param task_id:
        :param teams_payload: json formatted data
        :param teams_mrkdow: true/false to support markdown format
        :return: formatted card for transmission
        """

        incident_url = build_incident_url(build_resilient_url(self.opts['host'], self.opts['port']), incident_id)
        type = 'Incident'

        # build url back to resilient
        if task_id:
            incident_url = "{}{}{}".format(incident_url, TASK_FRAGMENT, task_id)
            type = 'Task'

        # url back to resilient
        card.addLinkButton("Resilient {}".format(type), incident_url)

        if teams_payload.get("title"):
            card.title(teams_payload.get("title"))

        mrkdown = MarkdownParser()

        card.text(mrkdown.convert(teams_payload.get("summary", "-None-")))

        for section in teams_payload.get("sections", []):

            cardsection = pymsteams.cardsection()
            if teams_mrkdow:
                cardsection.enableMarkdown()

            if section.get("title"):
                cardsection.title(teams_payload.get("title"))

            if section.get("text"):
                cardsection.text(section.get("text"))

            for fact in section.get("facts", []):
                cardsection.addFact(fact.get("name"), fact.get("value"))

            card.addSection(cardsection)

        return card
