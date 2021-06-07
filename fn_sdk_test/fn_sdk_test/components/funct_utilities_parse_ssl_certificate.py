# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

PACKAGE_NAME = "fn_sdk_test"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'utilities_parse_ssl_certificate''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("utilities_parse_ssl_certificate")
    def _utilities_parse_ssl_certificate_function(self, event, *args, **kwargs):
        """Function: This function produces the structured data from a provided SSL certificate. Three inputs are accepted by the function. There are 2 defined ways to use this function for parsing certificates.

Option 1 involves providing a JSON-encoded representation of a certificate. In this case the certificate input parameter should be this JSON string.

Option 2 involves providing a certificate file for parsing. When the rule is triggered on an artifact, both the incident_id for that incident and the artifact_id for the specified certificate file must be provided.

NOTE: The Parse SSL Certificate function expects a certificate of type PEM. If you require a way to get a PEM formatted certificate from a URL consider using this in conjunction with the Extract SSL Cert from URL function."""
        try:

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting 'utilities_parse_ssl_certificate' running in workflow '{0}'".format(wf_instance_id))

            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            utilities_certificate = kwargs.get("utilities_certificate")  # text
            artifact_id = kwargs.get("artifact_id")  # number

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            log.info("utilities_certificate: %s", utilities_certificate)
            log.info("artifact_id: %s", artifact_id)

            ##############################################
            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE #
            ##############################################

            yield StatusMessage("Finished 'utilities_parse_ssl_certificate' that was running in workflow '{0}'".format(wf_instance_id))

            results = {
                "content": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
