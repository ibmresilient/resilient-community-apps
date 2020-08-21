# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, RequestsCommon, validate_fields
from fn_urlhaus.util.helper import CONFIG_DATA_SECTION, make_api_call

PACKAGE_NAME = CONFIG_DATA_SECTION


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_urlhaus''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("fn_urlhaus")
    def _fn_urlhaus_function(self, event, *args, **kwargs):
        """Function: Perform a lookup on several artifacts of types"""
        try:

            log = logging.getLogger(__name__)
            rc = RequestsCommon(self.opts, self.options)
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Get + validate the app.config parameters:
            app_configs = validate_fields(["url"], self.options)
            log.info("Validated app configs")

            # Get + validate the function parameters:
            fn_inputs = validate_fields(["urlhaus_artifact_value", "urlhaus_artifact_type"], kwargs)
            log.info("Validated function inputs: %s", fn_inputs)

            yield StatusMessage("Checking {0} {1} against URLhaus'".format(
                fn_inputs.get("urlhaus_artifact_type"), fn_inputs.get("urlhaus_artifact_value")))

            res = make_api_call(
                call_type="lookup",
                base_url=app_configs.get("url"),
                artifact_type=fn_inputs.get("urlhaus_artifact_type"),
                artifact_value=fn_inputs.get("urlhaus_artifact_value"),
                rc=rc
            )

            res_json = res.json()

            yield StatusMessage("Query Status: {0}".format(res_json.get("query_status")))

            results = rp.done(success=True, content=res_json)

            log.info("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
