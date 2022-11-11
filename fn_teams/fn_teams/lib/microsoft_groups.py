# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
'''
 (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
'''

import json

from urllib import parse
from resilient_lib import IntegrationError

from fn_teams.lib import constants
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


    def _find_group(self, **kwargs):
        """
        Allows for locating a group based on its displayName or mailNickname attribute
        This function at least required either the group_name or the group_mail_nickname
        keyword argument.

        Kwargs:
        -------
            group_name          <str> : Display name of the group
            group_mail_nickname <str> : Mail nickname of the group

        Raises:
        -------
            IntegrationError: Unable to locate the group

        Returns:
        --------
            <dict> : Details of the detected group
        """

        if "group_name" in kwargs:
            self.log.info(constants.INFO_FIND_GROUP_BY_NAME)
            _name = kwargs.get("group_name")
            error_msg = constants.ERROR_DIDNOT_FIND_GROUP.format("Group Name", _name)
            _query = constants.QUERY_GROUP_FIND_BY_NAME.format(_name)

        if "group_mail_nickname" in kwargs:
            self.log.info(constants.INFO_FIND_GROUP_BY_MAIL)
            _name = kwargs.get("group_mail_nickname")
            if "@" in _name:
                _name = _name.split("@")[0]
            error_msg = constants.ERROR_DIDNOT_FIND_GROUP.format("Mail Nickname", _name)
            _query = constants.QUERY_GROUP_FIND_BY_MAIL.format(_name)

        url = parse.urljoin(
            constants.BASE_URL,
            constants.URL_GROUPS_QUERY.format(_query))

        response = self.rc.execute(
            method="get",
            url=url,
            headers=self.headers,
            callback=self.response_handler.check_response)

        self.log.debug(json.dumps(response, indent=2))

        if len(response.get("value")) > 0 :
            self.log.info(constants.INFO_FOUND_GROUP)
            return response.get("value")

        self.log.error(error_msg)
        raise IntegrationError(error_msg)


    def _read_user_info(self, user_id, *args):
        """
        Fetches information using the email address of the SOAR user and assigns
        a role (member or owner) depending upon the information that was provided 
        in the function, and saves this information in self.user_db for later use.

        Arguments:
        ----------
            user_id (_type_): _description_

        Updates:
        --------
            self.user_db       <dict> : User database dictionary with all relevant information
            self.group_owners  <dict> : Owners database dictionary with all relevant information
            self.group_members <dict> : Members database dictionary with all relevant information
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
        Retrieves all the user information from the SOAR instance and validates if these users'
        email addresses are associated with a valid Microsoft account. These users are then
        segregated into owners and members and their general information is saved in a 
        dictionary.

        Inputs:
        -------
            self.required_parameters["owners_list"]  <list> : List of owners email addresses
            self.required_parameters["members_list"] <list> : List of members email addresses

        Updates:
        -------
            self.owners_list  <list> : List of owners' email addresses
            self.members_list <list> : List of owners members addresses
            self.user_db      <dict> : User database dictionary with all relevant information
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


    def _is_direct_member(self, incident_member_id, org_member_list):
        """
        Checks to see if the member Id acquired from the incident or task belongs to the
        list of users from the organization. Upon a match, it then extracts the email
        address for that particular user.

        Args:
        -----
            incident_member_id <str>  : The user Id acquired from the incident
            org_member_list    <list> : The list of member Ids of all organization members

        Returns:
        --------
            <str>: Email address of the incident member
        """
        for user in org_member_list:
            if incident_member_id == user.get("id"):
                return user.get(constants.EMAIL)


    def _is_group_member(self, incident_member_id, org_member_list, org_group_list):
        """
        Checks to see if the member Id acquired from the incident or task belongs to
        the list of all groups from the organization. Upon a match, it then queries a list
        of Ids associated with that group and matches with a user using the
        >>is_direct_member<< function

        Args:
        -----
            incident_member_id  <str> : The user Id acquired from the incident
            org_member_list    <list> : The list of member Ids of all organization members
            org_group_list     <list> : The list of group Ids of all organization members

        Returns:
        --------
            <list>: list of all email addresses of incident members
        """
        ret = []
        for group in org_group_list:
            if incident_member_id == group.get("id"):
                for member in group.get("members"):
                    ret.append(self._is_direct_member(member, org_member_list))
        return ret


    def _generate_member_list(self):
        """
        Generates a list of email addresses of the members of a SOAR instance. The main 
        goal is to extract user email addresses from the SOAR instance for specific users.
        While querying an incident or a task for members, user ids are returned as appose to
        entire user data. These ids are then converted to useful information (in this case
        user email address) by fetching user information based on the retrieved ids.

        Returns:
        --------
            members_email_ids <list> : a list of all participant email addresses to be added
        """
        org_member_list  = self.resclient.post(constants.RES_USERS, payload={}).get("data")
        org_group_list   = self.resclient.get(constants.RES_GROUPS)
        add_members_from = self.required_parameters.get("add_members_from").lower().strip()
        add_members_from = None if add_members_from == "none" else add_members_from

        email_ids = []
        if add_members_from:
            if add_members_from.strip().lower() == "task":
                incident_members = self.resclient.get(parse.urljoin(constants.RES_TASK,
                    constants.MEMBERS_URL.format(self.required_parameters.get("task_id"))))
            else:
                incident_members = self.resclient.get(parse.urljoin(constants.RES_INCIDENT,
                    constants.MEMBERS_URL.format(self.required_parameters.get("incident_id"))))
            if len(incident_members.get("members")) == 0:
                self.log.warn(constants.WARN_INCIDENT_NO_MEMBERS)
            for incident_member in incident_members.get("members"):
                if self._is_direct_member(incident_member, org_member_list):
                    email_ids.append(self._is_direct_member(incident_member,
                                                            org_member_list))
                elif self._is_group_member(incident_member,
                                          org_member_list,
                                          org_group_list):
                    email_ids.extend(self._is_group_member(incident_member,
                                                         org_member_list,
                                                         org_group_list))
            self.log.debug(email_ids)
        elif not self.required_parameters.get("additional_members"):
            self.log.warn(constants.WARN_NO_ADDITIONAL_PARTICIPANTS)
        if self.required_parameters.get("additional_members"):
            email_ids += (self.required_parameters
            .get("additional_members")
            .lower()
            .replace(" ", "")
            .split(","))
        self.members_email_ids = list(set(email_ids))
        self.log.info(constants.INFO_ADD_MEMEBERS.format(self.members_email_ids))


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
        self._generate_member_list()
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

        groups_info = self._find_group(
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
            group_details = self._find_group(
                group_mail_nickname=self.required_parameters.get("group_mail_nickname"))
        elif self.required_parameters.get("group_name"):
            group_details = self._find_group(
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
