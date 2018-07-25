# -*- coding: utf-8 -*-
# Copyright IBM Corp. - Confidential Information
"""Function implementation"""

import logging
import time
from fn_mcafee_atd.util.helper import submit_url, check_atd_status, get_atd_report, create_report_file, remove_dir, \
    check_status_code, check_timeout, get_incident_id, check_config, _get_atd_session_headers
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

log = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'mcafee_atd_analyze_file"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        # check_config is handling all of the error checking
        config_opts = check_config(opts)
        self.atd_url = config_opts.get("atd_url")
        self.atd_username = config_opts.get("atd_username")
        self.atd_password = config_opts.get("atd_password")
        self.timeout_mins = config_opts.get("timeout_mins")
        self.polling_interval = config_opts.get("polling_interval")
        self.vm_profile_list = config_opts.get("vm_profile_list")
        self.filePriority = config_opts.get("filePriority")
        self.trust_cert = config_opts.get("trust_cert")

        # Verify can make connection to ATD with given config values
        _get_atd_session_headers(self)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_mcafee_atd", {})

    @function("mcafee_atd_analyze_url")
    def _mcafee_atd_analyze_url_function(self, event, *args, **kwargs):
        """Function: """
        report_file = None
        try:
            inputs = {}
            start_time = time.time()
            yield StatusMessage("Starting...")

            # Get the function parameters:
            incident_id = get_incident_id(**kwargs)
            artifact_id = kwargs.get("artifact_id")  # number
            url_to_analyze = kwargs.get("artifact_value")  # text
            atd_report_type = self.get_select_param(kwargs.get("mcafee_atd_report_type"))  # select
            atd_url_submit_type = self.get_select_param(kwargs.get("mcafee_atd_url_submit_type"))  # select

            log.info("incident_id: %s", incident_id)
            inputs["incident_id"] = incident_id
            if artifact_id is not None:
                log.info("artifact_id: %s", artifact_id)
                inputs["artifact_id"] = artifact_id
            if url_to_analyze is not None:
                yield StatusMessage("URL value: {}".format(url_to_analyze))
                log.info("artifact_value: $s", url_to_analyze)
                inputs["artifact_value"] = url_to_analyze
            if atd_report_type is not None:
                log.info("macfee_atd_report_type: %s", atd_report_type)
                inputs["macfee_atd_report_type"] = atd_report_type
            if atd_url_submit_type is not None:
                log.info("mcafee_atd_url_submit_type: %s", atd_url_submit_type)
                inputs["mcafee_atd_url_submit_type"] = atd_url_submit_type

            submit_type = None
            if atd_url_submit_type == "Analyze URL":
                submit_type = '1'
            elif atd_url_submit_type == "Download and analyze file from URL":
                submit_type = '3'
            else:
                yield FunctionError("atd_url_submit_type is not set correctly.")
            response = submit_url(self, url_to_analyze, submit_type)
            check_status_code(response)
            content = response.json()

            atd_task_id = content["results"][0]["taskId"]
            files_wait = content["filesWait"]
            estimated_time = content["estimatedTime"]
            yield StatusMessage("URL submitted to ATD with taskId: {}".format(str(atd_task_id)))
            yield StatusMessage("Files waiting on: {}".format(files_wait))
            yield StatusMessage("Estimated Time: {} minutes".format(estimated_time))

            timeout_seconds = self.timeout_mins * 60
            start = time.time()
            try:
                while check_atd_status(self, atd_task_id) is False:
                    yield StatusMessage("Analysis on {} is still running".format(url_to_analyze))
                    check_timeout(start, self.polling_interval, timeout_seconds)
            except ValueError:
                yield StatusMessage("ATD analysis probably failed, please check ATD system.")
                raise FunctionError()

            yield StatusMessage("Analysis Completed")
            if atd_report_type == "pdf" or atd_report_type == "html":
                yield StatusMessage("Obtaining {} report".format(atd_report_type))
                report_file = create_report_file(url_to_analyze, atd_report_type)

            results = get_atd_report(self, atd_task_id, atd_report_type, report_file)

            if report_file is not None:
                # Create Resilient Rest client
                resilient_client = self.rest_client()
                resilient_client.post_attachment("/incidents/{}/attachments/".format(incident_id),
                                                  report_file["report_file"], filename=report_file["report_file_name"])
                yield StatusMessage("Report added to incident {} as Attachment".format(str(incident_id)))

            end_time = time.time()
            results["Run Time"] = str(end_time - start_time)
            results["Inputs"] = inputs

            yield StatusMessage("done...")
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            log.info(e)
            yield FunctionError("Failed")
        finally:
            if report_file is not None:
                remove_dir(report_file["tmp_dir"])
