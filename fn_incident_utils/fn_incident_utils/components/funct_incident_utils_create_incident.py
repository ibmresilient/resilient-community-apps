# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
from resilient import SimpleHTTPException
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, RequestsCommon, validate_fields

PACKAGE_NAME = "fn_incident_utils"
FN_NAME = "incident_utils_create_incident"

INCIDENT_URL = "/incidents"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'incident_utils_create_incident''"""

    def __init__(self, opts):
        """Constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.fn_options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.fn_options = opts.get(PACKAGE_NAME, {})

    @function(FN_NAME)
    def _incident_utils_create_incident_function(self, event, *args, **kwargs):
        """Function: Create an incident from a function"""
        try:
            LOG = logging.getLogger(__name__)
            rc = RequestsCommon(self.opts, self.fn_options)
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting '{0}' running in workflow '{1}'".format(FN_NAME, wf_instance_id))

            fn_inputs = validate_fields(
                ["inc_create_fields"],
                kwargs)

            LOG.info("'{0}' inputs: %s", fn_inputs)

            yield StatusMessage("Validations complete. Starting business logic")

            rest_client = self.rest_client()
            try:
                create_fields = json.loads(fn_inputs['inc_create_fields'])
                incident = rest_client.post(INCIDENT_URL, create_fields)
                reason = None
            except SimpleHTTPException as err:
                LOG.error("Failure creating incident: %s", str(err))
                incident = None
                reason = str(err)

            yield StatusMessage("Finished '{0}' that was running in workflow '{1}'".format(FN_NAME, wf_instance_id))

            results = rp.done(False if reason else True, incident, reason=reason)

            LOG.info("'%s' complete", FN_NAME)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
