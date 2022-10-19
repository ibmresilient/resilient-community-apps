# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

# Teams Authentication
BASE_URL = "https://graph.microsoft.com/"
AUTH_URL = "https://login.microsoftonline.com/"

EMAIL = "email"
DEFAULT_SCOPE = ".default"
SETTINGS_GROUP_TYPE = "Unified"
SETTINGS_GROUP_MAIL_ENABLED = False
SETTINGS_GROUP_SECURITY_ENABLED = False

QUERY_GROUP_FIND_BY_NAME = "?$filter=displayName eq \'{}\'"
QUERY_GROUP_FIND_BY_MAIL = "?$filter=mailNickname eq \'{}\'"

# MS GROUPS API call
URL_GROUPS = "/v1.0/groups/{}"
URL_LIST_GROUPS = "/v1.0/groups"
URL_GROUPS_QUERY = "/v1.0/groups{}"
URL_GROUPS_OWNERS = "/v1.0/groups/{}/owners"
URL_GROUPS_MEMBERS = "/v1.0/groups/{}/members"
URL_DIRECTORY_OBJECT = "/v1.0/directoryObjects/{}"
URL_GROUP_ADD_MEMBERS = "/v1.0/groups/{}/members/$ref"

# MS USERS API call
URL_USERS = "/v1.0/users/{}"
URL_LIST_USERS = "/v1.0/users"

# Soar rest-client URLs
RES_GROUPS = "/groups"
RES_USERS = "/users/query_paged?return_level=normal"
RES_TASK = "/tasks/"
RES_INCIDENT = "/incidents/"

# LOG & Status Messages
INFO_RETRIEVED_BEARER_ID = "[Microsoft Authentication] Successfully retrieved Bearer ID"
INFO_CREATING_GROUP = "[Microsoft Groups] Creating new Group"
INFO_GROUP_CREATION_REQUEST = "[Microsoft Groups] Group creation request:"
INFO_FIND_GROUP_BY_NAME = "[Microsoft Groups] Searching for group using Name"
INFO_FIND_GROUP_BY_MAIL = "[Microsoft Groups] Searching for group using Mail Nickname"
INFO_FOUND_GROUP = "[Microsoft Groups] Found one or more Groups"
INFO_SUCCESSFULLY_DELETED = "Successfully deleted {} {}"
INFO_ADD_MEMEBERS = "[Microsoft Groups] Members to be added to the Group {}"

DEBUG_BEARER_ID = "[Microsoft Authentication] Bearer ID {}"
DEBUG_SKIPPING_USER = "[Microsoft Groups] User information already exist"

WARN_DIDNOT_FIND_USER = "[Microsoft Groups] User not found {}"
WARN_NO_OWNER_EMAIL_ID_PROVIDED = "[Microsoft Groups] No owner Email ID provided. Group preferences cannot be modified until an owner is assigned to the group"
WARN_NO_ADDITIONAL_PARTICIPANTS = "No participants were added to the {}. ADD MEMBERS FROM field was set to None and no list of participants were provided in the Additional members field."
WARN_INCIDENT_NO_MEMBERS = "Webex: There are no members assigned to this incident"

ERROR_AUTHENTICATION_FAILED = "[Microsoft Authentication] Failed to retrieve AccessToken. Check Credentials!"
ERROR_NO_ARG_PASSED = "[Microsoft Groups] No parameter passed to method read_user_info"
ERROR_DIDNOT_FIND_GROUP = "[Microsoft Groups] Did not find any group with {} {}"
ERROR_MISSING_NAME_MAIL_NAME = "[Microsoft Groups] Either the Group's name or the Mail Nickname has to be specified to find the group"
ERROR_FOUND_MANY_GROUP = "[Microsoft Groups] Foud more than one group with the same name. Please specify the Mail Nickname to delete the group"

STATUS_STARTING_APP = "Starting App Function: {}"
STATUS_GENERATE_HEADER = "Retriving AccessToken for this session"
STATUS_SUCCESSFULLY_AUTHENTICATED = "Secure connection Established!"
STATUS_AUTHENTICATION_FAILED = "Authentication failed! Could not retrieve AccessToken."
STATUS_FAILED_APP = "Failed to run App Function : {}"

# Self Test LOG MESSAGES
MSG_AUTHENTICATION_PASSED = "TEST_AUTHENTICATION: Passed! "
MSG_AUTHENTICATION_FAILED = "TEST_AUTHENTICATION: Failed! {} "
MSG_LIST_USER_PASSED = "TEST_LIST_USERS: Passed! "
MSG_LIST_USER_FAILED = "TEST_LIST_USERS: failed! {} "
MSG_POST_MSG_PASSED = "TEST_POST_MESSAGE: Passed! "
MSG_POST_MSG_FAILED = "TEST_POST_MESSAGE: Failed! {} "
WARN_NO_WEBHOOKS_FOUND = "No webhook found for selftest. Skipping Selftest for post message functionality "

# Response Handler Messages
MSG_RESPONSE_NONE = "API call failed! Invalid METHOD passed to rc.execute()! Response returned was None"
MSG_RESPONSE_204  = "API call successful! No content returned"
MSG_RESPONSE_400  = "API call failed! Entity or Object already exists. API returned 401! {}"
MSG_RESPONSE_401  = "API call failed! Security context is invalid. API returned 401! {}"
MSG_RESPONSE_404  = "API call failed! Item not found. API returned 404! {}"
MSG_RESPONSE_405  = "API call failed! Method Not Allowed. API returned 405! {}"