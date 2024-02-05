# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""Function implementation"""

from resilient_circuits import AppFunctionComponent, FunctionResult, app_function
from resilient_lib import IntegrationError, str_to_bool
from sys import version_info
if version_info.major < 3:
    from fn_misp.lib import misp_2_helper as misp_helper
else:
    from fn_misp.lib import misp_3_helper as misp_helper

PACKAGE_NAME = "fn_misp"
FN_NAME = "misp_create_attribute"


class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function(s)"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(
            opts, PACKAGE_NAME, ["misp_key", "misp_url"])

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Create attribute in MISP"""
        # Get the function parameters:
        misp_event_id = getattr(fn_inputs, "misp_event_id")  # number
        misp_attribute_value = getattr(
            fn_inputs, "misp_attribute_value")  # text
        misp_attribute_type = getattr(fn_inputs, "misp_attribute_type")  # text

        # ensure misp_event_id is an integer so we can get an event by it's index
        if not isinstance(misp_event_id, int):
            raise IntegrationError(f"Unexpected input type for MISP Event ID. \
                                   Expected and integer, received {type(misp_event_id)}")

        self.LOG.info("misp_event_id: %s", misp_event_id)
        self.LOG.info("misp_attribute_value: %s", misp_attribute_value)
        self.LOG.info("misp_attribute_type: %s", misp_attribute_type)

        yield self.status_message("Setting up connection to MISP")

        verify = str_to_bool(self.options.get("verify_cert", "false").lower())

        misp_client = misp_helper.get_misp_client(
            self.options.get("misp_url"),
            self.options.get("misp_key"),
            verify,
            proxies=self.rc.get_proxies()
        )

        yield self.status_message(
            f"Creating new misp attribute {misp_attribute_type} {misp_attribute_value}")

        attribute = misp_helper.create_misp_attribute(
            misp_client,
            misp_event_id,
            misp_attribute_type,
            misp_attribute_value
        )

        self.LOG.debug(attribute)

        yield self.status_message("Attribute has been created")

        # Produce a FunctionResult with the results
        yield FunctionResult(attribute)
