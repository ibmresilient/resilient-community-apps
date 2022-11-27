# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

""" Helper function for funct_ms_teams_post_message"""
import json
import pymsteams
from urllib import parse

from resilient_lib import build_resilient_url, MarkdownParser, build_incident_url, build_task_url
from resilient_lib import IntegrationError
from fn_teams.lib import constants


class PostMessageClient:
    def __init__(self, rc, logger, **kwargs):
        """
        A pymsteams wrapper object that allows for posting incident or task
        information in a teams channel
        """
        self.rc  = rc
        self.log = logger


    def post_message(self, options, **kwargs):
        """
        This method is responsible for the construction and sending of the message

        options:  
        --------
            options from app.conf file
            host <str> : Host URL of the SOAR Instance
            port <int> : Port number 

        required_parameters:
        -------------------
            task_id       <str> : If called from task then Task ID
            incident_id   <str> : Incident ID
            teams_channel <str> : Name of the channel
            teams_payload <str> : The payload generated with incident/task details
            teams_mrkdown <bol> : Enables/Disables markdown formatting
            webhook_url   <str> : URL generated from a MS Teams channel, which enables
                                  this client to post message

        Returns:
        --------
            status       <bool> : True/False
         """
        teams_channel = kwargs.get("teams_channel")
        webhook_url   = kwargs.get("webhook_url")
        teams_payload = kwargs.get("teams_payload")

        if not webhook_url:
            raise IntegrationError(
                constants.ERROR_UNABLE_TO_FIND_CHANNEL.format(teams_channel))

        payload_json = json.loads(
            teams_payload.replace("\n", "").replace("None", "null"))

        self.log.info(json.dumps(teams_payload, indent=2))
        proxies = self.rc.get_proxies()

        card = pymsteams.connectorcard(
            webhook_url,
            http_proxy  = proxies.get('http')  if proxies else None,
            https_proxy = proxies.get('https') if proxies else None,
            http_timeout=constants.TIMEOUT)

        self.build_conversation(
            options,
            card,
            org_id=kwargs.get ("org_id"),
            task_id=kwargs.get("task_id"),
            incident_id=kwargs.get("incident_id"),
            teams_payload=payload_json,
            teams_mrkdown=kwargs.get("teams_mrkdown"))

        status = card.send()
        return status


    def build_conversation(self, options, card, **kwargs):
        """
        Constructs the message to be posted in the teams channel

        options:
        -------
            task_id       <str> : If called from task then Task ID
            incident_id   <str> : Incident ID
            teams_payload <str> : The payload generated with incident/task details
            teams_mrkdown <bol> : Enables/Disables markdown formatting

        card:
        -----
            card <pyteams.card> : Allows for establishing a connection
                                  with the MS Channel.

        Returns:
        --------
            card <pyteams.card> : A card object with the message body
         """
        org_id = kwargs.get("org_id")
        task_id = kwargs.get("task_id")
        incident_id = kwargs.get("incident_id")
        teams_payload = kwargs.get("teams_payload")
        teams_mrkdown = kwargs.get("teams_mrkdown")

        incident_url = build_incident_url( 
            build_resilient_url(
                options.get('host'),
                options.get('port')),
                orgId=org_id,
                incidentId=incident_id)
        case_type = constants.INCIDENT.title()

        # build url back to resilient

        if task_id:
            incident_url = build_task_url(
                build_resilient_url(
                    options.get('host'),
                    options.get('port')),
                org_id=org_id,
                task_id=task_id,
                incident_id=incident_id)
            case_type = constants.TASK.title()

        # url back to resilient
        card.addLinkButton(f"View {case_type}", incident_url)
        if teams_payload.get(constants.TITLE):
            card.title(teams_payload.get(constants.TITLE))

        mrkdown = MarkdownParser()
        card.text(mrkdown.convert(teams_payload.get("summary", "-None-")))

        for section in teams_payload.get("sections", []):

            cardsection = pymsteams.cardsection()
            if teams_mrkdown:
                cardsection.enableMarkdown()
            if section.get(constants.TITLE):
                cardsection.title(section.get(constants.TITLE))
            if section.get(constants.TEXT):
                cardsection.text(section.get(constants.TEXT))
            for fact in section.get("facts", []):
                cardsection.addFact(fact.get("name"), fact.get("value"))

            card.addSection(cardsection)
        return card

