# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_qradar_integration
"""

import logging
from fn_qradar_integration.util.qradar_utils import QRadarClient, QRadarServers
from fn_qradar_integration.util.qradar_constants import PACKAGE_NAME

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """

    options = opts.get(PACKAGE_NAME, {})

    if not options:
        servers = QRadarServers(opts, options)
        server_list = servers.get_server_name_list()
    else:
        server_list = [PACKAGE_NAME]

    try:
        for server_name in server_list:
            server = opts.get(server_name, {})

            log.info("Verifying app.config values for {}".format(PACKAGE_NAME))

            cafile = False if server.get("verify_cert", "").lower() == "false" else server.get("verify_cert")
            qradar_client = QRadarClient(host=server.get("host"),
                                        username=server.get("username", None),
                                        password=server.get("qradarpassword", None),
                                        token=server.get("qradartoken", None),
                                        cafile=cafile,
                                        opts=opts,
                                        function_opts=server)

            connected = qradar_client.verify_connect()

            log.info("Verifying QRadar connection...")

            log.info("Test for {} was successful".format(server.get("host")))

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
                server.get("host"),
                server.get("username") or "service token"
            )

            log.error(err_reason_msg)

            return {
                "state": "failure",
                "reason": err_reason_msg
            }
