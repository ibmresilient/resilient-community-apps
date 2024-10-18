# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, line-too-long
#(c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

import json
import logging

from urllib import parse
from resilient_lib import IntegrationError

from fn_teams.lib import constants, microsoft_commons
from fn_teams.lib.microsoft_commons import ResponseHandler

class GroupsInterface:
    """
        This application allows for creating a Microsoft Group using the Microsoft Graph API. This
        provides SOAR with the ability to create Groups from within a SOAR incident or a task.

        Inputs:
        -------
            task_id                <str> : If called from task then Task ID
            incident_id            <str> : Incident ID
            ms_group_name          <str> : Name of the Microsoft Group to be created
            ms_owners_list         <str> : List of owners email addresses
            add_members_from       <str> : Specifies if members to be added form incident or task
            additional_members     <str> : List of email addresses of additional members to be added
            ms_group_description   <str> : Description for the group to be created
            ms_group_mail_nickname <str> : Mail nickname for the group (Must be unique)

        Returns:
        --------
            Response <dict> : A response with the room/team options and details
                              or the error message if the meeting creation
    """
    def __init__(self, required_parameters):
        self.app_message = ""
        self.required_parameters = required_parameters
        self.log = logging.getLogger(__name__)
        self.response_handler = ResponseHandler()
        self.rc = required_parameters["rc"]
        self.headers = required_parameters["header"]
        self.resclient = required_parameters["resclient"]


    def _write_group(self, **kwargs):
        """
        Creates a group based on all gathered information. This function specifies the owners
        and members to be added to the group while creation. Do note that only a maximum of
        15 users (members + owners) can be added while group creations. Additional members are
        to be added later on after the group is successfully created.

        kwargs:
        ------
            description  <str>  : Description for the group that is being created
            displayName  <str>  : Name of the Group being that is created
            mailNickname <str>  : Mail nickname for the group (Must be unique)
            owners       <list> : list of email addresses of the owners
            members      <list> : list of email addresses of the members

        Returns:
        -------
            response <dict> : details of the group created
        """
        body = {
            "description" : kwargs.get("description", ""),
            "displayName" : kwargs.get("displayName"),
            "groupTypes"  : [constants.SETTINGS_GROUP_TYPE],
            "mailEnabled" : constants.SETTINGS_GROUP_MAIL_ENABLED,
            "mailNickname": kwargs.get("mailNickname"),
            "securityEnabled" : constants.SETTINGS_GROUP_SECURITY_ENABLED}

        if "owners" in kwargs:
            body["owners@odata.bind"] = kwargs.get("owners")
        if "members" in kwargs:
            body["members@odata.bind"] = kwargs.get("members")

        body.update(constants.CREATE_GROUP_CONFIGURATION)

        self.log.debug(constants.INFO_GROUP_CREATION_REQUEST)
        self.log.debug(json.dumps(body, indent=2))

        url = parse.urljoin(
            constants.BASE_URL,
            constants.URL_LIST_GROUPS)

        response = self.rc.execute(
            method="post",
            url=url,
            data=json.dumps(body),
            headers=self.headers,
            callback=self.response_handler.check_response)

        self.log.debug(json.dumps(response, indent=2))
        return response


    def _find_all_users(self, owners_list: list, members_list: list):
        """
        Retrieves all the user information from the SOAR instance and validates if these users'
        email addresses are associated with a valid Microsoft account. They are then segerated
        segregated into owners and members and their general information is saved in a
        dictionary.

        Inputs:
        -------
            owners_list  <str> : owners email addresses in a comma
            members_list <list> : List of members email addresses

        Updates:
        -------
            self.owners_list  <list> : List of owners' email addresses
            self.members_list <list> : List of owners members addresses
            self.user_db      <dict> : User database dictionary with all relevant information
        """
        group_owners, group_members, unfound_user = [], [], []
        self.response_handler.add_exempt_codes(404)

        user_finder = microsoft_commons.MSFinder(
            rc=self.rc,
            rh=self.response_handler,
            headers=self.headers)

        if owners_list:
            for member in owners_list:
                if member not in group_owners:
                    response = user_finder.find_user(member)
                    if response:
                        response["owner"] = True
                        group_owners.append(response.get("id"))
                    else:
                        unfound_user.append(member)
                else:
                    self.log.debug(constants.DEBUG_SKIPPING_USER)
            if len(group_owners) > 0:
                self.log.debug(json.dumps(group_members, indent=2))
        else:
            self.log.warning(constants.WARN_NO_OWNER_EMAIL_ID_PROVIDED)

        if members_list:
            for member in members_list:
                if member not in group_owners:
                    response = user_finder.find_user(member)
                    if response:
                        response["owner"] = False
                        group_members.append(response.get("id"))
                    else:
                        unfound_user.append(member)
                else:
                    self.log.debug(constants.DEBUG_SKIPPING_USER)
            if len(group_members) > 0:
                self.log.debug(json.dumps(group_members, indent=2))
        else:
            self.log.warning(constants.WARN_NO_MEMBER_EMAIL_ID_PROVIDED)

        self.response_handler.clear_exempt_codes(default=True)
        return group_owners, group_members, unfound_user


    def _add_members_group(self, group_id: str, members_list: list):
        """
        Allows for adding Users to the Microsoft Group. This function plays
        a vital role as the Group creation call can only support up to 15 objects
        (members and owners). So members are then added recursively.

        Arguments:
        ----------
            group_id     <str>  : ID of the group to which users are to be added
            members_list <list> : A list of email addresses to be added to the
                                  group

        Returns:
        --------
            <None>  : Makes POST calls to Microsoft endpoint to add members to the
                      group
        """
        self.response_handler.add_exempt_codes(400)
        url = parse.urljoin(
            constants.BASE_URL,
            constants.URL_GROUP_ADD_MEMBERS.format(group_id))
        self.log.debug(constants.DEBUG_ADDING_MEMBER_TO_GROUP.format(url))
        for member in members_list:
            body = json.dumps({"@odata.id" : member}, indent=2)
            self.log.debug(body)
            self.rc.execute(
                "post",
                url=url,
                data=body,
                headers=self.headers,
                callback=self.response_handler.check_response)
        self.response_handler.clear_exempt_codes(default=True)


    def create_group(self):
        """
        Main wrapper function that orchestrates the creation of a Microsoft Group. This function
        executes in the following order:
            * Generates a list of incident or task members that are to be added to the group
            * Retrieves all the user information from the SOAR instance
            * Validates these credentials and checks if the email addresses are associated with
              a valid Microsoft account.
            * They are then segregated into owners and members.
            * Basic group details along with the owners' email addresses are passed on the create
              the group
            * Members are then added recursively once the group is created

        Returns:
        --------
            response <dict> : Information of the group created
        """
        owners_list = (self.required_parameters
            .get("owners_list", "")
            .lower()
            .replace(" ", "")
            .split(","))

        members_list = microsoft_commons.generate_member_list(
            resclient=self.resclient,
            task_id=self.required_parameters.get("task_id"),
            incident_id=self.required_parameters.get("incident_id"),
            add_members_from=self.required_parameters.get("add_members_from"),
            additional_members=self.required_parameters.get("additional_members"))

        owners_list, members_list, unfound_users = self._find_all_users(owners_list, members_list)

        # Generating a list of members' and owners' principal URL by joining:
        # BASE_URL + URL_DIRECTORY_OBJECT + UNIQUE_PRINCIPAL_ID
        # ex: https://graph.microsoft.com/v1.0/directoryObjects/4562bcc8-****-****-*****-4f8ce89dca5e

        members = list(map(lambda id: parse.urljoin(
            constants.BASE_URL,
            constants.URL_DIRECTORY_OBJECT.format(id)), members_list))
        owners  = list(map(lambda id: parse.urljoin(
            constants.BASE_URL,
            constants.URL_USERS.format(id)), owners_list))

        self.log.info(constants.INFO_CREATING_GROUP)
        response = self._write_group(
            displayName=self.required_parameters["group_name"],
            description=self.required_parameters["group_description"],
            mailNickname=self.required_parameters["group_mail_nickname"],
            owners=owners)

        self._add_members_group(response.get("id"), members)

        group_finder = microsoft_commons.MSFinder(
            rc=self.rc,
            rh=self.response_handler,
            headers=self.headers)
        groups_info = group_finder.find_group(
            {"group_mail_nickname" : self.required_parameters["group_mail_nickname"]})

        group_info = groups_info[0]
        group_info.update({
            "teamsEnabled" : False,
            "unfoundUsers" : unfound_users})
        return group_info


    def delete_group(self, options):
        """
        Microsoft Groups can be deleted using this function. Either the group_name or the
        group_mail_nickname must be provided. Since group_mail_nickname is a unique value
        where no two groups can have the same ID, this is recommended to be used for
        deletion. Do note that the function is designed in a way that it prioritizes
        group_mail_nickname over group_name, so when both values are provided, the function
        automatically chooses the group_mailNickname to locate and delete the group

        Inputs:
        -------
            group_name          <str> : Name of the group to be deleted
            group_mail_nickname <str> : Mail nickname of the group to be delete. This is
                                        preffered over group_name as this value is unique

        Raises:
        -------
            IntegrationError: Raised when neither the group name nor the group mail name
                              is not specified.
            IntegrationError: Raised when found more than one group. This can happen when
                              2 or more groups have the same display name. To avoid this,
                              mail nickname is always recommended to be used.

        Returns:
            <dict>: Message that reads successfully deleted group and status code
        """
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
            constants.URL_LOCATE_GROUPS.format(group_id))
        self.log.debug(url)

        response = self.rc.execute(
            method="delete",
            url=url,
            headers=self.headers,
            callback=self.response_handler.check_response)

        if response.get("status_code") == 204:
            response["message"] = constants.INFO_SUCCESSFULLY_DELETED.format(
                "Group",
                group_details[0].get("displayName"))
            self.log.info(response["message"])
        return response
