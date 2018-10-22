# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import os
import tempfile
import time
from fn_virustotal.lib.resilient_common import validateFields, get_input_entity, get_resilient_client
from fn_virustotal.lib.errors import IntegrationError
from virus_total_apis import PublicApi as VirusTotal
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

RC_NOT_FOUND = 0
RC_READY     = 1
RC_IN_QUEUE  = -2

HTTP_OK = 200
HTTP_RATE_LIMIT = 204

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'virustotal"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_virustotal", {})
        self.resilient = opts.get("resilient", {})
        self.vt = self._init_virustotal()

    def _init_virustotal(self):
        """ validate required fields for app.config """
        validateFields(('api_token', 'polling_interval_sec', 'max_polling_wait_sec'), self.options)
        return VirusTotal(self.options['api_token'], self.options['proxies'])


    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_virustotal", {})
        self.resilient = opts.get("resilient", {})
        self.vt = self._init_virustotal()


    @function("virustotal")
    def _virustotal_function(self, event, *args, **kwargs):
        """Function: perform different scans on the following types:
            ip addresses
            hash - this will attempt to find an existing file report on the hash
            domain
            url - this will attempt to find an existing file report on the url. If none exist, a new scan is queued
            file - this will start a new scan for the file and queue for a report later.
        """
        try:
            validateFields(('incident_id', 'vt_type'), kwargs)  # required

            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            artifact_id = kwargs.get("artifact_id")  # number
            attachment_id = kwargs.get("attachment_id")  # number
            vt_type = kwargs.get("vt_type")  # text
            vt_data = kwargs.get("vt_data")  # text

            self.log = logging.getLogger(__name__)
            self.log.info("incident_id: %s", incident_id)
            self.log.info("artifact_id: %s", artifact_id)
            self.log.info("attachment_id: %s", attachment_id)
            self.log.info("vt_type: %s", vt_type)
            self.log.info("vt_data: %s", vt_data)

            yield StatusMessage("starting...")

            # determine next steps based on the API call to make
            if vt_type.lower() == 'file':
                entity = get_input_entity(get_resilient_client(self.resilient), incident_id, attachment_id, artifact_id)
                # Create a temporary file to write the binary data to.
                with tempfile.NamedTemporaryFile('w+b', delete=False) as temp_file_binary:
                    # Write binary data to a temporary file. Make sure to close the file here...this
                    # code must work on Windows and on Windows the file cannot be opened a second time
                    # While open.  Floss will open the file again to read the data, so close before
                    # calling Floss.
                    temp_file_binary.write(entity["data"])
                    temp_file_binary.close()
                    try:
                        response = self.vt.scan_file(temp_file_binary.name, filename=entity["name"])
                    except Exception as err:
                        raise err
                    finally:
                        os.unlink(temp_file_binary.name)

                file_result = self.return_response(response, self.vt.get_file_report, time.time())

                ## was a sha-256 returned? try an existing report first
                if file_result.get("sha256"):
                    response = self.vt.get_file_report(file_result.get("sha256"))
                    report_result = self.return_response(response, None, time.time())

                    if report_result.get("response_code") and report_result.get("response_code") == 1:
                        result = report_result
                    else:
                        result = file_result

            elif vt_type.lower() == 'url':
                # attempt to see if a report already exists
                response = self.vt.get_url_report(vt_data)
                result = self.return_response(response, None, time.time())

                # check if result is not found, meaning no report exists
                if result['response_code'] == RC_NOT_FOUND:
                    response = self.vt.scan_url(vt_data)
                    result = self.return_response(response, self.vt.get_url_report, time.time())

            elif vt_type.lower() == 'ip':
                response = self.vt.get_ip_report(vt_data)
                result = self.return_response(response, None, time.time())

            elif vt_type.lower() == 'domain':
                response = self.vt.get_domain_report(vt_data)
                result = self.return_response(response, None, time.time())

            elif vt_type.lower() == 'hash':
                response = self.vt.get_file_report(vt_data)
                result = self.return_response(response, None, time.time())

            else:
                raise ValueError("Unknown type field: {}. Check workflow pre-processor script.".format(vt_type))

            results = {
                "scan": result
            }

            self.log.debug("scan: {}".format(results))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()


    def return_response(self, response, callback, start_time):
        """
        parse the response and return the json results if successful
        :param resp:
        :return:
        """
        if response and type(response) is not dict:
            raise IntegrationError('Invalid response: {}'.format(response))

        status = response.get('response_code', -1)

        if status == HTTP_RATE_LIMIT:
            raise IntegrationError('API rate limit exceeded')

        self.log.info(response)

        if status != HTTP_OK:
            raise IntegrationError('Invalid response status: {}'.format(status))

        return self.check_results(response['results'], callback, start_time)

    def check_results(self, results, callback, start_time):
        '''
        continue checking for the scans to complete
        :param results: possibly interim results
        :return: final results of scan
        '''
        code = results.get('response_code', None)
        scan_id = results.get('scan_id', None)
        if code == RC_READY or code == RC_NOT_FOUND:
            return results

        elif code == RC_IN_QUEUE:
            curr_time = time.time()
            if int(curr_time - start_time)/1000 >= int(self.options('max_polling_wait_sec')):
                raise IntegrationError("exceeded max wait time: {}".format(self.options('max_polling_wait_sec')))

            if callback:
                time.sleep(int(self.options['polling_interval_sec']))
                # start again to review results
                response = callback(id)
                results = self.return_response(response, callback, start_time)
            else:
                raise IntegrationError("no callback function specified with response code: {} scan id {}".format(code, scan_id))
        else:
            raise IntegrationError("unexpected response code: {} for scan_id {}".format(code, scan_id))

        self.log.debug(results)
        return results