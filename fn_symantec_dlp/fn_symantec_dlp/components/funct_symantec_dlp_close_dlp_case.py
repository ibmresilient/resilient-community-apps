# -*- coding: utf-8 -*-

"""AppFunction implementation"""
import logging
from resilient import get_client
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields
from fn_symantec_dlp.lib.resilient_common import ResilientCommon
from fn_symantec_dlp.lib.dlp_common import SymantecDLPCommon
from fn_symantec_dlp.lib.jinja_common import JinjaEnvironment

DEFAULT_CREATE_DLP_CASE = "templates/dlp_create_case_template.jinja"
DEFAULT_SOAR_CLOSE_CASE = "templates/dlp_close_case_template.jinja"
DEFAULT_SOAR_UPDATE_CASE = "templates/dlp_update_case_template.jinja"

PACKAGE_NAME = "fn_symantec_dlp"
FN_NAME = "symantec_dlp_close_dlp_case"

LOG = logging.getLogger(__name__)

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'symantec_dlp_close_dlp_case'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Close SOAR case when the DLP incident status is set to Resolve.
        Inputs:
            -   fn_inputs.incident_id
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))
        soar_case_id = fn_inputs.incident_id

        rest_client = get_client(self.opts)
        res_common = ResilientCommon(rest_client)
        sdlp_client = SymantecDLPCommon(self.rc, self.options)
        jinja_env = JinjaEnvironment()

        # Get the SOAR incident
        uri = u"/incidents/{}?handle_format=names".format(soar_case_id)
        incident = self.rest_client().get(uri)

        if not incident:
            IntegrationError("Symantec DLP: Close DLP Case: case {0} not found".format(soar_case_id))

        # Make sure there is an Symantec DLP incident associated with this incident
        sdlp_incident_id = incident.get('properties', {}).get('sdlp_incident_id', None)
        if not sdlp_incident_id:
            IntegrationError("Symantec DLP: Close DLP Case: sdlp_incident_id {0} not found".format(sdlp_incident_id))

        # Get the SDLP 
        sdlp_incident_payload = sdlp_client.get_sdlp_incident_editable_detail_payload(sdlp_incident_id)

        # Close the case in SOAR
        incident_close_payload = jinja_env.make_payload_from_template(
                                                    self.options.get("close_case_template"),
                                                    DEFAULT_SOAR_CLOSE_CASE,
                                                    sdlp_incident_payload)

        _close_resilient_incident = res_common.update_incident(
                                                    soar_case_id,
                                                    incident_close_payload)               
                
        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        results = {"success": True}
                   
        yield FunctionResult(results)