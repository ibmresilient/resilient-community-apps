# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
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
        """
        Function: Lists users part of a group in Panorama.
        Inputs:
            -   fn_inputs.panorama_user_group_xpath
            -   fn_inputs.panorama_label
            -   fn_inputs.panorama_location
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate required parameters
        validate_fields(["panorama_user_group_xpath"], fn_inputs)

        # Log inputs
        self.LOG.info(fn_inputs)

        # Create connection to the user specifiec Panorama Server
        panorama_util = PanoramaClient(self.opts,
                                       get_server_settings(self.opts, getattr(fn_inputs, "panorama_label", None)),
                                       self.get_select_param(getattr(fn_inputs, "panorama_location", None)),
                                       None)

        try:
            # Get the users in a group in xml format
            xml_response = panorama_util.get_users_in_a_group(fn_inputs.panorama_user_group_xpath)
        except KeyError:
            yield self.status_message("No users returned.") # No users returned

        # Create results dictionary from the above results
        results = parse(xml_response)

        members = results.get("response", {}).get("result", {}).get("entry", {}).get("user", {}).get("member")
        # Create a list of the returned users
        user_list = [m for m in members] if isinstance(members, list) else [members.get("#text")]

        yield self.status_message(f"{len(user_list)} users returned.")

        # Add list of users recieved from the get_users_in_a_group call to the results dict
        results["user_list"] = user_list
        # Add get_users_in_a_group response to the results dict in xml format
        results["xml_response"] = xml_response

        # Produce a FunctionResult with the results
        yield FunctionResult(results)
