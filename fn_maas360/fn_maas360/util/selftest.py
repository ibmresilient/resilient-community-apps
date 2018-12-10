# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_maas360
"""
from fn_maas360.util.maas360_common import selftest_maas360
from resilient_lib.components.resilient_common import validate_fields
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(options):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    # options = opts.get("fn_maas360", {})
    validate_fields(['maas360_url', 'maas360_billing_id', 'maas360_platform_id',
                     'maas360_app_id', 'maas360_app_version', 'maas360_app_access_key',
                     'maas360_username', 'maas360_password'], options)

    # configuration specific slack parameters
    url = options['maas360_url']
    billing_id = options['maas360_billing_id']
    platform_id = options['maas360_platform_id']
    app_id = options['maas360_app_id']
    app_version = options['maas360_app_version']
    app_access_key = options['maas360_app_access_key']
    username = options['maas360_username']
    password = options['maas360_password']

    try:
        log.info(
            'Calling createPartnerConfigurations with WS Server base: ' + url + ', Blling ID: ' + billing_id + ', User: '
            + username + ', App Id: ' + app_id + ', Platform Id: ' + platform_id + ', App Version: ' + app_version)

        response = selftest_maas360(url, billing_id, username, password, app_id, app_version, platform_id, app_access_key)
        if response:
            state = "success"
        else:
            state = "failure"
            #reason = response
    except Exception as ex:
        state = "failure"
        reason = str(ex)

    result = {
        "state": state,
        "reason": reason
    }

    log.info(result)
    return result