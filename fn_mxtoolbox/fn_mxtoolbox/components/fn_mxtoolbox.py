# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import requests
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

HEADERS = {'content-type': 'application/json'}
class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_mxtoolbox"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_mxtoolbox", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_mxtoolbox", {})

    @function("fn_mxtoolbox")
    def _fn_mxtoolbox_function(self, event, *args, **kwargs):
        """Function allowing MxToolbox customers to query the status of their monitors and run lookups (blacklist, smtp, mx, etc.)"""
        try:
            # Get the function parameters:
            mx_command = self.get_select_param(kwargs.get("mx_command"))  # select, values: "mx", "a", "dns", "spf", "txt", "soa", "ptr", "blacklist", "smtp", "tcp", "http", "https", "ping", "trace"
            mx_argument = kwargs.get("mx_argument")  # text
            mx_param1 = kwargs.get("mx_param1")  # text

            log = logging.getLogger(__name__)
            log.info("mx_command: %s", mx_command)
            log.info("mx_argument: %s", mx_argument)
            log.info("mx_param1: %s", mx_param1)
            
            url = '/'.join((self.options['url'], mx_command, "?argument={}&Authorization={}"))
            url = url.format(mx_argument, self.options['api_token'])
            response = requests.get(url, headers=HEADERS)
            if(response.status_code == 200):
                res = response.json()
            else:
                res = {}
                log.info("Some error occured while retrieving the information from MXToolbox")

            results = {
                "value": res
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()