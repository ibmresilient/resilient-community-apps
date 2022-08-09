# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

import json
from multiprocessing.sharedctypes import Value

from resilient_lib import IntegrationError
from resilient_circuits import FunctionError
from multiprocessing import AuthenticationError


class WebexTeams:
    def __init__(self, requiredParameters):
        self.requiredParameters = requiredParameters
        self.rc = self.requiredParameters.get("rc")
        self.header = requiredParameters.get("header")
        self.LOG = self.requiredParameters.get("logger")
        self.resclient = requiredParameters.get("resclient")


    def isDirectMember(self, ids, orgMemberList):
        for user in orgMemberList:
            if ids == user.get("id"): 
                return user.get("email")
            
    def isGroupMember(self, ids, orgMemberList, orgGroupList):
        ret = []
        for group in orgGroupList:
            if ids == group.get("id"):
                for member in group.get("members"):
                    ret.append(self.isDirectMember(member, orgMemberList))
        return ret


    def generate_member_list(self):
        emailIDs = []
        incidentMembers = self.resclient.get("/incidents/{}/members".format(self.requiredParameters["incidentID"]))
        orgMemberList   = self.resclient.post("/users/query_paged?return_level=normal", payload={}).get("data")
        orgGroupList    = self.resclient.get("/groups")

        if self.requiredParameters["addAllMembers"]:
            if len(incidentMembers.get("members")) == 0:
                self.LOG.info("Webex: There are no members assigned to this incident")
            for incident_member in incidentMembers.get("members"):
                if self.isDirectMember(incident_member, orgMemberList):
                    emailIDs.append(self.isDirectMember(incident_member, orgMemberList))
                elif self.isGroupMember(incident_member, orgMemberList, orgGroupList):
                    emailIDs.extend(self.isGroupMember(incident_member, orgMemberList, orgGroupList))
        elif not self.requiredParameters["additionalAttendee"]:
            raise ValueError("ERROR: No participants were added to the team. ADD_ALL_INCIDENT_MEMBERS was set to NO and no list of participants were provided in the ADDITIONAL_ATTENDEE field.")
        
        if self.requiredParameters["additionalAttendee"]:
            emailIDs += self.requiredParameters["additionalAttendee"].lower().strip().replace(" ", "").split(",")
        self.emailIDs = emailIDs
        self.LOG.info("Webex: Members to be added to the team {}".format(self.emailIDs))


    def createRetrieveTeam(self):
        def createTeam():
            data = "{\"name\" : \"" + self.requiredParameters.get("teamName") + "\"}"
            response = self.rc.execute("post", "https://webexapis.com/v1/teams/", headers=self.header, data=data, proxies=self.rc.get_proxies())
            res = json.loads(response.text)
            self.requiredParameters["teamID"] = res.get("id")
            self.LOG.info("Webex: Created new team: {}".format(self.requiredParameters["teamID"]))

        self.requiredParameters["teamID"] = None
        response = self.rc.execute("get", "https://webexapis.com/v1/teams/", headers=self.header, proxies=self.rc.get_proxies())
        res = json.loads(response.text)
        if len(res.get('items')) == 0:
            createTeam()
        else:
            for team in res.get("items"):
                if team.get("name") == self.requiredParameters.get("teamName"):
                    self.requiredParameters["teamID"] = team.get("id")
                    break
            if not self.requiredParameters.get("teamID"):
                createTeam()
            self.LOG.info("Webex: Retrieving existing team: {}".format(self.requiredParameters["teamID"]))


    def addMembership(self):
        for user in self.emailIDs:
            data = "{\"teamId\" : \"" + self.requiredParameters.get("teamID") + "\", \"personEmail\" : \"" + user + "\"}" 
            try:
                _ = self.rc.execute("post", "https://webexapis.com/v1/team/memberships", headers=self.header, data=data, proxies=self.rc.get_proxies())
                self.LOG.info("Webex: User {} added to incident team".format(user))
            except IntegrationError as err:
                self.LOG.info("Webex: User {} is already a member of the team".format(user))


    def getTeamDetails(self):
        res = self.rc.execute("get", "https://webexapis.com/v1/teams/{}".format(self.requiredParameters.get("teamID")), headers=self.header,  proxies=self.rc.get_proxies())
        if res.status_code == 200:
            self.LOG.info("Webex: Retrieved team details, team Name : {}".format(self.requiredParameters.get("teamName")))
            response = json.loads(res.text)
            response["Attendees"] = ", ".join(self.emailIDs)
            response["status"] = True
        else:
            self.LOG.info("Webex: Unable to retrieve team details, team ID : {}".format(self.requiredParameters.get("teamID")))
            response = json.loads(res.text)
            response["status"] = False
        return response

 