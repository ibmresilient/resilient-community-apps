# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Function implementation"""

import logging
import requests
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'call_rest_api"""

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
            rest_body = self.get_textarea_param(kwargs.get("rest_body"))  # textarea
            rest_verify = kwargs.get("rest_verify")  # boolean

            log = logging.getLogger(__name__)
            log.info("rest_method: %s", rest_method)
            log.info("rest_url: %s", rest_url)
            log.info("rest_headers: %s", rest_headers)
            log.info("rest_body: %s", rest_body)
            log.info("rest_verify: %s", rest_verify)

            # Read newline-separated 'rest_headers' into a dictionary
            headers_dict = {}
            if rest_headers is not None:
                lines = rest_headers.split("\n")
                for line in lines:
                    keyval = line.strip().split(":", 1)
                    if len(keyval) == 2:
                        headers_dict[keyval[0].strip()] = keyval[1].strip()

            resp = requests.request(rest_method, rest_url,
                                    headers=headers_dict,
                                    data=rest_body,
                                    verify=rest_verify)

            try:
                response_json = resp.json()
            except:
                response_json = None

            results = {
                "ok": resp.ok,
                "url": resp.url,
                "status_code": resp.status_code,
                "reason": resp.reason,
                "cookies": dict(resp.cookies),
                "headers": dict(resp.headers),
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