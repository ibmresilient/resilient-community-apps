# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_service_now
"""

import logging
from fn_splunk_integration.util.splunk_constants import PACKAGE_NAME
from fn_splunk_integration.util.splunk_utils import SplunkServers, SplunkClient

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
LOG.addHandler(logging.StreamHandler())

def selftest_function(opts):
    """
    This test uses configs in the app.config file to call attempt a splunk connect
    To try and get a status_code=200, else its a failure
    """
    options = opts.get(PACKAGE_NAME, {})

    if options: # If no labels given [fn_splunk_integration]
        server_list = {PACKAGE_NAME}
    else: # If labels given [fn_splunk_integration:label]
        servers = SplunkServers(opts, options)
        server_list = servers.get_server_name_list()

    try:
        for server_name in server_list:
            server = opts.get(server_name, {})

            splunk_verify_cert = False if options.get("verify_cert", "").lower() != "true" else True

            LOG.info("Trying to connect to %s", server.get("host"))

            SplunkClient.connect(host=server.get("host"),
                                 port=server.get("port"),
                                 username=server.get("username"),
                                 password=server.get("splunkpassword"),
                                 verify=splunk_verify_cert)

            LOG.info("Test for {} was successful\n".format(server.get("host")))

        return {"state": "success"}

    except Exception as err:
        err_reason_msg = """Could not connect to Splunk.
            error: {0}
            ---------
            host: {1}
            username: {2}\n""".format(
            err,
            server.get("host"),
            server.get("username"))

        LOG.error(err_reason_msg)

        return {
            "state": "failure",
            "reason": err_reason_msg
        }
