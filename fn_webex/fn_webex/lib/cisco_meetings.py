import json
import time, datetime

from fn_webex.lib import constants, cisco_commons
from resilient_circuits import FunctionError


class WebexMeetings:
    def __init__(self, requiredParameters, meetingParameters):
        self.requiredParameters = requiredParameters
        self.meetingParameters = meetingParameters
        self.check_response = cisco_commons.check_response
        self.rc = requiredParameters.get("rc")
        self.LOG = requiredParameters.get("logger")
        self.header = requiredParameters.get("header")


    def create_meeting(self):
        '''
        Gathers all the required parameters to schedule a meeting and generates an output based
        on the response from endpoint server. This methord needs to be called externally and usually
        is the entry point to creating a meeting.
        
        Returns:
        --------
            (<dict>) : Vital meeting information and other configurations of the scheduled meeting
        '''
        webexurl = self.requiredParameters.get("meetingsURL")
        self.timezone = self.get_timeZones(self.requiredParameters.get("timezone"))
        self.LOG.info("Timezone set to: {}".format(self.timezone))
        self.check_time(self.timezone, self.requiredParameters.get("start"), self.requiredParameters.get("end"))
        meetingOptions = self.generate_meeting_parameters(self.meetingParameters)

        response = self.rc.execute("post", webexurl, data=meetingOptions,
                                        headers=self.header, callback=self.check_response)
        if not response.text:
            raise FunctionError("Failed to create meeting, null response")
        results = response.json()
        
        if response.status_code == 200:
            results["status"] = True
        else:
            results["status"] = False
            raise FunctionError("Failed to create meeting")
        return results


    def check_time(self, timezone, meeting_start, meeting_end):
        """
        This function determines and formats the meeting start and end time as per the webex api
        requirements. The meeting start and end datetime is specified in the forma of a timestamp. 
        These values are then converted to ISO 8601 format and passed on to the webex api. This 
        function provides the user with a certain level of flexibility when it comes to specifying 
        the meeting start and end time. For instance:

            - Only if end time is specified: meeting will start from current time + time in minutes 
              specified in MEETING_START_TIME_BUFFER
            - Only if start time is specified, meeting will start from the specified start time
              till 45 minutes from the start time
            - If neither start nor end time is specified, meeting starts from current time + time in
              minutes specified in MEETING_START_TIME_BUFFERto 45 minutes from the start time

        Args:
        -----
            timezone      (<str>) : The timezone in accordance to which the meeting is to be scheduled
            meeting_start (<int>) : Meeting start date and time in timestamp format
            meeting_end   (<int>) : Meeting end date and time in timestamp format

        Returns:
        --------
            meeting_start_time (<datetime>) : Meeting start datetime in ISO 8601 format
            meeting_end_time   (<datetime>) : Meeting end datetime in ISO 8601 format
        """
        if meeting_start:
            meeting_start = datetime.datetime.fromtimestamp(meeting_start/constants.REMOVE_MILLISECONDS)
        else :
            meeting_start = datetime.datetime.now() + datetime.timedelta(minutes=constants.MEETING_START_TIME_BUFFER)
        if meeting_end:
            meeting_end = datetime.datetime.fromtimestamp(meeting_end/constants.REMOVE_MILLISECONDS)
            if meeting_end < meeting_start:
                raise ValueError('Meeting end time {}, must be after meeting start time {}'.format(
                    meeting_end.strftime(constants.DATETIME_FORMAT), meeting_start.strftime(constants.DATETIME_FORMAT)))
            elif meeting_end < datetime.datetime.now():
                raise ValueError('Meeting end time {}, must be after current time {}'.format(
                    meeting_end.strftime(constants.DATETIME_FORMAT), datetime.datetime.now().strftime(constants.DATETIME_FORMAT)))
        else:
            meeting_end = meeting_start + datetime.timedelta(minutes=constants.DEFAULT_MEETING_LENGTH)

        self.meeting_start_time = meeting_start.strftime(constants.DATETIME_FORMAT) + timezone
        self.meeting_end_time   = meeting_end.strftime(constants.DATETIME_FORMAT) + timezone


    def get_timeZones(self, timezone):
        '''
        This function determines and formats the timezone for the meeting. If no timezone is provided, 
        the application automatially assigns systems local timezone. The timezone is to be provided in
        the form of a sting in the specified formats: GMT +01:00 or UMT -0500 or -05:30. The function
        automatically formats the timezone in accordance with the webex api requirements.

        Args:
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
        Formating the meeting parameters into key-value pairs
        
        Args:
        -----
            meetingParameters (<dict>) : required meeting settings in the form of a json

        Returns:
        --------
            (<str>) : Meeting options in a key-value pairs
        '''
        request_parameters = {"start" : self.meeting_start_time, "end" : self.meeting_end_time}
        for key in meetingParameters.keys():
            request_parameters[key] = meetingParameters.get(key)
        return json.dumps(request_parameters)
