# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from fn_microsoft_sentinel.lib.sentinel_common import SentinelAPI, PACKAGE_NAME
from fn_microsoft_sentinel.lib.resilient_common import ResilientCommon
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields

PACKAGE_NAME = "fn_microsoft_sentinel"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'sentinel_get_incident_comments''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("sentinel_get_incident_comments")
    def _sentinel_get_incident_comments_function(self, event, *args, **kwargs):
        """Function: Get Comments from a Sentinel Incident"""
        try:
            validate_fields(
                ["sentinel_profile", "sentinel_incident_id"],
                kwargs
            )

            yield StatusMessage("Starting 'sentinel_get_incident_comments'")

            rc = ResultPayload(PACKAGE_NAME, **kwargs)

            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # int
            sentinel_incident_id = kwargs.get("sentinel_incident_id")  # text
            sentinel_profile = kwargs.get("sentinel_profile")  # text

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            log.info("sentinel_incident_id: %s", sentinel_incident_id)
            log.info("sentinel_profile: %s", sentinel_profile)

            sentinel_api = SentinelAPI(self.options['tenant_id'],
                                       self.options['client_id'],
                                       self.options['app_secret'],
                                       self.opts, self.options)

            resilient_api = ResilientCommon(self.rest_client())

            result, status, reason = sentinel_api.get_comments(sentinel_incident_id,
                                                               sentinel_profile)
            # need to avoid creating same comments over and over
            # this logic will read a datatable of sentinel incident comment_ids
            #  and remove those comments which have already sync
            # WARNING: This logic will not update an existing comment (which may have been updated)
            new_comments = []
            if status:
                # get incident comments and filter out those already sync'd
                incident_comments = resilient_api.get_comment_datatable(incident_id)

                if incident_comments:
                    for comment in result['value']:
                        if comment['name'] not in incident_comments:
                            new_comments.append(comment)
                else:
                    new_comments = result['value']

                log.info("Filtered new comments %s out of %s", len(new_comments),
                                                               len(result['value']))

            yield StatusMessage("Finished 'sentinel_get_incident_comments'")

            results = rc.done(status, { "value": new_comments }, reason=reason)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
