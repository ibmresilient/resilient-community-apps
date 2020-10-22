# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from urlparse import urlparse
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, ResultPayload

PACKAGE_NAME = "fn_url_to_dns"
LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'url_to_dns''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("url_to_dns")
    def _url_to_dns_function(self, event, *args, **kwargs):
        """Function: None"""
        try:
            # Initialize the results payload
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            # Validate fields
            validate_fields(['urltodns_url'], kwargs)

            # Get the function parameters:
            urltodns_url = kwargs.get("urltodns_url")  # text

            LOG.info("urltodns_url: %s", urltodns_url)

            yield StatusMessage("starting...")
            url = urlparse(urltodns_url)
            dns = "{}".format(url.netloc)
            yield StatusMessage("Integration Complete")

            content = {
                "dns": dns
            }

            results = rp.done(True, content)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)

        except Exception as err:
            LOG.error(err)
            yield FunctionError(err)