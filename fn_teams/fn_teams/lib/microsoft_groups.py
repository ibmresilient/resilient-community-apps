# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
#(c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

import json

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
            additional_mambers     <str> : List of email addresses of additional members to be added
            ms_group_description   <str> : Description for the group to be created
            ms_group_mail_nickname <str> : Mail nickname for the group (Must be unique)

        Returns:
        --------
            Response <dict> : A response with the room/team options and details
                              or the error message if the meeting creation
    """
    def __init__(self, required_parameters):
        self.members_email_ids = []
        self.user_db, self.app_message = {}, ""
        self.group_owners, self.group_members = [], []
        self.required_parameters = required_parameters

        self.response_handler = ResponseHandler()
        self.rc = required_parameters["rc"]
        self.log = required_parameters["logger"]
        self.headers = required_parameters["header"]
        self.resclient = required_parameters["resclient"]


    def _write_group(self, **kwargs):
        """
        Creates a group based on all gathered information. This function specifies the owners
        and members to be added to the group while creation. Do note that only a maximum of
        15 users (members + owners) can be added while group creations. Additonal members are
        to be added later on creation.

        kwargs:
        ------
            owners  <list> : list of email addresses of the owners
            members <list> : list of email addresses of the members

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


    def _read_user_info(self, user_id, *args):
        """
        Fetches information based on the email address of a user and assigns
        role (member or owner) to this information and stores it in
        self.user_db for use later.

        Arguments:
        ----------
            user_id (_type_): _description_

        Updates:
        --------
            self.user_db <dict> : User database dictionary with all relavent information
            self.group_owners <dict> : Owners database dictionary with all relavent information
            self.group_members <dict> : Members database dictionary with all relavent information

        """
        url = parse.urljoin(
            constants.BASE_URL,
            constants.URL_USERS.format(user_id))

        response = self.rc.execute(
            method="get",
            url=url,
            headers=self.headers,
            callback=self.response_handler.check_response)

        if "mail" in response:
            if "owner" in args:
                response["owner"] = True
                self.group_owners.append(response.get("id"))
            else:
                response["owner"] = False
                self.group_members.append(response.get("id"))
            self.user_db[user_id] = response
        else:
            _msg = constants.WARN_DIDNOT_FIND_USER.format(user_id)
            self.app_message += "\n" + _msg
            self.log.warn(_msg)


    def _find_all_users(self):
        """
        The email addresses of the associated users are retrieved from the SOAR instance
        and passed on to the Microsoft Endpoint to check if they are valid users. If said
        users are valid, then their email addresses are segregated into owners and members
        and their general information is saved in a dictionary.

        Inputs:
        -------
            self.required_parameters["owners_list"]  <list> : List of owners email addresses
            self.required_parameters["members_list"] <list> : List of members email addresses

        Updates:
        -------
            self.owners_list  <list> : List of owners email addresses
            self.members_list <list> : List of owners members addresses
            self.user_db      <dict> : User database dictionary with all relavent information

        """
        self.response_handler.add_exempt_codes(404)

        if self.required_parameters.get("owners_list"):
            owners_list = (self.required_parameters
                .get("owners_list")
                .lower()
                .replace(" ", "")
                .split(","))
            for member in owners_list:
                if member not in self.user_db and member not in self.group_owners:
                    self._read_user_info(member, "owner")
                else:
                    self.log.debug(constants.DEBUG_SKIPPING_USER)
        else:
            self.log.warn(constants.WARN_NO_OWNER_EMAIL_ID_PROVIDED)

        for member in self.members_email_ids:
            if member not in self.user_db and member not in self.group_owners:
                self._read_user_info(member, "member")
            else:
                self.log.debug(constants.DEBUG_SKIPPING_USER)

        self.log.debug(json.dumps(self.user_db, indent=2))
        self.response_handler.clear_exempt_codes(default=True)


    def _add_members_group(self, group_id, members_list):
        """
        Allows for adding Users to the Microsoft Group. This function plays
        a vital role as the Group creation call can only support upto 15
        members and owners combined. So members are then added in a recursive
        manner.

        Arguments:
        ----------
            group_id     <str>  : ID of the group to which users are to be added
            members_list <list> : A list of email addresses to be added to the
                                  group

        Returns:
        --------
            <None> : Makes POST calls to Microsoft endpoint to add members to group
        """
        self.response_handler.add_exempt_codes(400)
        url = parse.urljoin(
            constants.BASE_URL,
            constants.URL_GROUP_ADD_MEMBERS.format(group_id))
        self.log.debug(constants.DEBUG_ADDING_MEMBER_TO_GROUP.format(url))
        self.log.debug(members_list)
        for member in members_list:
            body = {"@odata.id" : member}
            self.rc.execute(
                "post",
                url=url,
                data=json.dumps(body),
                headers=self.headers,
                callback=self.response_handler.check_response)
        self.response_handler.clear_exempt_codes(default=True)


    def create_group(self):
        """
        Main wrapper function that orchestrates the creation of a Microsoft Group. This function
        executes in the following order:
            * Generates a list of incident or task members that are to be added to the group
            * These member email addresses are retrieved from the SOAR instance and store
            * Email addresses are then used to validate the user credentials on the MS endpoint
            * They are then segregated into owners and members.
            * Basic group details along with the owners email address is passed on the create
              the group
            * Members are then added in a recursive fashion once the group is created

        Returns:
        --------
            response <dict> : Information of the group created
        """
        microsoft_commons.generate_member_list(
            self.resclient,
            self.log,
            task_id=self.required_parameters.get("task_id"),
            incident_id=self.required_parameters.get("incident_id"),
            add_members_from=self.required_parameters.get("add_members_from"),
            additional_members=self.required_parameters.get("additional_members"))
        self._find_all_users()

        members = list(map(lambda id: parse.urljoin(
            constants.BASE_URL,
            constants.URL_DIRECTORY_OBJECT.format(id)), self.group_members))
        owners = list(map(lambda id: parse.urljoin(
            constants.BASE_URL,
            constants.URL_USERS.format(id)), self.group_owners))

        self.log.info(constants.INFO_CREATING_GROUP)
        response = self._write_group(
            description=self.required_parameters["group_description"],
            displayName=self.required_parameters["group_name"],
            mailNickname=self.required_parameters["group_mail_nickname"],
            owners=owners)

        self._add_members_group(response.get("id"), members)

        groups_info = microsoft_commons.find_group(
            rc = self.rc,
            logger = self.log,
            response_handler=self.response_handler,
            headers = self.headers,
            group_mail_nickname=self.required_parameters["group_mail_nickname"])

        return groups_info[0]


    def delete_group(self):
        """
        Microsoft Groups can be deleted using this function. Either the group_name or the
        group_mail_nickname must be provided. Since group_mail_nickname is a unique value
        where no two groups can have the same ID, this is recommended to be used for
        deletion.

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
        if  self.required_parameters.get("group_mail_nickname"):
            group_details = microsoft_commons.find_group(
                rc=self.rc,
                logger=self.log,
                response_handler=self.response_handler,
                headers=self.headers,
                group_mail_nickname=self.required_parameters.get("group_mail_nickname"))
        elif self.required_parameters.get("group_name"):
            group_details = microsoft_commons.find_group(
                rc=self.rc,
                logger=self.log,
                response_handler=self.response_handler,
                headers=self.headers,
                group_name=self.required_parameters.get("group_name"))
        else:
            raise IntegrationError(constants.ERROR_MISSING_NAME_MAIL_NAME)

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
