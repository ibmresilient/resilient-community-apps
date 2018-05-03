# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import requests
import time
from fn_mcafee_atd.util.helper import submit_file, check_atd_status, get_atd_report, create_report_file, remove_file
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
            self.xMode = self.options.get("xMode")
            if self.xMode is None:  # Default to ""
                self.xMode = ""
            self.overrideOS = self.options.get("overrideOS")
            if self.overrideOS is None:  # Default to ""
                self.overrideOS = ""
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

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_mcafee_atd", {})

    def _get_file(self, file_location, **kwargs):
        url = ""
        if file_location == "Artifact":
            url = "/incidents/{}/artifacts/{}/contents".format(kwargs["incident_id"], kwargs["artifact_id"])
        elif file_location == "Incident Attachment":
            url = "/incidents/{}/attachments/{}/contents".format(kwargs["incident_id"], kwargs["attachment_id"])
        elif file_location == "Task Attachment":
            url = "/tasks/{}/attachments/{}/contents".format(kwargs["task_id"], kwargs["attachment_id"])

        resilient_client = self.rest_client()
        response = resilient_client.get_content(url)

        return response

    # def submitFile(self, f, file_name):
    #     session_login = _get_atd_session_headers(self.atd_username, "?6l$$Izh", "https://161.69.151.33:8888")
    #     atd_url = "https://161.69.151.33:8888/php/fileupload.php"
    #     headers = {
    #         "Accept": "application/vnd.ve.v1.0+json",
    #         "VE-SDK-API": session_login
    #     }
    #     postdata = {'data': '{"data":{"xMode":0,"overrideOS":1,"vmProfileList":"11","submitType":"0"},"filePriorityQ":"add_to_q" }'}
    #
    #     files = {'amas_filename': (file_name, f)}
    #
    #     file_upload_req = requests.post(atd_url, postdata, files=files, headers=headers, verify=False)
    #     print(file_upload_req)

    @function("mcafee_atd_analyze_file")
    def _mcafee_atd_analyze_file_function(self, event, *args, **kwargs):
        """Function: """
        try:
            start_time = time.time()
            yield StatusMessage("Starting...")

            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            if not incident_id:
                yield FunctionError("incident_id is required")
            artifact_id = kwargs.get("artifact_id")  # number
            attachment_id = kwargs.get("attachment_id")  # number
            task_id = kwargs.get("task_id")  # number
            artifact_value = kwargs.get("artifact_value")  # text
            attachment_name = kwargs.get("attachment_name")  # text
            mcafee_atd_file_location = self.get_select_param(kwargs.get("mcafee_atd_file_location"))  # select
            atd_report_type = self.get_select_param(kwargs.get("mcafee_atd_report_type"))  # select
            file_name = ""

            log.info("incident_id: %s", incident_id)
            if artifact_id is not None:
                log.info("artifact_id: %s", artifact_id)
            if attachment_id is not None:
                log.info("attachment_id: %s", attachment_id)
            if task_id is not None:
                log.info("task_id: %s", task_id)
            if artifact_value is not None:
                log.info("artifact_name: %s", artifact_value)
                file_name = artifact_value
            if attachment_name is not None:
                log.info("attachment_name: %s", attachment_name)
                file_name = attachment_name
            log.info("mcafee_atd_file_location: %s", mcafee_atd_file_location)

            f = self._get_file(mcafee_atd_file_location, **kwargs)
            yield StatusMessage("File downloaded")

            response = submit_file(self, f, file_name)
            content = response.json()
            # self.submitFile(f, file_name)

            atd_task_id = content["results"][0]["taskId"]
            files_wait = content["filesWait"]
            estimated_time = content["estimatedTime"]
            yield StatusMessage("File uploaded to ATD with taskId: ".format(atd_task_id))
            yield StatusMessage("Files waiting on: {}".format(files_wait))
            yield StatusMessage("Estimated Time: {} minutes".format(estimated_time))

            timeout_seconds = self.timeout_mins * 60
            t = 0
            start = time.time()
            while check_atd_status(self, atd_task_id) is False and t < timeout_seconds:
                time.sleep(self.polling_interval)
                end = time.time()
                t = end - start
            yield StatusMessage("Analysis Completed")
            yield StatusMessage("Obtaining PDF report")

            report_file = create_report_file(file_name)


            pdf_report = get_atd_report(self, atd_task_id, atd_report_type, report_file["report_file"])

            resilient_client = self.rest_client()
            resilient_client.post_attachment("/incidents/{}/attachments/".format(incident_id),
                                             report_file["report_file"], filename=report_file["report_file_name"])

            end_time = time.time()
            results = {
                "value": "xyz"
            }

            yield StatusMessage("done...")
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
        finally:
            remove_file(report_file["report_file"])
