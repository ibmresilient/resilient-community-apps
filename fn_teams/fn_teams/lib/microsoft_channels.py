# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, line-too-long, wrong-import-order
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.

''' Helper function for funct_ms_teams_create_teams'''

import json
import logging

from urllib import parse
from resilient_lib import IntegrationError

from fn_teams.lib import constants, microsoft_commons
from fn_teams.lib.microsoft_commons import ResponseHandler


class ChannelInterface:
    """
        An interface that allows for creating MS Channels for an MS Team or deleting
        an existing channel from an MS Team. An MS Team can have multiple channels.

        required_parameters:
        --------------------
            rc               <obj> : request_common object from AppFunctionComponent
            headers          <dct> : Request header generated during Authentication
            response_handler <obj> : Handler for endpoint responses
    """

    def __init__(self, required_parameters):
        self.rc = required_parameters.get("rc")
        self.log = logging.getLogger(__file__)
        self.headers = required_parameters.get("header")
        self.response_handler = ResponseHandler()
        self.proxies = self.rc.get_proxies()


    def create_channel(self, options):
        """
        A MS Team can have multiple channels. This function can be used to add a Channel
        to an existing MS Team. Here a request is formulated and posted to the Microsoft
        Graph API for channel creation. To create a Channel for an MS Team, 4 key
        attributes are required, namely: teamId, displayName, description, and
        membershipType. Out of these attributes, teamId is crucial as the MS Team must be
        properly identified before channel addition operation can take place. The MSFinder
        class from microsoft_commons is being used. A team or a group can be located using
        any one of the 3 mentioned attributes.

            -> group_id
            -> group_mail_nickname
            -> group_name

        Note: If multiple options are provided to locate the Graph Object then
        ms_group_mail_nickname supersedes group_name and group_id supersedes the
        other two options.

        options:
        --------
            displayName         <str> : Name of the MS Channel to be created
            description         <str> : Description of the Channel being created
            group_mail_nickname <str> : Mail nickname for the group (Must be unique)
            group_name          <str> : Name of the Microsoft Group
            group_id            <str> : The group unique Id

        one of group_name_nickname, group_name or group_id is required


        Returns:
        --------
            Response <dict> : A response with the details of the team that was archived or
                              unarchived, or an error message from the MS Graph api if the
                              operation fails
        """

        group_finder = microsoft_commons.MSFinder(
            rc=self.rc,
            rh=self.response_handler,
            headers=self.headers)
        group_id = group_finder.find_group_id(options)

        url = parse.urljoin(
            constants.BASE_URL,
            constants.URL_LIST_CHANNEL.format(group_id))

        body = {
            "displayName": options.get("displayName"),
            "description": options.get("description"),
            "membershipType": constants.CHANNEL_MEMBERSHIP_TYPE}

        body = json.dumps(body, indent=2)
        self.log.debug("Request body for Channel creation")
        self.log.debug(body)

        response = self.rc.execute(
            method="post",
            url=url,
            data=body,
            headers=self.headers,
            proxies=self.proxies,
            callback=self.response_handler.check_response)

        if response.get("status_code") == 201:
            response["message"] = constants.INFO_SUCCESSFULLY_CREATED_CHANNEL.format(
                options.get("displayName"))
            return response

        raise IntegrationError(constants.ERROR_COULDNOT_CREATE_CHANNEL)


    def delete_channel(self, options):
        """
        A MS Team can have multiple channels. This function can be used to delete a Channel
        of an existing MS Team. Here a request is formulated and posted to the Microsoft
        Graph API for channel deletion. To delete a Channel for an MS Team, 2 key
        attributes are required, namely: channelId and groupID/teamID. The MSFinder
        class from microsoft_commons is being used. The MSFinder has a find_channel method
        that allows for locating a channel and extracting its channel Id. To located the
        group or team for which the channel is associated, one of the following options
        can be used:

            -> group_id
            -> group_mail_nickname
            -> group_name

        Note: If multiple options are provided to locate the Graph Object then
        ms_group_mail_nickname supersedes ms_group_name and group_id supersedes the
        other two options.

        options:
        --------
            channel_name        <str> : Name of the MS Channel to be deleted
            group_id            <str> : The group unique Id
            group_mail_nickname <str> : Mail nickname for the group (Must be unique)
            group_name          <str> : Name of the Microsoft Group

        Returns:
        --------
            Response <dict> : A response with the details of the team that was archived or
                              unarchived, or an error message from the MS Graph api if the
                              operation fails
        """

        channel_finder = microsoft_commons.MSFinder(
            rc=self.rc,
            rh=self.response_handler,
            headers=self.headers)
        channel = channel_finder.find_channel(options)

        url = parse.urljoin(
            constants.BASE_URL,
            constants.URL_LOCATE_CHANNEL.format(
                channel.get("group_id"),
                channel.get("id")))

        response = self.rc.execute(
            method="delete",
            url=url,
            headers=self.headers,
            proxies=self.proxies,
            callback=self.response_handler.check_response)

        if response.get("status_code") == 204:
            response["message"] = (constants
                .INFO_SUCCESSFULLY_DELETED_CHANNEL
                .format(channel.get("displayName")))
            return response

        raise IntegrationError(constants.ERROR_COULDNOT_DELETE_CHANNEL)
