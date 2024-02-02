# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2019
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn-icdx
"""

import logging
import traceback
import datetime
from fn_icdx.util.helper import ICDXHelper
from fn_icdx.util.amqp_facade import AmqpFacade

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get("fn_icdx", {})
    helper = ICDXHelper(options)
    try:
        # Initialise the AmqpFacade, pass in config values
        # An issue with the client such as a unreachable host or authentication issues will cause this to fail.
        amqp_client = AmqpFacade(host=helper.get_config_option("icdx_amqp_host"),
                                 port=helper.get_config_option(
                                     "icdx_amqp_port", True),
                                 virtual_host=helper.get_config_option(
                                     "icdx_amqp_vhost"),
                                 username=helper.get_config_option(
                                     "icdx_amqp_username"),
                                 amqp_password=helper.get_config_option(
                                     "icdx_amqp_password")
                                 )

        return {"state": "success"}
    # For the selftest, we want to catch ANY issue found when setting up the soap_client, then print out the issue.
    except Exception as self_test_ex:
        # Put the traceback into DEBUG
        log.debug(traceback.format_exc())
        log.error(u"Encountered error while initialising the AMQP Client; Reason (if any): {0}".format(
            str(self_test_ex)))

        return {"state": "failure"}
