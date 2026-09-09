# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
import json

from urllib import parse
from resilient_lib import IntegrationError
from resilient_circuits import FunctionResult

from fn_webex.lib import constants, cisco_commons


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
            entity_Id          (<str>)  : Team or Room ID
            entity_name        (<str>)  : Team or Room Name
            entity_url         (<str>)  : Teams API URL
            membershipURL      (<str>)  : Teams Membership API URL

        Returns:
        --------
            Response          (<dict>)  : A response with the room/team options and details
                                          or the error message if the meeting creation
                                          fails
    """
    def __init__(self, requiredParameters):
        self.required_parameters = requiredParameters
        self.rc = self.required_parameters.get("rc")
        self.header = self.required_parameters.get("header")
        self.LOG = self.required_parameters.get("logger")
        self.resclient = self.required_parameters.get("resclient")
        self.response_handler = cisco_commons.ResponseHandler()
        self.entity_Id, self.entity_name = None, None
        self.email_ids, self.entity_type = None, None
        self.retrieve_membership_url = None


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

        Returns:
        --------
            (<FunctionResult>): A dictionary with the response, the reason
                    should the operation fail, and a success
                    flag.
        '''
        try:
            self.find_api()
            self.generate_member_list()
            self.retrieve_entity()
            self.add_membership()
            response = self.get_entity_details()
            return FunctionResult(response, success=True)
        except IntegrationError as err:
            return FunctionResult(None, success=False, reason = str(err))


    def find_api(self):
        """
        This function detemines the operaiton that is being perofrmed. All the below functions
        work for Room as well as teams. So this detemine the API to be used.

        Returns:
        --------
            entity_url  (<str>): Teams or Room api URL
            entity_type (<str>): Teams or Room api selector
            entity_name (<str>): teamName or RoomName depending on the API
            calling_key (<str>): name or title depending on the API to fetch
                                title of the entity.
        """
        self.entity_url  = self.required_parameters.get("entityURL")
        self.entity_type = self.required_parameters.get("entityType")
        self.entity_name = self.required_parameters.get("entityName")
        self.calling_key = constants.TEAMS_CALLING_KEY if self.entity_type == constants.TEAM else constants.ROOMS_CALLING_KEY

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
            email_ids (<list>) : a list of all participant email addresses to be added
        """
        email_ids = []
        if self.required_parameters.get("taskId"):
            incidentMembers = self.resclient.get(parse.urljoin(constants.RES_TASK,
                        "{}/members".format(self.required_parameters.get("taskId"))))
        else:
            incidentMembers = self.resclient.get(parse.urljoin(constants.RES_INCIDENT,
                                "{}/members".format(self.required_parameters.get("incidentId"))))
        org_member_list = self.resclient.post(constants.RES_USERS, payload={}).get("data")
        org_group_list  = self.resclient.get(constants.RES_GROUPS)
        if self.required_parameters.get("addAllMembers"):
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


    def add_membership(self):
        """
        Adds members to the room/team using the email addresses from >>email_ids<<. If user already
        a member of the room/team, ignores.
        """
        idName = constants.TEAM_ID if self.entity_type == constants.TEAM else constants.ROOM_ID
        for user in self.email_ids:
            data = {idName : self.entity_Id, "personEmail" : user}
            try:
                _ = self.rc.execute("post", self.required_parameters.get("membershipUrl"),
                    headers=self.header, data=json.dumps(data))
                self.LOG.info("Webex: User {} added to incident {}".format(user,
                    self.entity_type))
            except IntegrationError:
                self.LOG.info("Webex: User {} is already a member of the room/team".format(user))


    def retrieve_entity(self):
        """
        Trys and retrieves room/team details if available, if not creates a new room/team

        Returns:
        --------
            room/team Id   (<str>) : Id of the room/team
            room/team Name (<str>) : Name of the room/team
        """
        self.entity_Id = None
        res = self.rc.execute("get", self.entity_url,
            headers=self.header, callback=self.response_handler.check_response)
        if len(res.get('items')) == 0:
            self.create_entity()
        else:
            for objs in res.get("items"):
                if objs.get(self.calling_key) == self.entity_name:
                    self.LOG.info("Webex: Retrieving existing room/team: {}".format(
                        self.entity_Id))
                    raise IntegrationError(constants.MSG_ENTITY_EXISTS.format(self.entity_type,
                        self.entity_name))
            if not self.entity_Id:
                self.create_entity()
                self.LOG.info("Webex: Creating new room/team: {}".format(
                    self.entity_Id))
        retrieve_membership_url = parse.urljoin(self.entity_url, self.entity_Id + "/")
        if self.entity_type == constants.ROOM:
            retrieve_membership_url = parse.urljoin(retrieve_membership_url, "meetingInfo")
        self.retrieve_membership_url = retrieve_membership_url


    def create_entity(self):
        """
        Creates a room/team with the required configurations such as:
            * room/team name
            * Existing teamId
            * list of Attendees

        Returns:
        -------
            room/team Id   (<str>) : Id of the room/team
            room/team Name (<str>) : Name of the room/team
        """
        data = {self.calling_key : self.entity_name}
        if self.entity_type == constants.ROOM and self.required_parameters.get(constants.TEAM_ID):
            self.LOG.info(constants.LOG_ADD_TEAM_TO_ROOM.format(
                self.required_parameters.get(constants.TEAM_ID)))
            data[constants.TEAM_ID] = self.required_parameters.get(constants.TEAM_ID)
        res = self.rc.execute("post", self.entity_url,
            headers=self.header, data=json.dumps(data),
            callback=self.response_handler.check_response)
        self.entity_Id = res.get("id")
        self.entity_name = res.get(self.calling_key)
        self.LOG.info(constants.LOG_CREATING_NEW_ENTITY.format(self.entity_type, self.entity_Id))


    def get_entity_details(self):
        """
        Upon successfully creating a team, it retrieves the room details and returns the
        result back to the SOAR platform in the form of dictionary.

        Returns:
        --------
            (<dict>): response from the endpoint with room name and other information
        """
        response = self.rc.execute("get", self.retrieve_membership_url,
            headers=self.header, callback=self.response_handler.check_response)
        self.LOG.info(constants.LOG_RETRIVING_ENTITY_DETAILS.format(self.entity_type,
            self.entity_name))
        response["id"] = self.entity_Id
        response["name"] = self.entity_name
        response["attendees"] = ", ".join(self.email_ids)
        return response
