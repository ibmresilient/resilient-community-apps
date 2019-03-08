# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import requests
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import fn_useragentanalysis.util.selftest as selftest


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_useragentanalysis"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_useragentanalysis", {})
        selftest.selftest_function(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_useragentanalysis", {})

    @function("fn_useragentanalysis")
    def _fn_useragentanalysis_function(self, event, *args, **kwargs):
        """Function: As a SOC analysis, I want to perform data enrichment on user agent strings found in web and firewall logs. These entries can provide clues as to potential attempted malicious access and what follow on steps are needed to restrict access.

An integration function is required, sending an artifact string of user agent infromation to a user agent analysis website, returning detailed information as an incident note. An example workflow and rule to execute the function will be included in the packaging."""
        try:
            # Get the function parameters:
            user_agent_string = kwargs.get("user_agent_string")  # text

            log = logging.getLogger(__name__)
            log.info("user_agent_string: %s", user_agent_string)

            url = self.options.get('url', None)
            api_key = self.options.get('api_key', None)
            if not url or not api_key:
                raise ValueError('missing url and/or api_key from [fn_useragentanalysis] app_config')

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")
            data = {"user_agent": user_agent_string}
            headers = {'X-API-KEY': api_key}
            api_response = requests.post(url, headers=headers, json=data)
            if api_response.status_code != 200:
                raise Exception("Unexpected return code of {}".format(api_response.status_code))

            user_agent_analysis = api_response.text

            results = {
                "user_agent_string": user_agent_string,
                "source_api_url": url,
                "user_agent_analysis": user_agent_analysis
            }
            yield StatusMessage("done...")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)


