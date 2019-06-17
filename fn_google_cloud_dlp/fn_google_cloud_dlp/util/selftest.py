# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_google_cloud_dlp
"""

import logging
from fn_google_cloud_dlp.util.gcp_helper import GCPHelper
from resilient_circuits.rest_helper import get_resilient_client

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get("fn_google_cloud_dlp", {})

    # When the helper is instantiated, we make a connection to Google Cloud by also instantiating the DLP Class
    # If credentials aren't set right this will fail
    helper = GCPHelper(options, res_client=get_resilient_client(opts=opts))

    # Config Appears to be okay and can make A connection to google
    # Now to test if we can inspect a string of content

    try:

        helper.inspect_string(content_string="Test", info_types=[])
    except Exception as dlp_exception:
        log.error(u"Encountered Exception when interfacing with DLP; Exception: {}".format(dlp_exception))
        return {"state": "failure", "reason": dlp_exception}

    return {"state": "success"}
