# -*- coding: utf-8 -*-
# Copyright IBM Corp. 2010, 2020 - Confidential Information
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import time
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_mcafee_tie.lib.mcafee_tie_common import get_trust_level_value, get_mcafee_client, get_tie_client, \
                                                get_mcafee_hash_type, PACKAGE_NAME, MyReputationChangeCallback
from resilient_lib import ResultPayload, validate_fields

LOG = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'mcafee_tie_set_file_reputation''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})
        self.client = get_mcafee_client(self.options)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})
        self.client = get_mcafee_client(self.options)

    @function("mcafee_tie_set_file_reputation")
    def _mcafee_tie_set_file_reputation_function(self, event, *args, **kwargs):
        """Function: Set a file's reputation. This works on MD5, SH1 and SHA256 hashes."""
        try:
            yield StatusMessage("Starting")

            # Get the function parameters:
            mcafee_tie_hash_type = kwargs.get("mcafee_tie_hash_type")  # text
            mcafee_tie_comment = kwargs.get("mcafee_tie_comment")  # text
            mcafee_tie_trust_level = self.get_select_param(kwargs.get("mcafee_tie_trust_level"))  # select, values: "KNOWN_TRUSTED_INSTALLED", "KNOWN_TRUSTED", "MOST_LIKELY_TRUSTED", "MIGHT_BE_TRUSTED", "UNKNOWN", "MIGHT_BE_MALICIOUS", "MOST_LIKELY_MALICIOUS", "KNOWN_MALICIOUS", "NOT SET"
            mcafee_tie_hash = kwargs.get("mcafee_tie_hash")  # text
            mcafee_tie_filename = kwargs.get("mcafee_tie_filename")  # text

            log = logging.getLogger(__name__)
            log.info("mcafee_tie_hash_type: %s", mcafee_tie_hash_type)
            log.info("mcafee_tie_comment: %s", mcafee_tie_comment)
            log.info("mcafee_tie_trust_level: %s", mcafee_tie_trust_level)
            log.info("mcafee_tie_hash: %s", mcafee_tie_hash)
            log.info("mcafee_tie_filename: %s", mcafee_tie_filename)

            validate_fields(["mcafee_tie_hash_type", "mcafee_tie_hash", "mcafee_tie_trust_level"], kwargs)

            result_payload = ResultPayload(PACKAGE_NAME, **kwargs)

            tie_client = get_tie_client(self.client)

            hash_type = get_mcafee_hash_type(mcafee_tie_hash_type)
            trust_level = get_trust_level_value(mcafee_tie_trust_level)
            hash_payload = {
                    hash_type: mcafee_tie_hash
                }
            LOG.debug("Trust Level: %s, payload: %s", trust_level, hash_payload)

            # set the call back routine to catch changes or errors
            result_callback = MyReputationChangeCallback()
            tie_client.add_file_reputation_change_callback(result_callback)            

            # Set the Enterprise reputation for notepad.exe to Known Trusted
            tie_client.set_file_reputation(
                trust_level,
                hash_payload,
                comment=mcafee_tie_comment,
                filename=mcafee_tie_filename
            )

            # wait for result or a timeout
            wait_iter = 4
            sleep_time = 5
            # sleep while waiting for a call back. Sleep time progesses: 5, 10, 15, ...
            while wait_iter > 0 and not result_callback.result:
                time.sleep(sleep_time)
                sleep_time += 5
                wait_iter -= 1

            yield StatusMessage("Finished" if result_callback.result else "No result received. Check McAfee console")
            results = result_payload.done(True if result_callback.result else False, result_callback.result)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
