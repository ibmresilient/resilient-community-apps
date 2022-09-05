import json
import time, datetime

from fn_webex.lib import constants, cisco_commons
from resilient_lib import IntegrationError
from resilient_circuits import FunctionResult


class WebexMeetings:
    def __init__(self, requiredParameters, meetingParameters):
        self.requiredParameters = requiredParameters
        self.meetingParameters = meetingParameters
        self.response_handler = cisco_commons.ResponseHandler()
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
        self.LOG.info("Wenex Meeting: Timezone set to: {}".format(self.timezone))

        self.check_time(self.timezone, self.requiredParameters.get("start"), self.requiredParameters.get("end"))
        meetingOptions = self.generate_meeting_parameters(self.meetingParameters)

        response = self.rc.execute("post", webexurl, data=meetingOptions,
                                        headers=self.header, callback=self.response_handler.check_response)
        return response


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
            if meeting_start < datetime.datetime.now():
                raise IntegrationError(constants.MSG_INVLAID_STARTTIME.format(meeting_start.strftime(constants.DATETIME_FORMAT)))
        else :
            meeting_start = datetime.datetime.now() + datetime.timedelta(minutes=constants.MEETING_START_TIME_BUFFER)
        if meeting_end:
            meeting_end = datetime.datetime.fromtimestamp(meeting_end/constants.REMOVE_MILLISECONDS)
            _current_time = datetime.datetime.now().strftime(constants.DATETIME_FORMAT)
            if meeting_end < meeting_start:
                raise IntegrationError(constants.MSG_INVALID_ENDTIME.format(
                    meeting_end.strftime(constants.DATETIME_FORMAT), meeting_start.strftime(constants.DATETIME_FORMAT), _current_time))
            elif meeting_end < datetime.datetime.now():
                raise IntegrationError(constants.MSG_INVALID_ENDTIME.format(
                    meeting_end.strftime(constants.DATETIME_FORMAT), meeting_start.strftime(constants.DATETIME_FORMAT), _current_time))
        else:
            meeting_end = meeting_start + datetime.timedelta(minutes=constants.DEFAULT_MEETING_LENGTH)

        self.meeting_start_time = meeting_start.strftime(constants.DATETIME_FORMAT) + timezone
        self.meeting_end_time   = meeting_end.strftime(constants.DATETIME_FORMAT) + timezone


    def get_timeZones(self, timezone):
        '''
        This function determines and formats the timezone for the meeting. If no timezone is provided, 
        the application automatially assigns systems local timezone. The timezone is to be provided in
        the form of a sting in the specified formats: UTC -05:30. The function
        automatically formats the timezone in accordance with the webex api requirements.

        Args:
        ---------
        timezone : String
                    Timezone to be provided as a sting. Acceptable format 
                    UTC +01:00
        '''
        if timezone is None:
            return time.strftime("%z", time.localtime())
        else:
            timezone = timezone.strip()
        timezone = timezone.replace(":", "")
        timezone = timezone.split(" ")
        if len(timezone) > 1:
            timezone = timezone[1].strip()
            if "+" not in timezone and "-" not in timezone:
                timezone = "".join(["+", timezone])
        else:
            raise IntegrationError(constants.MSG_INVALID_TIMEZONE)
        if not timezone[1:].isdigit():
            raise IntegrationError(constants.MSG_INVALID_TIMEZONE)
        return timezone


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
