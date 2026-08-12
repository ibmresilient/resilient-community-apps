# -*- coding: utf-8 -*-

"""AppFunction implementation"""

import logging
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult

PACKAGE_NAME = "fn_shadowserver"
FN_NAME = "fn_shadowserver"

LOG = logging.getLogger(__name__)

URL = "https://api.shadowserver.org/malware/info?sample="

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'fn_shadowserver'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: This function makes an API call to Shadowserver to check if the hash is in their database.
        Inputs:
            -   fn_inputs.shadowserver_artifact_type
            -   fn_inputs.shadowserver_artifact_value
        """
        

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        artifact_type = fn_inputs.shadowserver_artifact_type
        artifact_value = fn_inputs.shadowserver_artifact_value

        accepted_types = {
            "Malware MD5 Hash": "md5",
            "Malware SHA-1 Hash": "sha1"
        }

        if artifact_type not in accepted_types.keys():
            yield FunctionResult({}, success=False, reason="Shadowserver lookup not implemented for {0}".format(artifact_type))

        LOG.info("Shadow Server lookup started for Artifact Type {0} - Artifact Value {1}"
                 .format(artifact_type, artifact_value))

        request = "{0}{1}".format(self.options.get("shadowserver_url", URL),
                                    artifact_value)

        LOG.debug("Getting info from {0}".format(request))
        
        response = self.rc.execute("get", request)
        if response.status_code == 200:
            LOG.debug(response.text)
            results = response.json()
            yield FunctionResult(results)
        else:
          yield FunctionResult({}, success=False, reason="Received response status {0}".format(response.status_code))
