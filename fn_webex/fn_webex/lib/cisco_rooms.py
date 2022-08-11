# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

import json

from resilient_lib import IntegrationError
from resilient_circuits import FunctionError
from multiprocessing import AuthenticationError


class WebexRooms:
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
            self.LOG.info("Warning: No participants were added to the room. ADD_ALL_INCIDENT_MEMBERS was set to NO and no list of participants were provided in the ADDITIONAL_ATTENDEE field.")
        
        if self.requiredParameters["additionalAttendee"]:
            emailIDs += self.requiredParameters["additionalAttendee"].lower().strip().replace(" ", "").split(",")
        self.emailIDs = emailIDs
        self.LOG.info("Webex: Members to be added to the room {}".format(self.emailIDs))


    def createRoom(self):
        if self.requiredParameters.get("teamID"):
            data = "{\"title\" : \"" + self.requiredParameters.get("roomName") + "\", \"teamId\" : \"" + self.requiredParameters.get("teamID") + "\"}"
        else:
            data = "{\"title\" : \"" + self.requiredParameters.get("roomName") + "\"}"
        response = self.rc.execute("post", "https://webexapis.com/v1/rooms/", headers=self.header, data=data, proxies=self.rc.get_proxies())
        res = json.loads(response.text)
        self.requiredParameters["roomID"] = res.get("id")
        self.requiredParameters["roomName"] = res.get("title")
        self.LOG.info("Webex: Creating new room: {}".format(self.requiredParameters["roomID"]))


    def createRetrieveRoom(self):
        self.requiredParameters["roomID"] = None
        response = self.rc.execute("get", "https://webexapis.com/v1/rooms/", headers=self.header, proxies=self.rc.get_proxies())
        res = json.loads(response.text)
        if len(res.get('items')) == 0:
            self.createRoom()
        else:
            for room in res.get("items"):
                if room.get("title") == self.requiredParameters.get("roomName"):
                    self.requiredParameters["roomID"] = room.get("id")
                    self.requiredParameters["roomName"] = room.get("title")
                    break
            if not self.requiredParameters.get("roomID"):
                self.createRoom()
            self.LOG.info("Webex: Retrieving existing room: {}".format(self.requiredParameters["roomID"]))


    def addMembership(self):
        for user in self.emailIDs:
            data = "{\"roomId\" : \"" + self.requiredParameters.get("roomID") + "\", \"personEmail\" : \"" + user + "\"}" 
            try:
                _ = self.rc.execute("post", "https://webexapis.com/v1/memberships", headers=self.header, data=data, proxies=self.rc.get_proxies())
                self.LOG.info("Webex: User {} added to incident room".format(user))
            except IntegrationError as err:
                self.LOG.info("Webex: User {} is already a member of the room".format(user))


    def getRoomDetails(self):
        res = self.rc.execute("get", "https://webexapis.com/v1/rooms/{}/meetingInfo".format(self.requiredParameters.get("roomID")), headers=self.header,  proxies=self.rc.get_proxies())
        if res.status_code == 200:
            self.LOG.info("Webex: Retrieved room details, Room Name : {}".format(self.requiredParameters.get("roomName")))
            response = json.loads(res.text)
            response["attendees"] = ", ".join(self.emailIDs)
            response["status"] = True
            response["roomName"] = self.requiredParameters.get("roomName")
        else:
            self.LOG.info("Webex: Unable to retrieve room details, Room ID : {}".format(self.requiredParameters.get("roomID")))
            response = json.loads(res.text)
            response["status"] = False
        return response
