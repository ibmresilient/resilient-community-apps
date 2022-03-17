# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""AppFunction implementation"""
import ntpath
from fn_reaqta.lib.app_common import AppCommon, PACKAGE_NAME, get_hive_options
from resilient_lib import write_file_attachment
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

FN_NAME = "reaqta_attach_file"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'reaqta_attach_file'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Attach the file associated with a running process
        Inputs:
            -   fn_inputs.reaqta_program_path
            -   fn_inputs.reaqta_hive
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        validate_fields([
            "reaqta_hive",
            "reaqta_endpoint_id",
            "reaqta_incident_id",
            "reaqta_program_path"
            ], fn_inputs)

        hive_settings = get_hive_options(fn_inputs.reaqta_hive, self.opts)
        if not hive_settings:
            results = None
            err_msg = "Hive section not found: {}".format(fn_inputs.reaqta_hive)
        else:
            app_common = AppCommon(self.rc, hive_settings)
            file_contents = app_common.get_program_file(fn_inputs.reaqta_endpoint_id,
                                                        fn_inputs.reaqta_program_path)

            if file_contents:
                # collect the file name
                file_name = ntpath.basename(fn_inputs.reaqta_program_path)
                results = write_file_attachment(self.rest_client(),
                                                file_name,
                                                file_contents,
                                                fn_inputs.reaqta_incident_id)
                err_msg = None  # write_file_attachment will raise an exception if an error occurs
            else:
                results = None
                err_msg = "Unable to get contents of file attachment from SOAR"

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results, success=True if not err_msg else False, reason=err_msg)

