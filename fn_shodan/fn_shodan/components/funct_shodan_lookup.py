# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields, RequestsCommon
from fn_shodan.util.helper import CONFIG_DATA_SECTION, make_api_call

PACKAGE_NAME = CONFIG_DATA_SECTION


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'shodan_lookup''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("shodan_lookup")
    def _shodan_lookup_function(self, event, *args, **kwargs):
        """Function: Function to look up an IP Address in Shodan"""
        try:

            log = logging.getLogger(__name__)
            rc = RequestsCommon(self.opts, self.options)
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            # Get + validate the app.config parameters:
            app_configs = validate_fields([{"name": "shodan_apikey", "placeholder": "<your-api-key>"}], self.options)
            log.info("Validated app configs")

            # Get + validate the function parameters:
            fn_inputs = validate_fields(["shodan_lookuphost"], kwargs)
            log.info("Validated function inputs: %s", fn_inputs)

            yield StatusMessage("Querying Shodan for '{0}'".format(fn_inputs.get("shodan_lookuphost")))

            res = make_api_call(
                call_type="host",
                rc=rc,
                api_key=app_configs.get("shodan_apikey"),
                app_configs=app_configs,
                qry=fn_inputs.get("shodan_lookuphost")
            )

            # Handle if an invalid IP Address or it didn't find it
            if res.get("err"):
                yield StatusMessage("Error got while querying Shodan: {0}".format(res.get("reason")))
                results = rp.done(success=False, content=res, reason=res.get("reason"))

            else:
                results = rp.done(success=True, content=res)

                # For backwards compatability
                results["shodan_vulns"] = res.get("vulns", "None Found")
                results["shodan_ports"] = res.get("ports", "None Found")
                results["shodan_url"] = "https://www.shodan.io/host/{0}".format(fn_inputs.get("shodan_lookuphost"))

                yield StatusMessage("Finished querying Shodan")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
