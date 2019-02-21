# -*- coding: utf-8 -*-
#
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
#
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_qradar_integration.util.qradar_utils import QRadarClient

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'qradar_delete_reference_set_item"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_qradar_integration", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_qradar_integration", {})

    @function("qradar_delete_reference_set_item")
    def _qradar_delete_reference_set_item_function(self, event, *args, **kwargs):
        """Function: Delete an item from a given QRadar reference set"""
        try:
            # Get the function parameters:
            qradar_reference_set_name = kwargs.get("qradar_reference_set_name")  # text
            qradar_reference_set_item_value = kwargs.get("qradar_reference_set_item_value")  # text

            log = logging.getLogger(__name__)
            log.info("qradar_reference_set_name: %s", qradar_reference_set_name)
            log.info("qradar_reference_set_item_value: %s", qradar_reference_set_item_value)

            qradar_verify_cert = True
            if "verify_cert" in self.options and self.options["verify_cert"] == "false":
                qradar_verify_cert = False

            log.debug("Connection to {} using {}".format(self.options["host"], self.options["username"]))

            yield StatusMessage("starting...")
            qradar_client = QRadarClient(host=self.options["host"],
                                         username=self.options.get("username", None),
                                         password=self.options.get("qradarpassword", None),
                                         token=self.options.get("qradartoken", None),
                                         cafile=qradar_verify_cert)

            result = qradar_client.delete_ref_element(qradar_reference_set_name,
                                                   qradar_reference_set_item_value)
            yield StatusMessage("done...")

            # Produce a FunctionResult with the results
            yield FunctionResult(result)
        except Exception as e:
            log.error(str(e))
            yield FunctionError()