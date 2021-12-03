# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_service_now
"""

import logging
from .splunk_utils import SplunkClient
import fn_splunk_integration.util.splunk_constants as splunk_constants
from fn_splunk_integration.util.splunk_utils import SplunkServers

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
LOG.addHandler(logging.StreamHandler())

def selftest_function(opts):
    """
    This test uses configs in the app.config file to call attempt a splunk connect
    To try and get a status_code=200, else its a failure
    """
    options = opts.get(splunk_constants.PACKAGE_NAME, {})

    if not options:
        servers = SplunkServers(opts, options)
        server_list = servers.get_server_name_list()
    else:
        server_list = {splunk_constants.PACKAGE_NAME}

    try:
        for server_name in server_list:
            server = opts.get(server_name, {})

            LOG.info("Trying to connect to %s", server["host"])

            SplunkClient.connect(host=server["host"],
                                port=server.get("port"),
                                username=server.get("username"),
                                password=server.get("splunkpassword"),
                                verify=False)

            LOG.info("Test for {} was successful\n".format(server["host"]))

        return {"state": "success"}

    except Exception as err:
        err_reason_msg = """Could not connect to Splunk.
            error: {0}
            ---------
            host: {1}
            username: {2}\n""".format(err, server["host"], server.get("username"))

        LOG.error(err_reason_msg)

        return {
            "state": "failure",
            "reason": err_reason_msg
        }
