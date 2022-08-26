# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""Function implementation"""
import requests
import json
import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields
from fn_qradar_advisor.lib.qradar_ucm_client import QRadarUCMClient


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'qradar_advisor_map_rule

    Description:
    ------------
    This function takes a QRadar rule, and then calls QRAW to find
    the mappings to MITRE ATT&CK tactics
    """

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get("fn_qradar_advisor", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get("fn_qradar_advisor", {})

    @function("qradar_advisor_map_rule")
    def _qradar_advisor_map_rule_function(self, event, *args, **kwargs):
        """Function: Map rule to MITRE ATT&CK tactic"""
        log = logging.getLogger(__name__)
        validate_fields(["qradar_rule_name"], kwargs)

            # Get the function parameters:
        qradar_rule_name = kwargs.get("qradar_rule_name")  # text

        log.info("qradar_rule_name: %s", qradar_rule_name)

        qradar_verify_cert = True
        if "verify_cert" in self.options and self.options["verify_cert"] == "false":
            qradar_verify_cert = False

        yield StatusMessage("starting...")

        try:
            client = QRadarUCMClient(qradar_host=self.options["qradar_host"],
                                     qradar_token=self.options["qradar_ucm_token"],
                                     advisor_app_id=self.options["qradar_advisor_app_id"],
                                     cafile=qradar_verify_cert, log=log,
                                     opts=self.opts, function_opts=self.options)
            tactics = client.find_tactic_mapping(qradar_rule_name)
            
            yield StatusMessage("done...")

            results = {
                "tactics": tactics
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            log.exception(str(e))
            yield FunctionError()