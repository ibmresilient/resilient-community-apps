# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.1.0.695

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields
from fn_wiz.lib.app_common import (AppCommon, PACKAGE_NAME, MAX_VULN_RESULTS)
from json import loads, JSONDecodeError

FN_NAME = "wiz_pull_vulnerabilities"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'wiz_pull_vulnerabilities'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Query Wiz for vulnerability data
        Inputs:
            -   fn_inputs.wiz_project_ids
            -   fn_inputs.wiz_num_results
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Project ids come in as text field from SOAR, convert to list for query
        # These are optional, mainly used to in the OOTB Populate Case Playbook
        pids = getattr(fn_inputs, "wiz_project_ids", None)
        project_ids_list = []
        if pids:
            project_ids_list = pids.split(",")

        # If num_results was provided in input script for function, then use that; otherwise use default MAX_VULN_RESULTS
        num_results = getattr(fn_inputs, "wiz_num_results", MAX_VULN_RESULTS)

        app_common = AppCommon(self.rc, PACKAGE_NAME, self.options)

        custom_filter = getattr(fn_inputs, "wiz_query_filter", None)

        # If a custom filter is provided by the activation form inputs, load it into JSON
        if custom_filter:
            try:
                custom_filter = loads(custom_filter)
            except JSONDecodeError as err:
                raise IntegrationError(f"Provided `wiz_query_filter` is not formatted correctly. \
                                       Unable to make Wiz query. Please ensure input is JSON formatted: {err}.")
            if not isinstance(custom_filter, dict):
                raise IntegrationError(f"Provided `wiz_query_filter` is not formatted correctly. \
                                        Unable to make Wiz query. Please ensure input is JSON formatted, found input with type {type(custom_filter)}.")

            self.LOG.debug("Found `wiz_query_filter` to use for pulling Wiz vulnerabilities: %s", custom_filter)

        response = app_common.get_vulnerabilities(project_ids_list, custom_filter=custom_filter, num_results=num_results)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        results = { "response": response }

        yield FunctionResult(results)
