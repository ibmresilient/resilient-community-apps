# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, RequestsCommon, validate_fields, IntegrationError
from fn_urlhaus.util.helper import CONFIG_DATA_SECTION, make_api_call

PACKAGE_NAME = CONFIG_DATA_SECTION


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_urlhaus_submission''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("fn_urlhaus_submission")
    def _fn_urlhaus_submission_function(self, event, *args, **kwargs):
        """Function: Submit a url to URLhaus as distributing malware"""
        try:
            log = logging.getLogger(__name__)
            rc = RequestsCommon(self.opts, self.options)
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Get + validate the app.config parameters:
            app_configs = validate_fields(["submit_url", "submit_api_key"], self.options)
            log.info("Validated app configs")

            # Get + validate the function parameters:
            fn_inputs = validate_fields(["urlhaus_artifact_value"], kwargs)
            log.info("Validated function inputs: %s", fn_inputs)

            yield StatusMessage("Submitting {0} to URLhaus".format(
                fn_inputs.get("urlhaus_artifact_value")))

            res = make_api_call(
                call_type="submission",
                base_url=app_configs.get("submit_url"),
                api_key=app_configs.get("submit_api_key"),
                artifact_value=fn_inputs.get("urlhaus_artifact_value"),
                rc=rc
            )

            if "denied" in res.text:
                raise IntegrationError("Failed to submit artifact. API Key invalid")

            yield StatusMessage(u"Response from URLhaus: {0}".format(res.text))

            results = rp.done(success=True, content=res.text)

            log.info("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
