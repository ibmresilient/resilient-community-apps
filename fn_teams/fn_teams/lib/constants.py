# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

# Teams Authentication
PACKAGE_NAME  = "fn_teams"
BASE_URL = "https://graph.microsoft.com/"
AUTH_URL = "https://login.microsoftonline.com/"

EMAIL = "email"
BEARER = 'Bearer {}'
MEMBERS_URL = "{}/members"
DEFAULT_SCOPE = ".default"
SETTINGS_GROUP_TYPE = "Unified"
CHANNEL_MEMBERSHIP_TYPE = "standard"
SETTINGS_GROUP_MAIL_ENABLED = False
SETTINGS_GROUP_SECURITY_ENABLED = False


DELEGATED_GRANT_ACCESS = "authorization_code"
DELEGATED_GRANT_REFRESH = "refresh_token"

CODE_TYPE_ACCESS = "code"
CODE_TYPE_REFRESH = DELEGATED_GRANT_REFRESH

CONTENT_TYPE_JSON = "application/json"
CONTENT_TYPE_URLENCODED = "application/x-www-form-urlencoded"

OAUTH_TOKEN_URL = "oauth2/v2.0/token"
DEFAULT_REDIRECT_URI = "https://localhost:8080/callback"

# MS Finder
QUERY_GROUP_FIND_BY_NAME = '?$filter=displayName eq \'{}\''
QUERY_GROUP_FIND_BY_MAIL = '?$filter=mailNickname eq \'{}\''

# MS Post Message
TEXT = "text"
TASK = "Task"
TITLE = "title"
INCIDENT = "Incident"
TIMEOUT = 60
TASK_FRAGMENT = "?task={}"
ERROR_UNABLE_TO_FIND_CHANNEL = "Unable to find channel name {} in app.config"
SUCCESSFULLY_POSTED_MESSAGE = "Information successfully posted in channel {}"

# MS GROUPS API call
URL_GROUPS = "/v1.0/groups"
URL_LIST_GROUPS = URL_GROUPS
URL_GROUPS_QUERY = URL_GROUPS + "{}"
URL_LOCATE_GROUPS = URL_GROUPS + "/{}"
URL_GROUPS_OWNERS = URL_GROUPS + "/{}/owners"
URL_GROUPS_MEMBERS = URL_GROUPS + "/{}/members"
URL_GROUP_ADD_MEMBERS = URL_GROUPS + "/{}/members/$ref"
URL_DIRECTORY_OBJECT = "/v1.0/directoryObjects/{}"

CREATE_GROUP_CONFIGURATION = {
    "visibility": "Private"}

# MS USERS API call
URL_USERS = "/v1.0/users/{}"
URL_LIST_USERS = "/v1.0/users"
URL_USERS_QUERY = "/v1.0/users{}"

# MS TEAMS API call
TEAM_ID_REGEX = '\'(.+?)\''
URL_TEAMS = "/v1.0/teams"
URL_LIST_TEAMS = URL_TEAMS
URL_LOCATE_TEAM = URL_TEAMS + "/{}/"
URL_TEAMS_ARCHIVE = URL_TEAMS + "/{}/archive"
URL_TEAMS_UNARCHIVE = URL_TEAMS + "/{}/unarchive"
URL_TEAM_FROM_GROUP = URL_GROUPS + "/{}/team"
URL_ADD_MEMBER_CONTEXT = "members/add"
URL_TEAMS_STANDARD_TEMPLATE = "/v1.0/teamsTemplates('standard')"

# MS CHANNELS API call
URL_LIST_CHANNEL = URL_TEAMS + "/{}/channels"
URL_LOCATE_CHANNEL = URL_LIST_CHANNEL + "/{}"
URL_CHANNEL_MSG = URL_LOCATE_CHANNEL + "/messages"
URL_CHANNEL_MSG_REPLY = URL_CHANNEL_MSG + "/{}/replies"

TEAMS_FROM_GROUP_CONFIGURATION = {
    "visibility": "Private",

    "memberSettings": {
        "allowCreatePrivateChannels": True,
        "allowCreateUpdateChannels": True},

    "messagingSettings": {
        "allowUserEditMessages": True,
        "allowUserDeleteMessages": True},

    "funSettings": {
        "allowGiphy": True,
        "giphyContentRating": "strict"}}

# SOAR rest-client URLs
RES_TASK = "/tasks/"
RES_GROUPS = "/groups"
RES_INCIDENT = "/incidents/"
RES_USERS = "/users/query_paged?return_level=normal"

