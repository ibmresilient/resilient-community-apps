# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2023. All Rights Reserved.
# pragma pylint: disable=pointless-string-statement, line-too-long, wrong-import-order

"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import RequestsCommon, validate_fields

MAX_DEPTH_LIMIT = 10  # number of redirects to follow before giving up
SOCKET_TIMEOUT = 10 # number of seconds to wait for request to complete - this is socket level timeout, not http timeout

SECTION_HDR = "fn_network_utilities"

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'network_utilities_expand_url.
        Given any URL, it will continue to follow it through redirects to it's destinations. This is intended for shortened URLs but
        will work on any URL.
    """
    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get(SECTION_HDR, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get(SECTION_HDR, {})

    @function("network_utilities_expand_url")
    def _utilities_resilient_url_expander_function(self, event, *args, **kwargs):
        """Function: Follow a URL until it's destination URL. Returned is a list of the URLs found. """
        try:
            validate_fields(["network_utilities_resilient_url"], kwargs)

            # Get the function parameters:
            resilient_url = kwargs.get("network_utilities_resilient_url").strip()  # text

            self.log = logging.getLogger(__name__)
            self.log.info("resilient_url: %s", resilient_url)

            # Run the search and return the results
            yield StatusMessage("Starting...")

            rc = RequestsCommon(self.opts, self.options)
            results = self.expand_url(rc, resilient_url, 1)
            results = results[1:] # pop the first as that is the original url
            self.log.debug(results)

            # Produce a FunctionResult with the results
            yield FunctionResult({"urllist": results})
        except Exception as err:
            self.log.error(err)
            yield FunctionError()


    def expand_url(self, rc: RequestsCommon, url: str, depth: int):
        """ Starting point. Make sure the URL has a prefix. """
        if not url.lower().startswith('http'):
            url = 'https://' + url

        if depth > MAX_DEPTH_LIMIT:
            self.log.warning("Exceeded depth limit")
            return [url]

        self.log.debug(f"{url} depth {depth}")

        url_list = [url]

        try:
            response = rc.execute('HEAD', url, allow_redirects=False)

            self.log.info(f"{response.status_code}:{response.next}")
            if int(response.status_code/100) == 3:
                url_list.extend(self.expand_url(rc, response.next.url, depth+1))
        except Exception as err:
            self.log.error(err)
            return list()

        return url_list
