# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from traceback import format_exc
from data_feeder_plugins.resilientfeed.resilient_common import Resilient
from resilient_lib import str_to_bool
from resilient import get_client

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
LOG.addHandler(logging.StreamHandler())

class MockRestClientHelper():
    def __init__(self, rest_client):
        self.inst_rest_client = rest_client

    def get_inst_rest_client(self):
        return self.inst_rest_client

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """

    # default
    result = {
        "state": "success",
        "reason": None
    }

    try:
        options = opts.get("resilient_feed", {})

        is_source = str_to_bool(options.get("sync_role_source", "true"))

        rest_client = get_client(opts.get("resilient", {}))
        rest_client_helper = MockRestClientHelper(rest_client)

        # connects to source and database
        _resilient_source = Resilient(options, rest_client_helper, is_source)
        resilient_target = Resilient(options, None, is_source)

        # test the registry
        if is_source:
            if resilient_target.dbsync.find_registry_entry(options.get("org"),
                                                           options.get("host"),
                                                           rest_client.org_name,
                                                           rest_client.base_url):
                result["state"]  = "failure"
                result["reason"] = "source/source configuration detected"
            
    except Exception as err:
        LOG.error(format_exc())
        result["state"] = "failure"
        result["reason"] = str(err)

    LOG.info(result)
    return result
