# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use, undefined-variable
# (c) Copyright IBM Corp. 2021. All Rights Reserved.
import requests
from interface.remedy_api import RemedyAPI
# Load constant values for API Calls
from RemedyConstants import *

class RemedyClient(RemedyAPI):

    def __init__(self, host, username, password, port=None, verify=True, proxies={}):
        self.host = host
        self.username = username
        self.password = password
        self.verify = verify
        self.proxies = proxies
        self.port = port or DEFAULT_HTTPS_PORT if self.verify else port or DEFAULT_HTTP_PORT
        self.base_url = HTTPS_BASE_URL(self.host, self.port) if self.verify else HTTP_BASE_URL(self.host, self.port)
        self.authHeaders = {"content-type": "application/x-www-form-urlencoded"}
        self.reqHeaders = self.build_request_headers()

    def get_token(self):
        """
        Accesses the Remedy simple authentication endpoint
        to retrieve a JWT authorization token. The token is
        decoded based on the apparent_encoding.

        :return: the token
        :rtype: string
        """
        url = self.base_url + "/jwt/login"
        data = {"username": self.username, "password": self.password}

        response = requests.request("POST", url, data=data, headers=self.authHeaders, verify=self.verify, proxies=self.proxies)
        response.raise_for_status()
        token = response.content
        encoding = response.apparent_encoding
        token = token.decode(encoding)

        return token

    def build_request_headers(self):
        """
        Builds the request headers that Remedy expects
        for calls to the REST API

        :return: dict of request headers
        :rtype: dict
        """
        token = self.get_token()
        reqHeaders = {
            "content-type": "application/json",
            "Authorization": token
        }

        return reqHeaders

    def release_token(self):
        """
        Releases a JWT token so that it cannot be used
        for further interaction with the REST API.

        :return: null
        """
        url = self.base_url + "/jwt/logout"
        data = {"username": self.username, "password": self.password}

        response = requests.request("POST", url, data=data, headers=self.authHeaders, verify=self.verify, proxies=self.proxies)
        response.raise_for_status()

        return

    def create_form_entry(self, form_name, values, return_values, payload={}):
        """
        create_form_entry is a member function used to take a payload
        and form name and use it to create a new entry on the Remedy system. 
        The function returns: the response as json

        :param form_name: name of the form to add an entry for
        :type form_name: str
        :param values: dictionary of incident values
        :type values: dict
        :param return_values: list of field names to return from the created entry
        :type return_values: list
        :param payload: Any extra options you want to include on the incident, defaults to {}
        :type payload: dict, optional
        :return: The Response as json
        :rtype: json
        """
        field_list = ', '.join(return_values)
        url = self.base_url + "/arsys/v1/entry/{}?fields=values({})".format(form_name, field_list)
        entry = {
            "values": values
        }

        response = requests.request("POST", url, json=entry, headers=self.reqHeaders, verify=self.verify, proxies=self.proxies)
        response.raise_for_status()
        
        return response.json()

        # return response, response_json["values"]["Incident Number"], response_json["values"]["Request ID"]

    def get_form_entry(self, form_name, req_id, payload={}):
        """
        get_form_entry is a member function used to gather form data
        based on a form name and request ID
        The function returns: the response as json

        :param form_name: name of the form to query
        :type form_name: str
        :param req_id: the request ID of the desired entry
        :type req_id: str
        :param payload: Any extra options you want to include on the incident, defaults to {}
        :type payload: dict, optional
        :return: The Response as json
        :rtype: json
        """
        url = self.base_url + "/arsys/v1/entry/{}/{}".format(form_name, req_id)
        response = requests.request("GET", url, headers=self.reqHeaders, verify=self.verify, proxies=self.proxies)
        response.raise_for_status()

        return response.json()

    def update_form_entry(self, form_name, req_id, values, payload={}):
        """
        update_form_entry is a member function used to update form data
        based on a form name and request ID
        The function returns: the response as json

        :param form_name: name of the form to query
        :type form_name: str
        :param req_id: the request ID of the desired entry
        :type req_id: str
        :param values: dict of incident values to update
        :type values: dict
        :param payload: Any extra options you want to include on the incident, defaults to {}
        :type payload: dict, optional
        :return: The Response as json
        :rtype: json
        """
        entry = {
            "values": values
        }
        url = self.base_url + "/arsys/v1/entry/{}/{}".format(form_name, req_id)

        response = requests.request("PUT", url, json=entry, headers=self.reqHeaders, verify=self.verify, proxies=self.proxies)
        response.raise_for_status()

        # Remedy returns an empty 204 for form updates.
        # return True in the absence of response content
        return True
