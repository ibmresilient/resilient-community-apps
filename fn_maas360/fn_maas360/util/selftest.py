# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2019. All Rights Reserved.

"""Function implementation
   test with: resilient-circuits selftest -l fn_maas360
"""
from fn_maas360.lib.maas360_common import MaaS360Utils
from resilient_lib.components.resilient_common import validate_fields
from resilient_lib.components.integration_errors import IntegrationError
import logging

CONFIG_DATA_SECTION = 'fn_maas360'
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
LOG.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    # Get app.config parameters.
    options = opts.get(CONFIG_DATA_SECTION, {})

    validate_fields(['maas360_host_url', 'maas360_billing_id', 'maas360_platform_id',
                     'maas360_app_id', 'maas360_app_version', 'maas360_username'], options)

    # Read configuration settings:
    url = options['maas360_host_url']
    billing_id = options['maas360_billing_id']
    platform_id = options['maas360_platform_id']
    app_id = options['maas360_app_id']
    app_version = options['maas360_app_version']
    username = options['maas360_username']

    try:
        LOG.info(
            'Calling createPartnerConfigurations with WS Server base: ' + url + ', Blling ID: ' + billing_id + ', User: '
            + username + ', App Id: ' + app_id + ', Platform Id: ' + platform_id + ', App Version: ' + app_version)

        state, reason = "", ""
        # Create MaaS360Utils singleton
        maas360_utils = MaaS360Utils.get_the_maas360_utils(opts, CONFIG_DATA_SECTION)

        if maas360_utils and maas360_utils.get_auth_token():
            state = "success"
        else:
            state = "failure"
            reason = "N/A"
    except IntegrationError as err:
        state = "failure"
        reason = err.value

    result = {
        "state": state,
        "reason": reason
    }

    LOG.info(result)
    return result
