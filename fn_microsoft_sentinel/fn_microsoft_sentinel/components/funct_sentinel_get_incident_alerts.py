# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields
from fn_microsoft_sentinel.lib.function_common import PACKAGE_NAME, SentinelProfiles
from fn_microsoft_sentinel.lib.sentinel_common import SentinelAPI


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'sentinel_get_incident_alerts''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})
        self.sentinel_profiles = SentinelProfiles(opts, self.options)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})
        self.sentinel_profiles = SentinelProfiles(opts, self.options)

    @function("sentinel_get_incident_alerts")
    def _sentinel_get_incident_alerts_function(self, event, *args, **kwargs):
        """Function: Get the alerts associated with a Sentinel Incident"""
        try:
            validate_fields(
                ["sentinel_profile", "sentinel_incident_id"],
                kwargs
            )

            yield StatusMessage("Starting 'sentinel_get_incident_alerts'")

            rc = ResultPayload(PACKAGE_NAME, **kwargs)

            # Get the function parameters:
            sentinel_incident_id = kwargs.get("sentinel_incident_id")  # text
            sentinel_profile = kwargs.get("sentinel_profile")  # text

            log = logging.getLogger(__name__)
            log.info("sentinel_incident_id: %s", sentinel_incident_id)
            log.info("sentinel_profile: %s", sentinel_profile)

            sentinel_api = SentinelAPI(self.options['tenant_id'],
                                       self.options['client_id'],
                                       self.options['app_secret'],
                                       self.opts, self.options)

            profile_data = self.sentinel_profiles.get_profile(sentinel_profile)
            # read all alerts associated with a Sentinel incident
            result, status, reason = sentinel_api.get_incident_alerts(profile_data,
                                                                      sentinel_incident_id)

            log.debug(result) #TODO

            yield StatusMessage("Finished 'sentinel_get_incident_alerts'")

            results = rc.done(status, result, reason=reason)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
