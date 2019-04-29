# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2019. All Rights Reserved.

import logging
import requests
from resilient_lib.components.resilient_common import validate_fields, str_to_bool
from resilient_lib.components.requests_common import RequestsCommon


log = logging.getLogger(__name__)
URI_PATH = "restapi/9.0"


class PanoramaClient:
    """
    Object to handle the communication and authentication between the integration and Panorama
    """
    def __init__(self, opts, location, vsys=None):
        pan_config = opts.get("fn_pa_panorama")
        pan_config["location"] = location

        # validate config fields
        validate_fields(["panorama_host", "api_key", "location"], pan_config)

        self.__key = pan_config["api_key"]
        self.__location = pan_config["location"]
        self.__vsys = vsys
        self.__output_format = "json"

        self.verify = str_to_bool(pan_config.get("verify_cert"))
        self.host = pan_config["panorama_host"]
        self.rc = RequestsCommon(opts, pan_config)
        self.query_parameters = self.__build_query_parameters()

    def __build_query_parameters(self):
        query_params = dict()
        query_params["key"] = self.__key
        query_params["location"] = self.__location
        query_params["output-format"] = self.__output_format
        if self.__location == "vsys" or self.__location == "panorama-pushed":
            query_params["vsys"] = self.__vsys

        return query_params

    def __get(self, resource_uri, parameters):
        """Generic GET"""
        uri = u"{}/{}/{}".format(self.host, URI_PATH, resource_uri)
        response = self.rc.execute_call("GET", uri, payload=parameters, log=log, verify_flag=self.verify)
        log.debug("Response: {}".format(response))
        return response

    def __post(self, resource_uri, payload):
        """Generic POST"""
        uri = u"{}/{}/{}".format(self.host, URI_PATH, resource_uri)
        response = self.rc.execute_call("POST", uri, payload=payload, log=log, verify_flag=self.verify)
        log.debug("Response: {}".format(response))
        return response

    def __put(self, resource_uri, payload):
        """Generic PUT"""
        uri = u"{}/{}/{}".format(self.host, URI_PATH, resource_uri)
        response = requests.put(uri, uri, params=self.query_parameters, json=payload, verify=self.verify)
        log.debug("Status code: {}, Response: {}".format(response.status_code, response.content))
        response.raise_for_status()
        return response.json()

    def get_addresses(self):
        """Get list of addresses"""
        return self.__get("Object/Addresses", self.query_parameters)

    def get_address_groups(self, name_param=None):
        """Get list of address groups"""
        params = self.query_parameters
        if name_param:
            params["name"] = name_param
        return self.__get("Objects/AddressGroups", params)

    def edit_address_groups(self, payload):
        """Edits an address group, adds/removes addresses"""
        return self.__get("Object/AddressGroups", payload)

    def add_address(self, payload):
        """Creates a new address"""
        return self.__post("Objects/Addresses", payload)
