# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use, undefined-variable
# (c) Copyright IBM Corp. 2021. All Rights Reserved.
from .interface.remedy_api import RemedyAPI
# Load constant values for API Calls
from .RemedyConstants import *

REQUEST_PREFIX = "/arsys/v1/entry"


class RemedyClient(RemedyAPI):

    def __init__(self, host, username, password, rc, port=None, verify=True):
        self.host = host
        self.username = username
        self.password = password
        self.rc = rc
        self.verify = verify
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
        :rtype: str
        """
        url = self.base_url + "/jwt/login"
        data = {"username": self.username, "password": self.password}

        response = self.rc.execute_call_v2("POST", url, data=data, headers=self.authHeaders, verify=self.verify)
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
            "Authorization": "AR-JWT " + token
        }

        return reqHeaders

    def release_token(self):
        """
        Releases a JWT token so that it cannot be used
        for further interaction with the REST API.
        The function returns: a tuple with the response content as json and the http status code.

        :return: the response content and http status code as a tuple
        :rtype: tuple(json, int)
        """
        url = self.base_url + "/jwt/logout"

        response = self.rc.execute_call_v2("POST", url, headers=self.reqHeaders, verify=self.verify)

        # logging off returns an empty 204
        # return empty json in the absence of response/incident content
        response_json = response.json() if response.content else {}

        return response_json, response.status_code

    def create_form_entry(self, form_name, values, return_values=[], payload={}):
        """
        create_form_entry is a member function used to take a payload
        and form name and use it to create a new entry on the Remedy system. 
        The function returns: a tuple with the response content as json and the http status code.

        :param form_name: name of the form to add an entry for
        :type form_name: str
        :param values: dictionary of incident values
        :type values: dict
        :param return_values: list of field names to return from the created entry
        :type return_values: list
        :param payload: Any extra options you want to include on the incident, defaults to {}
        :type payload: dict, optional
        :return: the response content and http status code as a tuple
        :rtype: tuple(json, int)
        """
        field_list = ', '.join(return_values)
        url = self.base_url + REQUEST_PREFIX + "/{}?fields=values({})".format(form_name, field_list)
        entry = {
            "values": values
        }

        response = self.rc.execute_call_v2("POST", url, json=entry, headers=self.reqHeaders, verify=self.verify)
        
        return response.json(), response.status_code

    def get_form_entry(self, form_name, req_id, payload={}):
        """
        get_form_entry is a member function used to gather form data
        based on a form name and request ID
        The function returns: a tuple with the response content as json and the http status code.

        :param form_name: name of the form to query
        :type form_name: str
        :param req_id: the request ID of the desired entry
        :type req_id: str
        :param payload: Any extra options you want to include on the incident, defaults to {}
        :type payload: dict, optional
        :return: the response content and http status code as a tuple
        :rtype: tuple(json, int)
        """
        url = self.base_url + REQUEST_PREFIX + "/{}/{}".format(form_name, req_id)
        response = self.rc.execute_call_v2("GET", url, headers=self.reqHeaders, verify=self.verify)

        return response.json(), response.status_code

    def update_form_entry(self, form_name, req_id, values, payload={}):
        """
        update_form_entry is a member function used to update form data
        based on a form name and request ID
        The function returns: a tuple with the response content as json and the http status code.

        :param form_name: name of the form to query
        :type form_name: str
        :param req_id: the request ID of the desired entry
        :type req_id: str
        :param values: dict of incident values to update
        :type values: dict
        :param payload: Any extra options you want to include on the incident, defaults to {}
        :type payload: dict, optional
        :return: the response content and http status code as a tuple
        :rtype: tuple(json, int)
        """
        entry = {
            "values": values
        }
        url = self.base_url + REQUEST_PREFIX + "/{}/{}".format(form_name, req_id)

        response = self.rc.execute_call_v2("PUT", url, json=entry, headers=self.reqHeaders, verify=self.verify)
        
        # Remedy returns an empty 204 for form updates.
        # get the updated incident and return it with the update status code
        status_code = response.status_code
        updated_incident, _ = self.get_form_entry(form_name, req_id, values)

        return updated_incident, status_code

    def delete_form_entry(self, form_name, req_id, payload={}):
        """
        delete_form_entry is a member function used to delete
        a form entry based on a form name and request ID.
        The function returns: a tuple with the response content as json and the http status code.

        :param form_name: name of the form to query
        :type form_name: str
        :param req_id: the request ID of the desired entry
        :type req_id: str
        :param payload: Any extra options you want to include on the incident, defaults to {}
        :type payload: dict, optional
        :return: the response content and http status code as a tuple
        :rtype: tuple(json, int)
        """
        url = self.base_url + REQUEST_PREFIX + "/{}/{}".format(form_name, req_id)
        response = self.rc.execute_call_v2("DELETE", url, headers=self.reqHeaders, verify=self.verify)

        response_json = response.json() if response.content else {}

        # Remedy returns an empty 204 for form deletion.
        # return empty json in the absence of response/incident content
        return response_json, response.status_code

    # used in selftest
    def get_form_schema(self, form_name):
        """Gets a form definition schema from remedy

        :param form_name: name of the form schema to retrieve
        :type form_name: str
        :return: the response content and http status code as a tuple
        :rtype: tuple(json, int)
        """
        url = self.base_url + REQUEST_PREFIX + "/{}".format(form_name)
        response = self.rc.execute_call_v2("GET", url, headers=self.reqHeaders, verify=self.verify)

        return response.json(), response.status_code
        