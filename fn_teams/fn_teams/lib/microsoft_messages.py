# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

""" Helper function for funct_ms_teams_post_message"""
import json, logging
import pymsteams
from urllib import parse

from resilient_lib import build_resilient_url, build_incident_url, build_task_url
from resilient_lib import IntegrationError, MarkdownParser
from fn_teams.lib import constants, microsoft_commons


class MessageClient:
    """
        This application allows for posting Incident/Task details to a MS Teams channel.
        The application can be triggered from either incident or task level where,
        information about the incident or task is formulated and posted in a convenient
        manner. This information is posted to a channel specified by the teams_channel
        input. This channel name (specified by teams_channel) is used to lookup
        app.config to retrieve the appropriate channel webhook url.

        Args:
        -----
            rc <obj> : request_common object from AppFunctionComponent
        
        Returns:
        --------
            status  <bool> : True/False
    """
    def __init__(self, rc):
        self.rc  = rc
        self.log = logging.getLogger(__file__)


    def post_message(self, options, **kwargs):
        """
        This method is responsible for the construction and sending of the message

        options:  (options from app.conf file)
        --------
            host <str> : Host URL of the SOAR Instance
            port <int> : Port number 

        kwargs:
        -------
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

        if task_id:
            incident_url = build_task_url(
                build_resilient_url(
                    options.get('host'),
                    options.get('port')),
                org_id=org_id,
                task_id=task_id,
                incident_id=incident_id)
            case_type = constants.TASK.title()

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


    def read_messages(self, dual_headers, options):
        """
        The Graph API's read message method is one of Microsoft's protected APIs since
        it has access to sensitive data. The user must grant this application permission
        to access their data in order for this application to function. This means that
        only the resources to which the user has access, such as channels and teams, will
        be available to this application. This feature allows to read all of the messages
        on the channel or the replies to a specific message. The function can retrieve all
        replies to a certain message if it is given the message id for that message. The
        function will dump all messages in that channel back into SOAR if the channel name
        attribute is given. 

        options:
        --------
            message_id             <str> : Id of the message who's replies are to be retrieved
            channel_id             <str> : Id of the channel, the message belongs
            group_id               <str> : Id of the group, the channel belongs
            channel_name           <str> : Name of the MS Channel to be deleted
            ms_description         <str> : Description for the Channel
            ms_group_mail_nickname <str> : Mail nickname for the group (Must be unique)
            ms_group_name          <str> : Name of the Microsoft Group

        Returns:
        --------
            Response <dict> : A response with all the messages of a channel or the replies
                              to a particular message and all information related to it,
                              or an error message from the MS Graph api if the operation
                              fails
        """
        response_handler = microsoft_commons.ResponseHandler()

        if "message_id" in options:
            url = parse.urljoin(
                constants.BASE_URL,
                constants.URL_CHANNEL_MSG_REPLY.format(
                    options.get("group_id"),
                    options.get("channel_id"),
                    options.get("message_id")))

        else:
            channel_finder = microsoft_commons.MSFinder(
                rc=self.rc,
                rh=response_handler,
                headers=dual_headers.get("application"))
            channel = channel_finder.find_channel(options)

            url = parse.urljoin(
                constants.BASE_URL,
                constants.URL_CHANNEL_MSG.format(
                    channel.get("group_id"),
                    channel.get("id")))

        response = self.rc.execute(
            "get",
            url=url,
            headers=dual_headers.get("delegated"),
            callback=response_handler.check_response)

        self.log.info(response)
        return response.get("value")
