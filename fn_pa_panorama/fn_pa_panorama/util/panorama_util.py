# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.

from logging import getLogger
from json import loads
from resilient_lib.components.resilient_common import validate_fields, str_to_bool
from resilient_lib.components.requests_common import RequestsCommon, IntegrationError

LOG = getLogger(__name__)
DEFAULT_API_VERSION = "v9.1"
URI_PATH = "restapi"
PACKAGE_NAME = "fn_pa_panorama"


class PanoramaClient:
    """Object to handle the communication and authentication between the integration and Panorama"""

    def __init__(self, opts, pan_config, location, vsys=None, device_group=None):
        pan_config["location"] = location

        # validate config fields
        validate_fields(["panorama_host", "api_key", "location"], pan_config)

        api_version = pan_config.get("api_version", DEFAULT_API_VERSION)
        self.__key = pan_config["api_key"]
        self.__url_path = "/".join([URI_PATH, api_version])
        self.__vsys = vsys

        self.verify = str_to_bool(pan_config.get("cert", "True"))
        self.host = pan_config["panorama_host"]
        self.rc = RequestsCommon(opts, pan_config)
        self.proxies = self.rc.get_proxies()
        self.query_parameters = {"location": location,
                                 "output-format": "json"}
        if api_version == "9.0":
            self.query_parameters["key"] = self.__key
        else:
            self.header = {"X-PAN-KEY": self.__key}

        # If location equals vsys or panorama-pushed then vsys is required.
        if location in ["vsys", "panorama-pushed"]:
            self.query_parameters["vsys"] = self.__vsys

        # If location equals device-group then device-group is required.
        if location == "device-group":
            self.query_parameters["device-group"] = device_group

    def __build_url(self, resource_uri):
        """build url for api calls"""
        return "/".join([self.host, self.__url_path, resource_uri])

    def __get(self, resource_uri, parameters):
        """Generic GET"""
        response = self.rc.execute("GET",
                                   self.__build_url(resource_uri),
                                   params=parameters,
                                   verify=self.verify,
                                   headers=self.header,
                                   proxies=self.proxies
                                )
        LOG.debug(f"Response: {response}")
        return response.json()

    def __post(self, resource_uri, params, payload):
        """Generic POST"""
        response = self.rc.execute("POST",
                                   self.__build_url(resource_uri),
                                   params=params,
                                   json=loads(payload),
                                   verify=self.verify,
                                   headers=self.header,
                                   proxies=self.proxies
                                )
        LOG.debug(
            f"Status code: {response.status_code}, Response: {response.content}")
        return response.json()

    def __put(self, resource_uri, params, payload):
        """Generic PUT"""
        response = self.rc.execute("PUT",
                                   self.__build_url(resource_uri),
                                   params=params,
                                   json=loads(payload),
                                   verify=self.verify,
                                   headers=self.header,
                                   proxies=self.proxies
                                )
        LOG.debug(
            f"Status code: {response.status_code}, Response: {response.content}")
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
           Returns XML string"""
        params = {"type": "config",
                  "action": "get",
                  "key": self.__key,
                  "xpath": xpath}
        response = self.rc.execute(
            "POST",
            f"{self.host}/api/",
            params=params,
            verify=self.verify,
            headers=self.header
        )
        response.raise_for_status()
        return response.text

    def edit_users_in_a_group(self, xpath, xml_object):
        """Edits list of users in a group, uses custom POST method due to this being a SOAP based call.
           Returns XML string"""
        params = {"type": "config",
                  "action": "edit",
                  "key": self.__key,
                  "xpath": xpath,
                  "element": xml_object}
        response = self.rc.execute(
            "POST",
            f"{self.host}/api/?",
            params=params,
            verify=self.verify,
            headers=self.header
        )
        response.raise_for_status()
        return response.text

    def commit_changes(self):
        """Commit changes made to the Panorama server

        Returns:
            _type_: _description_
        """
        response = self.rc.execute(
            "POST",
            f"{self.host}/api?type=commit&cmd=<commit></commit>",
            verify=self.verify,
            headers=self.header,
            proxies=self.proxies
        )
        response.raise_for_status()
        return response.text

class PanoramaServers():
    """ Get multiple servers from the app.config """

    def __init__(self, opts):
        """
        Initialize the PanoramaServers class
        :param opts: Dictionary of options
        """
        self.servers, self.server_name_list = self._load_servers(opts)

    def _load_servers(self, opts):
        """
        Create list of label names and a dictionary of the servers and their configs
        :param opts: Dict of options
        :return servers: Dictionary of all the Panorama servers from the app.config that contains each servers configurations
        :return server_name_list: List filled with all of the labels for the servers from the app.config
        """
        servers = {}
        server_name_list = self._get_server_name_list(opts)
        for server in server_name_list:
            server_data = opts.get(server)
            if not server_data:
                raise KeyError(f"Unable to find Panorama server: {server}")

            servers[server] = server_data

        return servers, server_name_list

    def panorama_label_test(self, panorama_label, servers_list):
        """
        Check if the given panorama_label is in the app.config
        :param panorama_label: User selected server
        :param servers_list: List of Panorama servers
        :return: Dictionary of options for chosen server
        """
        # If label not given and using previous versions app.config [fn_pa_panorama]
        if not panorama_label and servers_list.get(PACKAGE_NAME):
            return servers_list.get(PACKAGE_NAME)
        if not panorama_label:
            raise IntegrationError(
                "No label was given and is required if servers are labeled in the app.config")

        label = f"{PACKAGE_NAME}:{panorama_label}"
        if panorama_label and label in servers_list:
            options = servers_list.get(label)
        elif len(servers_list) == 1:
            options = servers_list[list(servers_list.keys())[0]]
        else:
            raise IntegrationError(
                f"{panorama_label} did not match labels given in the app.config")

        return options

    def _get_server_name_list(self, opts):
        """
        Return the list of Panorama server names defined in the app.config in fn_pa_panorama.
        :param opts: List of options
        :return: List of servers
        """
        return [key for key in opts.keys() if key.startswith(f"{PACKAGE_NAME}:")]

    def get_server_name_list(self):
        """
        Return list of all server names
        """
        return self.server_name_list


def get_server_settings(opts, panorama_label):
    """
    Used for initializing or reloading the options variable
    :param opts: List of options
    :return: panorama server settings for specified server
    """
    server_list = {PACKAGE_NAME} if opts.get(
        PACKAGE_NAME, {}) else PanoramaServers(opts).get_server_name_list()

    # Creates a dictionary that is filled with the panorama servers
    # and there configurations
    servers_list = {server_name: opts.get(
        server_name, {}) for server_name in server_list}

    # Get configuration for panorama server specified
    return PanoramaServers(opts).panorama_label_test(panorama_label, servers_list)
