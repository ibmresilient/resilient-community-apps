# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# Generated with resilient-sdk v49.0.4423

import logging
from resilient_lib import RequestsCommon
from fn_azure_automation_utilities.util.helper import AzureClient

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    app_configs = opts.get("fn_azure_automation_utilities", {})
    rc = RequestsCommon(opts, app_configs)

    # If the below can run without an IntegrationError occurring then connection to Azure is successful
    client = AzureClient(
        rc,
        app_configs.get("client_id"),
        app_configs.get("client_secret"),
        app_configs.get("tenant_id"),
        app_configs.get("subscription_id"),
        app_configs.get("scope"),
        rc.get_proxies(),
        refresh_token=app_configs.get("refresh_token")
    )

    return {
        "state": "success",
        "reason": None
    }
