# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult, FunctionError
from resilient_lib import IntegrationError, validate_fields, write_file_attachment, write_to_tmp_file
from fn_harfanglab_edr.lib.harfanglab_sdk import *
from fn_harfanglab_edr.lib.resilient_common import ResilientCommon


PACKAGE_NAME = "fn_harfanglab_edr"
FN_NAME = "harfanglab_telemetry_search_driver_by_hash"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'harfanglab_telemetry_search_driver_by_hash'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Search a driver load in HarfangLab EDR's telemetry per hash
        Inputs:
            - fn_inputs.harfanglab_hash
            - fn_inputs.harfanglab_limit
            - fn_inputs.harfanglab_ibm_soar_incident_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        verify = True
        if self.options.get('verify').lower() == 'false':
            verify = False
        conn = HarfangLabConnector(self.options.get('api_url'), self.options.get(
            'api_key'), verify, self.options.get('http_proxy'), self.options.get('https_proxy'))

        validate_fields(["harfanglab_hash"], fn_inputs)

        hash = fn_inputs.harfanglab_hash
        limit = getattr(fn_inputs, "harfanglab_limit", 10)
        incident_id = getattr(
            fn_inputs, "harfanglab_ibm_soar_incident_id", None)

        try:
            if not limit or limit == '':
                limit = None
            else:
                limit = int(limit)

            args = {
                'hash': hash,
                'limit': limit
            }

            results = conn.search_telemetry('searchDriverByHash', args)

            if incident_id:
                self.resilient_common = ResilientCommon(self.rest_client())
                self.resilient_common.add_csv_file_to_incident_attachments(
                    incident_id, f'{FN_NAME}-{hash}.csv', results.get('output'))

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionResult({}, success=False, reason=str(e))
