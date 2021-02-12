# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2020. All Rights Reserved.
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, ResultPayload
from fn_qradar_integration.util.qradar_utils import QRadarClient

PACKAGE_NAME = "fn_qradar_integration"

LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'qradar_get_reference_tables''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("qradar_get_reference_tables")
    def _qradar_get_reference_tables_function(self, event, *args, **kwargs):
        """Function: Get all reference tables from a QRadar instance"""
        try:

            # Get the wf_instance_id of the workflow this Function was called in, if not found return a backup string
            wf_instance_id = event.message.get("workflow_instance", {}).get("workflow_instance_id", "no instance id found")

            yield StatusMessage("Starting 'qradar_reference_table_add_item' that was running in workflow '{0}'".format(wf_instance_id))
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            qradar_verify_cert = True
            if "verify_cert" in self.options and self.options["verify_cert"].lower() == "false":
                qradar_verify_cert = False

            LOG.debug("Connecting to QRadar instance @ {}".format(self.options["host"]))

            qradar_client = QRadarClient(host=self.options["host"],
                                         username=self.options.get("username", None),
                                         password=self.options.get("qradarpassword", None),
                                         token=self.options.get("qradartoken", None),
                                         cafile=qradar_verify_cert,
                                         opts=self.opts, function_opts=self.options)

            result = qradar_client.get_all_ref_tables()

            status_code = isinstance(result, list)
            reason = None if status_code else result.get('http_response', {}).get('message', 'unknown')
            results = rp.done(success=status_code, 
                              content=result,
                              reason=reason)
            yield StatusMessage("Finished 'qradar_reference_table_add_item' that was running in workflow '{0}'".format(wf_instance_id))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
