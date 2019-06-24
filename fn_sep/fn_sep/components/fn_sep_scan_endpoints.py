# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Resilient functions component to run a Symantec SEPM action - initiate eoc scan. """

# Set up:
# Destination: a Queue named "fn_sep".
# Manual Action: Execute a REST action against a SYMANTEC SEPM server.import json
import json
import logging
from os import path

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields
from fn_sep.lib.sep_client import Sepclient
from fn_sep.lib.helpers import CONFIG_DATA_SECTION, transform_kwargs

LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_sep_scan_endpoints' of package fn_sep.

    The Function takes the following parameter:
            sep_group_ids, sep_computer_ids, sep_scan_type, sep_file_name, sep_sha256, sep_description

    An example of a set of query parameter might look like the following:
            sep_group_ids =
            sep_computer_ids =
            sep_scan_type = "QUICK_SCAN"
            sep_file_name =
            sep_sha256 =
            sep_sha1 =
            sep_md5 =
            sep_description =
            sep_scan_action = None

    The function will execute a REST api get request against a SYMANTEC  SEPM server for information on endpoints and
    returns a result in JSON format similar to the following.
    {
        'inputs': {u'sep_description': u'Scan eoc for file in the SEP environment.',
                   u'sep_computer_ids': u'D31AA16E0946C25D40C83823C500518B,89AD1BBB0946C25D25E6C0984E971D8A',
                   u'sep_scan_action': None,  u'sep_file_path': u'C:\\temp\\New Text Document.txt',
                   u'sep_sha1': None, u'sep_sha256': None, u'sep_md5': None, u'sep_scan_type': u'QUICK_SCAN'
                  },
        'metrics': {'package': 'fn-sep', 'timestamp': '2019-05-14 14:26:03', 'package_version': '1.0.0',
                    'host': 'myhost', 'version': '1.0', 'execution_time_ms': 1079
                   },
        'success': True,
        'content': {u'commandID_computer': u'E50FDD8C541D4405A3B5CDB83EC7E1DC'},
        'raw': '{"commandID_computer": "E50FDD8C541D4405A3B5CDB83EC7E1DC"}',
        'reason': None,
        'version': '1.0'
    }
    """
    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    @function("fn_sep_scan_endpoints")
    def _fn_sep_scan_endpoints_function(self, event, *args, **kwargs):
        """Function: Run a Evidence of Compromise (EOC) scan on Symantec Endpoint Protection endpoints."""
        try:
            params = transform_kwargs(kwargs) if kwargs else {}

            # Instantiate result payload object.
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Get the function parameters:
            sep_group_ids = kwargs.get("sep_group_ids")  # text
            sep_computer_ids = kwargs.get("sep_computer_ids")  # text
            sep_scan_type = self.get_select_param(kwargs.get("sep_scan_type"))  # select, values: "QUICK_SCAN", "FULL_SCAN"
            sep_file_name = kwargs.get("sep_file_path")  # text
            sep_sha256 = kwargs.get("sep_sha256")  # text
            sep_sha1 = kwargs.get("sep_sha1")  # text
            sep_md5 = kwargs.get("sep_md5")  # text
            sep_description = kwargs.get("sep_description")  # text
            sep_scan_action = self.get_select_param(kwargs.get("sep_scan_action"))  # select, values: "scan", "remediate"

            log = logging.getLogger(__name__)
            log.info("sep_group_ids: %s", sep_group_ids)
            log.info("sep_computer_ids: %s", sep_computer_ids)
            log.info("sep_scan_type: %s", sep_scan_type)
            log.info("sep_file_path: %s", sep_file_name)
            log.info("sep_sha256: %s", sep_sha256)
            log.info("sep_sha1: %s", sep_sha1)
            log.info("sep_md5: %s", sep_md5)
            log.info("sep_description: %s", sep_description)
            log.info("sep_scan_action: %s", sep_scan_action)

            validate_fields(["sep_scan_type", "sep_description", "sep_scan_action"], kwargs)

            yield StatusMessage("Running Symantec SEP Scan Endpoints command...")


            sep = Sepclient(self.options, params)

            rtn = sep.scan_endpoints(**params)

            results = rp.done(True, rtn)
            yield StatusMessage("Returning 'Symantec SEP Scan Endpoints' results")

            log.debug(json.dumps(results["content"]))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            LOG.exception("Exception in Resilient Function for Symantec SEP.")
            yield FunctionError()
