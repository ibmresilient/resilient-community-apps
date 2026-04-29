# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use, undefined-variable
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.

from .interface.helix_api import HelixAPI
# Load constant values for API Calls
from .HelixConstants import *

REQUEST_PREFIX = "/arsys/v1/entry"

class HelixClient(HelixAPI):

    def __init__(self, host, username, password, rc, port=None, verify=True):
        self.host = host
        self.username = username
        self.password = password
        self.rc = rc
        self.verify = verify
        self.port = port or DEFAULT_HTTPS_PORT
        self.base_url = HTTPS_BASE_URL(self.host, self.port)
        self.reqHeaders = {
            "content-type": "application/json",
            "Authorization": f"AR-JWT {self.get_token()}"
        }

    def get_token(self):
        """
        Accesses the BMC Helix simple authentication endpoint
        to retrieve a JWT authorization token.
        :return: The token
        :rtype: str
        """
        response = self.rc.execute("POST",
            f"{self.base_url}/jwt/login",
            data={"username": self.username, "password": self.password},
            headers={"content-type": "application/x-www-form-urlencoded"},
            verify=self.verify)

        return response.text

    def release_token(self):
        """
        Releases a JWT token so that it cannot be used
        for further interaction with the REST API.
        The function returns: a tuple with the response content as json and the http status code.

        :return: The response content and http status code as a tuple
        :rtype: tuple(json, int)
        """
        response = self.rc.execute(
            "POST",
            f"{self.base_url}/jwt/logout",
            headers=self.reqHeaders,
            verify=self.verify)

        # Logging off returns an empty 204
        # Return empty json in the absence of response/incident content
        response_json = response.json() if response.content else {}

        return response_json, response.status_code

    def create_form_entry(self, form_name, values, return_values=[], payload={}):
        """
        create_form_entry is a member function used to take a payload
        and form name and use it to create a new entry on the BMC Helix system.
        The function returns: a tuple with the response content as json and the http status code.

        :param form_name: Name of the form to add an entry for
        :type form_name: str
        :param values: Dictionary of incident values
        :type values: dict
        :param return_values: List of field names to return from the created entry
        :type return_values: List
        :param payload: Any extra options you want to include on the incident, defaults to {}
        :type payload: dict, optional
        :return: The response content and http status code as a tuple
        :rtype: tuple(json, int)
        """
        field_list = ', '.join(return_values)

        response = self.rc.execute(
            "POST",
            f"{self.base_url}{REQUEST_PREFIX}/{form_name}?fields=values({field_list})",
            json={"values": values},
            headers=self.reqHeaders,
            verify=self.verify)

        return response.json(), response.status_code

    def get_form_entry(self, form_name, req_id, payload={}):
        """
        get_form_entry is a member function used to gather form data
        based on a form name and request ID.
        The function returns: a tuple with the response content as json and the http status code.

        :param form_name: Name of the form to query
        :type form_name: str
        :param req_id: The request ID of the desired entry
        :type req_id: str
        :param payload: Any extra options you want to include on the incident, defaults to {}
        :type payload: dict, optional
        :return: The response content and http status code as a tuple
        :rtype: tuple(json, int)
        """
        response = self.rc.execute(
            "GET",
            f"{self.base_url}{REQUEST_PREFIX}/{form_name}/{req_id}",
            headers=self.reqHeaders,
            verify=self.verify)

        return response.json(), response.status_code

    def update_form_entry(self, form_name, req_id, values, payload={}):
        """
        update_form_entry is a member function used to update form data
        based on a form name and request ID.
        The function returns: a tuple with the response content as json and the http status code.

        :param form_name: Name of the form to query
        :type form_name: str
        :param req_id: The request ID of the desired entry
        :type req_id: str
        :param values: dict of incident values to update
        :type values: dict
        :param payload: Any extra options you want to include on the incident, defaults to {}
        :type payload: dict, optional
        :return: The response content and http status code as a tuple
        :rtype: tuple(json, int)
        """
        response = self.rc.execute(
            "PUT",
            f"{self.base_url}{REQUEST_PREFIX}/{form_name}/{req_id}",
            json={"values": values},
            headers=self.reqHeaders,
            verify=self.verify)

        # BMC Helix returns an empty 204 for form updates.
        # Get the updated incident and return it with the update status code
        updated_incident, _ = self.get_form_entry(form_name, req_id, values)

        return updated_incident, response.status_code

    def delete_form_entry(self, form_name, req_id, payload={}):
        """
        delete_form_entry is a member function used to delete
        a form entry based on a form name and request ID.
        The function returns: a tuple with the response content as json and the http status code.

        :param form_name: Name of the form to query
        :type form_name: str
        :param req_id: The request ID of the desired entry
        :type req_id: str
        :param payload: Any extra options you want to include on the incident, defaults to {}
        :type payload: dict, optional
        :return: The response content and http status code as a tuple
        :rtype: tuple(json, int)
        """
        response = self.rc.execute(
            "DELETE",
            f"{self.base_url}{REQUEST_PREFIX}/{form_name}/{req_id}",
            headers=self.reqHeaders,
            verify=self.verify)

        response_json = response.json() if response.content else {}

        # BMC Helix returns an empty 204 for form deletion.
        # Return empty json in the absence of response/incident content
        return response_json, response.status_code

    def query_form_entry(self, form_name, id, payload={}):
        """
        query_form_entry is a member function used to query
        a form entry based on a form name and request ID.
        The query matches an incident number to the provided ID.
        The function returns: a tuple with the response content as json and the http status code.

        :param form_name: Name of the form to query
        :type form_name: str
        :param req_id: The request ID of the desired entry
        :type req_id: str
        :param payload: Any extra options you want to include on the incident, defaults to {}
        :type payload: dict, optional
        :return: The response content and http status code as a tuple
        :rtype: tuple(json, int)
        """
        # This url formatting is less than ideal, but the BMC Helix API is very picky with how we specify endpoints
        # and therefore we cannot fully url encode.
        response = self.rc.execute(
            "GET",
            f"{self.base_url}{REQUEST_PREFIX}/{form_name}?q=%27Incident+Number%27+%3D+%22{id}%22",
            headers=self.reqHeaders,
            verify=self.verify)

        return response.json(), response.status_code

    # Used in selftest
    def get_form_schema(self, form_name):
        """
        Gets a form definition schema from BMC Helix

        :param form_name: Name of the form schema to retrieve
        :type form_name: str
        :return: The response content and http status code as a tuple
        :rtype: tuple(json, int)
        """
        response = self.rc.execute(
            "GET",
            f"{self.base_url}{REQUEST_PREFIX}/{form_name}",
            headers=self.reqHeaders,
            verify=self.verify)

        return response.json(), response.status_code
