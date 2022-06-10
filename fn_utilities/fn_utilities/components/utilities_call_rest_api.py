# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Function implementation"""

from logging import getLogger
from resilient_lib import RequestsCommon
from resilient_circuits import ResilientComponent, function, FunctionResult, FunctionError

CONTENT_TYPE = "Content-type"
CONTENT_TYPE_JSON = "application/json"
LOG = getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'call_rest_api"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get("fn_utilities", {})

    @function("utilities_call_rest_api")
    def _call_rest_api_function(self, event, *args, **kwargs):
        """Function: Call a REST web service.
           The function parameters determine the type of call (GET, POST, etc),
           the URL, and optionally the headers and body."""
        try:
            # Get the function parameters:
            rest_method = self.get_select_param(kwargs.get("rest_method"))  # select, values: "GET", "HEAD", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"
            rest_url = kwargs.get("rest_url")  # text
            rest_headers = self.get_textarea_param(kwargs.get("rest_headers"))  # textarea
            rest_cookies = self.get_textarea_param(kwargs.get("rest_cookies"))  # textarea
            rest_body = self.get_textarea_param(kwargs.get("rest_body"))  # textarea
            rest_verify = kwargs.get("rest_verify")  # boolean
            rest_timeout = kwargs.get("rest_timeout", 600) # Default timeout to 600 seconds

            LOG.info("rest_method: %s", rest_method)
            LOG.info("rest_url: %s", rest_url)
            LOG.info("rest_headers: %s", rest_headers)
            LOG.info("rest_cookies: %s", rest_cookies)
            LOG.info("rest_body: %s", rest_body)
            LOG.info("rest_verify: %s", rest_verify)
            LOG.info("rest_timeout: %s", rest_timeout)

            # Read newline-separated 'rest_headers' into a dictionary
            headers_dict = rest_headers
            if not isinstance(rest_headers, dict):
                headers_dict = build_dict(rest_headers)

            # Read newline-separated 'rest_cookies' into a dictionary
            cookies_dict = rest_cookies
            if not isinstance(rest_cookies, dict):
                cookies_dict = build_dict(rest_cookies)

            resp = make_rest_call(self.opts, self.options, rest_method, rest_url,
                                  headers_dict, cookies_dict, rest_body, rest_verify, rest_timeout)

            try:
                response_json = resp.json()
            except:
                response_json = None

            results = {
                "ok": resp.ok,
                "url": resp.url,
                "status_code": resp.status_code,
                "reason": resp.reason,
                "cookies": dedup_dict(resp.cookies),
                "headers": dedup_dict(resp.headers),
                "elapsed": int(resp.elapsed.total_seconds() * 1000.0),
                "apparent_encoding": resp.apparent_encoding,
                "text": resp.text,
                "json": response_json,
                "links": resp.links,
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()

def build_dict(rest_temp):
    """
    Builds a dictionary from either the rest_headers or rest_cookies
    :param rest_temp: rest_headers or rest_cookies
    :return: Dictionary
    """
    temp_dict = {}
    if rest_temp is not None:
        lines = rest_temp.split("\n")
        for line in lines:
            keyval = line.strip().split(":", 1)
            if len(keyval) == 2:
                temp_dict[keyval[0].strip()] = keyval[1].strip()

    return temp_dict

def make_rest_call(opts, options, rest_method, rest_url, headers_dict, cookies_dict, rest_body, rest_verify, rest_timeout):
    rc = RequestsCommon(opts, options)

    if CONTENT_TYPE in headers_dict and CONTENT_TYPE_JSON in headers_dict[CONTENT_TYPE]:
        return rc.execute_call_v2(rest_method, rest_url,
                                  headers=headers_dict,
                                  cookies=cookies_dict,
                                  json=rest_body,
                                  verify=rest_verify,
                                  timeout=rest_timeout)

    return rc.execute_call_v2(rest_method, rest_url,
                              headers=headers_dict,
                              cookies=cookies_dict,
                              data=rest_body,
                              verify=rest_verify,
                              timeout=rest_timeout)

def dedup_dict(item_list):
    """
    this is needed to ensure headers or cookies keys are not duplicated
    :param item_list:
    :return: dictionary representation
    """
    return {k: v for k, v in item_list.items()}
