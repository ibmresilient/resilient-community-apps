# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_service_now
"""

import logging
from .splunk_utils import SplunkClient

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
LOG.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    This test uses configs in the app.config file to call attempt a splunk connect
    To try and get a status_code=200, else its a failure
    """
    options = opts.get("fn_splunk_integration", {})

    host = options['host']
    port = options['port']
    username = options['username']
    password = options['splunkpassword']

    try:

        LOG.info("Trying to connect to %s", host)

        SplunkClient.connect(host, port, username, password,
                             verify=False
                             )

        return {"state": "success"}

    except Exception as err:
        err_reason_msg = """Could not connect to Splunk.
            error: {0}
            ---------
            host: {1}
            username: {2}\n""".format(err, host, username)

        LOG.error(err_reason_msg)

        return {
            "state": "failure",
            "reason": err_reason_msg
        }
