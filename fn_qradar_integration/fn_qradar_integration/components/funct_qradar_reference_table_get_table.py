# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, ResultPayload
from fn_qradar_integration.util.qradar_utils import QRadarClient
PACKAGE_NAME = "fn_qradar_integration"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'qradar_reference_table_get_tables''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("qradar_reference_table_get_table")
    def _qradar_reference_table_get_table_function(self, event, *args, **kwargs):
        """Function: None"""
        try:

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting 'qradar_reference_table_get_table' running in workflow '{0}'".format(wf_instance_id))
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            # Get the function parameters:
            qradar_reference_table_name = kwargs.get("qradar_reference_table_name")  # text

            log = logging.getLogger(__name__)
            log.info("qradar_reference_table_name: %s", qradar_reference_table_name)

            qradar_verify_cert = True
            if "verify_cert" in self.options and self.options["verify_cert"].lower() == "false":
                qradar_verify_cert = False

            log.debug("Connecting to QRadar instance @ {}".format(self.options["host"]))

            qradar_client = QRadarClient(host=self.options["host"],
                                         username=self.options.get("username", None),
                                         password=self.options.get("qradarpassword", None),
                                         token=self.options.get("qradartoken", None),
                                         cafile=qradar_verify_cert,
                                         opts=self.opts, function_opts=self.options)

            result = qradar_client.get_ref_table_element(qradar_reference_table_name)
            yield StatusMessage("Call made to QRadar and response code returned: {}".format(result.get('status_code', 'no response code found')))
            results = rp.done(success=True,
                              content=result)

            log.info(results['content'].keys())
            log.info(results['content']['data'].keys())
            for inner_key, item in results['content'].get('data', []).items():
  
                for outer_key, inner_item in item.items():
                    print(inner_key, outer_key, inner_item)

            yield StatusMessage("Finished 'qradar_reference_table_get_table' that was running in workflow '{0}'".format(wf_instance_id))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
