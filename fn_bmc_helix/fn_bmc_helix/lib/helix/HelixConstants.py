# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.

# Constant values
DEFAULT_HTTPS_PORT = 8443

# Interpreted values
HTTPS_BASE_URL = lambda host, port: "https://{0}:{1}/api".format(host, str(port))

PACKAGE_NAME = "fn_bmc_helix"
TABLE_NAME = "bmc_helix_incidents"

# Fields we want BMC Helix to return when creating an incident
RETURN_FIELDS = ["Incident Number", "Request ID"]