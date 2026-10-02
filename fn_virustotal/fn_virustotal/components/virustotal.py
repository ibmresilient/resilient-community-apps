# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from os import unlink
from tempfile import NamedTemporaryFile
from time import time
from resilient_lib import IntegrationError, validate_fields
from fn_virustotal.lib.resilient_common import get_input_entity
from fn_virustotal.lib.vt_common import VirusTotalClient
from resilient_circuits import AppFunctionComponent, FunctionResult, app_function

PACKAGE_NAME = "fn_virustotal"
FN_NAME = "virustotal"

class FunctionComponent(AppFunctionComponent):
    """Component that implements Resilient function 'virustotal"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: perform different scans on the following types:
            ip addresses
            hash - this will attempt to find an existing file report on the hash
            domain
            url - this will attempt to find an existing file report on the url. If none exist, a new scan is queued
            file - this will start a new scan for the file and queue for a report later.
        """
        try:
            validate_fields(['incident_id', 'vt_type'], fn_inputs)  # required

            # Create a VirusTotal instance with the API Token and any proxies gathered by RequestsCommon
            vt = VirusTotalClient(self.opts, self.options)

            # Get the function parameters:
            incident_id = getattr(fn_inputs, "incident_id", None)  # number
            artifact_id = getattr(fn_inputs, "artifact_id", None)  # number
            attachment_id = getattr(fn_inputs, "attachment_id", None)  # number
            task_id = getattr(fn_inputs, "task_id", None)  # number
            vt_type = getattr(fn_inputs, "vt_type", None)  # text
            vt_data = getattr(fn_inputs, "vt_data", None)  # text

            self.LOG.info("incident_id: %s", incident_id)
            self.LOG.info("artifact_id: %s", artifact_id)
            self.LOG.info("attachment_id: %s", attachment_id)
            self.LOG.info("task_id: %s", task_id)
            self.LOG.info("vt_type: %s", vt_type)
            self.LOG.info("vt_data: %s", vt_data)

            yield self.status_message(f"Starting App Function: '{FN_NAME}'")

            # determine next steps based on the API call to make
            if vt_type.lower() == 'file':
                entity = get_input_entity(self.rest_client(), incident_id, attachment_id, artifact_id, task_id)
                # Create a temporary file to write the binary data to.
                with NamedTemporaryFile('w+b', delete=False) as temp_file_binary:
                    # Write binary data to a temporary file. Make sure to close the file here...this
                    # code must work on Windows and on Windows the file cannot be opened a second time
                    # While open. 
                    temp_file_binary.write(entity["data"])
                    temp_file_binary.close()
                    try: 
                        scan_response, code = vt.scan_file(temp_file_binary.name, filename=entity["name"])
                    except Exception as err:
                        raise IntegrationError(err)
                    finally:
                        unlink(temp_file_binary.name)

                if code != "success":
                    raise IntegrationError(f"VirusTotal file scan error: {code}")

                file_result, status = vt.wait_for_scan_to_complete(scan_response, time())

                if status != "completed":
                    raise IntegrationError(f"VirusTotal file scan note complete: {status}")

                ## was a sha-256 returned? try an existing report first
                sha256 = vt.get_sha256_from_file_result(file_result)
                response = file_result
                if sha256:
                    report_result, code = vt.get_file_report(sha256)

                    response = file_result
                    if report_result.get("data", None) and code == "success":
                        response = report_result

            elif vt_type.lower() == 'url':
                # attempt to see if a report already exists
                response, code = vt.get_url_report(vt_data)

                # check if result is not found, meaning no report exists
                if code == "NotFoundError":
                    scan_response, code = vt.scan_url(vt_data)

                    if scan_response.get("data", None):
                        response, status = vt.wait_for_scan_to_complete(scan_response, time())
                        if status != "completed":
                            raise IntegrationError(f"VirusTotal URL scan not complete: {status}")

                elif code != "success":
                    raise IntegrationError(f"Error getting VirusTotal URL scan report: {code}")

            elif vt_type.lower() == 'ip':
                response, code = vt.get_ip_report(vt_data)

            elif vt_type.lower() == 'domain':
                response, code  = vt.get_domain_report(vt_data)

            elif vt_type.lower() == 'hash':
                response, code = vt.get_file_report(vt_data)

            else:
                raise ValueError(f"Unknown type field: {vt_type}. Check pre-processor script.")

            results = {
                "scan": response,
                "code": code
            }

            self.LOG.debug(f"scan: {results}")
            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
