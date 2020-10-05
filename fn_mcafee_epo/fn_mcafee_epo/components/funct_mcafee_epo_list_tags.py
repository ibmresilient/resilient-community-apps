# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from fn_mcafee_epo.lib.epo_helper import init_client
from resilient_lib import ResultPayload
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

PACKAGE_NAME = "fn_mcafee_epo"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'mcafee_epo_list_tags''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get(PACKAGE_NAME, {})

    @function("mcafee_epo_list_tags")
    def _mcafee_epo_list_tags_function(self, event, *args, **kwargs):
        """Function: None"""
        try:
            yield StatusMessage("Starting")

            log = logging.getLogger(__name__)

            rc = ResultPayload(PACKAGE_NAME, **kwargs)

            client = init_client(self.opts, self.options)
            response = client.request("system.findTag", {})

            yield StatusMessage("Finished")

            results = rc.done(True, response)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
