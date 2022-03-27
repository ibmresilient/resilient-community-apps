# -*- coding: utf-8 -*-

"""AppFunction implementation"""

import logging
from resilient import get_client
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields
from fn_symantec_dlp.lib.resilient_common import ResilientCommon
from fn_symantec_dlp.lib.dlp_common import SymantecDLPCommon

PACKAGE_NAME = "fn_symantec_dlp"
FN_NAME = "symantec_dlp_get_notes"

LOG = logging.getLogger(__name__)

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'symantec_dlp_get_notes'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Synchronize the notes between Symantec DLP and corresponding SOAR incident.
        Inputs:
            -   fn_inputs.incident_id
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        soar_case_id = fn_inputs.incident_id

        rest_client = get_client(self.opts)
        res_common = ResilientCommon(rest_client)
        sdlp_client = SymantecDLPCommon(self.rc, self.options)

        # Get the SOAR incident
        uri = u"/incidents/{}?handle_format=names".format(soar_case_id)
        incident = self.rest_client().get(uri)

        if not incident:
            IntegrationError("Symantec DLP: Get DLP Notes: Case {0} not found".format(soar_case_id))

        # Make sure there is an Symantec DLP incident associated with this incident
        sdlp_incident_id = incident.get('properties', {}).get('sdlp_incident_id', None)
        if not sdlp_incident_id:
            IntegrationError("Symantec DLP Get Notes: sdlp_incident_id {0} not found".format(sdlp_incident_id))

        # SYNC DLP Comments
        sdlp_notes  = sdlp_client.get_sdlp_incident_notes(sdlp_incident_id)
        new_comments = res_common.filter_resilient_comments(soar_case_id, sdlp_notes)
        LOG.info(new_comments)

        for comment in new_comments:
            res_common.create_incident_comment(soar_case_id, comment)

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        results = {}
        yield FunctionResult(results)

