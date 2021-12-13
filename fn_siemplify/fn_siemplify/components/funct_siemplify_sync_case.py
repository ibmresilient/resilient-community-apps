# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields
from fn_siemplify.lib.resilient_common import ResilientCommon
from fn_siemplify.lib.siemplify_common import SiemplifyCommon

PACKAGE_NAME = "fn_siemplify"
FN_NAME = "siemplify_sync_case"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'siemplify_sync_case'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Sync a SOAR Case to Siemplify
        Inputs:
            -   fn_inputs.siemplify_incident_id
            -   fn_inputs.siemplify_sync_attachments
            -   fn_inputs.siemplify_sync_comments
            -   fn_inputs.siemplify_sync_artifacts
            -   fn_inputs.siemplify_environment
            -   fn_inputs.siemplify_assigned_user
            -   fn_inputs.siemplify_case_id
            -   fn_inputs.siemplify_alert_id
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        # validate app.config settings
        validate_fields([
                {"name": "api_key"},
                {"name": "base_url"},
                {"name": "default_environment"}
            ],
            self.app_configs._asdict())

        resilient_env = ResilientCommon(self.rest_client())

        # collect the incident information
        incident_info = resilient_env.get_incident(fn_inputs.siemplify_incident_id)
        # add placeholders
        incident_info["comments"] = []
        incident_info["artifacts"] = []
        incident_info["attachments"] = []

        # collect the incident comments
        if fn_inputs.siemplify_sync_comments:
            incident_info["comments"] = resilient_env.get_incident_comments(fn_inputs.siemplify_incident_id)

        # collect the incident artifacts
        if fn_inputs.siemplify_sync_artifacts:
            incident_info['artifacts'] = resilient_env.get_incident_artifacts(fn_inputs.siemplify_incident_id)

        # collect the incident attachments
        if fn_inputs.siemplify_sync_attachments:
            # incident_info['attachments'] = resilient_env.get_incident_attachments(fn_inputs.siemplify_incident_id)
            pass

        # assemble all the data for Siemplify incident creation
        incident_info['siemplify_assigned_user'] = fn_inputs.siemplify_assigned_user
        incident_info['siemplify_environment'] = fn_inputs.siemplify_environment if fn_inputs.siemplify_environment else self.app_configs.default_environment
        incident_info['siemplify_case_id'] = fn_inputs.siemplify_case_id
        incident_info['siemplify_alert_id'] = fn_inputs.siemplify_alert_id

        self.LOG.debug(incident_info)

        siemplify_env = SiemplifyCommon(self.rc, self.app_configs)
        results = siemplify_env.sync_case(incident_info)

        # get the results based on the data returned
        if isinstance(results, int):
            # get the full case information
            case_results = siemplify_env.get_case(results)
            case_results['siemplify_case_url'] = "{}/#/main/cases/classic-view/{}".format(self.app_configs.base_url, results)
            status = True
            results = case_results
        else:
            status = False

        yield self.status_message("Endpoint reached successfully and returning results for App Function: '{0}'".format(FN_NAME))
        yield FunctionResult(results, success=status)
