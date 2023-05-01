# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Symantec SEP client support classes. """

import logging, json
from resilient_lib import RequestsCommon, validate_fields
from urllib.parse import urljoin
from fn_sep.lib.sep_client import Sepclient

LOG = logging.getLogger(__name__)


class Symantec_SEP:
    """
    Client class for Symantec SEP.
    """

    def __init__(self, function_options: dict, request_common: RequestsCommon) -> None:
        """
        Class constructor.

        :param function_options: contains app.config details
        :type function_options: dict
        :param request_common: object of resilient class 'RequestsCommon'. \
            The class represents common functions around the use of the requests package for REST based APIs
        :type request_common: RequestsCommon
        """
        self.request_common=request_common

        sep_object=Sepclient(function_options)

        self.headers = sep_object._headers
        self.base_url=sep_object.base_url
        self.base_path=sep_object.base_path

    def transform_inputs(self, input_dict: dict) -> dict:
        """
        Update input dictionary.
        This function will perform the following actions:
            - Removes common prefix 'Symantec_SEP_' from all keys in 'input_dict'.
            - Strip whitespaces from beginning and end of string parameters in 'input_dict'.

        :param input_dict: Resilient Function input parameters.
        :type input_dict: dict
        :return: Processed input parameters for Symantec SEP api.
        :rtype: dict
        """
        params = {
            key.replace('sep_','') \
            : val.strip() if isinstance(val, str) else val \
            for key,val in input_dict.items()
        }
        return params


    def make_api_call(self, method: str, url: str, use_callback=False, query_params: dict=None, payload_data: dict=False, message: str='OK') -> dict:
        """This function is used to call a specific API and return the response.

        :param method: specific method for the API call (GET,POST,PUT,DELETE)
        :type method: str
        :param url: specific url to hit the API
        :type url: str
        :param query_params: query parameters to pass to the API, defaults to None
        :type query_params: dict, optional
        :param payload_data: payload data to pass to the API, defaults to False
        :type payload_data: dict, optional
        :param message: success message to return in response, defaults to 'OK'
        :type message: str, optional
        :raises ValueError: returns reason of failure in response
        :return: returns the json response
        :rtype: dict
        """
        
        path = f'{self.base_path}{url}'
        url = urljoin(self.base_url, path)

        if use_callback:
            response,err = self.request_common.execute(
                method, url=url, params=query_params, json=payload_data, headers=self.headers, verify=False,callback=callback)
            if err==None and not bool(response):
                response = {"message": message}
            return response, err
        
        else:
            response = self.request_common.execute(
                method, url=url, params=query_params, json=payload_data, headers=self.headers, verify=False)
            if response.ok:
                if not response.content :
                    response = {"message": message}
                else:
                    response = response.json()

        return response


def callback(response):
    """This function fetches original API returned error message.
    :return: returns response and error message if any
    """
    error_msg = None
    content = None
    if response.status_code >= 300:
        msg = json.loads(response.content.decode('utf-8'))
        if 'errorMessage' in msg:
            msg = msg['errorMessage']
        elif 'message' in msg:
            msg = msg['message']  

        error_msg = f"Status Code: {response.status_code}, ErrorMessage: {msg}"

    else:
        try:
            if response.content:
                content = json.loads(response.content.decode("utf-8"))
            else:
                content=""
        except:
            content = ""

    return content, error_msg