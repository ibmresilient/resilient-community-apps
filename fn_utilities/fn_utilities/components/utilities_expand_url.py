# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Function implementation"""

try:
    import httplib
except:
    import http.client as httplib

try:
    import urlparse
except:
    import urllib.parse as urlparse

try:
    from urllib2 import urlopen
except:
    from urllib.request import urlopen

import logging
import requests
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import RequestsCommon

MAX_DEPTH_LIMIT = 10  # number of redirects to follow before giving up
SOCKET_TIMEOUT = 10 # number of seconds to wait for request to complete - this is socket level timeout, not http timeout

SECTION_HDR = "fn_utilities"

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'utilities_expand_url.
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

    def init_proxies(self):
        self.proxy_host = None
        self.proxy_port = None

        rc = RequestsCommon(self.opts, self.options)
        proxies = rc.get_proxies()

        if proxies:
            proxy = proxies.get('https', proxies.get('http'))

            if proxy:
                proxy_url = urlparse.urlparse(proxy)
                self.proxy_host = proxy_url.hostname
                self.proxy_port = proxy_url.port

    @function("utilities_expand_url")
    def _utilities_resilient_url_expander_function(self, event, *args, **kwargs):
        """Function: Follow a URL until it's destination URL. Returned is a list of the URLs found. """
        try:
            # Get the function parameters:
            resilient_url = kwargs.get("resilient_url")  # text

            self.log = logging.getLogger(__name__)
            self.log.info("resilient_url: %s", resilient_url)

            # Run the search and return the results
            yield StatusMessage("Starting...")

            self.init_proxies()
            results = self.expand_url(resilient_url.strip())
            self.log.debug(results)

            # Produce a FunctionResult with the results
            yield FunctionResult({"urllist": results})
        except Exception as err:
            self.log.error(err)
            yield FunctionError()


    def expand_url(self, url):
        """ Starting point. Make sure the URL has a prefix. """
        if not url.lower().startswith('http'):
            url = 'http://' + url
        urls = []
        return self.follow_url(url, urls, 1)


    def follow_url(self, url, url_list, depth):
        """ This is called recursively to follow any redirects on a URL. The max depth is checked so not be unlimited """
        if depth > MAX_DEPTH_LIMIT:
            self.log.warning("Exceeded depth limit")
            return url_list

        self.log.debug("{} depth {}".format(url, depth))
        try:
            parsed = urlparse.urlparse(url)     # this ensures we have a valid url
            # add proxy logic, if specified
            if self.proxy_host:
                self.log.debug("Using proxy: %s:%s", self.proxy_host, self.proxy_port)
                h = httplib.HTTPConnection(self.proxy_host, self.proxy_port, timeout=SOCKET_TIMEOUT)
                h.set_tunnel(parsed.netloc, parsed.port)

            else:
                h = httplib.HTTPConnection(parsed.netloc, parsed.port, timeout=SOCKET_TIMEOUT)

            h.request('HEAD', parsed.path)
            response = h.getresponse()
        except Exception as err:
            self.log.error(err)
            return list()

        new_url = response.getheader('location') if response.getheader('location') else None

        if int(response.status/100) == 3 and new_url:
            if new_url in url_list:
                return url_list
            else:
                url_list.append(new_url)
                return self.follow_url(new_url, url_list, depth+1)

        elif int(response.status/100) == 2 and new_url:
            self.log.info("Status code: {} on url {}".format(response.status, new_url))

        if new_url and new_url not in url_list:
            url_list.append(new_url)

        return url_list
