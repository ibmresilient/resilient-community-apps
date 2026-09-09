# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.2.1096

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_algosec.util.helper import PACKAGE_NAME, algosec_client, firewall_analyzer

FN_NAME = "algosec_traffic_simulation_query"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'algosec_traffic_simulation_query'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Performs a batch Traffic Simulation Query on a single device or group of devices.
        Inputs:
            -   fn_inputs.algosec_includeruleszones
            -   fn_inputs.algosec_service
            -   fn_inputs.algosec_includedevicespaths
            -   fn_inputs.algosec_query_target
            -   fn_inputs.algosec_destination
            -   fn_inputs.algosec_source
            -   fn_inputs.algosec_application
            -   fn_inputs.algosec_user
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")
        # Validate required fields
        validate_fields(["algosec_source", "algosec_service", "algosec_destination"], fn_inputs)

        # Create connection to AlgoSec server and get a SessionID
        sessionID = algosec_client(self.options, self.rc).firewall_analyzer_auth()
        # Create a traffic simulation query request
        results = firewall_analyzer(self.rc, sessionID).traffic_simulation_query(fn_inputs.algosec_source,
                                                                  fn_inputs.algosec_destination,
                                                                  fn_inputs.algosec_service,
                                                                  getattr(fn_inputs, "algosec_query_target", "ALL_FIREWALLS"),
                                                                  getattr(fn_inputs, "algosec_application", "any"),
                                                                  getattr(fn_inputs, "algosec_user", "any"),
                                                                  getattr(fn_inputs, "algosec_includeruleszones", False),
                                                                  getattr(fn_inputs, "algosec_includedevicespaths", False))

        # Edit the queryHTMLPath to use the correct AlgoSec host address
        if results.get("queryResult", []) and "https://aglosec/" in results.get("queryResult", [])[0].get("queryHTMLPath", ""):
            queryPath = results.get("queryResult", [])[0].get("queryHTMLPath", "")
            results["queryResult"][0]["queryHTMLPath"] = queryPath.replace("aglosec", self.options.get("server_ip", ""))

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)
