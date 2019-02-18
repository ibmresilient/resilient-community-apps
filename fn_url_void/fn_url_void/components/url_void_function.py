# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import xmltodict
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib.components.resilient_common import validate_fields
from resilient_lib import RequestsCommon, ResultPayload
try:
    from urlparse import urlparse  # Python 2 import
except:
    from urllib.parse import urlparse  # Python 3 import


log = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'url_void_retrive_information"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_url_void", {})

        validate_fields(["api_key"], self.options)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_url_void", {})

    @function("url_void_function")
    def _url_void_function(self, event, *args, **kwargs):
        """Function: Retrieves information of a URL from the  URL Void database."""
        try:
            yield StatusMessage("URL Void function started...")
            rp = ResultPayload("fn_url_void", **kwargs)

            # Add support for Requests Common
            req_common = RequestsCommon(self.opts, self.options)

            api_key = self.options.get("api_key")
            identifier = self.options.get("identifier", "api1000")

            # Get the function parameters:
            artifact_value = kwargs.get("artifact_value")  # text
            url_void_endpoint = self.get_select_param(kwargs.get("url_void_endpoint", "Retrieve"))  # select
            validate_fields(["artifact_value", "url_void_endpoint"], kwargs)

            log.info("artifact_value: %s", artifact_value)
            log.info("url_void_endpoint: %s", url_void_endpoint)

            response = call_url_void_api(req_common, artifact_value, identifier, api_key, url_void_endpoint)

            yield StatusMessage("URL Void function completed successfully...")
            results = rp.done(True, response)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)


def get_netloc(url):
    parsed_url = urlparse(url)

    return parsed_url.netloc


def get_endpoint(url_api):
    if url_api.lower() == "retrieve":
        return ""
    elif url_api.lower() == "scan":
        return "scan"
    elif url_api.lower() == "rescan":
        return "rescan"
    else:
        raise ValueError("Unhandled url_api value: {0}. Supported values: retrieve, scan and rescan".format(url_api))


def call_url_void_api(requests_common, artifact_value, identifier, api_key, url_void_api):
    netloc = get_netloc(artifact_value)
    endpoint = get_endpoint(url_void_api)
    url = "https://api.urlvoid.com/{}/{}/host/{}/{}".format(identifier, api_key, netloc, endpoint)

    response = requests_common.execute_call("get", url, payload={}, log=log, resp_type="text")

    # Convert and return response to a dictionary
    return xmltodict.parse(response)
