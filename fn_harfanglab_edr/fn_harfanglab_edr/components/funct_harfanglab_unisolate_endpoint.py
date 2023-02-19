# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields
from fn_harfanglab_edr.lib.harfanglab_sdk import *


PACKAGE_NAME = "fn_harfanglab_edr"
FN_NAME = "harfanglab_unisolate_endpoint"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'harfanglab_unisolate_endpoint'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):

        """
        Function: Unisolate an endpoint
        Inputs:
            - fn_inputs.harfanglab_agent_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        verify = True
        if self.options.get('verify').lower() == 'false':
            verify = False
        conn = HarfangLabConnector(self.options.get('api_url'), self.options.get('api_key'), verify, self.options.get('http_proxy'), self.options.get('https_proxy'))

        agent_id = fn_inputs.harfanglab_agent_id
        try:
            results = conn.unisolate_endpoint(agent_id)
            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionResult({}, success=False, reason=str(e))

