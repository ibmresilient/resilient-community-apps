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
