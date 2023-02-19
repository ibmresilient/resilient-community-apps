# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields
from fn_harfanglab_edr.lib.harfanglab_sdk import *

PACKAGE_NAME = "fn_harfanglab_edr"
FN_NAME = "harfanglab_add_ioc_to_source"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'harfanglab_add_ioc_to_source'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Add an IOC to a Threat Intelligence source
        Inputs:
            - fn_inputs.harfanglab_ioc_type
            - fn_inputs.harfanglab_ioc_value
            - fn_inputs.harfanglab_ioc_comment
            - fn_inputs.harfanglab_ioc_status
            - fn_inputs.harfanglab_ioc_source_name

        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        verify = True
        if self.options.get('verify').lower() == 'false':
            verify = False
        conn = HarfangLabConnector(self.options.get('api_url'), self.options.get('api_key'), verify, self.options.get('http_proxy'), self.options.get('https_proxy'))

        ioc_type = fn_inputs.harfanglab_ioc_type
        ioc_value = fn_inputs.harfanglab_ioc_value
        ioc_comment = ''
        ioc_status = fn_inputs.harfanglab_ioc_status
        source_name = fn_inputs.harfanglab_source_name

        try:
            ioc_comment = fn_inputs.harfanglab_ioc_comment
        except Exception as e:
            ioc_comment = ''


        try:

            results = conn.add_ioc_to_source(ioc_value, ioc_type, ioc_comment, ioc_status, source_name)

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionResult({}, success=False, reason=str(e))
