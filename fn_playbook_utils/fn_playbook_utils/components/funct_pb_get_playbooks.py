# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields
from fn_playbook_utils.lib.common import get_playbooks

PACKAGE_NAME = "fn_playbook_utils"
FN_NAME = "pb_get_playbooks"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'pb_get_playbooks'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get playbooks which match the type and optionally name criteria
        Inputs:
            -   fn_inputs.pbm_name_contains
            -   fn_inputs.pbm_type
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        validate_fields(["pbm_type"], fn_inputs)

        results = get_playbooks(self.rest_client(),
                                getattr(fn_inputs, 'pbm_type', {}),
                                getattr(fn_inputs, 'pbm_name_contains'))

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results, success=bool(results))
