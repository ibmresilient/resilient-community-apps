# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields, clean_html
from fn_qradar_enhanced_data.util.qradar_constants import (GLOBAL_SETTINGS, PACKAGE_NAME)
from fn_qradar_enhanced_data.util.qradar_utils import AuthInfo
from fn_qradar_enhanced_data.util.function_utils import get_qradar_client, get_server_settings, get_sync_notes

FN_NAME = "qradar_create_note"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'qradar_create_note'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Create a note on the linked QRadar offense.
        Inputs:
            -   fn_inputs.qradar_label
            -   fn_inputs.qradar_offense_id
            -   fn_inputs.qradar_note
        """
        try:
            yield self.status_message(f"Starting App Function: '{FN_NAME}'")

            # Validate required parameters
            validate_fields(["qradar_offense_id", "qradar_note"], fn_inputs)

            # Log inputs
            self.LOG.info(str(fn_inputs))

            # Get configuration for QRadar server specified
            options = get_server_settings(self.opts, getattr(fn_inputs, "qradar_label", None))
            # Create connection to QRadar server
            get_qradar_client(self.opts, options)
            # Get authorization info for connected QRadar server
            auth_info = AuthInfo.get_authInfo()
            # API url
            api_url = auth_info.api_url
            # Set results to be None
            results = None

            # If the sync_notes setting in the app.config equals True
            if get_sync_notes(self.opts.get(GLOBAL_SETTINGS, {}), options):
                # Make POST call to the specified QRadar server to add a note to the specified QRadar offense
                results = auth_info.make_call("POST",
                    f"{api_url}siem/offenses/{fn_inputs.qradar_offense_id}/notes?note_text={clean_html(fn_inputs.qradar_note)}"
                ).json()

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

            yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
