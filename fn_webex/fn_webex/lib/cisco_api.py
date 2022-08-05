# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

import time
import datetime
import json

from resilient_lib import IntegrationError
from resilient_circuits import FunctionError
from multiprocessing import AuthenticationError

DEFAULT_MEETING_LENGTH = 45


class WebexAPI:
    def __init__(self, requiredParameters, optionalParameters):
        self.resclient = requiredParameters["resclient"]
        self.optionalParameters = optionalParameters
        self.requiredParameters = requiredParameters
        self.rc = self.requiredParameters.get("rc")
        self.LOG = self.requiredParameters["logger"]
        self.timezone = self.get_timeZones(self.requiredParameters.get("timezone"))
        self.check_time(self.timezone, self.requiredParameters["start"], self.requiredParameters["end"])


    def Authenticate(self):
        '''
        Helper method that establishes a connection with the Client servers and performs an OAuth
        authentication. The server returns a beareID for the session, which then is used to make
        requests. This bearerID is incorporated with the header for every request henceforth
        '''
        self.bearerID = self.generate_bearerID()
        self.header = self.generate_header(self.bearerID)


    def generate_bearerID(self):
        '''
        This function perfroms OAuth authentication and retrieves the bearerID which is necessary
        to interact with the webex endpoint.

        Options:
        -------
        client_id : This ID is generated while creating an integration on the webex endpoint
        
        
        '''
        data = {
            "client_id": self.requiredParameters["clientID"],
            "scope": self.requiredParameters["scope"],
            "client_secret": self.requiredParameters["clientSecret"],
            "refresh_token": self.requiredParameters["refreshToken"],
            "grant_type": "refresh_token"
        }
        try:
            result = self.rc.execute("POST", self.requiredParameters["tokenURL"], data=data)
        except IntegrationError as err:
                raise IntegrationError("Unable to authenticate: Error: Is the refresh_token up to date?")

        if "access_token" in result.json():
            return result.json().get("access_token")

        msg = u"Unable to authenticate: Error: {}\nDescription: {}"\
            .format(result.json().get("error"), result.json().get("error_description"))
        raise FunctionError(msg)


    def convert_to_dict(self, to_convert):
        '''
        The primary purpose of this function is to covert a string in a json format to a dictionary.
        This function will be replaced with json.loads() function from the json library.

        Arguments:
        ---------
        to_convert : String
                     Any string in a json format (key value pair) can be passed in as a string
        '''
        ret = {}
        for bracket in ["[", "]", "{", "}", "\""]:
            to_convert = to_convert.replace(bracket,"")
        for pair in to_convert.split(","):
            key = pair.split(":")[0]
            value = pair[len(key)+1:]
            ret[key] = value
        return ret

    def generate_attendee_list(self):
        def isDirectMember(ids):
            for user in orgMemberList:
                if ids == user.get("id"): 
                    return user.get("email")
                
        def isGroupMember(ids):
            ret = []
            for group in orgGroupList:
                if ids == group.get("id"):
                    for member in group.get("members"):
                        ret.append(isDirectMember(member))
            return ret

        emailIDs = []
        incidentMembers = self.resclient.get("/incidents/{}/members".format(self.requiredParameters["incidentID"]))
        orgMemberList   = self.resclient.post("/users/query_paged?return_level=normal", payload={}).get("data")
        orgGroupList    = self.resclient.get("/groups")

        if self.requiredParameters["addAllMembers"]:
            if len(incidentMembers.get("members")) == 0:
                self.LOG.info("Webex: There are no members assigned to this incident")
            for incident_member in incidentMembers.get("members"):
                if isDirectMember(incident_member):
                    emailIDs.append(isDirectMember(incident_member))
                elif isGroupMember(incident_member):
                    emailIDs.extend(isGroupMember(incident_member))
        elif self.requiredParameters["additionalAttendee"].lower().strip() == "none":
            raise ValueError("Error: Failed to add participants to the meeting. ADD_ALL_INCIDENT_MEMBERS was set to NO and no list of participants were provided in the ADDITIONAL_ATTENDEE field.")
        
        if self.requiredParameters["additionalAttendee"].lower().strip() != "none":
            emailIDs += self.requiredParameters["additionalAttendee"].lower().strip().replace(" ", "").split(",")
        self.emailIDs = emailIDs
        self.LOG.info("Webex: Members to be added to the room {}".format(self.emailIDs))


    def createRetrieveRoom(self):
        response = self.rc.execute("get", "https://webexapis.com/v1/rooms/", headers=self.header, proxies=self.rc.get_proxies())
        res = json.loads(response.text)
        if len(res.get('items')) == 0:
            data = "{\"title\" : \"Incident " + self.requiredParameters["incidentID"] + ": " + self.optionalParameters["title"] + "\"}"
            response = self.rc.execute("post", "https://webexapis.com/v1/rooms/", headers=self.header, data=data, proxies=self.rc.get_proxies())
            res = json.loads(response.text)
            self.requiredParameters["roomID"] = res.get("id")
            self.LOG.info("Webex: Creating new room: {}".format(self.requiredParameters["roomID"]))
        else:
            self.requiredParameters["roomID"] = res.get("items")[0].get("id")
            self.LOG.info("Webex: Retrieving existing room: {}".format(self.requiredParameters["roomID"]))

    def addMembership(self):
        for user in self.emailIDs:
            data = "{\"roomId\" : \"" + self.requiredParameters["roomID"] + "\", \"personEmail\" : \"" + user + "\"}" 
            try:
                _ = self.rc.execute("post", "https://webexapis.com/v1/memberships", headers=self.header, data=data, proxies=self.rc.get_proxies())
                self.LOG.info("Webex: User {} added to incident room".format(user))
            except IntegrationError as err:
                self.LOG.info("Webex: User {} is already a member of the room".format(user))
                

    def create_meeting(self):
        '''
        Gathers all the required parameters to schedule a meeting and generates an output based
        on the response from endpoint server.
        '''
        meetingOptions = self.generate_meeting_parameters(self.optionalParameters)
        response = self.webex_request("POST", meetingOptions)

        if not response.text:
            raise FunctionError("Failed to create meeting, null response")
        
        results = self.convert_to_dict(response.text)
        if response.status_code == 200:
            results["status"] = True
        else:
            results["status"] = False
            raise FunctionError("Failed to create meeting")
        return results


    def check_time(self, timezone, meeting_start, meeting_end):
        '''
        This function determines and formats the meeting start and end time as per the webex api
        requirements. The meeting start and end datetime is specified in the forma of a timestamp. 
        These values are then converted to ISO 8601 format and passed on to the webex api. This 
        function provides the user with a certain level of flexibility when it comes to specifying 
        the meeting start and end time. For instance:

            * Only if end time is specified: meeting will start at 2 minutes from current time 
              till the specified end time
            * Only if start time is specified, meeting will start from the specified start time
              till 45 minutes from the start time
            * If neither meeting start or end time is specified meeting starts 2 minutes from 
              current time till 45 minutes from the start time

        Arguments:
        ---------
        timezone      : String
                        The timezone in accordance to which the meeting is to be scheduled
        meeting_start : Integer
                        Meeting start date and time in timestamp format
        meeting_end   : Integer
                        Meeting end date and time in timestamp format
        '''
        if meeting_start is not None:
            meeting_start = datetime.datetime.fromtimestamp(meeting_start/1000)
        else :
            meeting_start = datetime.datetime.now() + datetime.timedelta(minutes=2)
        if meeting_end is not None:
            meeting_end = datetime.datetime.fromtimestamp(meeting_end/1000)
            if meeting_end < meeting_start:
                raise ValueError('Meeting end time {}, must be after meeting start time {}'.format(
                    meeting_end.strftime('%Y-%m-%dT%H:%M:%S'), meeting_start.strftime('%Y-%m-%dT%H:%M:%S')))
            elif meeting_end < datetime.datetime.now():
                raise ValueError('Meeting end time {}, must be after current time {}'.format(
                    meeting_end.strftime('%Y-%m-%dT%H:%M:%S'), datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')))
        else:
            meeting_end = meeting_start + datetime.timedelta(minutes=DEFAULT_MEETING_LENGTH)

        self.meeting_start_time = meeting_start.strftime('%Y-%m-%dT%H:%M:%S') + timezone
        self.meeting_end_time   = meeting_end.strftime('%Y-%m-%dT%H:%M:%S') + timezone


    def generate_header(self, bearerID):
        '''
        Checks for bearerID and returns it in a json format for request header
        
        Arguments:
        ---------
        bearerID : Integer
                   Session ID that is required for authentication
        '''
        if not bearerID:
            raise ValueError("Bearer ID not specified")
        return {
            'Authorization' : "Bearer {}".format(bearerID),
            'Content-Type'  : 'application/json'}


    def get_timeZones(self, timezone):
        '''
        This function determines and formats the timezone for the meeting. If no timezone is provided, 
        the application automatially assigns systems local timezone. The timezone is to be provided in
        the form of a sting in the specified formats: GMT +01:00 or UMT -0500 or -05:30. The function
        automatically formats the timezone in accordance with the webex api requirements.

        Arguments:
        ---------
        timezone : String
                   Timezone to be provided as a sting. Acceptable format 
                   GMT -01:00, GMT -0100, UMT -01:00, -01:00
        '''
        if timezone is None:
            return time.strftime("%z", time.localtime())
        else:
            timezone = timezone.strip()
        formatted_timezone = ""
        _temp = timezone.split(" ")
        if len(_temp) > 1:
            if "gmt" in _temp[0].lower() or "utc" in _temp[0].lower():
                if "-" not in _temp[1] and "+" not in _temp[1]:
                    formatted_timezone = "+"
                formatted_timezone += _temp[1].replace(":", "")
            else:
                raise ValueError("Unsupported timezone specified. Supported timezones GMT or UTC")
        elif len(_temp) == 1:
            if "-" not in timezone and "+" not in timezone:
                formatted_timezone = "+"
            formatted_timezone += timezone.replace(":", "")
        
        if not formatted_timezone[1:].isdigit():
            raise ValueError("Invalid Timezone format. Expected format GMT -01:00")
        return formatted_timezone 


    def generate_meeting_parameters(self, meetingParameters):
        '''
        Formating the meeting parameters in json format
        
        Arguments:
        ---------
        meetingParameters : dict
                            required meeting settings in the form of a json
        '''
        request_parameters = '{\"start\":\"' + self.meeting_start_time + '\", \"end\":\"' + self.meeting_end_time + '\"'
        for key in meetingParameters.keys():
            request_parameters +=  ', \"{}\":\"{}\" '.format(key, meetingParameters[key])
        request_parameters +=  "}"
        return request_parameters


    def webex_request(self, method, data):
        """
        Wrapper for requests, appends content-type and fills in site url
        
        Arguments:
        ---------
        method  : String
                  request execution method
        data    : String
                  request body
        """
        webexurl = self.requiredParameters.get("siteURL")
        response = self.rc.execute(method, webexurl, data=data,
                                        headers=self.header, proxies=self.rc.get_proxies())
        if response is None:
            raise FunctionError("Invalid METHOD passed to webex_request! Method: {}".format(method))
        if response.status_code not in [200, 201, 401]:
            raise FunctionError("API call failed! HTTP Status: {}, URL: {}".format(response.status_code, webexurl))
        elif response.status_code == 401:
            raise FunctionError("Security context is invalid, API returned 401!")
        return response
        