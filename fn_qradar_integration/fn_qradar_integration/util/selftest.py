# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_qradar_integration
"""

import logging
from fn_qradar_integration.lib.functions_common import QRadarServers
from fn_qradar_integration.util.qradar_utils import QRadarClient

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """

    options = opts.get("fn_qradar_integration", {})
    server_list = ["fn_qradar_integration"]

    if not options:
        servers = QRadarServers(opts, options)
        server_list = servers.get_server_name_list()

    try:
        for server_name in server_list:
            options = opts.get(server_name, {})

            log.info("Verifying app.config values for fn_qradar_integration")

            cafile = False if options.get("verify_cert", "").lower() == "false" else options["verify_cert"]
            qradar_client = QRadarClient(host=options["host"],
                                        username=options.get("username", None),
                                        password=options.get("qradarpassword", None),
                                        token=options.get("qradartoken", None),
                                        cafile=cafile,
                                        opts=opts,
                                        function_opts=options)

            connected = qradar_client.verify_connect()

            log.info("Verifying QRadar connection...")

            log.info("Test for {} was successful".format(options["host"]))

        return {
            "state" : "success"
        }

    except Exception as err:
            err_reason_msg = """Could not connect to QRadar.
                error: {0}
                ---------
                Current Configs in app.config file::
                ---------
                host: {1}
                credentials: {2}\n""".format(
                err,
                options["host"],
                options.get("username") or "service token"
            )

            log.error(err_reason_msg)

            return {
                "state": "failure",
                "reason": err_reason_msg
            }
