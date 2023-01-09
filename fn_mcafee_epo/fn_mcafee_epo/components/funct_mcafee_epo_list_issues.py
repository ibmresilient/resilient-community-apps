# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_mcafee_epo.lib.epo_helper import init_client, PACKAGE_NAME, clear
from datetime import datetime

FN_NAME = "mcafee_epo_list_issues"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'mcafee_epo_list_issues'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: List the issues on the ePO server
        Inputs:
            -   fn_inputs.mcafee_epo_issue_id
            -   fn_inputs.mcafee_epo_search_text
            -   fn_inputs.datatable_name
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Log parameters
        self.LOG.info(str(fn_inputs))

        # Connect to ePO server
        client = init_client(self.opts, self.options)

        response = client.request(
            "issue.listIssues",
            {"id": getattr(fn_inputs, "mcafee_epo_issue_id", None)}
        )

        for x in response:
            # Convert str time to unix timestamp
            if x.get("dueDate"):
                dat = x.get("dueDate")
                x["dueDate"] = int(datetime.timestamp((datetime.strptime(dat[:len(dat)-6], '%Y-%m-%dT%H:%M:%S')))*1000)
            # Convert untyped to BASIC. The only type is BASIC, so all issues are type BASIC
            if x.get('type') == 'issue.type.untyped':
                x['type'] = 'BASIC'

         # Clear datatable if required params are given
        if hasattr(fn_inputs, "datatable_name") and hasattr(fn_inputs, "incident_id"):
            clear(self.rest_client(), fn_inputs.datatable_name, fn_inputs.incident_id)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(response)
