# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

import json

from urllib import parse
from resilient_lib import IntegrationError

from fn_teams.lib import constants
from fn_teams.lib.microsoft_commons import ResponseHandler

class GroupsInterface:

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


    def create_group(self):
        self.generate_member_list()
        self.find_all_users()
        members = list(map(lambda id: parse.urljoin(
            constants.BASE_URL,
            constants.URL_DIRECTORY_OBJECT.format(id)), self.group_members))
        owners = list(map(lambda id: parse.urljoin(
            constants.BASE_URL,
            constants.URL_USERS.format(id)), self.group_owners))
        self.log.info(constants.INFO_CREATING_GROUP)
        response = self.write_group(
            description=self.required_parameters["group_description"],
            name=self.required_parameters["group_name"],
            mail_name=self.required_parameters["group_mail_nickname"],
            owners=owners)
        self.add_members_group(response.get("id"), members)
        groups_info = self.find_group(
            group_mail_nickname=self.required_parameters["group_mail_nickname"])
        return groups_info[0]


    def write_group(self, **kwargs):
        body = {
            "description" : kwargs.get("description", ""),
            "displayName" : kwargs.get("name"),
            "groupTypes"  : [constants.SETTINGS_GROUP_TYPE],
            "mailEnabled" : constants.SETTINGS_GROUP_MAIL_ENABLED,
            "mailNickname": kwargs.get("mail_name"),
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


    def find_group(self, **kwargs):

        if "group_name" in kwargs:
            self.log.info(constants.INFO_FIND_GROUP_BY_NAME)
            _name = kwargs.get("group_name")
            error_msg = constants.ERROR_DIDNOT_FIND_GROUP.format("Group Name", _name)
            _query = constants.QUERY_GROUP_FIND_BY_NAME.format(_name)

        if "group_mail_nickname" in kwargs:
            self.log.info(constants.INFO_FIND_GROUP_BY_MAIL)
            _name = kwargs.get("group_mail_nickname")
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
        else:
            self.log.error(error_msg)
            raise IntegrationError(error_msg)


    def read_user_info(self, user_id, *args):
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


    def find_all_users(self):
        self.response_handler.add_exempt_codes(404)

        if self.required_parameters.get("owners_list"):
            owners_list = (self.required_parameters
                .get("owners_list")
                .lower()
                .replace(" ", "")
                .split(","))
            for member in owners_list:
                if member not in self.user_db and member not in self.group_owners:
                    self.read_user_info(member, "owner")
                else:
                    self.log.debug(constants.DEBUG_SKIPPING_USER)

        for member in self.members_email_ids:
            if member not in self.user_db and member not in self.group_owners:
                self.read_user_info(member, "member")
            else:
                self.log.debug(constants.DEBUG_SKIPPING_USER)

        else:
            self.log.warn(constants.WARN_NO_OWNER_EMAIL_ID_PROVIDED)

        self.log.debug(json.dumps(self.user_db, indent=2))
        self.response_handler.clear_exempt_codes(default=True)


    def add_members_group(self, group_id, members_list):
        self.response_handler.add_exempt_codes(400)
        url = parse.urljoin(
            constants.BASE_URL,
            constants.URL_GROUP_ADD_MEMBERS.format(group_id))
        self.log.debug("Adding members to Group object {}".format(url))
        for member in members_list:
            body = {"@odata.id" : member}
            self.rc.execute(
                "post",
                url=url,
                data=json.dumps(body),
                headers=self.headers,
                callback=self.response_handler.check_response)

        self.response_handler.clear_exempt_codes(default=True)


    def find_group_by_mail(self, mail_id):

        if "@" in mail_id:
            mail_id = mail_id.split("@")[0]

        _query = constants.QUERY_GROUP_FIND_BY_MAIL.format(mail_id)
        url = parse.urljoin(
            constants.BASE_URL,
            constants.URL_GROUPS_QUERY.format(_query))

        response = self.rc.execute(
            "get",
            url=url,
            headers=self.headers)

        print(response, url)
        self.log.info(json.dumps(response.text, indent=2))
        return response


    def is_direct_member(self, incident_member_id, org_member_list):
        """
        Checks to see if the member Id accquired from the incident belongs to the list of all
        users from the organization. Upon match, it then extracts the email address for that
        particular user.

        Args:
        -----
            incident_member_id (<str>) : The user Id accquired from the incident
            org_member_list    (<list>): The list of member Ids of all organization members

        Returns:
        --------
            (<str>): Email address of the incident member
        """
        for user in org_member_list:
            if incident_member_id == user.get("id"):
                return user.get(constants.EMAIL)


    def is_group_member(self, incident_member_id, org_member_list, org_group_list):
        """
        Checks to see if the member Id accquired from the incident belongs to the list of
        all groups from the organization. Upon match, it then queries a list of Ids
        associated with that group and matches with user using the >>is_direct_member<<
        function

        Args:
        -----
            incident_member_id (<str>) : The user Id accquired from the incident
            org_member_list    (<list>): The list of member Ids of all organization members
            org_group_list     (<list>): The list of group Ids of all organization members

        Returns:
        --------
            (<list>): list of all email addresses of incident members
        """
        ret = []
        for group in org_group_list:
            if incident_member_id == group.get("id"):
                for member in group.get("members"):
                    ret.append(self.is_direct_member(member, org_member_list))
        return ret


    def generate_member_list(self):
        """
        Generates a list of email addresses of the members to be added to the room/team. The
        function queries incident member list or task member list, organization group list, 
        and organization user list. Using these, it then compares and accquires the email 
        addresses of all users that are members to the incident or task, if >>addAllMembers<<
        in enabled. Else just adds the email addresses specified in >>additionalAttendee<<

        Returns:
        --------
            members_email_ids (<list>) : a list of all participant email addresses to be added
        """
        add_members_from = self.required_parameters.get("add_members_from").lower().strip()
        add_members_from = None if add_members_from == "none" else add_members_from

        email_ids = []
        org_member_list = self.resclient.post(constants.RES_USERS, payload={}).get("data")
        org_group_list  = self.resclient.get(constants.RES_GROUPS)

        if add_members_from:
            if add_members_from.strip().lower() == "task":
                incidentMembers = self.resclient.get(parse.urljoin(constants.RES_TASK,
                    "{}/members".format(self.required_parameters.get("task_id"))))
            else:
                incidentMembers = self.resclient.get(parse.urljoin(constants.RES_INCIDENT,
                    "{}/members".format(self.required_parameters.get("incident_id"))))
            if len(incidentMembers.get("members")) == 0:
                self.log.warn(constants.WARN_INCIDENT_NO_MEMBERS )
            for incident_member in incidentMembers.get("members"):
                if self.is_direct_member(incident_member, org_member_list):
                    email_ids.append(self.is_direct_member(incident_member,
                                                            org_member_list))
                elif self.is_group_member(incident_member,
                                          org_member_list,
                                          org_group_list):
                    email_ids.extend(self.is_group_member(incident_member,
                                                         org_member_list,
                                                         org_group_list))
            self.log.debug(email_ids)
        elif not self.required_parameters.get("additiona_members"):
            self.log.warn(constants.WARN_NO_ADDITIONAL_PARTICIPANTS)

        if self.required_parameters.get("additiona_members"):
            email_ids += self.required_parameters.get("additiona_members").lower().replace(" ", "").split(",")
        self.members_email_ids = set(email_ids)
        self.log.info(constants.INFO_ADD_MEMEBERS.format(self.members_email_ids))


    def delete_group(self):
        if "group_name" in self.required_parameters:
            group_details = self.find_group(
                group_name=self.required_parameters.get("group_name"))

        elif "group_mail_nickname" in self.required_parameters:
            group_details = self.find_group(
                group_mail_nickname=self.required_parameters.get("group_mail_nickname"))

        else:
            raise IntegrationError(constants.ERROR_MISSING_NAME_MAIL_NAME)

        if len(group_details) > 1:
            raise IntegrationError(constants.ERROR_FOUND_MANY_GROUP)

        group_id = group_details[0].get("id")

        url = parse.urljoin(
            constants.BASE_URL,
            constants.URL_GROUPS.format(group_id))

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