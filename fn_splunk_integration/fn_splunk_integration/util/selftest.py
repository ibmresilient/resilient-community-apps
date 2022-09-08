# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   Test with: resilient-circuits selftest -l fn_splunk_integration
"""

import logging
from fn_splunk_integration.util.function_utils import get_servers_list
from fn_splunk_integration.util.splunk_utils import SplunkClient
from resilient_lib import str_to_bool

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
LOG.addHandler(logging.StreamHandler())

def selftest_function(opts):
    """
    This test uses configs in the app.config file to call attempt a splunk connect
    To try and get a status_code = 200, else its a failure
    """

    servers_list = get_servers_list(opts)

    try:
        for server_name in servers_list:
            server = opts.get(server_name, {})

            splunk_verify_cert = str_to_bool(server.get("verify_cert", ""))

            LOG.info("Trying to connect to %s", server.get("host"))

            SplunkClient.connect(host=server.get("host"),
                                 port=server.get("port"),
                                 username=server.get("username", None),
                                 password=server.get("splunkpassword", None),
                                 token=server.get("token", None),
                                 verify=splunk_verify_cert)

            LOG.info("Test for {} was successful\n".format(server.get("host")))

        return {"state": "success"}

    except Exception as err:
        err_reason_msg = """Could not connect to Splunk.
            error: {0}
            ---------
            host: {1}
            port: {2}
            username: {3}\n""".format(
            err,
            server.get("host"),
            server.get("port"),
            server.get("username"))

        LOG.error(err_reason_msg)

        return {
            "state": "failure",
            "reason": err_reason_msg
        }
