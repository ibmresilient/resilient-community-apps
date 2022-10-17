# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_qradar_enhanced_data.util.qradar_constants import GLOBAL_SETTINGS, PACKAGE_NAME
from fn_qradar_enhanced_data.util.function_utils import clear_table, get_qradar_client, get_server_settings

FN_NAME = "qradar_get_offense_mitre_reference"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'qradar_get_offense_mitre_reference'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get the MITRE Tactics and Techniques in relation to the rules that were fired to cause the offense in QRadar.
        Inputs:
            -   fn_inputs.qradar_label
            -   fn_inputs.qradar_offense_id
            -   fn_inputs.soar_table_name
            -   fn_inputs.soar_incident_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate required parameters
        validate_fields(["qradar_offense_id"], fn_inputs)

        # Log inputs
        self.LOG.info(str(fn_inputs))

        # Get global settings from the app.config
        global_settings = self.opts.get(GLOBAL_SETTINGS, {})
        # Get configuration for QRadar server specified
        options = get_server_settings(self.opts, getattr(fn_inputs, "qradar_label", None))
        # Create connection to QRadar server
        qradar_client = get_qradar_client(self.opts, options)

        

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Clear specified data table in SOAR based on app.config settings
        clear_table(self.rest_client(), getattr(fn_inputs, "soar_table_name", None), getattr(fn_inputs, "soar_incident_id", None), global_settings)

        yield FunctionResult(results)
