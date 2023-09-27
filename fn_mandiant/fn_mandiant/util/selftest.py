# -*- coding: utf-8 -*-
# <<PUT YOUR COPYRIGHT TEXT HERE>>
# Generated with resilient-sdk v50.0.108

"""
Function implementation test.
Usage: 
    resilient-circuits selftest -l fn-mandiant
    resilient-circuits selftest --print-env -l fn-mandiant

Return examples:
    return {
        "state": "success",
        "reason": "Successful connection to third party endpoint"
    }

    return {
        "state": "failure",
        "reason": "Failed to connect to third party endpoint"
    }
"""

import logging

from fn_mandiant.lib.mandiant_client import MandiantClient
from resilient_lib.components import requests_common

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    
    app_rc       = requests_common(opts)
    app_configs  = opts.get("fn_mandiant", {})
    mandiant_cli = MandiantClient(app_rc, app_configs)
    
    mandiant_cli.authenticate()
    
    if mandiant_cli.check_authenticated():

        return {
            "state": "unimplemented",
            "reason": "Passed!"}


    return {
        
    }


"""
    
from stix_shifter_utils.modules.base.stix_transmission.base_ping_connector import BasePingConnector
from stix_shifter_utils.utils.error_response import ErrorResponder
from stix_shifter_utils.utils import logger

class PingConnector(BasePingConnector):
    def __init__(self, api_client):
        self.api_client = api_client
        self.logger = logger.set_logger(__name__)
        self.connector = __name__.split('.')[1]

    async def ping_connection(self):
        try:
            response_dict, response_code = await self.api_client.ping_mandiant()

            return_obj = dict()
            if response_code == 200:
                return_obj['success'] = True
                return_obj['code'] = response_code
                return_obj['connector'] = self.connector
            else:
                ErrorResponder.fill_error(return_obj, response_dict, ['message'], connector=self.connector)
                self.logger.error(return_obj)
            return return_obj
        except Exception as err:
            self.logger.error('error when pinging datasource {}:'.format(err))
            raise
    
    

"""