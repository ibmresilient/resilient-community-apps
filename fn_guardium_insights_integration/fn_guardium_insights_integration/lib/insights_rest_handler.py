# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

import json

import requests
from requests.exceptions import SSLError
from resilient_lib import str_to_bool

from fn_guardium_insights_integration.lib.custom_exceptions import *
from fn_guardium_insights_integration.lib.firewall_auth import firewall_authenticate


class GuardiumInsightsAPI(object):
    """
    Guardium Insights Restful Service handler.
    """

    def __init__(self, options, log=None):
        self.log = log
        self.headers = dict()
        self.auth_key = options.get("insights_encoded_token")
        self.proxy = {"http": options.get("proxy"), "https": options.get("proxy")}
        self.guardium_cert = str_to_bool(options.get("guardium_ca_file"))
        self.enable_firewall_auth = str_to_bool(options.get("enable_firewall_auth"))
        if self.enable_firewall_auth:
            self.bso_ip = options.get("bso_ip")
            self.bso_user = options.get("bso_user")
            self.bso_password = options.get("bso_password")

        self.set_headers_with_access_token()

    def set_headers_with_access_token(self):
        """
        Generates the Guardium Access token, and sets the header dict
        :return:
        """
        self.headers = {"Authorization": self.auth_key, "Content-Type": "application/json"}

    def grd_get(self, url, **kwargs):
        """
        Makes GET call to Guardium Insights with given url.
        :param url: A GET request url
        :param kwargs: other param needs to GET call
        :return: request response
        """
        response = self.invoke_request_validate_response(
            lambda r: requests.get(url=url, headers=self.headers, verify=self.guardium_cert, proxies=self.proxy,
                                   **kwargs))
        return response

    def grd_post(self, url, data=None, json=None, multipart_data=None, **kwargs):
        """
        Makes POST call to Guardium Insights with given url and data
        :param url:A POST URL for the new :class:`Request` object.

        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
        :param json: (optional) json data to send in the body of the :class:`Request`.
        :param kwargs: Optional arguments that ``request`` takes.
        :param multipart_data:optional, specify any multipart data
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """
        response = self.invoke_request_validate_response(lambda r: self.__grd_post(url, data=data, json=json,
                                                                                   multipart_data=multipart_data,
                                                                                   **kwargs))
        return response

    def __grd_post(self, url, data=None, json=None, multipart_data=None, **kwargs):
        headers = dict(self.headers)
        if multipart_data is not None:
            del headers["Content-Type"]
            response = requests.post(url=url, data=data, json=json, files=multipart_data, headers=self.headers,
                                     verify=self.guardium_cert, proxies=self.proxy, **kwargs)
        else:
            response = requests.post(url=url, data=data, json=json, headers=self.headers, verify=self.guardium_cert,
                                     proxies=self.proxy, **kwargs)
        return response

    def grd_put(self, url, **kwargs):
        """
        Makes PUT call to Guardium Insights with given url and data
        """
        response = self.invoke_request_validate_response(
            lambda r: requests.put(url=url, headers=self.headers, verify=self.guardium_cert, proxies=self.proxy,
                                   **kwargs))
        return response

    def grd_delete(self, url, **kwargs):
        """Sends a DELETE request to Guardium Insights.
        :param url: URL for the new :class:`Request` object.
        :param kwargs: Optional arguments that ``request`` takes.
        :return: class:`Response <Response>` object
        :rtype: requests.Response
        """
        response = self.invoke_request_validate_response(
            lambda r: requests.delete(url=url, headers=self.headers, verify=self.guardium_cert, proxies=self.proxy,
                                      **kwargs))
        return response

    def invoke_request_validate_response(self, invoke_request):
        """
        Generate the new access token whenever token becomes invalid.
        :param invoke_request: request GET/POST/PUT/DELETE function lambda object
        :return: class:`Response <Response>` object
        """
        response = dict()
        try:
            response = invoke_request(self)
        except SSLError:
            if self.enable_firewall_auth:
                self.log.info(u"Authentication with firewall")
                firewall_authenticate(self.bso_ip, self.bso_user, self.bso_password, self.log, proxies=self.proxy)
                response = invoke_request(self)
        if response.status_code == 200:
            try:
                return response.json()
            except Exception as json_err:
                return response.text

        if response.status_code != 200:
            raise GuardiumInsightsApiError(response.text)
