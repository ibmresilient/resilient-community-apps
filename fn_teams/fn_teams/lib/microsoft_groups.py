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


    def create_group(self):
        self.find_all_users()
        self.log.info(constants.INFO_CREATING_GROUP)
        response = self.write_group(
            description=self.required_parameters["group_description"],
            name=self.required_parameters["group_name"],
            mail_name=self.required_parameters["group_mail_nickname"],
            owners=self.group_owners,
            members=self.group_members)
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
        return response


    def write_group(self, **kwargs):
        body = {
            "description" : kwargs.get("description", ""),
            "displayName" : kwargs.get("name"),
            "groupTypes"  : [constants.SETTINGS_GROUP_TYPE],
            "mailEnabled" : constants.SETTINGS_GROUP_MAIL_ENABLED,
            "mailNickname": kwargs.get("mail_name"),
            "securityEnabled" : constants.SETTINGS_GROUP_SECURITY_ENABLED,
        }

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

        self.log.debug(response)
        return response


    def find_group(self, **kwargs):

        if "group_name" in kwargs:
            self.log.info(constants.INFO_FIND_GROUP_BY_NAME)
            _name = kwargs.get("group_name")
            error_msg = constants.ERROR_DIDNOT_FIND_GROUP.format("Group Name", _name)
            _query = "?$filter=displayName eq \'{}\'".format(_name)

        if "group_mail_nickname" in kwargs:
            self.log.info(constants.INFO_FIND_GROUP_BY_MAIL)
            _name = kwargs.get("group_mail_nickname")
            error_msg = constants.ERROR_DIDNOT_FIND_GROUP.format("Mail Nickname", _name)
            _query = "?$filter=mailNickname eq \'{}\'".format(_name)

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

        if "owner" in args:
            response["owner"] = True
            self.group_owners.append(
                parse.urljoin(
                    constants.BASE_URL,
                    constants.URL_USERS.format(response.get("id"))))
        else:
            response["owner"] = False
            self.group_members.append(
                parse.urljoin(
                    constants.BASE_URL,
                    constants.URL_USERS.format(response.get("id"))))
        if "mail" in response:
            self.user_db[user_id] = response
        else:
            raise IntegrationError(constants.ERROR_DIDNOT_FIND_USER.format(user_id))


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
