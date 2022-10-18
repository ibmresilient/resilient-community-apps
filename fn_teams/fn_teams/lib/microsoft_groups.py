# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

from distutils.log import error
import json
from textwrap import indent
from fn_teams.lib.microsoft_commons import ResponseHandler
from urllib import parse
from resilient_lib import IntegrationError

from fn_teams.lib import constants

class GroupsInterface:
    def __init__(self, required_parameters):
        self.user_db = {}
        self.group_owners, self.group_members = [], []
        self.rc = required_parameters["rc"]
        self.log = required_parameters["logger"]
        self.headers = required_parameters["header"]
        self.response_handler = ResponseHandler()
        self.required_parameters = required_parameters
        self.app_message = ""


    def create_group(self):
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
        group_info = self.find_group(
            group_mail_nickname=self.required_parameters["group_mail_nickname"])
        return group_info


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

        members_list = self.required_parameters.get("members_list")
        for member in members_list:
            if member not in self.user_db:
                self.read_user_info(member, "member")
            else:
                self.log.debug(constants.DEBUG_SKIPPING_USER)

        members_list = self.required_parameters.get("owners_list")
        for member in members_list:
            if member not in self.user_db:
                self.read_user_info(member, "owner")
            else:
                self.log.debug(constants.DEBUG_SKIPPING_USER)

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


    def generate_member_list(self, operation_level, add_all_members=False):
        """
        Generates a list of email addresses of the members to be added to the room/team. The
        function queries incident member list or task member list, organization group list, 
        and organization user list. Using these, it then compares and accquires the email 
        addresses of all users that are members to the incident or task, if >>addAllMembers<<
        in enabled. Else just adds the email addresses specified in >>additionalAttendee<<

        Returns:
        --------
            email_ids (<list>) : a list of all participant email addresses to be added
        """
        email_ids = []
        if operation_level == "task":
            incidentMembers = self.resclient.get(parse.urljoin(constants.RES_TASK,
                "{}/members".format(self.required_parameters.get("task_id"))))
        else:
            incidentMembers = self.resclient.get(parse.urljoin(constants.RES_INCIDENT,
                "{}/members".format(self.required_parameters.get("incident_id"))))
        org_member_list = self.resclient.post(constants.RES_USERS, payload={}).get("data")
        org_group_list  = self.resclient.get(constants.RES_GROUPS)
        if add_all_members:
            if len(incidentMembers.get("members")) == 0:
                self.LOG.info(constants.LOG_INCIDENT_NO_MEMBERS)
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
        elif not self.required_parameters.get("additionalAttendee"):
            self.LOG.warn(constants.LOG_WARN_NO_ADDITIONAL_PARTICIPANTS.format(
                self.entity_type))

        if self.required_parameters.get("additionalAttendee"):
            email_ids += self.required_parameters.get("additionalAttendee").lower().replace(" ", "").split(",")
        self.email_ids = set(email_ids)
        self.LOG.info(constants.LOG_ADD_MEMEBERS.format(
            self.entity_type, self.email_ids))
