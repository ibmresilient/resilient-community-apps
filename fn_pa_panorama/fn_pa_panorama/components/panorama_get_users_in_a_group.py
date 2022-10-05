# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""Function implementation"""

from xmltodict import parse
from fn_pa_panorama.util.panorama_util import PanoramaClient, PACKAGE_NAME, get_server_settings
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

FN_NAME = "panorama_get_users_in_a_group"

class FunctionComponent(AppFunctionComponent):
    """Component that implements Resilient function 'panorama_get_users_in_a_group"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Lists users part of a group in Panorama."""
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate required parameters
        validate_fields(["panorama_user_group_xpath"], fn_inputs)

        # Log inputs
        self.LOG.info(fn_inputs)

        # Get configuration for Panorama server specified
        options = get_server_settings(self.opts, getattr(fn_inputs, "panorama_label", None))

        panorama_util = PanoramaClient(self.opts,
                                       options,
                                       self.get_select_param(getattr(fn_inputs, "panorama_location", None)),
                                       None)
        xml_response = panorama_util.get_users_in_a_group(fn_inputs.panorama_user_group_xpath)
        dict_response = parse(xml_response)

        user_list = []
        try:
            members = dict_response["response"]["result"]["entry"]["user"]["member"]
            if isinstance(members, list):
                # Multiple existing users
                user_list = [m for m in members]
            else:
                # Single user in group
                user_list = [members.get("#text")]
        except KeyError:
            # No users returned
            yield self.status_message("No users returned.")

        yield self.status_message(f"{len(user_list)} users returned.")

        # add to dict_response to allow for more options in Resilient scripting and make some actions easier
        dict_response["user_list"] = user_list
        dict_response["xml_response"] = xml_response

        # Produce a FunctionResult with the results
        yield FunctionResult(dict_response)
