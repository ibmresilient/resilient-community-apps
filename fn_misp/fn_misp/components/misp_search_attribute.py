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
FN_NAME = "misp_search_attribute"


class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function(s)"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(
            opts, PACKAGE_NAME, ["misp_key", "misp_url"])

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: Search to see if an attribute exists for a given artifact value"""
        # Get the function parameters:
        search_attribute = getattr(fn_inputs, "misp_attribute_value")  # text

        self.LOG.info("search_attribute: %s", search_attribute)

        yield self.status_message("Setting up connection to MISP")

        verify = str_to_bool(self.options.get("verify_cert", "false").lower())

        misp_client = misp_helper.get_misp_client(self.options.get(
            "misp_url"), self.options.get("misp_key"), verify, proxies=self.rc.get_proxies())

        yield self.status_message(f"Searching for attribute - {search_attribute}")

        results = []

        search_results = misp_helper.search_misp_attribute(
            misp_client, search_attribute)

        self.LOG.debug(search_results)

        if search_results.get('search_status'):
            results = search_results.get('search_results', [])

        yield self.status_message("Attribute search complete.")

        # Produce a FunctionResult with the results
        yield FunctionResult(results, success=search_results.get("search_status"))
