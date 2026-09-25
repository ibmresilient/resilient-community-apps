# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use, line-too-long
"""Function implementation
   test with: resilient-circuits selftest -l fn_ipinfo
"""

import logging
import ipinfo

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
LOG.addHandler(logging.StreamHandler())


def get_config_option(option_name, opts, optional=False):
    """Given option_name, checks if it is in appconfig. Raises ValueError if a mandatory option is missing"""
    option = opts.get(option_name)

    if not option and optional is False:
        err = "'{0}' is mandatory and is not set in the app.config file. You must set this value to run this function".format(option_name)
        raise ValueError(err)
    else:
        return option


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """

    options = opts.get("fn_ipinfo", {})

    access_token = get_config_option("ipinfo_access_token", options)

    LOG.info("Gathered IP Info Access token")
    # Setup the IpInfo API Class
    ipinfo_handler = ipinfo.getHandler(access_token)
    details = None
    try:
        LOG.info("Sending query to IpInfo")
        # Submit query for Google DNS as a test
        details = ipinfo_handler.getDetails('8.8.8.8')

    except Exception as e:
        LOG.error(e)
        if '401 ' in e.args[0]:
            return {"state": "failed",
                    "reason": "Got a 401 error"}
        else:
            return {"state": "failed",
                    "reason": "Encountered an exception {0}".format(e.args[0])}

    # Will fail if we didn't get anything from IP Info
    if details:
        # details.all is what is accessed by the function code. A check to ensure it exists also
        if details.all:
            return {"state": "success"}
