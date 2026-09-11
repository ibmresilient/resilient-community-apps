# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.5.0.1475
# pragma pylint: disable=unused-argument, line-too-long, wrong-import-order

"""AppFunction implementation"""

from fn_search_for_py2.lib.soar_helper import SOARHelper
from fn_search_for_py2.lib.common import FindPY2_SOAR
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

PACKAGE_NAME = "fn_search_for_py2"
FN_NAME = "convert_to_python_3"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'convert_to_python_3'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Convert a script, playbook or playbook to use Python 3 scripting engine.
        Inputs:
            -   fn_inputs.py2_item_type
            -   fn_inputs.py2_item_id
        """

        validate_fields(["py2_item_type", "py2_item_id"], fn_inputs)

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        soar_helper = SOARHelper(self.rest_client())

        reason = None
        success = True
        if fn_inputs.py2_item_type == "script":
            results = self.fix_script(fn_inputs, soar_helper)
            if not results.get("script"):
                reason = f"Script: {fn_inputs.py2_item_id} already set to Python 3"
        elif fn_inputs.py2_item_type in ["workflow", "playbook"]:
            results = self.fix_bpmn(fn_inputs, soar_helper)
            if not results.get(fn_inputs.py2_item_type):
                reason = f"{fn_inputs.py2_item_type}: {fn_inputs.py2_item_id} already set to Python 3"
        else:
            reason = f"'{fn_inputs.py2_item_type}' not 'script', 'workflow' or 'playbook'."
            success = False

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results,
                             success=success,
                             reason=reason)

    def fix_script(self, fn_inputs, soar_helper: SOARHelper) -> dict:
        find_py2 = FindPY2_SOAR(soar_helper)
        script = soar_helper.get_script(fn_inputs.py2_item_id)

        changed, script = find_py2.fix_py2_script(script)

        if not changed:
            results = {"script": None}
        else:
            soar_helper.put_script(fn_inputs.py2_item_id, script)
            results = {"script": script}

        return results

    def fix_bpmn(self, fn_inputs, soar_helper: SOARHelper) -> dict:
        find_py2 = FindPY2_SOAR(soar_helper)
        if fn_inputs.py2_item_type == "workflow":
            bpmn_item = soar_helper.get_workflow(fn_inputs.py2_item_id)
        else:
            bpmn_item = soar_helper.get_playbook(fn_inputs.py2_item_id, add_headers=False)

        found_py2_components, bpmn_changed = find_py2.fix_py2_bpmn(bpmn_item)

        if not found_py2_components:
            results = {fn_inputs.py2_item_type: None}
        else:
            if fn_inputs.py2_item_type == "workflow":
                soar_helper.put_workflow(fn_inputs.py2_item_id, bpmn_changed)
            else:
                soar_helper.put_playbook(fn_inputs.py2_item_id, bpmn_changed)
            results = {fn_inputs.py2_item_type: bpmn_changed}

        return results