# LOG & Status Messages
INFO_RETRIEVED_BEARER_ID = "Successfully retrieved Bearer ID"
INFO_CREATING_GROUP = " Creating new Group"
INFO_GROUP_CREATION_REQUEST = " Group creation request:"
INFO_FIND_GROUP_BY_NAME = " Searching for group using Name"
INFO_FIND_GROUP_BY_MAIL = " Searching for group using Mail Nickname"
INFO_FIND_GROUP_BY_ID = "Searching for group using Group ID"
INFO_FOUND_GROUP = " Found one or more Groups"
INFO_SUCCESSFULLY_DELETED = "Successfully deleted {}: {}"
INFO_ADD_MEMEBERS = " Members to be added to the Group {}"
INFO_SUCCESSFULLY_ENABLED = "Successfully enabled Teams for Group: {}"
INFO_SUCCESSFULLY_ARCHIVED = "Successfully archived Team: {}"
INFO_SUCCESSFULLY_UNARCHIVED = "Successfully unarchived Team: {}"
INFO_SUCCESSFULLY_CREATED_CHANNEL = "Successfully created channel: {}"
INFO_SUCCESSFULLY_DELETED_CHANNEL = "Successfully deleted channel: {}"

DEBUG_BEARER_ID = "Bearer ID {}"
DEBUG_SKIPPING_USER = " User information already exist"
DEBUG_ADDING_MEMBER_TO_GROUP = " Adding members to Group object {}"

WARN_DIDNOT_FIND_USER = " User not found {}"
WARN_NO_OWNER_EMAIL_ID_PROVIDED = ''' No owner Email ID provided.
 Either no Owner Id was provided or the ID has no valid MS account. Group preferences
 cannot be modified until an owner is assigned to the group'''
WARN_NO_MEMBER_EMAIL_ID_PROVIDED = ''' No member Email ID found.
 Unable to find a user associated with the Incident/Task who has a valid MS account'''
WARN_NO_ADDITIONAL_PARTICIPANTS = '''No participants were added to the {}.
 ADD MEMBERS FROM field was set to None and no list of participants were provided
 in the Additional members field.'''
WARN_INCIDENT_NO_MEMBERS = "There are no members assigned to this incident"

ERROR_AUTHENTICATION_FAILED = '''Failed to retrieve AccessToken.
 Check Credentials!'''
ERROR_NO_ARG_PASSED = " No parameter passed to method"
ERROR_DIDNOT_FIND_GROUP = " Did not find any group with {} {}"
ERROR_MISSING_NAME_MAIL_NAME = ''' Either the Group's name or the
 Mail Nickname has to be specified to find the group'''
ERROR_FOUND_MANY_GROUP = "Found more than one group with the same name"
ERROR_INVALID_OPTION_PASSED = "Invalid Option passed!"

ERROR_COULDNOT_CREATE_TEAM = "Unable to create team"
ERROR_COULDNOT_CREATE_CHANNEL = "Unable to create channel"
ERROR_COULDNOT_FIND_CHANNEL = "Unable to locate channel: {}"
ERROR_COULDNOT_DELETE_CHANNEL = "Unable to delete channel"
ERROR_UNABLE_TO_AUTHENTICATE = "Unable to authenticate: {} {}"
ERROR_NO_REFRESH_TOKEN = "Unable to find refresh_token in app.conf"

STATUS_STARTING_APP = "Starting App Function: {}"
STATUS_GENERATE_HEADER = "Retrieving AccessToken for this session"
STATUS_SUCCESSFULLY_AUTHENTICATED = "Secure connection Established!"
STATUS_AUTHENTICATION_FAILED = "Authentication failed! Could not retrieve AccessToken."
STATUS_FAILED_APP = "Failed to run App Function : {}"
STATUS_STARTING_APP = "App successfully executed!"

# Self Test LOG MESSAGES
MSG_APP_AUTHENTICATION_PASSED = "TEST APPLICATION PERMISSION: Passed! "
MSG_APP_AUTHENTICATION_FAILED = "TEST APPLICATION PERMISSION: Failed! {} "
MSG_DEL_AUTHENTICATION_PASSED = "TEST DELEGATION PERMISSION: Passed! "
MSG_DEL_AUTHENTICATION_FAILED = "TEST DELEGATION PERMISSION: Failed! {} "
MSG_LIST_USER_PASSED = "TEST LIST_USERS: Passed! "
MSG_LIST_USER_FAILED = "TEST LIST_USERS: failed! {} "
MSG_POST_MSG_PASSED = "TEST POST_MESSAGE: Passed! "
MSG_POST_MSG_FAILED = "TEST POST_MESSAGE: Failed! {} "
WARN_NO_WEBHOOKS_FOUND = "No webhook found for selftest. Skipping webhook test"
WARN_NO_APP_PERMISSION = "No Application token found. Skipping application permission test"
WARN_NO_DEL_PERMISSION = "No refresh token found. Skipping delegated permission test"

# Response Handler Messages
MSG_UNSUPPORTED_TYPE = "Unsupported object specified to function. Accepted types int or list"
MSG_RESPONSE_NONE = '''API call failed! Invalid METHOD passed to rc.execute()!
 Response returned was None'''
MSG_RESPONSE_204  = "API call successful! No content returned"
MSG_RESPONSE_400  = "API call failed! API returned 400! {}"
MSG_RESPONSE_401  = "API call failed! Security context is invalid. API returned 401! {}"
MSG_RESPONSE_404  = "API call failed! Item not found. API returned 404! {}"
MSG_RESPONSE_405  = "API call failed! Method Not Allowed. API returned 405! {}"
MSG_RESPONSE_409  = "API call failed! Conflict in the request. API returned 405! {}"