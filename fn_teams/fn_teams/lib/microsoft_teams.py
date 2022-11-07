# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

''' Helper function for funct_ms_teams_create_teams'''

import json

from urllib import parse
from resilient_lib import IntegrationError

from fn_teams.lib import constants, microsoft_commons
from fn_teams.lib.microsoft_commons import ResponseHandler

'''
POST https://graph.microsoft.com/v1.0/teams
Content-Type: application/json
'''
{
   "template@odata.bind":"https://graph.microsoft.com/v1.0/teamsTemplates('standard')",
   "displayName":"My Sample Team",
   "description":"My Sample Team’s Description",
   "members":[
      {
         "@odata.type":"#microsoft.graph.aadUserConversationMember",
         "roles":["owner"],
         "user@odata.bind":"https://graph.microsoft.com/v1.0/users('0040b377-61d8-43db-94f5-81374122dc7e')"
      }
   ]
}


{
  "template@odata.bind": "https://graph.microsoft.com/v1.0/teamsTemplates('standard')",
  "description": "sample incident",
  "displayName": "newTeam",
  "members": [
    {
      "@odata.type": "#microsoft.graph.aadUserConversationMember",
      "roles": [
        "owner"
      ],
      "user@odata.bind": "https://graph.microsoft.com/v1.0/users('6c259569-f2c0-430b-af73-40081b5de19d')"
    }
  ]
}

class TeamsInterface:
    def __init__(self, required_parameters):
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
            raise IndentationError(constants.WARN_DIDNOT_FIND_USER.format(email_id))
        else:
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
        self.log.info("Owners Information")
        self.log.info(json.dumps(owners_list, indent=2))
        self.log.info("Members Information")
        self.log.info(json.dumps(member_list, indent=2))
        self.response_handler.clear_exempt_codes(default=True)
        return owners_list, member_list


    def create_teams(self, required_parameters):

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

        self.log.debug(json.dumps(body, indent=2))
        response = self.rc.execute(
            method="post",
            url=url,
            data=json.dumps(body),
            headers=self.headers,
            callback=self.response_handler.check_response)

        self.log.debug("\n\n\n")
        self.log.debug(json.dumps(response, indent=2))
        return response
