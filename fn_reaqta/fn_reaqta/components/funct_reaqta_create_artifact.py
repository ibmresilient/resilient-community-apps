# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""AppFunction implementation"""
import ntpath
from fn_reaqta.lib.app_common import AppCommon, PACKAGE_NAME, get_hive_options
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from resilient.co3 import SimpleHTTPException
from retry import retry

FN_NAME = "reaqta_create_artifact"

ARTIFACT_TYPE_LOOKUP = {
    "Malware Sample": 12,
    "Other File": 16
}

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
            -   fn_inputs.reaqta_hive
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        validate_fields(["reaqta_hive", "reaqta_endpoint_id", "reaqta_incident_id",
                        "reaqta_program_path", "reaqta_artifact_type"], fn_inputs)

        hive_settings = get_hive_options(fn_inputs.reaqta_hive, self.opts)
        if not hive_settings:
            results = {}
            err_msg = "Hive section not found: {}".format(fn_inputs.reaqta_hive)
        else:
            app_common = AppCommon(self.rc, hive_settings)
            file_contents, err_msg = app_common.get_program_file(fn_inputs.reaqta_endpoint_id,
                                                            fn_inputs.reaqta_program_path)

            results = {}
            if not err_msg:
                # collect the file name
                file_name = ntpath.basename(fn_inputs.reaqta_program_path)

                artifact_uri = "/incidents/{0}/artifacts/files".format(fn_inputs.reaqta_incident_id)

                artifact_type = ARTIFACT_TYPE_LOOKUP.get(fn_inputs.reaqta_artifact_type, 12)

                results = self.create_artifact(artifact_uri,
                                               artifact_type,
                                               file_contents,
                                               file_name)

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results,
                             success=True if results else False,
                             reason=err_msg)

    @retry(SimpleHTTPException, tries=3, delay=2, backoff=20)
    def create_artifact(self, artifact_uri, artifact_type, file_contents, file_name):
        return self.rest_client().post_artifact_file(artifact_uri,
                                                     artifact_type,
                                                     None,
                                                     bytes_handle=file_contents,
                                                     description="Extracted from ReaQta",
                                                     value=file_name)
