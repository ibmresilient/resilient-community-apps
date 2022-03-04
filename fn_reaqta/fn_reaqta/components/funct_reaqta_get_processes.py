# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""AppFunction implementation"""

from fn_reaqta.lib.app_common import AppCommon, PACKAGE_NAME
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

FN_NAME = "reaqta_get_processes"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'reaqta_get_processes'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get active processes from a given endpoint
        Inputs:
            -   fn_inputs.reaqta_endpoint_id
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        validate_fields(["reaqta_url",
                        "api_version",
                        "cafile",
                        "api_key",
                        "api_secret"],
                        self.app_configs)

        validate_fields(["reaqta_endpoint_id"], fn_inputs)

        # Example getting access to self.get_fn_msg()
        # fn_msg = self.get_fn_msg()
        # self.LOG.info("fn_msg: %s", fn_msg)

        app_common = AppCommon(self.rc, self.app_configs._asdict())
        results = app_common.get_processes(fn_inputs.reaqta_endpoint_id)

        # collect the filters, reaqta_has_incident and reaqta_suspended, and apply
        func_params = fn_inputs._asdict()
        has_incident = func_params.get('reaqta_has_incident')
        suspended = func_params.get('reaqta_suspended')

        for filter, field_name in [(has_incident, 'hasIncident'), (suspended, 'suspended')]:
            if filter is not None and isinstance(results, list):
                results = [proc for proc in results if proc.get(field_name) == filter]

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)
