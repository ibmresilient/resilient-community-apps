# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

# Teams Authentication
BASE_URL = "https://graph.microsoft.com/"
AUTH_URL = "https://login.microsoftonline.com/"

LIST_USERS = "v1.0/users"
DEFAULT_SCOPE = ".default"

# LOG & Status Messages
INFO_RETRIEVED_BEARER_ID = "Teams Authentication: Successfully retrieved Bearer ID"

DEBUG_BEARER_ID = "Teams Authentication: Bearer ID {}"
ERROR_AUTHENTICATION_FAILED = "Teams Authentication: Failed to retrieve AccessToken. Check Credentials!"

STATUS_STARTING_APP = "Starting App Function: {}"
STATUS_GENERATE_HEADER = "Retriving AccessToken for this session"
STATUS_SUCCESSFULLY_AUTHENTICATED = "Secure connection Established!"
STATUS_AUTHENTICATION_FAILED = "Authentication failed! Could not retrieve AccessToken."
STATUS_FAILED_APP = "Failed to run App Function : {}"


# Self Test LOG MESSAGES
MSG_AUTHENTICATION_PASSED = "TEST_AUTHENTICATION: Passed!"
MSG_AUTHENTICATION_FAILED = "TEST_AUTHENTICATION: Failed! {}"
MSG_LIST_USER_PASSED = "\nTEST_LIST_USERS: Passed!"
MSG_LIST_USER_FAILED = "\nTEST_LIST_USERS: failed! {}"
MSG_POST_MSG_PASSED = "\nTEST_POST_MESSAGE: Passed!"
MSG_POST_MSG_FAILED = "\nTEST_POST_MESSAGE: Failed! {}"
WARN_NO_WEBHOOKS_FOUND = "No webhook found for selftest. Skipping Selftest for post message functionality"