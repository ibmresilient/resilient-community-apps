# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

''' Helper function for funct_ms_teams_create_teams'''

import json, re

from urllib import parse
from resilient_lib import IntegrationError

from fn_teams.lib import constants, microsoft_commons
from fn_teams.lib.microsoft_commons import ResponseHandler


class TeamsInterface:
    '''
        This application allows for creating a Microsoft Team using the Microsoft Graph API. This
        provides SOAR with the ability to create Teams from within a SOAR incident or a task. Teams
        can be created in two different ways:
                * Create Team using an existing MS Group
                * Create a Team from scratch

        Inputs:
        -------
            task_id                <str> : If called from task then Task ID
            incident_id            <str> : Incident ID
            ms_team_name           <str> : Name of the Microsoft Team to be created
            ms_owners_list         <str> : List of owners email addresses
            add_members_from       <str> : Specifies if members to be added form incident or task
            additional_mambers     <str> : List of email addresses of additional members to be added
            ms_team_description    <str> : Description for the Team to be created

        Returns:
        --------
            Response <dict> : A response with the room/team options and details
                              or the error message if the meeting creation
    '''
    def __init__(self, required_parameters):
        self.users_not_found = []
        self.response_handler = ResponseHandler()
        self.rc = required_parameters["rc"]
        self.log = required_parameters["logger"]
        self.headers = required_parameters["header"]
        self.resclient = required_parameters["resclient"]


    def _build_member_format(self, email_id, owner=False):
        url = parse.urljoin(
            constants.BASE_URL,
            constants.URL_USERS.format(email_id))

        response = self.rc.execute(
            method="get",
            url=url,
            headers=self.headers,
            callback=self.response_handler.check_response)

        if "mail" in response:
            return {
                "@odata.type"     : "#microsoft.graph.aadUserConversationMember",
                "roles"           : ["owner"] if owner else [],
                "user@odata.bind" : parse.urljoin(
                    constants.BASE_URL,
                    constants.URL_USERS_QUERY.format("".join(["('", response.get("id"), "')"])))
                }
        if owner:
            raise IntegrationError(constants.WARN_DIDNOT_FIND_USER.format(email_id))
        else:
            self.users_not_found.append(email_id)
            self.log.warn(constants.WARN_DIDNOT_FIND_USER.format(email_id))


    def _get_all_emails(self, owners_list, task_id, incident_id, add_members_from, additional_members):
        self.response_handler.add_exempt_codes(404)
        owners_list = owners_list.split(",") if owners_list else owners_list
        owners_list = [self._build_member_format(owner, True) for owner in owners_list]

        member_list = microsoft_commons.generate_member_list(
            self.resclient,
            self.log,
            task_id=task_id,
            incident_id=incident_id,
            add_members_from=add_members_from,
            additional_members=additional_members)

        member_list = [self._build_member_format(member) for member in member_list]
        self.response_handler.clear_exempt_codes(default=True)
        return owners_list, member_list


    def _add_members(self, team_id, members):

        self.log.info("Members Information")
        self.log.info(json.dumps(members, indent=2))

        url = parse.urljoin(
                parse.urljoin(
                constants.BASE_URL,
                constants.URL_LOCATE_TEAM.format(team_id)),
                constants.URL_ADD_MEMBER_CONTEXT)
        
        self.log.debug(url)

        self.response_handler.set_return_raw(False)
        self.log.info("Adding members to the team {}".format(team_id))

        body = json.dumps({"values" : members})

        response = self.rc.execute(
            method="post",
            url=url,
            data=body,
            headers=self.headers,
            callback=self.response_handler.check_response)

        self.log.debug(json.dumps(response, indent=2))


    def create_team(self, required_parameters):

        owners_email_list, members_email_list = self._get_all_emails(
            required_parameters.get("owners_list"),
            required_parameters.get("task_id"),
            required_parameters.get("incident_id"),
            required_parameters.get("add_members_from"),
            required_parameters.get("additional_members"))

        url = parse.urljoin(
            constants.BASE_URL,
            constants.URL_LIST_TEAMS)

        body = json.dumps({
            "template@odata.bind" : parse.urljoin(
                constants.BASE_URL,
                constants.URL_TEAMS_STANDARD_TEMPLATE),
            "displayName" : required_parameters.get("displayName"),
            "description" : required_parameters.get("description"),
            "members"     : owners_email_list}.update(
                constants.TEAMS_FROM_GROUP_CONFIGURATION), indent=2)
        self.log.debug(body)

        self.response_handler.add_empty_response_code(202)
        self.response_handler.set_return_raw(True)
        response = self.rc.execute(
            method="post",
            url=url,
            data=body,
            headers=self.headers,
            callback=self.response_handler.check_response)
        self.log.debug(response.raw.info())

        _team_id = (response
            .raw
            .info()
            .get("location"))
        if not _team_id:
            raise IndentationError(constants.ERROR_COULDNOT_CREATE_TEAM)
        _team_id = re.search(constants.TEAM_ID_REGEX, _team_id).group(1)

        if len(members_email_list) > 0: 
            self._add_members(_team_id, members_email_list)

        return {
            "teamId"       : _team_id,
            "displayName"  : required_parameters.get("displayName"),
            "description"  : required_parameters.get("description"),
            "unfoundUsers" : self.users_not_found if len(self.users_not_found) > 0 else None}


    def create_team_from_group(self, group_id):
        '''
        Creates a MS Team from an existing MS Group. Major attributes like the members, description
        etc, is inherited from the Group. While creating a MS Team, certain configurations are 
        required and so the Microsoft recommended bare minimum settings is used create a team.
        These settings are available in the constants folder.
        '''
        url = parse.urljoin(
            constants.BASE_URL,
            constants.URL_TEAM_FROM_GROUP.format(group_id))

        self.log.debug("URL " + url)
        self.log.debug("body " +  json.dumps(constants.TEAMS_FROM_GROUP_CONFIGURATION, indent=2))

        response = self.rc.execute(
            method="put",
            url=url,
            data=json.dumps(constants.TEAMS_FROM_GROUP_CONFIGURATION),
            headers=self.headers,
            callback=self.response_handler.check_response)

        self.log.debug( json.dumps(response))

        return{
            "teamId"      : response.get("id"),
            "displayName" : response.get("displayName"),
            "description" : response.get("description")}
