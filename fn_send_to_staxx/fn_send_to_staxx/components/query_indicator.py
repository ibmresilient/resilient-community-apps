# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from fn_send_to_staxx.lib.staxx_lib import StaxxClient
from resilient_lib import RequestsCommon, ResultPayload
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError

STAXX_SECTION = "staxx"
DEFAULT_MAX_RESULTS = 10

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function(s)"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get(STAXX_SECTION, {})
        self.staxx_ip = self.options.get('staxx_ip')
        self.staxx_port = self.options.get('staxx_port')
        self.staxx_user = self.options.get('staxx_user')
        self.staxx_password = self.options.get('staxx_password')

    @function("query_staxx")
    def _query_staxx_indicator(self, event, *args, **kwargs):
        """Function: """
        try:
            rc = ResultPayload(STAXX_SECTION, **kwargs)
            # Get the function parameters:
            staxx_indicator = kwargs.get("staxx_indicator")  # text
            staxx_max_results = kwargs.get("staxx_max_results", DEFAULT_MAX_RESULTS)  # text

            log = logging.getLogger(__name__)

            yield StatusMessage("Querying for indicator {}".format(staxx_indicator))

            staxx = StaxxClient("https://{}:{}".format(self.staxx_ip,self.staxx_port),
                                self.staxx_user,
                                self.staxx_password,
                                RequestsCommon(self.opts, self.options)
                                )

            query = "value = '{}'".format(staxx_indicator)

            try:
                staxx_response = staxx.query(query=query, size=staxx_max_results)

                status = True
                reason = None
            except Exception as err:
                err = "Error Staxx query: {}".format(str(err))
                raise FunctionError(err)

            results = rc.done(status, staxx_response, reason=reason)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
