# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""Function implementation"""

from resilient_circuits import AppFunctionComponent, FunctionResult, app_function
from resilient_lib import str_to_bool
from sys import version_info
if version_info.major < 3:
    from fn_misp.lib import misp_2_helper as misp_helper
else:
    from fn_misp.lib import misp_3_helper as misp_helper

PACKAGE_NAME = "fn_misp"
FN_NAME = "misp_create_sighting"


class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function(s)"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(
            opts, PACKAGE_NAME, ["misp_key", "misp_url"])

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Create MISP sighting"""
        # Get the function parameters:
        misp_sighting = getattr(fn_inputs, "misp_sighting")  # text

        self.LOG.info("misp_sighting: %s", misp_sighting)

        yield self.status_message("Setting up connection to MISP")

        verify = str_to_bool(self.options.get("verify_cert", "false").lower())

        # Create connection to MISP server
        misp_client = misp_helper.get_misp_client(self.options.get(
            "misp_url"), self.options.get("misp_key"), verify, proxies=self.rc.get_proxies())

        yield self.status_message(f"Marking {misp_sighting} as sighted")

        sighting = misp_helper.create_misp_sighting(misp_client, misp_sighting)

        self.LOG.debug(sighting)

        yield self.status_message("Sighting has been created")

        # Produce a FunctionResult with the results
        yield FunctionResult(sighting)
