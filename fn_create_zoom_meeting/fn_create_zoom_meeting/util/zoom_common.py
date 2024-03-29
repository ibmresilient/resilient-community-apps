# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

from resilient_lib import RequestsCommon
import json
import base64
import time
import datetime
import logging
from resilient_circuits import FunctionError
try:
    from urlparse import urlparse, parse_qs
    from urllib import urlencode
except:
    from urllib.parse import urlencode, urlparse, parse_qs

LOG = logging.getLogger(__name__)
PWD_IN_URL = "pwd"
AUTH_URL = "https://zoom.us/oauth/token?grant_type=account_credentials&account_id="
USERS_PATH = "/users?status=active&page_size=30&page_number="

class ZoomCommon:

    def __init__(self, opts, options):
        self.opts = opts
        self.options = options
        self.api_url = options.get("zoom_api_url")
        self.account_id = options.get("zoom_account_id")
        self.client_id = options.get("zoom_client_id")
        self.client_secret = options.get("zoom_client_secret")


    def generate_auth_token(self):
        """Generates authentication token used to authenticate with Zoom API"""
        req_common = RequestsCommon(self.opts, self.options)
        url = f"{AUTH_URL}{self.account_id}"
        auth_str = f"{self.client_id}:{self.client_secret}"
        auth_bytes = base64.b64encode(auth_str.encode("utf-8"))
        encoded_auth = str(auth_bytes, "utf-8")
        headers = {
            "Authorization" : f"Basic {encoded_auth}" 
        }
        response = req_common.execute("post", url, headers=headers).json()
        return response["access_token"]

    def zoom_request(self, path=None, method="GET", query=None, headers=None):
        """Generates and makes specified request to Zoom API"""
        url = self.api_url + path
        
        access_token = self.generate_auth_token()
        headers = {'Authorization': f'Bearer {access_token}',
               'Content-type': 'application/json'}
        
        
        req_common = RequestsCommon(self.opts, self.options)

        response = None
        if method == "GET":
            response = req_common.execute('get', url, headers=headers, verify=False)
        elif method == "POST":
            response = req_common.execute('post', url, json=query, verify=True, headers=headers)

        if response is None:
            raise FunctionError("Invalid METHOD passed to zoom_request! Method: {}".format(method))

        if response.status_code != 200 and response.status_code != 201 and response.status_code != 401:
            raise FunctionError("API call failed! HTTP Status: {}, URL: {}".format(response.status_code, url))
        elif response.status_code == 401:
            # access token probably expired
            access_token = self.generate_auth_token()
            return self.zoom_request(path, method, query, headers)

        return response

    def get_zoom_host_id(self, host_email):
        """Gets the Zoom User ID of the host"""
        path = USERS_PATH
        users_request = self.zoom_request(path + "1")
        user_data = json.loads(users_request.text)

        for page_number in range(0, user_data.get("page_count")):
            current_page_data = json.loads(self.zoom_request(path + str(page_number + 1)).text)
            for user in current_page_data.get("users"):
                if user.get("email") == host_email:
                    return user.get("id")

    @staticmethod
    def generate_meeting_post(agenda_string, record_boolean, post_time, topic, password, timezone):
        """Generates the request that will be used to create the zoom meeting"""
        set_auto_recording = "none"
        if record_boolean:
            set_auto_recording = "local"

        # https://zoom.github.io/api/#meetings
        data = {
            "topic": topic,  # Meeting topic
            "type": 1,  # Meeting type (1 = Instant meeting, 2 = Scheduled meeting, 3 = Recurring meeting no fixed time, 8 = Recurring meeting fixed time)
            "start_time": post_time,  # Meeting start time
            "duration": 0,  # Meeting duration, only used for scheduled meetings
            "timezone": timezone,  # Timezone of start_time, list: https://zoom.github.io/api/#timezones
            "password": password,  # Meeting password
            "agenda": agenda_string,  # Meeting description
            "recurrence": {
                "type": 1,  # Recurrence meeting type (1 = Daily, 2 = Weekly, 3 = Monthly)
                "repeat_interval": 0,  # Interval meeting should repeat
                "weekly_days": 1,  # Days of the week meeting should repeat, separated by comma
                "monthly_day": 0,  # Day of the month for the meeting to be scheduled
                "monthly_week": -1,  # Week for which the meeting should recur each month
                "monthly_week_day": 1,  # Day for which the meeting should recur each month
                "end_times": 0,  # How many times meeting should occur before it is canceled
                "end_date_time": post_time  # End date time
            },
            "settings": {"host_video": True,  # Start video when host joins meeting
                         "participant_video": True,  # Start video when participants join meeting
                         "cn_meeting": False,  # Host meeting in China
                         "in_meeting": False,  # Host meeting in India
                         "join_before_host": False,  # Allow participants to join before host starts meeting (only for scheduled or recurring meetings)
                         "mute_upon_entry": False,  # Mute participants on entry
                         "watermark": False,  # Add watermark when viewing shared screen
                         "use_pmi": False,  # Personal meeting ID, only for scheduled and recurring meetings w/ no fixed time
                         "approval_type": 2,  # (0 = Automatically approve, 1 = Manually approve, 2 = No Reg. Required)
                         "registration_type": 1,  # Registration type (only for recurring meetings)
                         "audio": "both",  # Determine how participants can join the audio portion of the meeting
                         "auto_recording": set_auto_recording,    # turn on option to save recording locally
                         "enforce_login": True    # Only signed-in users can join this meeting
                         }
        }

        LOG.debug(json.dumps(data))

        return data

    def create_meeting(self, host_email, agenda_string, record_boolean, meeting_topic, meeting_password, timezone):
        """Creates a Zoom Meeting"""
        access_token = self.generate_auth_token()

        meeting_time = datetime.datetime.now()  # type: datetime
        post_time_format = meeting_time.strftime('yyyy-MM-dd\'T\'HH:mm:ss%Z')
        meeting_time = meeting_time.strftime('%m/%d/%Y %H:%M:%S')

        query = self.generate_meeting_post(agenda_string, record_boolean, post_time_format, meeting_topic, meeting_password, timezone)
        host_id = self.get_zoom_host_id(host_email)
        if host_id is None:
            raise FunctionError("Unable to find user with that email.")

        path = "/users/" + host_id + "/meetings"

        response = self.zoom_request(path, "POST", query, {'content-type': 'application/json'})

        if not response or response.status_code >= 300 or not response.content:
            raise FunctionError('api call failure: {} on {}'.format(response.status_code, path))
        else:
            try:
                json_data = json.loads(response.text)
            except ValueError:
                raise FunctionError("Unable to parse response text")

            LOG.debug(json.dumps(json_data))

            zoom_host_url = json_data["start_url"]
            zoom_join_url = self.strip_password_from_join_url(json_data["join_url"])
            zoom_url_with_pass = json_data["join_url"]

        results = {
            "host_url": zoom_host_url,
            "attendee_url": zoom_join_url,
            "date_created": meeting_time,
            "attendee_url_with_pass": zoom_url_with_pass
        }

        return results

    @staticmethod
    def strip_password_from_join_url(original):
        """ Parse query - pwd - password part from url """
        if PWD_IN_URL in original:
            parsed_url = urlparse(original)
            query_dict = parse_qs(parsed_url.query)
            query_dict.pop(PWD_IN_URL, None)
            parsed_url = parsed_url._replace(query=urlencode(query_dict, True))
            return parsed_url.geturl()
        else:
            return original

