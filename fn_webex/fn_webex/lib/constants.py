# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

# Webex Meeting constants
REMOVE_MILLISECONDS = 1000
MEETING_START_TIME_BUFFER = 2
DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S"

# Cisco Authentication URL
TOKEN_URL = "/v1/access_token"


# Cisco Webex Rooms and teams API URLs
ROOMS_URL = "/v1/rooms/"
TEAMS_URL = "/v1/teams/"
MEETINGS_URL = "/v1/meetings/"
ROOMS_MEMBERSHIP_URL = "/v1/memberships/"
TEAMS_MEMBERSHIP_URL = "/v1/team/memberships/"

# Soar rest-client URLs
RES_GROUPS = "/groups"
RES_USERS = "/users/query_paged?return_level=normal"
RES_INCIDENT = "/incidents/"

# Log and status messages
MSG_CREATE_SECURITY =  "Webex: Creating a Security context and establishing a connection with the Webex EndPoint"
MSG_FAILED_AUTH = "Failed to create Security Context. Failed to Authenticate!"
MSG_INVALID_TIMEZONE = "Invalid Timezone format. Supported format UTC +01:00"
MSG_INVLAID_STARTTIME = "Meeting start time ({}), must be after current time"
MSG_INVALID_ENDTIME = "Meeting end time ({}), must be after meeting start time({}) and current time ({})"
MSG_SUCCESS_AUTHENTICATED = "Security context create! Successfully Authenticated!"

MSG_SUCCESS_DELETION = "Successfully deleted {} : {}"
MSG_ENTITY_NOT_FOUND = "The specified {} could not be found!"
MSG_ENTITY_NO_DIRECT_DELETE = "This room cannot be deleted directly. Delete the team associated with it to clear this space."
MSG_UNFAMILIAR_RESPONSE_CODE = "Unfamiliar response. Status code : {}"

LOG_WARN_NO_PARTICIPANTS = "No participants were added to the {}. ADD_ALL_INCIDENT_MEMBERS was set to NO and no list of participants were provided in the ADDITIONAL_ATTENDEE field."
LOG_ADD_MEMEBERS = "Webex: Members to be added to the {} {}"
LOG_INCIDENT_NO_MEMBERS = "Webex: There are no members assigned to this incident"