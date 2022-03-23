# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Function implementation"""

import logging
from resilient_lib import RequestsCommon
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

CONTENT_TYPE = "Content-type"
CONTENT_TYPE_JSON = "application/json"

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
            rest_method = self.get_select_param(kwargs.get("rest_method"))  # select, values: "GET", "HEAD", "POST", "PUT", "DELETE", "OPTIONS"
            rest_url = kwargs.get("rest_url")  # text
            rest_headers = self.get_textarea_param(kwargs.get("rest_headers"))  # textarea
            rest_cookies = self.get_textarea_param(kwargs.get("rest_cookies"))  # textarea
            rest_body = self.get_textarea_param(kwargs.get("rest_body"))  # textarea
            rest_verify = kwargs.get("rest_verify")  # boolean

            log = logging.getLogger(__name__)
            log.info("rest_method: %s", rest_method)
            log.info("rest_url: %s", rest_url)
            log.info("rest_headers: %s", rest_headers)
            log.info("rest_cookies: %s", rest_cookies)
            log.info("rest_body: %s", rest_body)
            log.info("rest_verify: %s", rest_verify)

            # Read newline-separated 'rest_headers' into a dictionary
            if isinstance(rest_headers, dict):
                headers_dict = rest_headers
            else:
                headers_dict = {}
                if rest_headers is not None:
                    lines = rest_headers.split("\n")
                    for line in lines:
                        keyval = line.strip().split(":", 1)
                        if len(keyval) == 2:
                            headers_dict[keyval[0].strip()] = keyval[1].strip()

            # Read newline-separated 'rest_cookies' into a dictionary
            if isinstance(rest_cookies, dict):
                cookies_dict = rest_cookies
            else:
                cookies_dict = {}
                if rest_cookies is not None:
                    lines = rest_cookies.split("\n")
                    for line in lines:
                        keyval = line.strip().split(":", 1)
                        if len(keyval) == 2:
                            cookies_dict[keyval[0].strip()] = keyval[1].strip()

            resp = make_rest_call(self.opts, self.options, rest_method, rest_url,
                                  headers_dict, cookies_dict, rest_body, rest_verify)

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

def make_rest_call(opts, options, rest_method, rest_url, headers_dict, cookies_dict, rest_body, rest_verify):
    rc = RequestsCommon(opts, options)

    if CONTENT_TYPE in headers_dict and CONTENT_TYPE_JSON in headers_dict[CONTENT_TYPE]:
        return rc.execute_call_v2(rest_method, rest_url,
                                  headers=headers_dict,
                                  cookies=cookies_dict,
                                  json=rest_body,
                                  verify=rest_verify)

    return rc.execute_call_v2(rest_method, rest_url,
                              headers=headers_dict,
                              cookies=cookies_dict,
                              data=rest_body,
                              verify=rest_verify)

def dedup_dict(item_list):
    """
    this is needed to ensure headers or cookies keys are not duplicated
    :param item_list:
    :return: dictionary representation
    """
    return {k: v for k, v in item_list.items()}
