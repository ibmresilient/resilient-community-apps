# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""Function implementation"""

import sys
if sys.version_info.major < 3:
    from fn_misp.lib import misp_2_helper as misp_helper
else:
    from fn_misp.lib import misp_3_helper as misp_helper
from resilient_circuits import AppFunctionComponent, FunctionResult, app_function
from resilient_lib import validate_fields, str_to_bool

PACKAGE_NAME = "fn_misp"
FN_NAME = "misp_create_event"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function(s)"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        validate_fields([
            {"name": "misp_key", "placeholder": "http://localhost"},
            {"name": "misp_url", "placeholder": "<your key>"},
            {"name": "verify_cert"}
        ], self.options)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: create a MISP event from an incident """
        # Get the function parameters:
        misp_event_name = getattr(fn_inputs, "misp_event_name")  # text
        misp_distribution = getattr(fn_inputs, "misp_distribution")  # number
        misp_analysis_level = getattr(fn_inputs, "misp_analysis_level")  # number
        misp_threat_level = getattr(fn_inputs, "misp_threat_level")  # number

        self.LOG.info("misp_event_name: %s", misp_event_name)
        self.LOG.info("misp_distribution: %s", misp_distribution)
        self.LOG.info("misp_analysis_level: %s", misp_analysis_level)
        self.LOG.info("misp_threat_level: %s", misp_threat_level)

        yield self.status_message("Setting up connection to MISP")

        verify = str_to_bool(self.options.get("verify_cert", "false").lower())

        misp_client = misp_helper.get_misp_client(self.options.get("misp_url"), self.options.get("misp_key"), verify, proxies=self.rc.get_proxies())

        yield self.status_message(f"Creating event {misp_event_name}")

        events = misp_helper.create_misp_event(misp_client, misp_distribution, misp_threat_level, misp_analysis_level, misp_event_name)

        self.LOG.debug(events)

        yield self.status_message("Event has been created")

        # Produce a FunctionResult with the results
        yield FunctionResult(events)
