# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import tempfile
import time
import json
import os
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

from resilient_lib import validate_fields, get_file_attachment, get_file_attachment_name, RequestsCommon, build_incident_url, build_resilient_url

from fn_sndbox_analyzer.util.uploader import ApiUploader

CONFIG_DATA_SECTION = "fn_sndbox_analyzer"
CHECK_REPORTS_SLEEP_TIME = 60


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_sndbox_sandbox_analyzer"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)

        # Get app.config parameters.
        self.opts = opts
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    def _init_sndbox_analyzer(self):
        """ validate required fields for app.config """
        validate_fields(('sndbox_analyzer_url', 'sndbox_api_key',
                         'sndbox_analyzer_report_request_timeout'), self.options)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(CONFIG_DATA_SECTION, {})
        self._init_sndbox_analyzer()

    @function("fn_sndbox_sandbox_analyzer")
    def _fn_sndbox_sandbox_analyzer_function(self, event, *args, **kwargs):
        """Function: for SNDBOX Cloud Analyzer integration"""

        def write_temp_file(data, name=None):
            if name:
                path = os.path.join(tempfile.gettempdir(), name)

            else:
                tf = tempfile.mkstemp()
                path = tf[1]

            fo = open(path, 'wb')
            fo.write(data)
            fo.close()
            return path

        try:
            # Get SNDBOX Sandbox options from app.config file
            SNDBOX_API_KEY = self.options.get("sndbox_api_key")
            SNDBOX_ANALYZER_URL = self.options.get("sndbox_analyzer_url")
            SNDBOX_ANALYSIS_REPORT_REQUEST_TIMEOUT = float(
                self.options.get("sndbox_analyzer_report_request_timeout"))

            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            artifact_id = kwargs.get("artifact_id")  # number
            attachment_id = kwargs.get("attachment_id")  # number
            sndbox_analysis_report_status = kwargs.get("sndbox_analysis_report_status")  # Boolean
            sample_ids = kwargs.get("sample_ids") or []  # List

            if not incident_id:
                raise ValueError("incident_id is required")
            if (not attachment_id) and (not artifact_id):
                raise ValueError("attachment_id or artifact_id is required")

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            log.info("artifact_id: %s", artifact_id)
            log.info("attachment_id: %s", attachment_id)
            log.info("sndbox_analysis_report_status: %s", sndbox_analysis_report_status)
            log.info("sample_ids: %s", sample_ids)

            if not sndbox_analysis_report_status:

                # SNDBOX client and Resilient client
                uploader = ApiUploader(
                    SNDBOX_API_KEY, url=SNDBOX_ANALYZER_URL, proxies=RequestsCommon().get_proxies())
                resilient = self.rest_client()

                # Get attachment entity we are dealing with (either attachment or artifact)
                # then submit it to SNDBOX Analyzer

                sample_file = get_file_attachment(res_client=resilient, incident_id=incident_id,
                                                  artifact_id=artifact_id,
                                                  attachment_id=attachment_id)
                sample_name = get_file_attachment_name(res_client=resilient, incident_id=incident_id,
                                                       artifact_id=artifact_id, attachment_id=attachment_id)

                with open(write_temp_file(sample_file, sample_name), "rb") as handle:
                    sample_id = uploader.submit_samples(handle, sample_name)

                log.info("sample_id: " + str(sample_id))

                # New samples submission might need take as long as hours to finished,
                # need to check the if the analysis have been done.
                time_of_begin_check_report = time.time()
                is_samples_analysis_finished = uploader.check(sample_id)

                while not is_samples_analysis_finished:
                    if time.time() - time_of_begin_check_report > SNDBOX_ANALYSIS_REPORT_REQUEST_TIMEOUT:
                        yield StatusMessage(
                            "Analysis processing still running at Cloud SNDBOX Analyzer, please check it later. ")
                        break
                    yield StatusMessage("Analysis Report not done yet, retrieve every {} seconds".format(CHECK_REPORTS_SLEEP_TIME))
                    time.sleep(CHECK_REPORTS_SLEEP_TIME)
                    is_samples_analysis_finished = uploader.check(sample_id)

                sample_final_result = []
                if is_samples_analysis_finished:
                    sample_final_result.append({"sample_id": sample_id,
                                                "sample_report": uploader.get_sample_report(sample_id)})

                    sndbox_analysis_report_status = True

            results = {
                "sndbox_analysis_report_status": sndbox_analysis_report_status,
                "incident_id": incident_id,
                "artifact_id": artifact_id,
                "attachment_id": attachment_id,
                "sample_final_result": sample_final_result
            }

            log.info("results: " + str(results))
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
