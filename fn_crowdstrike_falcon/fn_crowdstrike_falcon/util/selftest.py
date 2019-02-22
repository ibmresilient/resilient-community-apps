# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_crowdstrike_falcon
"""

import logging
from fn_crowdstrike_falcon.util.cs_helper import CrowdStrikeHelper

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
LOG.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Verify OAuth2 and Basic Auth Credentials for CrowdStrike
    """

    try:

        LOG.info("Verifying app.config values for %s", CrowdStrikeHelper.app_config_section)

        app_configs = opts.get(CrowdStrikeHelper.app_config_section, {})

        cs_helper = CrowdStrikeHelper(app_configs)
        
        LOG.info("Verifying OAuth2 Credentials...")

        cs_helper.get_oauth2_token()

        LOG.info("Success")

        LOG.info("Verifying Basic Auth Credentials...")

        res = cs_helper.get_device_status("x")

        if res is not None and res.get("err_msg") == "Could not get device status for device_id x.":
            LOG.info("Success")
        else:
            raise ValueError("Failed to verify Basic Auth Credentials")

        LOG.info("Test was successful")

        return {
            "state": "success"
        }

    except Exception as err:
        err_reason_msg = """Could not connect to CrowdStrike.
            error: {0}
            ---------
            Current Configs in app.config file::
            ---------
            cs_falcon_oauth2_base_url: {1}
            cs_falcon_oauth2_cid: {2}
            cs_falcon_bauth_base_url: {3}
            cs_falcon_bauth_api_uuid: {4}\n""".format(
                err,
                cs_helper.oauth2_base_url,
                cs_helper.oauth2_cid,
                cs_helper.bauth_base_url,
                cs_helper.bauth_api_uuid)

        LOG.error(err_reason_msg)

        return {
            "state": "failure",
            "reason": err_reason_msg
        }
