# -*- coding: utf-8 -*-
#
# (c) Copyright IBM Corp. 2022. All Rights Reserved.
#
#   Qradar constants

# URL from https://qradar_instance/api/
HELP_VERSIONS = "help/versions"
ARIEL_SEARCHES = "ariel/searches"
ARIEL_SEARCHES_RESULT = "ariel/searches/{}/results"
REFERENCE_SET_URL = "reference_data/sets"
REFERENCE_TABLE_URL = "reference_data/tables"
PACKAGE_NAME = "fn_qradar_integration"

SEARCH_STATUS_COMPLETED = "COMPLETED"
SEARCH_STATUS_EXECUTE = "EXECUTE"
SEARCH_STATUS_WAIT = "WAIT"
SEARCH_STATUS_SORTING = "SORTING"

UPDATE_FIELD = "/types/actioninvocation/fields/{}"
GET_FIELD = "/types/actioninvocation/fields/{}?include_principals=true"
