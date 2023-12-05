# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import sys
if sys.version_info.major < 3:
    from fn_misp.lib import misp_2_helper as misp_helper
else:
    from fn_misp.lib import misp_3_helper as misp_helper
from resilient_circuits import AppFunctionComponent, FunctionResult, app_function, FunctionError
from resilient_lib import IntegrationError, str_to_bool

PACKAGE_NAME = "fn_misp"
FN_NAME = "misp_create_tag"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function(s)"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Creates a Tag"""
        # Get the function parameters:
        misp_tag_type = self.get_select_param(getattr(fn_inputs, "misp_tag_type"))  # select, values: "Event", "Attribute"
        misp_tag_name = getattr(fn_inputs, "misp_tag_name")  # text
        misp_attribute_value = getattr(fn_inputs, "misp_attribute_value")  # text
        misp_event_id = getattr(fn_inputs, "misp_event_id")  # number

        # ensure misp_event_id is an integer so we can get an event by it's index
        if not isinstance(misp_event_id, int):
            raise IntegrationError(
                f"Unexpected input type for MISP Event ID. Expected and integer, received {type(misp_event_id)}")

        self.LOG.info("misp_tag_type: %s", misp_tag_type)
        self.LOG.info("misp_tag_name: %s", misp_tag_name)
        self.LOG.info("misp_attribute_value: %s", misp_attribute_value)
        self.LOG.info("misp_event_id: %s", misp_event_id)

        if sys.version_info.major < 3:
            raise FunctionError("Tagging is only supported when using Python 3")

        yield self.status_message("Setting up connection to MISP")

        verify = str_to_bool(self.options.get("verify_cert", "false").lower())

        misp_client = misp_helper.get_misp_client(self.options.get("misp_url"), self.options.get("misp_key"), verify, proxies=self.rc.get_proxies())

        yield self.status_message(f"Tagging {misp_tag_type} with {misp_tag_name}")

        tag_result = misp_helper.create_tag(misp_client, misp_attribute_value, misp_tag_type, misp_tag_name, misp_event_id)
        if 'errors' in tag_result:
            raise IntegrationError(f"Unable to save the tag. {tag_result['errors'][1]['errors']}")

        self.LOG.debug(tag_result)

        yield self.status_message("Tag has been created")

        response_results = {"success": True}

        # Produce a FunctionResult with the results
        yield FunctionResult(response_results)
