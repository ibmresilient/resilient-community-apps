# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, RequestsCommon

CONFIG_DATA_SECTION = 'fn_mxtoolbox'
HEADERS = {'content-type': 'application/json'}
class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_mxtoolbox"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(CONFIG_DATA_SECTION, {})
        self._init()

    def _init(self):
        validate_fields(['api_token','mx_command','mx_argument'], self.options)


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

            # Setup the URL request
            url = '/'.join((self.options['url'], mx_command, "?argument={}&Authorization={}"))
            url = url.format(mx_argument, self.options['api_token'])

            # Make URL request
            rc = RequestsCommon(self.opts, self.options)
            response = rc.execute_call_v2("get", url, headers=HEADERS)

            # Check the results
            if(response.status_code == 200):
                res = response.json()
            else:
                msg = "Some error occurred while retrieving the information from MXToolbox with status code: {}"
                raise ValueError(msg.format(response.status_code))

            # Send results back
            results = {
                "value": res
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
