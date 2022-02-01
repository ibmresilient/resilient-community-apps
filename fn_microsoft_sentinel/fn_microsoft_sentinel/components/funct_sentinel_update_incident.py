# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
"""Function implementation"""

import logging
import traceback
from resilient_circuits import ResilientComponent, ActionMessage, handler
from resilient_lib import validate_fields
from fn_microsoft_sentinel.lib.function_common import PACKAGE_NAME, SentinelProfiles, DEFAULT_SENTINEL_UPDATE_INCIDENT_TEMPLATE, \
  DEFAULT_SENTINEL_CLOSE_INCIDENT_TEMPLATE
from fn_microsoft_sentinel.lib.sentinel_common import SentinelAPI
from fn_microsoft_sentinel.lib.jinja_common import JinjaEnvironment
from fn_microsoft_sentinel.lib.constants import SENTINEL_INCIDENT_NUMBER

CHANNEL = "fn_microsoft_sentinel"

INCIDENT_TYPE = 0

LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """This component handles initial population of a feed and ongoing
    modifications from the associated queue."""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts)

        try:
            self.options = opts.get(PACKAGE_NAME, {})

            self.sentinel_profiles = SentinelProfiles(opts, self.options)
            self.jinja_env = JinjaEnvironment()

            self.channel = ".".join(["actions", CHANNEL])
        except Exception as err:
            LOG.error("exception: %s", err)
            error_trace = traceback.format_exc()
            LOG.error("Traceback %s", error_trace)

    @handler()
    def _sentinel_update_incident_function(self, event, *args, **kwargs):    # pylint: disable=unused-argument
        """Ingests data of any type that can be sent to a Resilient message destination"""
        # dismiss none Action events
        if not isinstance(event, ActionMessage):
            return

        # make sure to only handle incident changes
        if event.message['object_type'] != INCIDENT_TYPE:
            return

        # get the incident data
        resilient_incident = event.message['incident']

        # confirm that we have custom fields
        for confirm_field in ["sentinel_profile", SENTINEL_INCIDENT_NUMBER]:
          if not resilient_incident['properties'].get(confirm_field):
            raise ValueError("Custom field: %s and/or value not found", confirm_field)

        # Get the function parameters:
        sentinel_profile = resilient_incident['properties'].get("sentinel_profile")  # text
        sentinel_incident_id = resilient_incident['properties'].get(SENTINEL_INCIDENT_NUMBER)  # text

        log = logging.getLogger(__name__)
        log.info("sentinel_profile: %s", sentinel_profile)
        log.info("sentinel_incident_id: %s", sentinel_incident_id)

        sentinel_api = SentinelAPI(self.options['tenant_id'],
                                   self.options['client_id'],
                                   self.options['app_secret'],
                                   self.opts, self.options)

        profile_data = self.sentinel_profiles.get_profile(sentinel_profile)

        # is this SOAR incident active or closed?
        if resilient_incident["plan_status"] == "A":
          template = profile_data.get("sentinel_update_incident_template")
          default_template = DEFAULT_SENTINEL_UPDATE_INCIDENT_TEMPLATE
        else:
          template = profile_data.get("sentinel_close_incident_template")
          default_template = DEFAULT_SENTINEL_CLOSE_INCIDENT_TEMPLATE


        incident_payload = self.jinja_env.make_payload_from_template(
                                template,
                                default_template,
                                resilient_incident)

        result, status, reason = sentinel_api.create_update_incident(
                                                profile_data,
                                                sentinel_incident_id,
                                                incident_payload
                                              )

        if status:
            log.info("Sentinel incident updated. incident: %s", result['properties']['incidentNumber'])
        else:
            log.error("Sentinel incident failure for incident %s: %s", sentinel_incident_id, reason)
