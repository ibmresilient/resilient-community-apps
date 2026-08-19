# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# Generated with resilient-sdk v51.0.1.1.1.dev16+g03d1460d
# pragma pylint: disable=line-too-long, wrong-import-order

"""AppFunction implementation"""

import traceback
from resilient_lib import str_to_bool
from requests.exceptions import HTTPError, ReadTimeout
from requests import Response
from json import loads, dumps

from fn_low_code.lib.constants import INTEGRATION_ERROR
from fn_low_code.lib.helpers import set_security_data, clean_encoding
from resilient_circuits import AppFunctionComponent, low_code_function
from resilient_circuits.action_message import LowCodeResult
from resilient_lib import RequestsCommon, IntegrationError
from simplejson.errors import JSONDecodeError

PACKAGE_NAME = "fn_low_code"
FN_NAME = "low_code"

# These defaults should be integrated with the UI parameters/payload which will be made available TBD
DEFAULT_VERIFY = "True"
DEFAULT_TIMEOUT = 60
DEFAULT_RETRIES = 1
DEFAULT_RETRY_DELAY = 2
DEFAULT_RETRY_BACKOFF = 2

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'low_code'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @low_code_function()
    def _app_function(self, low_code_request: dict):
        """
        Given RestAPIExecutionEventDTO.request_payload as a message input
        """
        yield self.status_message(f"Low Code execution started {FN_NAME}")

        try:
            # Extract vars to make request
            method = low_code_request.get("method", "")     # REST method
            url = low_code_request.get("server_url")    # url to make request to
            headers: dict = low_code_request.get("headers", {})   # headers to pass with request

            # handle path_params in URL endpoint
            path_params: dict = low_code_request.get("path_params", {})
            if path_params:
                url = url.format(**path_params)

            query_params: dict = low_code_request.get("query_params", {})
            query_params = {k: clean_encoding(v) for k, v in query_params.items()}

            headers["Accept"] = low_code_request.get("response_content_type", "application/json")        # Accept (send) JSON as default
            headers["Content-Type"] = low_code_request.get("request_content_type", "application/json")    # Content-type (receive) JSON as default

            rc = RequestsCommon(self.opts, self.options)

            # pull out security info
            new_headers, new_query_params = set_security_data(low_code_request.get("security", {}), rc)
            # merge new settings
            headers = headers | new_headers if new_headers else headers
            query_params = query_params | new_query_params if new_query_params else query_params
            self.LOG.debug("Headers: %s", headers)
            self.LOG.debug("Query parameters: %s", query_params)

            # merge the parameters together
            rest_properties = {
                "params"  : query_params,
                "headers" : headers,
            } | get_env_params(low_code_request.get("custom_params", {})) # timeout, retries, verify

            request_body: dict = loads(low_code_request.get("request_body") if low_code_request.get("request_body") else "{}")
            if method.lower() in ["post", "put"]:
                rest_properties["json"] = request_body
            else:
                rest_properties["data"] = request_body

            response: Response = rc.execute(method, url, callback=lowcode_callback, **rest_properties)

            if response:
                self.is_json(response) # just a check of the data returned

                # Formatting response
                results = make_results(True, response.status_code, response.text)
            else:
                self.LOG.error("No response received from: %s. Could be num_retries", url)
                results = make_results(False, INTEGRATION_ERROR, dumps({"err": "no response"}), reason="no response")
        except IntegrationError as err:
            self.LOG.error("REST API call error %s", str(err))
            if isinstance(err.__cause__, HTTPError):
                msg = err.__cause__.errno
                err_code = err.__cause__.strerror
            elif isinstance(err.__cause__, ReadTimeout):
                msg = "URL Timeout"
                err_code = INTEGRATION_ERROR
            else:
                msg = str(err)
                err_code = INTEGRATION_ERROR

            results = make_results(False, err_code, dumps({"err": msg}), reason=msg)
        except Exception as exception_err:
            self.LOG.error(traceback.format_exc())
            self.LOG.error("low_code app error %s", str(exception_err))
            results = make_results(False, INTEGRATION_ERROR, dumps({"err": str(exception_err)}), reason=str(exception_err))

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield LowCodeResult(results, success=results["success"], reason=results["reason"])

    def is_json(self, response: Response) -> bool:
        """simple check of response returned. It is not an error if the result is not JSON.
            Some API calls return text

        :param response: API call response
        :type response: Response
        :return: True is JSON result is present
        :rtype: bool
        """
        try:
            self.LOG.debug("Attempting to JSON decode response")
            if hasattr(response, "json"):
                response_json = response.json()
                self.LOG.debug(dumps(response_json, indent=2))
                return True
        except JSONDecodeError:
            self.LOG.warning("Unable to decode json response: %s", response.text)

        return False

def lowcode_callback(response: Response) -> Response:
    """ custom callback function to retry 400 error codes, if retry is enabled """
    if response.status_code >= 400 and response.status_code < 500:
        # raise HTTPError which will be retried
        raise HTTPError(f"{response.status_code}: {response.text}", response.status_code)

    # all other status codes should return normally
    # note this bypasses the normal rc.execute logic which
    # would raise an error for 500 errors
    return response

def make_results(success: bool, status_code: int, content: str, reason: str=None) -> dict:
    """simple result dictionary maker

    :param status_code: API call status code or 999 when error occurred
    :type status_code: int
    :param content: result of api call
    :type content: dict
    :param reason: error reason, defaults to None
    :type reason: str, optional
    :return: result dictionary to return to SOAR
    :rtype: dict
    """
    return {
        "success": success,
        "status_code": status_code,
        "reason": reason,
        "content": content
    }

def get_env_params(env_params: dict) -> dict:
    """get the settings which control the behavior of the REST API call. Ex. timeout and retries.
        Default values are used when no value is found from the connector

    :param env_params: settings from the connector
    :type env_params: dict
    :return: values from the connector or defaults
    :rtype: dict
    """
    return {
        "verify"  : str_to_bool(env_params.get("verify_cert", DEFAULT_VERIFY)),
        "timeout" : env_params.get("request_timeout", DEFAULT_TIMEOUT),
        "retry_tries" : env_params.get("num_retries", DEFAULT_RETRIES),
        "retry_delay" : env_params.get("retry_delay", DEFAULT_RETRY_DELAY),
        "retry_backoff" : env_params.get("retry_backoff", DEFAULT_RETRY_BACKOFF),
    }
