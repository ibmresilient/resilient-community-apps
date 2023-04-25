# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import os
import tempfile
import time
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import IntegrationError, validate_fields
from fn_virustotal.lib.resilient_common import get_input_entity, get_resilient_client
from fn_virustotal.lib.vt_common import VirusTotalClient


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'virustotal"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get("fn_virustotal", {})
        self.resilient = opts.get("resilient", {})
        self._init_virustotal()

    def _init_virustotal(self):
        """ validate required fields for app.config """
        validate_fields(('api_token', 'polling_interval_sec', 'max_polling_wait_sec'), self.options)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get("fn_virustotal", {})
        self.resilient = opts.get("resilient", {})
        self._init_virustotal()


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

            # Init RequestsCommon with app.config options
            #rc = RequestsCommon(opts=self.opts, function_opts=self.options)

            # Create a VirusTotal instance with the API Token and any proxies gathered by RequestsCommon
            vt = VirusTotalClient(self.opts, self.options)

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
                        response = vt.scan_file(temp_file_binary.name, filename=entity["name"])
                    except Exception as err:
                        raise err
                    finally:
                        os.unlink(temp_file_binary.name)

                file_result, code = self.return_response(response, vt.get_file_report, time.time())

                ## was a sha-256 returned? try an existing report first
                meta = file_result.get("meta", None)
                if meta and meta.get("file_info", None):
                    file_info = meta.get("file_info", None)
                    if file_info and file_info.get("sha256", None):
                        response = vt.get_file_report(file_info.get("sha256"))
                        report_result, code = self.return_response(response, None, time.time())

                        if report_result.get("data", None) and code == "success":
                            result = report_result
                        else:
                            result = file_result

            elif vt_type.lower() == 'url':
                # attempt to see if a report already exists
                response = vt.get_url_report(vt_data)
                result, code = self.return_response(response, None, time.time())

                # check if result is not found, meaning no report exists
                if code == "NotFoundError":
                    response = vt.scan_url(vt_data)
                    result, code = self.return_response(response, vt.get_url_report, time.time())

            elif vt_type.lower() == 'ip':
                response = vt.get_ip_report(vt_data)
                result, code = self.return_response(response, None, time.time())

            elif vt_type.lower() == 'domain':
                response = vt.get_domain_report(vt_data)
                result, code = self.return_response(response, None, time.time())

            elif vt_type.lower() == 'hash':
                response = vt.get_file_report(vt_data)
                result, code  = self.return_response(response, None, time.time())

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
            raise IntegrationError("Invalid response: {}".format(response))
 
        data = response.get("data", None)
        if data:
            return response, "success"

        error_status = response.get("error", None)
        if error_status:
            raise IntegrationError('Unrecognized response from VirusTotal.')

        code = error_status.get("code", None)
        message = error_status.get("message", None)

        self.log.info(response)

        if code != "NotAvailableYet":
            raise IntegrationError('Invalid response code: {} message: {}'.format(code, message))

        return self.check_results(response, callback, start_time)

    def check_results(self, results, callback, start_time):
        '''
        continue checking for the scans to complete
        :param results: possibly interim results
        :return: final results of scan
        '''
        data = results.get('data', None)
        if data:
            self.log.debug(results)
            return results, "success"

        error_status = response.get('error', None)
        code = error_status.get('code', None)
        message = error_status.get('message', None)
        if code == 'NotAvailableYet':
            curr_time = time.time()
            if int(curr_time - start_time)/1000 >= int(self.options.get('max_polling_wait_sec')):
                raise IntegrationError("exceeded max wait time: {}".format(self.options.get('max_polling_wait_sec')))

            if callback:
                time.sleep(int(self.options['polling_interval_sec']))
                # start again to review results
                response = callback(id)
                results, code = self.return_response(response, callback, start_time)
            else:
                raise IntegrationError("no callback function specified with response code: {0} message: {}".format(code, message))
        else:
            raise IntegrationError("unexpected response error: {0} message: {1}".format(code, message))

        self.log.debug(results)
        return results, code