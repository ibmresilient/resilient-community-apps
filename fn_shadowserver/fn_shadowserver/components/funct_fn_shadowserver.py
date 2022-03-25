# -*- coding: utf-8 -*-

"""AppFunction implementation"""

import logging
import json
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields

PACKAGE_NAME = "fn_shadowserver"
FN_NAME = "fn_shadowserver"

LOG = logging.getLogger(__name__)

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'fn_shadowserver'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: None
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
            yield self.status_message("Artifact type not one of the expected values")
            LOG.info("Shadow Server lookup not implemented for {0}".format(artifact_type))
            return

        LOG.info("Shadow Server lookup started for Artifact Type {0} - Artifact Value {1}"
                 .format(artifact_type, artifact_value))

        # Example validating app_configs
        validate_fields([
            {"name": "shadow_server_url"}],
            self.app_configs)


        url = "{0}?{1}={2}".format(self.options.get("shadow_server_url", "http://bin-test.shadowserver.org/api"),
                                accepted_types.get(artifact_type),
                                artifact_value)
        LOG.debug("Getting info from {0}".format(url))
        response = self.rc.execute("get", url)
        if response.status_code == 200:
                LOG.debug(response.text)

                # return hash {...} for found result or just hash
                if not response.text.strip() ==  artifact_value:
                    results = json.loads(response.text.replace(artifact_value, "", 1))
                    yield FunctionResult(results)        
        else:
            LOG.warn("Got response status {0} from Shadow Server".format(response.status_code))

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))
