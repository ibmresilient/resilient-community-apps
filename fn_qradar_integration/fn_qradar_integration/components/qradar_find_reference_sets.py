# -*- coding: utf-8 -*-
#
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
#
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_qradar_integration.util.qradar_utils import QRadarClient

"""
    For a given (artifact) value, find all the QRadar reference sets that contain it.
"""


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'qradar_find_reference_sets"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_qradar_integration", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_qradar_integration", {})

    @function("qradar_find_reference_sets")
    def _qradar_find_reference_sets_function(self, event, *args, **kwargs):
        """Function: Find reference sets that contain a given item value, together with information about this item in those reference sets. Information includes whether this item is added to the reference set manually or by a rule."""
        try:
            # Get the function parameters:
            qradar_reference_set_item_value = kwargs.get("qradar_reference_set_item_value")  # text

            log = logging.getLogger(__name__)
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

            r_items = qradar_client.find_all_ref_set_contains(qradar_reference_set_item_value)

            yield StatusMessage("done...")

            results = {
                "reference_items": r_items
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            log.exception(e)
            yield FunctionError()