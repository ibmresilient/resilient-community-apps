# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_qradar_integration
"""

import logging
from fn_qradar_integration.util.qradar_utils import QRadarClient


log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    try:

        options = opts.get("fn_qradar_integration", {})
        res_options = opts.get("resilient", {})

        log.info("Verifying app.config values for fn_qradar_integration")

        if res_options["cafile"].lower() == "false":
            qradar_client = QRadarClient(host=options["host"],
                                         username=options.get("username", None),
                                         password=options.get("qradarpassword", None),
                                         token=options.get("qradartoken", None),
                                         cafile=False,
                                         opts=opts,
                                         function_opts=options)
        else:
            qradar_client = QRadarClient(host=options["host"],
                                         username=options.get("username", None),
                                         password=options.get("qradarpassword", None),
                                         token=options.get("qradartoken", None),
                                         cafile=res_options["cafile"],
                                         opts=opts,
                                         function_opts=options)

        connected = qradar_client.verify_connect()

        log.info("Verifying QRadar connection...")

        log.info("Test was successful")

        return {
            "state": "success"
        }

    except Exception as err:
        err_reason_msg = """Could not connect to QRadar.
            error: {0}
            ---------
            Current Configs in app.config file::
            ---------
            host: {1}
            username: {2}
            qradarpassword: {3}
            qradartoken: {4}\n""".format(
            err,
            options["host"],
            options.get("username"),
            options.get("qradarpassword"),
            options.get("qradartoken")
        )

        log.error(err_reason_msg)

        return {
            "state": "failure",
            "reason": err_reason_msg
        }
