# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_qradar_integration
"""

import logging
from fn_qradar_enhanced_data.util.qradar_utils import QRadarClient, QRadarServers
from fn_qradar_enhanced_data.util.qradar_constants import PACKAGE_NAME, GLOBAL_SETTINGS

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

        if not options:
            servers = QRadarServers(opts, options)
            server_list = servers.get_server_name_list()
        else:
            server_list = {PACKAGE_NAME}
        
        if GLOBAL_SETTINGS in server_list:
            server_list.remove(GLOBAL_SETTINGS)

        for server_name in server_list:
            server = opts.get(server_name, {})

            log.info("Verifying app.config values for {} config section".format(str(server.get("host"))))

            cafile = False if server.get("verify_cert", "false").lower() == "false" else server.get("verify_cert")
            qradar_client = QRadarClient(host=server.get("host"),
                                        username=server.get("username", None),
                                        password=server.get("qradarpassword", None),
                                        token=server.get("qradartoken", None),
                                        cafile=cafile,
                                        opts=opts,
                                        function_opts=server)

            log.info("Verifying QRadar connection...")

            connected = qradar_client.verify_connect()

            if connected:
                log.info("Verifying QRadar GraphQL connection...")

                graphql_installed = qradar_client.verify_graphql_connect()

                if not graphql_installed:
                    log.warning("QRadar GraphQL connection check failed. This is needed for qradar_enhanced_data. "
                                "Check for QRadar Analyst workflow installation\n")
                else:
                    log.info("Test was successful\n")

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
            verify_cert: {2}
            username: {3}
            qradarpassword: {4}
            qradartoken: {5}\n""".format(
            err,
            server.get("host"),
            server.get("verify_cert"),
            server.get("username"),
            server.get("qradarpassword"),
            server.get("qradartoken"))

        log.error(err_reason_msg)

        return {
            "state": "failure",
            "reason": err_reason_msg
        }
