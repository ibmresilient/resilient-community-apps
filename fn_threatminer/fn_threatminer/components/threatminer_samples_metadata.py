# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import requests
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import fn_threatminer.util.selftest as selftest


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'threatminer_samples_metadata"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_threatminer", {})
        selftest.selftest_function(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_threatminer", {})

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

            url = self.options.get('url', None)
            if not url:
                raise ValueError('missing url from [fn_threatminer] in app_config')

            response = requests.get('{}/sample.php?q={}&rt=1'.format(url, md5_hash))

            if response.status_code == 200:
                yield StatusMessage('Results returned for {}'.format(md5_hash))
            elif response.status_code == 404:
                yield StatusMessage('No Results Returned for {}'.format(md5_hash))
            else:
                yield StatusMessage('Unexpected return code of {}'.format(response.status_code))

            metadata = response.text

            yield StatusMessage("done...")

            results = {
                "metadata": metadata
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)