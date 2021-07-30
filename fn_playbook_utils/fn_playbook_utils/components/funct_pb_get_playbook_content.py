# -*- coding: utf-8 -*-
#(c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
#pragma pylint: disable=unused-argument, no-self-use, line-too-long

"""AppFunction implementation"""
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_playbook_utils.lib.common import get_playbook, get_process_elements

PACKAGE_NAME = "fn_playbook_utils"
FN_NAME = "pb_get_playbook_content"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'pb_get_playbook_content'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get the content of functions, scripts, tasks and sub-workflows used within a workflow
        Inputs:
            -   fn_inputs.pb_id
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        playbook_xml = get_playbook(self.rest_client(), fn_inputs.pb_id)
        if not playbook_xml:
            msg = "playbook_id not found: {}".format(fn_inputs.pb_id)
            yield self.status_message(msg)
            yield FunctionResult({}, success=False, reason=msg)
        else:
            results = get_process_elements(playbook_xml)
            yield FunctionResult(results)
