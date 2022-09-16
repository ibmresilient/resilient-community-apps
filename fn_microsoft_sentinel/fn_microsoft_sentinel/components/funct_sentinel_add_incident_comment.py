# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
"""Function implementation"""

import logging
from resilient_lib import validate_fields, ResultPayload, clean_html
from resilient_circuits import ResilientComponent, function, handler, StatusMessage,\
                               FunctionResult, FunctionError
from fn_microsoft_sentinel.lib.function_common import PACKAGE_NAME, SentinelProfiles
from fn_microsoft_sentinel.lib.sentinel_common import SentinelAPI
from fn_microsoft_sentinel.lib.constants import FROM_SENTINEL_COMMENT_HDR, SENT_TO_SENTINEL_HDR


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'sentinel_add_incident_comment''"""

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

    @function("sentinel_add_incident_comment")
    def _sentinel_add_incident_comment_function(self, event, *args, **kwargs):
        """Function: Create a comment for a given Sentinel incident"""
        try:
            yield StatusMessage("Starting 'sentinel_add_incident_comment'")
            validate_fields(
                ["sentinel_profile", "sentinel_incident_id", "sentinel_incident_comment"],
                kwargs
            )

            rc = ResultPayload(PACKAGE_NAME, **kwargs)

            # Get the function parameters:
            sentinel_profile = kwargs.get("sentinel_profile")  # text
            sentinel_incident_id = kwargs.get("sentinel_incident_id")  # text
            sentinel_incident_comment = kwargs.get("sentinel_incident_comment")  # text

            log = logging.getLogger(__name__)
            log.info("sentinel_profile: %s", sentinel_profile)
            log.info("sentinel_incident_id: %s", sentinel_incident_id)
            log.info("sentinel_incident_comment: %s", sentinel_incident_comment)

            sentinel_api = SentinelAPI(self.options['tenant_id'],
                                       self.options['client_id'],
                                       self.options['app_secret'],
                                       self.opts, self.options)

            # do not resync comments originating from Sentinel
            if FROM_SENTINEL_COMMENT_HDR in sentinel_incident_comment or SENT_TO_SENTINEL_HDR in sentinel_incident_comment:
                yield StatusMessage("Bypassing synchronization of note: {}".format(sentinel_incident_comment))
                result = {}
                reason = None
                status = False
            else:
                profile_data = self.sentinel_profiles.get_profile(sentinel_profile)
                result, status, reason = sentinel_api.create_comment(profile_data,
                                                                    sentinel_incident_id,
                                                                    clean_html(sentinel_incident_comment))
                if status:
                    yield StatusMessage("Sentinel comment added to incident: {}"\
                        .format(sentinel_incident_id))
                else:
                    yield StatusMessage("Sentinel comment failure for incident {}: {}"\
                        .format(sentinel_incident_id, reason))

            yield StatusMessage("Finished 'sentinel_add_incident_comment'")

            results = rc.done(status, result, reason=reason)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
