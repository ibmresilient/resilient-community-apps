# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_qradar_integration
"""

import logging
from fn_qradar_enhanced_data.util.qradar_utils import QRadarClient


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

        log.info("Verifying app.config values for fn_qradar_integration config section")

        cafile = False if options.get("verify_cert", "").lower() == "false" else options["verify_cert"]
        qradar_client = QRadarClient(host=options["host"],
                                     username=options.get("username", None),
                                     password=options.get("qradarpassword", None),
                                     token=options.get("qradartoken", None),
                                     cafile=cafile,
                                     opts=opts,
                                     function_opts=options)

        log.info("Verifying QRadar connection...")

        connected = qradar_client.verify_connect()

        if connected:
            log.info("Verifying QRadar GraphQL connection...")

            graphql_installed = qradar_client.verify_graphql_connect()

            if not graphql_installed:
                log.warning("QRadar GraphQL connection check failed. This is needed for qradar_enhanced data. "
                            "Check for QRadar Analyst workflow installation ")
            else:
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
            options["username"],
            options["qradarpassword"],
            options["qradartoken"])

        log.error(err_reason_msg)

        return {
            "state": "failure",
            "reason": err_reason_msg
        }
