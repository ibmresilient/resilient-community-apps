# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

import requests
from resilient_lib import RequestsCommon
from resilient_lib.components.integration_errors import IntegrationError
from resilient_lib.components.requests_common import verify_headers

class RequestsSep(RequestsCommon):
    """
    This class inherits from class RequestsCommon and over-rides the execute_call method.
    The class will be used to manage REST calls.

    """
    def __init__(self, opts, function_opts):
        RequestsCommon.__init__(self, opts, function_opts)

    def execute_call(self, verb, url, params=None, payload=None, log=None, basicauth=None, verify_flag=True, headers=None,
                     proxies=None, timeout=None, resp_type='json', callback=None):
        """
        Function: perform the http API call. Different types of http operations are supported:
        GET, HEAD, PATCH, POST, PUT, DELETE
        Errors raise IntegrationError
        If a callback method is provided, then it's called to handle the error

        Using the 'json' parameter in the request will change the Content-Type in the header to application/json.
        If the headers you send include a specific Content-Type, your payload will be send as 'data' and not 'json'.

        :param verb: GET, HEAD, PATCH, POST, PUT, DELETE
        :param url:
        :param basicauth: used for basic authentication - (user, password)
        :param params: (optional) Dictionary or bytes to be sent in the query of the request.
        :param payload:
        :param log: optional log statement
        :param verify_flag: True/False - False used for debugging generally
        :param headers: dictionary of http headers
        :param proxies: http and https proxies for call
        :param timeout: timeout before call should abort
        :param resp_type: type of output to return: json, text, bytes
        :param callback: callback routine used to handle errors
        :return: json of returned data
        """

        try:
            (payload and log) and log.debug(payload)

            if verb.lower() not in ('get', 'post', 'put', 'patch', 'delete', 'head'):
                raise IntegrationError("unknown verb {}".format(verb))

            if proxies is None:
                proxies = self.get_proxies()

            if verb.lower() in {"post", "patch", "put"}:
                if verify_headers(headers):
                    # If headers dict specifies Content-Type,
                    # pass the payload to the data argument.
                    # Use Content-Type specified in headers.
                    resp = requests.request(verb.upper(), url, verify=verify_flag, headers=headers, params=params, data=payload,
                                            auth=basicauth, timeout=timeout, proxies=proxies)
                else:
                    # If headers dict does not specify Content-Type,
                    # pass payload to the json argument.
                    # Content-Type will automatically set to application/json.
                    resp = requests.request(verb.upper(), url, verify=verify_flag, headers=headers, params=params, json=payload,
                                            auth=basicauth, timeout=timeout, proxies=proxies)
            else:
                resp = requests.request(verb.upper(), url, verify=verify_flag, headers=headers, params=params,
                                        auth=basicauth, timeout=timeout, proxies=proxies)

            if resp is None:
                raise IntegrationError('no response returned')

            # custom handler for response handling?
            if callback:
                return callback(resp)

            # standard error handling
            if resp.status_code >= 300:
                # get the result
                # log resp.status_code in case resp.text isn't available
                raise IntegrationError(
                    "status_code: {}, msg: {}".format(resp.status_code, resp.text if resp.text else "N/A"))

            # check if anything returned
            log and log.debug(resp.text)

            # get the result
            if resp_type == 'json':
                r = resp.json()
            elif resp_type == 'text':
                r = resp.text
            elif resp_type == 'bytes':
                r = resp.content
            else:
                raise IntegrationError("incorrect response type: {}".format(resp_type))

            # Produce a IntegrationError with the return value
            return r      # json object needed, not a string representation
        except Exception as err:
            msg = str(err)
            log and log.error(msg)
            raise IntegrationError(msg)
