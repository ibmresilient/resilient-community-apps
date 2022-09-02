# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.


REMOVE_MILLISECONDS = 1000
DEFAULT_MEETING_LENGTH = 45
MEETING_START_TIME_BUFFER = 2
DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S"

TOKEN_URL = "/v1/access_token"

ROOMS_URL = "/v1/rooms/"
TEAMS_URL = "/v1/teams/"
MEETINGS_URL = "/v1/meetings/"

ROOMS_MEMBERSHIP_URL = "/v1/memberships/"
TEAMS_MEMBERSHIP_URL = "/v1/team/memberships/"

RES_GROUPS = "/groups"
RES_USERS = "/users/query_paged?return_level=normal"
RES_INCIDENT = "/incidents/"


MSG_CREATE_SECURITY =  "Webex: Creating a Security context and establishing a connection with the Webex EndPoint"
MSG_FAILED_AUTH = "Failed to create Security Context. Failed to Authenticate!"