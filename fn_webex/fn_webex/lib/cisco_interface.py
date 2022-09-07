# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
import json

from urllib import parse
from fn_webex.lib import constants, cisco_commons
from resilient_lib import IntegrationError
from resilient_circuits import FunctionResult


class WebexInterface:
    """
        This application allows for creating a team or a room using the Cisco Webex API. This
        provides SOAR with the ability to create teams and rooms from within a SOAR incident
        or a task. 

        Inputs:
        -----
            teamName           (<str>)  : Name of the team to be created
            incidentId         (<str>)  : Incident ID
            addAllMembers      (<bool>) : Adds all members of the incident to the team
            additionalAttendee (<str>)  : Additonal attendees to be added
            entityId           (<str>)  : always >>teamId<<
            entityName         (<str>)  : always >>teamName<<
            entityURL          (<str>)  : Teams API URL
            membershipURL      (<str>)  : Teams Membership API URL

        Returns:
        --------
            Response          (<dict>)  : A response with the room/team options and details
                                          or the error message if the meeting creation
                                          fails

    """
    def __init__(self, requiredParameters):
        self.requiredParameters = requiredParameters
        self.rc = self.requiredParameters.get("rc")
        self.header = requiredParameters.get("header")
        self.LOG = self.requiredParameters.get("logger")
        self.resclient = requiredParameters.get("resclient")
        self.response_handler = cisco_commons.ResponseHandler()


    def create_team_room(self):
        '''
        A wrapper function that allows for creating a team or a room. For a room or a team
        to be created, the following functions are executed in the specified order.

            * find_operation       : Determines if a room or team is to be created.
            * generate_member_list : Generates a list of members to be added.
            * retrieve_entity      : Tries to find a room or a team with the same name.
                                     Else creates a new one using create_entity
            * add_membership       : Adds the list of members to the room or team
            * get_entity_details   : Retrieves the room/team information
        '''
        self.find_operation()
        self.generate_member_list()
        self.retrieve_entity()
        self.add_membership()
        return self.get_entity_details()

      
    def find_operation(self):
        """
        This function detemines the operaiton that is being perofrmed. All the below functions
        work for Room as well as teams. So this detemine the API to be used.

        Returns:
        --------
            entityId   (<str>): teamId or RoomId depending on the API
            entityName (<str>): teamName or RoomName depending on the API
        """
        self.entityId   = self.requiredParameters.get("entityId")
        self.entityName = self.requiredParameters.get("entityName")


    def is_direct_member(self, incidentMemberId, orgMemberList):
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


    def is_group_member(self, incidentMemberId, orgMemberList, orgGroupList):
        """
        Checks to see if the member Id accquired from the incident belongs to the list of
        all groups from the organization. Upon match, it then queries a list of Ids 
        associated with that group and matches with user using the >>is_direct_member<< 
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
                    ret.append(self.is_direct_member(member, orgMemberList))
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
        incidentMembers = self.resclient.get(parse.urljoin(constants.RES_INCIDENT, "{}/members".format(self.requiredParameters.get("incidentId"))))
        orgMemberList   = self.resclient.post(constants.RES_USERS, payload={}).get("data")
        orgGroupList    = self.resclient.get(constants.RES_GROUPS)

        if self.requiredParameters.get("addAllMembers"):
            if len(incidentMembers.get("members")) == 0:
                self.LOG.info("Webex: There are no members assigned to this incident")
            for incident_member in incidentMembers.get("members"):
                if self.is_direct_member(incident_member, orgMemberList):
                    emailIds.append(self.is_direct_member(incident_member, orgMemberList))
                elif self.is_group_member(incident_member, orgMemberList, orgGroupList):
                    emailIds.extend(self.is_group_member(incident_member, orgMemberList, orgGroupList))
        elif not self.requiredParameters.get("additionalAttendee"):
            self.LOG.warn("Warning: No participants were added to the room/team. ADD_ALL_INCIDENT_MEMBERS was set to NO and no list of participants were provided in the ADDITIONAL_ATTENDEE field.")
        
        if self.requiredParameters.get("additionalAttendee"):
            emailIds += self.requiredParameters.get("additionalAttendee").lower().replace(" ", "").split(",")
        self.emailIds = emailIds
        self.LOG.info("Webex: Members to be added to the room/team {}".format(self.emailIds))


    def add_membership(self):
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


    def retrieve_entity(self):
        """
        Trys and retrieves room/team details if available, if not creates a new room/team

        Returns:
        --------
            room/team Id   (<str>) : Id of the room/team
            room/team Name (<str>) : Name of the room/team
        """
        self.requiredParameters[self.entityId] = None
        callingKey = "name" if self.entityName == "teamName" else "title"
        res = self.rc.execute("get", self.requiredParameters.get("entityURL"), headers=self.header, callback=self.response_handler.check_response)
        if len(res.get('items')) == 0:
            self.create_entity()
        else:
            for objs in res.get("items"):
                if objs.get(callingKey) == self.requiredParameters.get(self.entityName):
                    self.requiredParameters[self.entityId] = objs.get("id")
                    self.requiredParameters[self.entityName] = objs.get(callingKey)
                    self.LOG.info("Webex: Retrieving existing room/team: {}".format(self.requiredParameters.get(self.entityId)))
                    break
            if not self.requiredParameters.get(self.entityId):
                self.create_entity()
                self.LOG.info("Webex: Creating new room/team: {}".format(self.requiredParameters.get(self.entityId)))
        retrieveMembershipURL = parse.urljoin(self.requiredParameters.get("entityURL"), self.requiredParameters.get(self.entityId) + "/")
        if self.entityName == "roomName":
            retrieveMembershipURL = parse.urljoin(retrieveMembershipURL, "meetingInfo")
        self.retrieveMembershipURL = retrieveMembershipURL


    def create_entity(self):
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
        res = self.rc.execute("post", self.requiredParameters.get("entityURL"),
                                    headers=self.header, data=json.dumps(data), callback=self.response_handler.check_response)
        self.requiredParameters[self.entityId] = res.get("id")
        self.requiredParameters[self.entityName] = res.get(callingKey)
        self.LOG.info("Webex: Created new room/team: {}".format(self.requiredParameters.get(self.entityId)))


    def get_entity_details(self):
        """
        Upon successfully creating a team, it retrieves the room details and returns the result back to
        the SOAR platform in the form of dictionary.

        Returns:
        --------
            (<dict>): response from the endpoint with room name and other information
        """
        response = self.rc.execute("get", self.retrieveMembershipURL, headers=self.header, callback=self.response_handler.check_response)
        self.LOG.info("Webex: Retrieved room/team details, room/team  Name : {}".format(self.requiredParameters.get(self.entityName)))
        response["attendees"] = ", ".join(self.emailIds)
        response["status"] = True
        response[self.entityName] = self.requiredParameters.get(self.entityName)
        return response


    def delete_entity(self):
        """
        This function deletes a room or a team based on the id specified to it. It monitors the response returned
        from the endpoint for 204, 404 and 405 responses. 

        Response Codes:
        ---------------
            204 - Successfully deleted the room or team.
            404 - Room or team not found.
            405 - Room cannot be deleted, delete the team associated.

        Returns:
        --------
            (<dict>): Response from the endpoint
        """
        if "room" in self.requiredParameters.get("entityName").strip().lower():
            deletionURL = parse.urljoin(self.requiredParameters.get("baseURL"), constants.ROOMS_URL)
        else :
            deletionURL = parse.urljoin(self.requiredParameters.get("baseURL"), constants.TEAMS_URL)
        deletionURL = parse.urljoin(deletionURL, self.requiredParameters.get("entityId"))
        self.LOG.info("Webex: Deleting {}".format(self.requiredParameters.get("entityName")))
        self.response_handler.add_exempt_codes(codes=[404, 405])
        response = self.rc.execute("delete", deletionURL, headers=self.header, callback=self.response_handler.check_response)
        self.response_handler.clear_exempt_codes()
        if response.get("status_code") == 204:
            return FunctionResult(response, success=True)
        elif response.get("status_code") == 404:
            return FunctionResult(response, success=False, reason="The specified room/team ID could not be found!")
        elif response.get("status_code") == 405:
            return FunctionResult(response, success=False, reason="This room cannot be deleted directly. Delete the team associated with it to clear this space.")
        else:
            return FunctionResult(response, success=False, reason="Unfamiliar response. Status code : {}".format(response.get("status_code")))

