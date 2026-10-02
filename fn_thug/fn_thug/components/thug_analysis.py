# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_thug.util.thug_utils import ThugUtils, get_thug_client


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'thug_analysis"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_thug", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_thug", {})

    @function("thug_analysis")
    def _thug_analysis_function(self, event, *args, **kwargs):
        """Function: """
        try:
            # Get the function parameters:
            thug_args = kwargs.get("thug_args")  # text
            thug_url = kwargs.get("thug_url")  # text

            log = logging.getLogger(__name__)
            log.info("thug_args: %s", thug_args)
            log.info("thug_url: %s", thug_url)

            # Run thug analysis on the given input
            yield StatusMessage('Beginning thug analysis on %s' % thug_url)
            util = ThugUtils(self.options)
            results = util.run_thug(get_thug_client(), thug_args, thug_url)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()