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
FN_NAME = "harfanglab_run_job"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'harfanglab_run_job'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):

        """
        Function: Run a job on an endpoint
        Inputs:
            - fn_inputs.harfanglab_agent_id
            - fn_inputs.harfanglab_ibm_soar_incident_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["harfanglab_agent_id", "harfanglab_job_name"], fn_inputs)

        verify = True
        if self.options.get('verify').lower() == 'false':
            verify = False
        conn = HarfangLabConnector(self.options.get('api_url'), self.options.get('api_key'), verify, self.options.get('http_proxy'), self.options.get('https_proxy'))

        agent_id = fn_inputs.harfanglab_agent_id
        job_name = fn_inputs.harfanglab_job_name
        job_timeout =  getattr(fn_inputs, "harfanglab_job_timeout", self.options.get('job_timeout', 600))
        incident_id = getattr(fn_inputs, "harfanglab_ibm_soar_incident_id", None)

        try:
            results = conn.run_job(job_name, agent_id, int(job_timeout), 'html')

            if incident_id:
                link = None

                if len(results['output']):
                    if 'download_link' in results['output'][0]:
                        link = results['output'][0]['download_link']

                if link:
                    res = requests.get(link, verify=verify, stream=True)

                    try:
                        filename = f'{FN_NAME}-{job_name}-{results["output"][0].get("hostname",agent_id)}'
                        path_tmp_file, path_tmp_dir = write_to_tmp_file(res.content, filename)

                        password = self.options.get('archive_password', 'infected')

                        pyminizip.compress(path_tmp_file, None, f'{path_tmp_file}.zip', password, 5)

                        with open(f'{path_tmp_file}.zip', "rb") as data_stream:
                            res = write_file_attachment(self.rest_client(), f'{filename}.zip', data_stream, incident_id)

                    except Exception:
                        yield FunctionError()

                    finally:
                        if path_tmp_dir and os.path.isdir(path_tmp_dir):
                            shutil.rmtree(path_tmp_dir)

                yield self.status_message(f"Pushing file to SOAR: '{FN_NAME}'")
                self.resilient_common = ResilientCommon(self.rest_client())
                self.resilient_common.add_csv_file_to_incident_attachments(incident_id, f'{FN_NAME}-{job_name}-{agent_id}.csv', results.get('output'))

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionResult({}, success=False, reason=str(e))
