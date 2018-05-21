# -*- coding: utf-8 -*-
# Copyright IBM Corp. - Confidential Information
"""Function implementation"""

import logging
import time
from fn_mcafee_atd.util.helper import submit_url, check_atd_status, get_atd_report, create_report_file, remove_dir, \
    check_status_code, check_timeout, get_incident_id
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

log = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'mcafee_atd_analyze_file"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        try:
            self.options = opts.get("fn_mcafee_atd", {})
            self.atd_url = self.options.get("atd_url")
            self.atd_username = self.options.get("atd_username")
            self.atd_password = self.options.get("atd_password")
            self.timeout_mins = int(self.options.get("timeout"))
            if self.timeout_mins is None:  # Defaults to 30 min
                self.timeout_mins = 30
            self.polling_interval = int(self.options.get("polling_interval"))
            if self.polling_interval is None:  # Defaults to 60 sec
                self.polling_interval = 60
            self.vm_profile_list = self.options.get("vm_profile_list")
            self.filePriority = self.options.get("filePriority")
            if self.filePriority is None:  # Defaults to add_to_q
                self.filePriority = "add_to_q"
            self.trust_cert = self.options.get("trust_cert")
            if self.trust_cert is None:  # Defaults to False
                self.trust_cert = False

            if self.atd_url is None:
                log.error("atd_url is not set. You must set this value to run this function")
                raise ValueError("atd_url is not set. You must set this value to run this function")

            if self.atd_username is None:
                log.error("atd_username is not set. You must set this value to run this function")
                raise ValueError("atd_username is not set. You must set this value to run this function")

            if self.atd_password is None:
                log.error("atd_password is not set. You must set this value to run this function")
                raise ValueError("atd_password is not set. You must set this value to run this function")

            if self.vm_profile_list is None:
                log.error("vmProfileList is not set. You must set this value to run this function")
                raise ValueError("vmProfileList is not set. You must set this value to run this function")

        except AttributeError:
            log.error("There is no [fn_mcafee_atd] section in the config file, "
                      "please set that by running resilient-circuits config -u")
            raise AttributeError("[fn_mcafee_atd] section is not set in the config file")

        # Create Resilient Rest client
        self.resilient_client = self.rest_client()

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_mcafee_atd", {})

    @function("mcafee_atd_analyze_url")
    def _mcafee_atd_analyze_url_function(self, event, *args, **kwargs):
        """Function: """
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
            while check_atd_status(self, atd_task_id) is False:
                check_timeout(start, self.polling_interval, timeout_seconds)

            yield StatusMessage("Analysis Completed")
            if atd_report_type == "pdf" or atd_report_type == "html":
                yield StatusMessage("Obtaining {} report".format(atd_report_type))
                report_file = create_report_file(url_to_analyze, atd_report_type)

            results = get_atd_report(self, atd_task_id, atd_report_type, report_file["report_file"])

            if report_file is not None:
                self.resilient_client.post_attachment("/incidents/{}/attachments/".format(incident_id),
                                                  report_file["report_file"], filename=report_file["report_file_name"])
                yield StatusMessage("Report added to incident {} as Attachment".format(str(incident_id)))

            end_time = time.time()
            results["Run Time"] = str(end_time - start_time)
            results["Inputs"] = inputs

            yield StatusMessage("done...")
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            raise FunctionError()
        finally:
            if report_file is not None:
                remove_dir(report_file["tmp_dir"])
