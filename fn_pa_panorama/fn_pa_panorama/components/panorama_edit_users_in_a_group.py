# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""Function implementation"""

from xmltodict import parse
from fn_pa_panorama.util.panorama_util import PanoramaClient, PACKAGE_NAME, get_server_settings
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

FN_NAME = "panorama_edit_users_in_a_group"

class FunctionComponent(AppFunctionComponent):
    """Component that implements Resilient function 'panorama_edit_users_in_a_group"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Edits users in a group in Panorama.
        Inputs:
            -   fn_inputs.panorama_user_group_xpath
            -   fn_inputs.panorama_user_group_xml
            -   fn_inputs.panorama_label
            -   fn_inputs.panorama_location
        """
        # Response code should equal 20 indicating the call went through successfully
        PASS_CONSTANT = "20"

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate required parameters
        validate_fields(["panorama_user_group_xpath", "panorama_user_group_xml"], fn_inputs)

        # Log inputs
        self.LOG.info(fn_inputs)

        # Create connection to the user specific Panorama Server
        panorama_util = PanoramaClient(self.opts,
                                       get_server_settings(self.opts, getattr(fn_inputs, "panorama_label", None)),
                                       self.get_select_param(getattr(fn_inputs, "panorama_location", None)),
                                       None)
        # Initialize variables
        results = {}
        success = True
        reason = ""

        try:
            xml_response = panorama_util.edit_users_in_a_group(fn_inputs.panorama_user_group_xpath,
                           self.get_textarea_param(fn_inputs.panorama_user_group_xml))
            results = parse(xml_response)
        except KeyError as e:
            yield self.status_message("Editing the user group was unsuccessful.")
            success = False
            reason = e

        if success and results["response"].get("@code") == PASS_CONSTANT:
            yield self.status_message("User group was successfully edited.")
            if xml_response:
                # Add to dict_response to allow for more options in SOAR scripting and make some actions easier
                results["xml_response"] = xml_response
        else:
            success = False
            reason = f"Editing the user group was unsuccessful with code {results['response'].get('@code')}, raising FunctionError."

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(results, success=success, reason=reason)
