# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from fn_threatminer.lib.threatminer_common import ThreatMiner, PACKAGE
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'threatminer_samples_metadata"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE, {})
        self.threatminer = ThreatMiner(opts, self.options)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE, {})
        self.threatminer = ThreatMiner(opts, self.options)

    @function("threatminer_samples_metadata")
    def _threatminer_samples_metadata_function(self, event, *args, **kwargs):
        """Function: Query Threatminer Samples API for File MD5 Hash and return Metadata"""
        try:
            # Get the function parameters:
            md5_hash = kwargs.get("md5_hash")  # text

            log = logging.getLogger(__name__)
            log.info("md5_hash: %s", md5_hash)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")

            data, msg = self.threatminer.get(u'/sample.php?q={}&rt=1'.format(md5_hash))

            yield StatusMessage(u"{} for {}".format(msg, md5_hash))

            yield StatusMessage("done...")

            results = {
                "metadata": data
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
