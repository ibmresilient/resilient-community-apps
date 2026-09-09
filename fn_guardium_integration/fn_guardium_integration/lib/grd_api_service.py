# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2020
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

import requests
from requests.exceptions import SSLError
from resilient_lib import str_to_bool
from fn_guardium_integration.util.static_data import TOCKEN_URL
from fn_guardium_integration.lib.firewall_auth import firewall_authenticate


class GuardiumAPI(object):
    """
    Guardium Restful Service handler.
    """

    def __init__(self, options, client_secret, unique_id, log):
        self.log = log
        self.access_token = ""
        self.headers = dict()
        self.proxy = options.get("proxy")
        self.guardium_host = options.get("guardium_host")
        self.port = options.get("port")
        self.guardium_user = options.get("guardium_user")
        self.guardium_passowrd = options.get("guardium_password")
        self.guardium_cert = str_to_bool(options.get("guardium_cert"))
        self.enable_firewall_auth = str_to_bool(options.get("enable_firewall_auth"))
        if self.enable_firewall_auth:
            self.bso_ip = options.get("bso_ip")
            self.bso_user = options.get("bso_user")
            self.bso_password = options.get("bso_password")
        self.client_secret = client_secret
        self.unique_id = unique_id
        if self.client_secret:
            self.set_headers_with_new_access_token()

    def set_headers_with_new_access_token(self):
        """
        Generates the Guardium Access token, and sets the header dict
        :return:
        """
        self.get_access_token()
        self.headers = {"Authorization": "Bearer " + self.access_token, "Content-Type": "application/json"}

    def get_access_token(self):
        """
        Generates the guardium access token
        :return:
        """
        data = [("client_id", self.unique_id), ("grant_type", "password"), ("client_secret", self.client_secret),
                ("username", self.guardium_user), ("password", self.guardium_passowrd), ]
        try:
            req_response = requests.post(TOCKEN_URL.format(host=self.guardium_host, port=self.port), data=data,
                                         verify=self.guardium_cert)
            if req_response.ok:
                self.access_token = req_response.json().get("access_token")
                self.log.debug(u"Generated Access Token: {}".format(self.access_token))
            else:
                raise ValueError("Error while Generating access token: {}".format(req_response.content))
        except SSLError:
            if self.enable_firewall_auth:
                firewall_authenticate(self.bso_ip, self.bso_user, self.bso_password, self.log)
                req_response = requests.post(TOCKEN_URL.format(host=self.guardium_host, port=self.port), data=data,
                                             verify=self.guardium_cert)
                if req_response.ok:
                    self.access_token = req_response.json().get("access_token")
                    self.log.debug(u"Generated Access Token: {}".format(self.access_token))
                else:
                    raise ValueError("Error while Generating access token: {}".format(req_response.content))

    def grd_get(self, url, **kwargs):
        """
        Makes GET call to Guardium with given url.
        :param url: A GET request url
        :param kwargs: other param needs to GET call
        :return: request response
        """
        response = self.invoke_with_retry_on_invalid_token(lambda r: requests.get(url=url, headers=self.headers,
                                                                                  verify=self.guardium_cert, **kwargs))
        return response

    def grd_post(self, url, data=None, json=None, multipart_data=None, **kwargs):
        """
        Makes POST call to Guardium with given url and data
        :param url:A POST URL for the new :class:`Request` object.

        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
        :param json: (optional) json data to send in the body of the :class:`Request`.
        :param kwargs: Optional arguments that ``request`` takes.
        :param multipart_data:optional, specify any multipart data
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """
        response = self.invoke_with_retry_on_invalid_token(lambda r: self.__grd_post(url, data=data, json=json,
                                                                                     multipart_data=multipart_data,
                                                                                     **kwargs))
        return response

    def __grd_post(self, url, data=None, json=None, multipart_data=None, **kwargs):
        headers = dict(self.headers)
        if multipart_data is not None:
            del headers["Content-Type"]
            response = requests.post(url=url, data=data, json=json, files=multipart_data, headers=self.headers,
                                     verify=self.guardium_cert, **kwargs)
        else:
            response = requests.post(url=url, data=data, json=json, headers=self.headers, verify=self.guardium_cert,
                                     **kwargs)
        return response

    def grd_put(self, url, **kwargs):
        """
        Makes PUT call to Guardium with given url and data
        """
        response = self.invoke_with_retry_on_invalid_token(lambda r: requests.put(url=url, headers=self.headers,
                                                                                  verify=self.guardium_cert, **kwargs))
        return response

    def grd_delete(self, url, **kwargs):
        """Sends a DELETE request to Guardium.
        :param url: URL for the new :class:`Request` object.
        :param kwargs: Optional arguments that ``request`` takes.
        :return: class:`Response <Response>` object
        :rtype: requests.Response
        """
        response = self.invoke_with_retry_on_invalid_token(lambda r: requests.delete(url=url, headers=self.headers,
                                                                                     verify=self.guardium_cert,
                                                                                     **kwargs))
        return response

    def invoke_with_retry_on_invalid_token(self, invoke_request):
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
                firewall_authenticate(self.bso_ip, self.bso_user, self.bso_password, self.log)
                response = invoke_request(self)

        if response.status_code == 400:
            return response

        if response.json():
            if self.grd_is_invalid_token(response):
                self.set_headers_with_new_access_token()
                response = invoke_request(self)
        return response

    @staticmethod
    def grd_is_invalid_token(response):
        """
        Wrapper to check Invalid token, if its invalid token returns `True` else `False`.
        """
        if response.status_code == 401 and not response.content is None and isinstance(response.json(), dict) and \
                "error" in response.json() and response.json()["error"] == "invalid_token":
            return True
        return False
