# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from logging import getLogger
from json import loads
from json.decoder import JSONDecodeError as ValueError
from resilient import SimpleHTTPException
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, RequestsCommon, validate_fields
from fn_soar_utils.util.soar_utils_common import PACKAGE_NAME

FN_NAME = "soar_utils_create_incident"
INCIDENT_URL = "/incidents"

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'soar_utils_create_incident''"""

    def __init__(self, opts):
        """Constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.fn_options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.fn_options = opts.get(PACKAGE_NAME, {})

    @function(FN_NAME)
    def _soar_utils_create_incident_function(self, event, *args, **kwargs):
        """Function: Create an incident from a function"""
        try:
            LOG = getLogger(__name__)
            rc = RequestsCommon(self.opts, self.fn_options)
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage(f"Starting '{FN_NAME}' running in workflow '{wf_instance_id}'")

            fn_inputs = validate_fields(
                ["soar_utils_create_fields"],
                kwargs)

            LOG.info("'{0}' inputs: %s", fn_inputs)

            yield StatusMessage("Validations complete. Starting business logic")

            rest_client = self.rest_client()
            incident = reason = None
            try:
                create_fields = loads(fn_inputs['soar_utils_create_fields'])
                incident = rest_client.post(INCIDENT_URL, create_fields)
            except ValueError as err:
                reason = f"Failure parsing 'soar_utils_create_fields': {fn_inputs['soar_utils_create_fields']}\n{str(err)}"
                LOG.error(reason)
            except SimpleHTTPException as err:
                reason = f"Failure creating incident: {str(err)}"
                LOG.error(reason)

            yield StatusMessage(f"Finished '{FN_NAME}' that was running in workflow '{wf_instance_id}'")

            results = rp.done(False if reason else True, incident, reason=reason)

            LOG.info("'%s' complete", FN_NAME)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
