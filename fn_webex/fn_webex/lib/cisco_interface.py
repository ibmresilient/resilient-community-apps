# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
import json

from fn_webex.lib import constants
from resilient_lib import IntegrationError
from resilient_circuits import FunctionError

class WebexInterface:
    def __init__(self, requiredParameters):
        self.requiredParameters = requiredParameters
        self.rc = self.requiredParameters.get("rc")
        self.header = requiredParameters.get("header")
        self.LOG = self.requiredParameters.get("logger")
        self.resclient = requiredParameters.get("resclient")
        self.entityId = requiredParameters.get("entityId")
        self.entityName = requiredParameters.get("entityName")


    def isDirectMember(self, incidentMemberId, orgMemberList):
        """
        Checks to see if the member Id accquired from the incident belongs to the list of all 
        users from the organization. Upon match, it then extracts the email address for that 
        particular user.

        Args:
        -----
            incidentMemberId (<str>) : The user Id accquired from the incident
            orgMemberList    (<list>): The list of member Ids of all organization members

        Returns:
        --------
            (<str>): Email address of the incident member
        """
        for user in orgMemberList:
            if incidentMemberId == user.get("id"): 
                return user.get("email")


    def isGroupMember(self, incidentMemberId, orgMemberList, orgGroupList):
        """
        Checks to see if the member Id accquired from the incident belongs to the list of
        all groups from the organization. Upon match, it then queries a list of Ids 
        associated with that group and matches with user using the >>iSDirectMember<< 
        function

        Args:
        -----
            incidentMemberId (<str>) : The user Id accquired from the incident
            orgMemberList    (<list>): The list of member Ids of all organization members
            orgGroupList     (<list>): The list of group Ids of all organization members

        Returns:
        --------
            (<list>): list of all email addresses of incident members
        """
        ret = []
        for group in orgGroupList:
            if incidentMemberId == group.get("id"):
                for member in group.get("members"):
                    ret.append(self.isDirectMember(member, orgMemberList))
        return ret


    def generate_member_list(self):
        """
        Generates a list of email addresses of the members to be added to the room/team. The 
        function queries incident member list, organization group list, and organization
        user list. Using these, it then compares and accquires the email addresses of all
        users that are members to the incident, if >>addAllMembers<< in enabled. Else just
        adds the email addresses specified in >>additionalAttendee<<

        Returns:
        --------
            emailIds (<list>) : a list of all participant email addresses to be added
        """
        emailIds = []
        incidentMembers = self.resclient.get(constants.RES_INCIDENT + "{}/members".format(self.requiredParameters["incidentId"]))
        orgMemberList   = self.resclient.post(constants.RES_USERS, payload={}).get("data")
        orgGroupList    = self.resclient.get(constants.RES_GROUPS)

        if self.requiredParameters["addAllMembers"]:
            if len(incidentMembers.get("members")) == 0:
                self.LOG.info("Webex: There are no members assigned to this incident")
            for incident_member in incidentMembers.get("members"):
                if self.isDirectMember(incident_member, orgMemberList):
                    emailIds.append(self.isDirectMember(incident_member, orgMemberList))
                elif self.isGroupMember(incident_member, orgMemberList, orgGroupList):
                    emailIds.extend(self.isGroupMember(incident_member, orgMemberList, orgGroupList))
        elif not self.requiredParameters["additionalAttendee"]:
            self.LOG.warn("Warning: No participants were added to the room/team. ADD_ALL_INCIDENT_MEMBERS was set to NO and no list of participants were provided in the ADDITIONAL_ATTENDEE field.")
        
        if self.requiredParameters["additionalAttendee"]:
            emailIds += self.requiredParameters["additionalAttendee"].lower().replace(" ", "").split(",")
        self.emailIds = emailIds
        self.LOG.info("Webex: Members to be added to the room/team {}".format(self.emailIds))


    def addMembership(self):
        """
        Adds members to the room/team using the email addresses from >>emailIds<<. If user already
        a member of the room/team, ignores.
        """
        for user in self.emailIds:
            data = {self.entityId : self.requiredParameters.get(self.entityId), "personEmail" : user}
            try:
                _ = self.rc.execute("post", self.requiredParameters.get("membershipUrl"),
                                    headers=self.header, data=json.dumps(data))
                self.LOG.info("Webex: User {} added to incident room/team".format(user))
            except IntegrationError as err:
                self.LOG.info("Webex: User {} is already a member of the room/team".format(user))


    def createRetrieveEntity(self):
        """
        Trys and retrieves room/team details if available, if not creates a new room/team

        Returns:
        --------
            room/team Id   (<str>) : Id of the room/team
            room/team Name (<str>) : Name of the room/team
        """
        self.requiredParameters[self.entityId] = None
        callingKey = "name" if self.entityName == "teamName" else "title"
        response = self.rc.execute("get", self.requiredParameters.get("entityURL"), headers=self.header, callback=self.check_response)
        res = response.json()
        if len(res.get('items')) == 0:
            self.createRoomTeam()
        else:
            for objs in res.get("items"):
                if objs.get(callingKey) == self.requiredParameters.get(self.entityName):
                    self.requiredParameters[self.entityId] = objs.get("id")
                    self.requiredParameters[self.entityName] = objs.get(callingKey)
                    self.LOG.info("Webex: Retrieving existing room/team: {}".format(self.requiredParameters[self.entityId]))
                    break
            if not self.requiredParameters.get(self.entityId):
                self.createRoomTeam()
                self.LOG.info("Webex: Creating new room/team: {}".format(self.requiredParameters[self.entityId]))
        self.retrieveMembershipURL = self.requiredParameters.get("entityURL") + self.requiredParameters.get(self.entityId)
        if self.entityName == "roomName":
            self.retrieveMembershipURL += "/meetingInfo"
        


    def createRoomTeam(self):
        """
        Creates a room/team with the required configurations such as:
            - room/team name
            - Existing teamId
            - list of Attendees

        Returns:
        -------
            room/team Id   (<str>) : Id of the room/team
            room/team Name (<str>) : Name of the room/team
        """
        callingKey = "name" if self.entityName == "teamName" else "title"
        data = {callingKey : self.requiredParameters.get(self.entityName)}
        if self.entityName == "roomName" and self.requiredParameters.get("teamId"):
            self.LOG.info("Webex: Adding team to room: {}".format(self.requiredParameters.get("teamId")))
            data["teamId"] = self.requiredParameters.get("teamId")
        response = self.rc.execute("post", self.requiredParameters.get("entityURL"),
                                    headers=self.header, data=json.dumps(data), callback=self.check_response)
        res = response.json()
        self.requiredParameters[self.entityId] = res.get("id")
        self.requiredParameters[self.entityName] = res.get(callingKey)
        self.LOG.info("Webex: Created new room/team: {}".format(self.requiredParameters[self.entityId]))


    def getEntityDetails(self):
        """
        Upon successfully creating a team, it retrieves the room details and returns the result back to
        the SOAR platform in the form of dictionary.

        Returns:
        --------
            (<dict>): response from the endpoint with room name and other information
        """
        response = self.rc.execute("get", self.retrieveMembershipURL, headers=self.header)
        self.LOG.info("Webex: Retrieved room/team details, room/team  Name : {}".format(self.requiredParameters.get(self.entityName)))
        response = response.json()
        response["attendees"] = ", ".join(self.emailIds)
        response["status"] = True
        response[self.entityName] = self.requiredParameters.get(self.entityName)
        return response


    def check_response(self, response):
        """
        A function to raise exceptions depending on the response from the endpoint

        Args:
        -----
            response (<response>): A response object from the server endpoint generated by the Request common

        Raises:
        -------
            FunctionError: Invalid API call methord passed to request common.
            FunctionError: Server rejected request due to malformed query.
            FunctionError: Invalid security context, check refresh token and scope.
        """
        if response is None:
            raise FunctionError("Invalid METHOD passed to webex_request!")
        if response.status_code not in [200, 201, 404]:
            raise FunctionError("API call failed! HTTP Status: {}, URL: {}".format(response.status_code, self.requiredParameters.get("meetingsURL")))
        elif response.status_code == 401:
            raise FunctionError("Security context is invalid, API returned 401!")
        return response