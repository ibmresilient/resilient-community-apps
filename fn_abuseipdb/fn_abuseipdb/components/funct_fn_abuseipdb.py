# -*- coding: utf-8 -*-

"""AppFunction implementation"""

import logging
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

PACKAGE_NAME = "fn_abuseipdb"
FN_NAME = "fn_abuseipdb"

LOG = logging.getLogger(__name__)

HEADER_TEMPLATE = {
    "Key": None,
    "Accept": "application/json"
}

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'fn_abuseipdb'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _lookup_net_ip(self, fn_inputs):
        """Lookup an artifact"""

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        # event.artifact is a ThreatServiceArtifactDTO
        artifact_type = fn_inputs.abuseipdb_artifact_type
        artifact_value = fn_inputs.abuseipdb_artifact_value
        rangeOfDays = fn_inputs.abuseipdb_range_of_days

        # Example validating app_configs
        validate_fields([
            {"name": "abuseipdb_key"},
            {"name": "abuseipdb_url"}],
            self.app_configs)

        LOG.info("AbuseIPDB lookup started for Artifact Type %s - Artifact Value %s",
                 artifact_type, artifact_value)

        params = {
                'ipAddress': artifact_value,
                'isWhitelisted': self.app_configs.ignore_white_listed,
                'verbose': True,
                'maxAgeInDays': rangeOfDays
            }

        headers = HEADER_TEMPLATE.copy()
        headers['Key'] = self.app_configs.abuseipdb_key

        url = self.app_configs.abuseipdb_url

        response = self.rc.execute("get", url, params=params, headers=headers)

        results = response.json()

        yield self.status_message("Endpoint reached successfully and returning results for App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)
