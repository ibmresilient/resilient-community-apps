# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.2.1096
# pragma pylint: disable=unused-argument, line-too-long, wrong-import-order

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError
from fn_search_for_py2.lib.common import FindPY2_SOAR
from fn_search_for_py2.lib.soar_helper import SOARHelper

PACKAGE_NAME = "fn_search_for_py2"
FN_NAME = "fn_search_for_py2"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'fn_search_for_py2'
    """

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Search for scripts, workflows and playbooks which are set to using Python 2. Python 2 will be removed from SOAR in an upcoming release.
                - fn_inputs.py2_inc_id
                - fn_inputs.py2_search_tags
                - fn_inputs.py2_item_id
                - fn_inputs.py2_item_name
                - fn_inputs.py2_item_type
                - fn_inputs.py2_clear_datatable
        """

        inputs = fn_inputs._asdict()
        # convert the item type as it may be a select object
        inputs["py2_item_type"] = self.get_select_param(inputs.get("py2_item_type"))

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        soar_helper = SOARHelper(self.rest_client())

        results = reason = None
        try:
            find_py2 = FindPY2_SOAR(soar_helper)
            results = find_py2.start(inputs)

            if inputs.get("py2_clear_datatable"):
                soar_helper.delete_datatable_rows(inputs["py2_inc_id"])
        except IntegrationError as e:
            reason = str(e)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results, success=bool(results), reason=reason)
