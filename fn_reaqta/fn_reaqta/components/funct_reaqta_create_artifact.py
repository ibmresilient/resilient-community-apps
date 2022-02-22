# -*- coding: utf-8 -*-

"""AppFunction implementation"""
from fn_reaqta.lib.app_common import AppCommon
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields

PACKAGE_NAME = "fn_reaqta"
FN_NAME = "reaqta_create_artifact"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'reaqta_create_artifact'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Create an artifact from the a process file
        Inputs:
            -   fn_inputs.reaqta_endpoint_id
            -   fn_inputs.reaqta_artifact_type
            -   fn_inputs.reaqta_program_path
            -   fn_inputs.reaqta_incident_id
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        validate_fields(["reaqta_url",
                        "api_version",
                        "cafile",
                        "api_key",
                        "api_secret"],
                        self.app_configs)

        validate_fields(["reaqta_endpoint_id", "reaqta_incident_id", "reaqta_program_path", "reaqta_artifact_types"], fn_inputs)

        # Example getting access to self.get_fn_msg()
        # fn_msg = self.get_fn_msg()
        # self.LOG.info("fn_msg: %s", fn_msg)

        app_common = AppCommon(self.rc, self.app_configs._asdict())
        file_contents = app_common.get_program_file(fn_inputs.reaqta_endpoint_id,
                                                  fn_inputs.reaqta_program_path)

        # TODO - create artifact poller_common?
        results = None
        if file_contents:
            results = xxx(self.rest_client(), file_contents,
                          fn_inputs.reaqta_artifact_types, fn_inputs.reaqta_incident_id)

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)