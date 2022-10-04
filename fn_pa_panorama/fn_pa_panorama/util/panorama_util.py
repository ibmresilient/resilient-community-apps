# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

from logging import getLogger
from json import loads
from resilient_lib.components.resilient_common import validate_fields, str_to_bool
from resilient_lib.components.requests_common import RequestsCommon

LOG = getLogger(__name__)
DEFAULT_API_VERSION="9.0"
URI_PATH = "restapi"
PACKAGE_NAME = "fn_pa_panorama"

class PanoramaClient:
    """Object to handle the communication and authentication between the integration and Panorama"""
    def __init__(self, opts, pan_config, location, vsys=None):
        pan_config["location"] = location

        # validate config fields
        validate_fields(["panorama_host", "api_key", "location"], pan_config)

        self.__key = pan_config["api_key"] 
        self.__url_path = "/".join([URI_PATH, pan_config.get("api_version", DEFAULT_API_VERSION)])
        self.__vsys = vsys

        self.verify = str_to_bool(pan_config.get("cert", "True"))
        self.host = pan_config["panorama_host"]
        self.rc = RequestsCommon(opts, pan_config)
        self.query_parameters = {
                                    "key": self.__key,
                                    "location": location,
                                    "output-format": "json"
                                }
        if location in ["vsys", "panorama-pushed"]:
            self.query_parameters["vsys"] = self.__vsys

    def __build_url(self, resource_uri):
        "build url for api calls"
        return u"/".join([self.host, self.__url_path, resource_uri])

    def __get(self, resource_uri, parameters):
        """Generic GET"""
        response = self.rc.execute_call_v2("GET", self.__build_url(resource_uri), params=parameters, verify=self.verify)
        LOG.debug(f"Response: {response}")
        return response.json()

    def __post(self, resource_uri, params, payload):
        """Generic POST"""
        response = self.rc.execute_call_v2("POST", self.__build_url(resource_uri), params=params, json=loads(payload), verify=self.verify)
        LOG.debug(f"Status code: {response.status_code}, Response: {response.content}")
        return response.json()

    def __put(self, resource_uri, params, payload):
        """Generic PUT"""
        response = self.rc.execute_call_v2("PUT", self.__build_url(resource_uri), params=params, json=loads(payload), verify=self.verify)
        LOG.debug(f"Status code: {response.status_code}, Response: {response.content}")
        return response.json()

    def get_addresses(self):
        """Get list of addresses"""
        return self.__get("Objects/Addresses", self.query_parameters)

    def get_address_groups(self, name_param=None):
        """Get list of address groups"""
        params = self.query_parameters
        if name_param:
            params["name"] = name_param
        return self.__get("Objects/AddressGroups", params)

    def edit_address_groups(self, name_param, payload):
        """Edits an address group, adds/removes addresses"""
        params = self.query_parameters
        params["name"] = name_param
        return self.__put("Objects/AddressGroups", params, payload)

    def add_address(self, name_param, payload):
        """Creates a new address"""
        params = self.query_parameters
        params["name"] = name_param
        return self.__post("Objects/Addresses", params, payload)

    def get_users_in_a_group(self, xpath):
        """Gets list of users in a group, uses custom POST method due to this being a SOAP based call.
           Returns XML string
        """
        params = {
            "type": "config",
            "action": "get",
            "key": self.__key,
            "xpath": xpath
        }
        response = self.rc.execute_call_v2("POST", f"{self.host}/api/", params=params, verify=self.verify)
        response.raise_for_status()
        return response.text

    def edit_users_in_a_group(self, xpath, xml_object):
        """Edits list of users in a group, uses custom POST method due to this being a SOAP based call.
           Returns XML string
        """
        params = {
            "type": "config",
            "action": "edit",
            "key": self.__key,
            "xpath": xpath,
            "element": xml_object
        }
        response = self.rc.execute_call_v2("POST", f"{self.host}/api/?", params=params, verify=self.verify)
        response.raise_for_status()
        return response.text
