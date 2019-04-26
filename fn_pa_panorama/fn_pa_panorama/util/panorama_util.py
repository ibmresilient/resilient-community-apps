# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2019. All Rights Reserved.

import logging
from resilient_lib.components.resilient_common import validate_fields, str_to_bool
from resilient_lib.components.requests_common import RequestsCommon


log = logging.getLogger(__name__)
URI_PATH = "restapi/9.0"


class PanoramaClient:
    """
    Object to handle the communication and authentication between the integration and Panorama
    """
    def __init__(self, opts):
        pan_config = opts.get("fn_pa_panorama")

        # validate config fields
        validate_fields(["panorama_host", "api_key", "location"], pan_config)

        self.__key = pan_config["api_key"]
        self.__location = pan_config["location"]
        self.__vsys = pan_config.get("vsys", None)
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

    def get(self, resource_uri):
        """Generic GET"""
        uri = u"{}/{}/{}".format(self.host, URI_PATH, resource_uri)
        response = self.rc.execute_call("GET", uri, payload=self.query_parameters, log=log, verify_flag=self.verify)
        log.debug("Response: {}".format(response))
        return response

    def get_address_groups(self):
        """Get list of address groups"""
        return self.get("Objects/AddressGroups")
