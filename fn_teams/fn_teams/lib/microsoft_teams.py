# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, line-too-long, wrong-import-order
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.

''' Helper function for funct_ms_teams_create_teams'''

import json
import re
import logging

from urllib import parse
from retry.api import retry_call
from resilient_lib import IntegrationError

from fn_teams.lib import constants, microsoft_commons
from fn_teams.lib.microsoft_commons import ResponseHandler


class TeamsInterface:
    '''
        An interface that allows for performing CRUD operations for MS Teams. While a
        MS Group is created using the MS Graph API, Teams functionality is disabled by
        default for that Group. To this functionality or to create an MS Team from
        scratch, this application can be used. This allows for creating a Team from
        scratch, enabling a Team for an existing MS Group, and Archiving, and unarchiving an
        existing Team.

        required_parameters:
        --------------------
            rc               <obj> : request_common object from AppFunctionComponent
            headers          <dct> : Request header generated during Authentication
            resclient        <obj> : Client that enables communication with SOAR
            response_handler <obj> : Handler for endpoint responses
    '''
    def __init__(self, required_parameters):
        self.users_not_found = []
        self.response_handler = ResponseHandler()
        self.rc = required_parameters["rc"]
        self.log = logging.getLogger(__file__)
        self.headers = required_parameters["header"]
        self.resclient = required_parameters["resclient"]
        self.proxies = self.rc.get_proxies()


    def _build_member_format(self, email_id, owner=False):
        """
        Builds the request body in the required format for the addition of members to the Team.
        The user is identified by his/her email and added to the team. The owner attribute
        specifies if the user is an owner or a member. The email address is firstly checked if
        it belongs to a valid user in the MS Endpoint. It is then used to construct the member
        request body.

        Args:
        -----
            email_id  <str> : Email address of the user
            owner    <bool> : Specifies if the user is an owner or a member of the group

        Returns:
        --------
            request_body <dict> : Request body for member addition
        """
        url = parse.urljoin(
            constants.BASE_URL,
            constants.URL_USERS.format(email_id))

        response = self.rc.execute(
            method="get",
            url=url,
            headers=self.headers,
            proxies=self.proxies,
            callback=self.response_handler.check_response)

        if "mail" in response:
            return {
                "@odata.type"     : "#microsoft.graph.aadUserConversationMember",
                "roles"           : ["owner"] if owner else [],
                "user@odata.bind" : parse.urljoin(
                    constants.BASE_URL,
                    constants.URL_USERS_QUERY.format("".join(["('", response.get("id"), "')"])))}
        if owner:
            raise IntegrationError(constants.WARN_DIDNOT_FIND_USER.format(email_id))

        self.users_not_found.append(email_id)
        self.log.warning(constants.WARN_DIDNOT_FIND_USER.format(email_id))


    def _get_all_emails(self, owners_list, task_id, incident_id, add_members_from, additional_members):
        """
        The function fetches all the user information from the SOAR incident or task and uses this
        information to add members to the Team that is being created. Since a SOAR incident or task
        only returns a user_id and not user details, this needs to be cross-referenced with the SOAR
        user DB for a valid email address. These email addresses are then used for adding members to the
        team.

        Args:
        -----
            task_id            <str> : If called from task then Task ID
            incident_id        <str> : Incident ID
            owners_list        <str> : List of owners email addresses
            add_members_from   <str> : Specifies if members to be added form incident or task
            additional_members <str> : List of email addresses of additional members to be added

        Returns:
        --------
            (owners_list, members_list) (<list>, <list>): email addresses
        """
        self.response_handler.add_exempt_codes(404)
        owners_list = owners_list.split(",") if owners_list else owners_list
        owners_list = [self._build_member_format(owner, True) for owner in owners_list]

        self.log.info("Successfully gathered Owners' information")

        _member_list = microsoft_commons.generate_member_list(
            resclient=self.resclient,
            task_id=task_id,
            incident_id=incident_id,
            add_members_from=add_members_from,
            additional_members=additional_members)

        member_list = []
        for member in _member_list:
            _user = self._build_member_format(member)
            if _user:
                member_list.append(_user)

        self.response_handler.clear_exempt_codes(default=True)
        self.log.info("Successfully gathered Users' information")
        return owners_list, member_list


    def _add_members(self, team_id, members):
        """
        Members are added after the team is created. This wrapper function allows for that.
        This uses the above two functions to formulate the add_members request body and then
        adds them. Members are added in bulk here. If a user email address does not exist
        in the MS Endpoint, only that user omitted and other users are added.

        Args:
        -----
            team_id <str> : Id of the team to which users are to be added
            members <list>: Request body list

        Returns:
        --------
            None

        """

        url = parse.urljoin(
                parse.urljoin(
                constants.BASE_URL,
                constants.URL_LOCATE_TEAM.format(team_id)),
                constants.URL_ADD_MEMBER_CONTEXT)
        self.log.debug(url)

        self.response_handler.set_return_raw(False)
        self.log.info("Adding members to the team {}".format(team_id))

        body = json.dumps({"values" : members}, indent=2)
        self.log.debug("Members Information")
        self.log.debug(body)

        response = self.rc.execute(
            method="post",
            url=url,
            data=body,
            headers=self.headers,
            proxies=self.proxies,
            callback=self.response_handler.check_response)

        self.log.debug(json.dumps(response, indent=2))


    def create_team(self, required_parameters):

        """
        Wrapper function that orchestrates the create team process. Firstly a MS Team
        is created with a MS Group, using the MS Teams' Graph API Backend. To this team
        SOAR users are added using their email addresses.

        required_parameters:
        -------------------
            task_id            <str> : If called from task then Task ID
            incident_id        <str> : Incident ID
            ms_team_name       <str> : Name of the Microsoft Team to be created
            ms_description     <str> : Description for the Team to be created
            ms_owners_list     <str> : List of owners email addresses
            add_members_from   <str> : Specifies if members to be added form incident or task
            additional_members <str> : List of email addresses of additional members to be added

        Returns:
        --------
            Response <dict> : A response with the room/team options and details
                              or the error message if the meeting creation
        """

        owners_email_list, members_email_list = self._get_all_emails(
            required_parameters.get("owners_list"),
            required_parameters.get("task_id"),
            required_parameters.get("incident_id"),
            required_parameters.get("add_members_from"),
            required_parameters.get("additional_members"))

        url = parse.urljoin(
            constants.BASE_URL,
            constants.URL_LIST_TEAMS)

        body = {
            "template@odata.bind" : parse.urljoin(
                constants.BASE_URL,
                constants.URL_TEAMS_STANDARD_TEMPLATE),
            "displayName" : required_parameters.get("displayName"),
            "description" : required_parameters.get("description"),
            "members"     : owners_email_list}
        body.update(
                constants.TEAMS_FROM_GROUP_CONFIGURATION)

        body = json.dumps(body, indent=2)

        self.log.debug("Request body for Team creation")
        self.log.debug(body)

        self.response_handler.add_empty_response_code(202)
        self.response_handler.set_return_raw(True)
        response = self.rc.execute(
            method="post",
            url=url,
            data=body,
            headers=self.headers,
            proxies=self.proxies,
            callback=self.response_handler.check_response)
        self.log.debug(response.raw.info())
        self.response_handler.set_return_raw(False)

        _team_id = (response
            .raw
            .info()
            .get("location"))
        if not _team_id:
            raise IndentationError(constants.ERROR_COULDNOT_CREATE_TEAM)
        _team_id = re.search(constants.TEAM_ID_REGEX, _team_id).group(1)

        if len(members_email_list) > 0:
            self._add_members(_team_id, members_email_list)

        group_finder = microsoft_commons.MSFinder(
            rc=self.rc,
            rh=self.response_handler,
            headers=self.headers)
        group_details = retry_call(
            group_finder.find_group,
            fargs=[{"group_id" : _team_id}],
            exceptions=IntegrationError,
            delay=3,
            backoff=2,
            tries=5)

        group_detail = group_details[0]
        group_detail.update({
            "teamsEnabled" : True,
            "unfoundUsers" : self.users_not_found if len(self.users_not_found) > 0 else None})
        return group_detail


    def enable_team_group(self, options):
        '''
        Creates a MS Team from an existing MS Group. Major attributes like the members, description
        etc, is inherited from the Group. While creating a MS Team, certain configurations are
        required and so the Microsoft recommended bare minimum settings is used create a team.
        These settings are available in the constants folder. To locate the group, one of the
        following inputs can be used:

            -> ms_group_id
            -> ms_group_mail_nickname
            -> ms_group_name

        Note: If multiple options are provided to locate the Graph Object then
        ms_group_mail_nickname supersedes ms_groupteam_name and ms_groupteam_id supersedes
        the other two options

        Inputs:
        -------
            ms_group_id            <str> : The unique Id generated while creating a group
            ms_group_mail_nickname <str> : Mail nickname for the group (Must be unique)
            ms_group_name          <str> : Name of the Microsoft Group

        Returns:
        --------
            Response <dict> : A response with the Team options and details
                              or the error message if the meeting creation
        '''
        group_finder = microsoft_commons.MSFinder(
            rc=self.rc,
            rh=self.response_handler,
            headers=self.headers)
        group_details = group_finder.find_group(options)

        if len(group_details) > 1:
            raise IntegrationError(constants.ERROR_FOUND_MANY_GROUP)

        group_id = group_details[0].get("id")

        url = parse.urljoin(
            constants.BASE_URL,
            constants.URL_TEAM_FROM_GROUP.format(group_id))

        self.log.debug(f"URL  {url}")
        self.log.debug(f"body {json.dumps(constants.TEAMS_FROM_GROUP_CONFIGURATION, indent=2)}")

        response = self.rc.execute(
            method="put",
            url=url,
            data=json.dumps(constants.TEAMS_FROM_GROUP_CONFIGURATION),
            headers=self.headers,
            proxies=self.proxies,
            callback=self.response_handler.check_response)

        self.log.debug(json.dumps(response))
        group_details = group_details[0]

        if response.get("status_code") == 201:
            group_details["message"] = constants.INFO_SUCCESSFULLY_ENABLED.format(
                group_details.get("displayName"))
            group_details.update({
                "teamsEnabled" : True})
        return group_details


    def archive_unarchive_team(self, options):
        '''
        Allows for archiving or unarchiving a MS Team for a MS Group. Archiving doesn't delete
        the MS Team. To locate the team, one of the following inputs can be used:

            -> group_id
            -> group_mail_nickname
            -> group_name

        Note: If multiple options are provided to locate the Graph Object then
        ms_group_mail_nickname supersedes group_name and group_id supersedes
        the other two options

        Inputs:
        -------
            operation           <str> : The operation to be performed (Archive/Unarchive)
            group_id            <str> : The unique Id generated while creating a group
            group_mail_nickname <str> : Mail nickname for the group (Must be unique)
            group_name          <str> : Name of the Microsoft Group

        Returns:
        --------
            Response <dict> : A response with the Team options and details
                              or the error message if the meeting creation
        '''
        operation = options.get("operation").lower().strip()
        group_finder = microsoft_commons.MSFinder(
            rc=self.rc,
            rh=self.response_handler,
            headers=self.headers)
        group_details = group_finder.find_group(options)
        team_id = group_details[0].get("id")

        url = None
        if operation == "archive":
            url = parse.urljoin(
                constants.BASE_URL,
                constants.URL_TEAMS_ARCHIVE.format(team_id))
        elif operation == "unarchive":
            url = parse.urljoin(
                constants.BASE_URL,
                constants.URL_TEAMS_UNARCHIVE.format(team_id))

        self.log.debug(f"URL {url}")

        self.response_handler.add_empty_response_code(202)
        response = self.rc.execute(
            method="post",
            url=url,
            headers=self.headers,
            proxies=self.proxies,
            callback=self.response_handler.check_response)
        self.response_handler.clear_empty_response_codes(default=True)

        group_details = group_details[0]

        if response.get("status_code") == 202:
            if operation == "archive":
                group_details["message"] = constants.INFO_SUCCESSFULLY_ARCHIVED.format(
                    group_details.get("displayName"))
                group_details["teamsEnabled"] = "Archived"
            else:
                group_details["message"] = constants.INFO_SUCCESSFULLY_UNARCHIVED.format(
                    group_details.get("displayName"))
                group_details["teamsEnabled"] = "Unarchived"
        return group_details

    def list_teams(self, team_filter: str):
        url = parse.urljoin(
            constants.BASE_URL,
            constants.URL_LIST_TEAMS)
        self.log.debug(url)

        params = {"$filter": team_filter} if team_filter else None

        response = self.rc.execute(
            method="get",
            url=url,
            headers=self.headers,
            proxies=self.proxies,
            params=params,
            callback=self.response_handler.check_response)

        return response

    def list_team_channels(self, team_id, team_filter):
        """GET /teams/{team-id}/allChannels"""
        url = parse.urljoin(
            constants.BASE_URL,
            constants.URL_LIST_TEAMS)
        url = f"{url}/{team_id}/allChannels"
        self.log.debug(url)

        params = {"$filter": team_filter} if team_filter else None

        response = self.rc.execute(
            method="get",
            url=url,
            headers=self.headers,
            proxies=self.proxies,
            params=params,
            callback=self.response_handler.check_response)

        return response
