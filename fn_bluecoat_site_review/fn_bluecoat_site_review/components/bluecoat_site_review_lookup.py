# -*- coding: utf-8 -*-
# (c) Copyright IBM Corporation 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
import xmltodict
from resilient_lib import RequestsCommon, ResultPayload
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


PACKAGE = "fn_bluecoat_site_review"
HEADERS = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'bluecoat_site_review_lookup"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get(PACKAGE, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get(PACKAGE, {})

    @function("bluecoat_site_review_lookup")
    def _bluecoat_site_review_lookup_function(self, event, *args, **kwargs):
        """Function: This function takes an artifact of type URL or DNS name and returns those results as a json object."""

        try:
            # Get the function parameters:
            artifact_value = kwargs.get("artifact_value")  # text

            log = logging.getLogger(__name__)
            log.info("artifact_value: %s", artifact_value)

            fr = ResultPayload(PACKAGE, **kwargs)
            # Assignment for successful completion of the code
            results_flag = True

            yield StatusMessage("starting...")

            response_json = self.sitereview(self.options['url'], artifact_value)

            # handles if there is no result in the JSON Return Object:
            msg = None
            if response_json is None:
                msg = "There were no results..."
                log.debug(msg)
                results_flag = False
            else:
                # This handles if the categorizaton is a list in the JSON object that needs to be traversed/isolated or not
                if response_json.get('FailedResult'):
                    results_flag = False
                    msg = response_json.get('FailedResult')

            yield StatusMessage("done...")

            results_payload = fr.done(results_flag, response_json, msg)
            # Produce a FunctionResult with the results
            yield FunctionResult(results_payload)
        except Exception:
            yield FunctionError()

    def sitereview(self, url, value):
        payload = {"url": value, "captcha":""}

        rc = RequestsCommon(self.opts, self.options)

        result = rc.execute_call('post', url, payload=payload, headers=HEADERS, resp_type='text')

        dict_to_str = json.dumps(xmltodict.parse(result))
        return json.loads(dict_to_str)