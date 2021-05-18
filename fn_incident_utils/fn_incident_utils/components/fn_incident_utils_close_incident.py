# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import close_incident, ResultPayload

PACKAGE_NAME = "fn_incident_utils"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'incident_utils_close_incident''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("incident_utils_close_incident")
    def _incident_utils_close_incident_function(self, event, *args, **kwargs):
        """Function: Function that takes a JSON String of field and value pairs to close an Incident."""
        try:
            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            close_fields = kwargs.get("close_fields")  # text

            log = logging.getLogger(__name__)
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            # Check JSON string and convert it to dict
            if close_fields is None:
                close_fields = {}
            else:
                try:
                    close_fields = json.loads(close_fields)
                except json.decoder.JSONDecodeError as jerr:
                    reason = "Failure parsing 'close_fields': {}".format(str(jerr))
                    log.error(reason)
                    yield FunctionResult(rp.done(False, None, reason=reason))
                    return

            log.info("incident_id: %s", incident_id)
            log.info("close_fields: %s", close_fields)

            yield StatusMessage("starting...")
            # Instansiate new Resilient API object
            res_client = self.rest_client()

            # API call to Close an Incident
            response = close_incident(res_client, incident_id, close_fields)

            results = rp.done(True, response.json())

            yield StatusMessage("done...")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
