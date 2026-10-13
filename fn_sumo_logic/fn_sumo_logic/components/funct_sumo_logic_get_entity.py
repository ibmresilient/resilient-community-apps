# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.2.1096

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_sumo_logic.lib.app_common import (PACKAGE_NAME, AppCommon)

PACKAGE_NAME = "fn_sumo_logic"
FN_NAME = "sumo_logic_get_entity"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'sumo_logic_get_entity'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Query Sumo Logic to get information of entities.
        Inputs:
            -   fn_inputs.sumo_logic_entity_type
            -   fn_inputs.sumo_logic_entity_value
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["sumo_logic_entity_type", "sumo_logic_entity_value"], fn_inputs)

        app_common = AppCommon(PACKAGE_NAME, self.options)

        results, error_msg = app_common.get_entity(entity_type=fn_inputs.sumo_logic_entity_type,
                                                   entity_value=fn_inputs.sumo_logic_entity_value)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results, success=False if error_msg else True, reason=error_msg)
