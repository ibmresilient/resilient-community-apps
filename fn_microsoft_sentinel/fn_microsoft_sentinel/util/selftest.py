# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.

"""
Function implementation test.
Usage: resilient-circuits selftest -l fn_microsoft_sentinel
"""

from logging import getLogger, INFO, StreamHandler
from resilient_lib import validate_fields, IntegrationError
from fn_microsoft_sentinel.lib.function_common import PACKAGE_NAME, SentinelProfiles
from fn_microsoft_sentinel.lib.sentinel_common import SentinelAPI

log = getLogger(__name__)
log.setLevel(INFO)
log.addHandler(StreamHandler())

def selftest_function(opts):
    options = opts.get(PACKAGE_NAME, {})
    reason = None

    try:
        # Check if setting ms_sentinel_labels is configured in the app.config
        if options.get("ms_sentinel_labels", None):
            sentinel_configs = SentinelProfiles(opts, options)
            # Loop though lst of Sentinel server labels configured in ms_sentinel_labels in the app.config
            for label in sentinel_configs.get_profiles():
                sentinel_api = SentinelAPI(opts, options, sentinel_configs.get_profile(label))

                status = True if sentinel_api._authenticate() else False
                log.info(f"Test for {label} was {'success' if status else 'failure'}")
        else:
            # Validate that required settings are configured
            validate_fields([
                {"name": "azure_url"},
                {"name": "tenant_id", "placeholder": "aaa-bbb-ccc"},
                {"name": "client_id", "placeholder": "aaa-bbb-ddd"},
                {"name": "app_secret", "placeholder": "aaa-bbb-eee"}],
                options
            )
            sentinel_api = SentinelAPI(opts, options, None)
            status = "success" if sentinel_api._authenticate() else "failure"

    except IntegrationError as err:
        status = False
        reason = f"""Could not connect to Microsoft Sentinel
        error: {err}
        ---------
        Current Configs in the app.config file:
        ---------
        azure_url: {options.get("azure_url")}
        ms_sentinel_labels: {options.get("ms_sentinel_labels", None)}
        sentinel_profiles: {options.get("sentinel_profiles", None)}
        verify: {options.get("verify", None)}
        api_version: {options.get("api_version", None)}
        """

    return {
        "state": "success" if status else "failure",
        "reason": reason
    }
