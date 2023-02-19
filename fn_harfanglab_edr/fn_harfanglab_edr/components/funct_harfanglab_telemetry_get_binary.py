# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult, FunctionError
from resilient_lib import IntegrationError, validate_fields, write_file_attachment, write_to_tmp_file
from fn_harfanglab_edr.lib.harfanglab_sdk import *
from fn_harfanglab_edr.lib.resilient_common import ResilientCommon
import os
import shutil
import pyminizip

PACKAGE_NAME = "fn_harfanglab_edr"
FN_NAME = "harfanglab_telemetry_get_binary"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'harfanglab_telemetry_get_binary'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: None
        Inputs:
            -   fn_inputs.harfanglab_hash
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        verify = True
        if self.options.get('verify').lower() == 'false':
            verify = False
        conn = HarfangLabConnector(self.options.get('api_url'), self.options.get('api_key'), verify, self.options.get('http_proxy'), self.options.get('https_proxy'))

        validate_fields(["harfanglab_hash", "harfanglab_ibm_soar_incident_id"], fn_inputs)

        hash = fn_inputs.harfanglab_hash
        incident_id = fn_inputs.harfanglab_ibm_soar_incident_id

        try:
            args = {
                'hash': hash
            }

            results = conn.search_telemetry('getBinary', args)

            link = None

            if len(results['output']):
                if 'download_link' in results['output'][0]:
                    link = results['output'][0]['download_link']

            if link:
                res = requests.get(link, verify=verify, stream=True)

                try:
                    path_tmp_file, path_tmp_dir = write_to_tmp_file(res.content, hash)

                    password = self.options.get('archive_password', 'infected')

                    pyminizip.compress(path_tmp_file, None, f'{path_tmp_file}.zip', password, 5)

                    with open(f'{path_tmp_file}.zip', "rb") as data_stream:
                        res = write_file_attachment(self.rest_client(), f'{hash}.zip', data_stream, incident_id)

                except Exception:
                    yield FunctionError()

                finally:
                    if path_tmp_dir and os.path.isdir(path_tmp_dir):
                        shutil.rmtree(path_tmp_dir)


            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionResult({}, success=False, reason=str(e))


