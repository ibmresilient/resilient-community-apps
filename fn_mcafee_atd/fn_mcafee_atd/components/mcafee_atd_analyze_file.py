# -*- coding: utf-8 -*-
# Copyright IBM Corp. - Confidential Information
"""Function implementation"""

import logging
import time
from fn_mcafee_atd.util.helper import submit_file, check_atd_status, get_atd_report, create_report_file, remove_dir, \
    check_status_code, check_timeout, get_incident_id, check_config, _get_atd_session_headers
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

log = logging.getLogger(__name__)


def _get_file(resilient_client, **kwargs):
    url = ""
    name_url = ""
    name = ""
    if kwargs.get("artifact_id") is not None:
        url = "/incidents/{}/artifacts/{}/contents".format(kwargs["incident_id"], kwargs["artifact_id"])
        name_url = "/incidents/{}/artifacts/{}".format(kwargs["incident_id"], kwargs["artifact_id"])
        log.debug("Downloading artifact attachment")
        name = str(resilient_client.get(name_url)["attachment"]["name"])
    elif kwargs.get("task_id") is not None:
        url = "/tasks/{}/attachments/{}/contents".format(kwargs["task_id"], kwargs["attachment_id"])
        name_url = "/tasks/{}/attachments/{}".format(kwargs["task_id"], kwargs["attachment_id"])
        log.debug("Downloading task attachment")
        name = str(resilient_client.get(name_url)["name"])
    elif kwargs.get("attachment_id") is not None:
        url = "/incidents/{}/attachments/{}/contents".format(kwargs["incident_id"], kwargs["attachment_id"])
        name_url = "/incidents/{}/attachments/{}".format(kwargs["incident_id"], kwargs["attachment_id"])
        log.debug("Downloading incident attachment")
        name = str(resilient_client.get(name_url)["name"])
    else:
        log.error("Inputs not set correctly, can not download file.")
        raise ValueError("Inputs not set correctly")

    f = resilient_client.get_content(url)
    response = {
        "file": f,
        "file_name": name
    }

    return response


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

    @function("mcafee_atd_analyze_file")
    def _mcafee_atd_analyze_file_function(self, event, *args, **kwargs):
        """Function: """
        report_file = None
        try:
            resilient_client = self.rest_client()
            inputs = {}
            start_time = time.time()
            yield StatusMessage("Starting...")

            # Get the function parameters:
            incident_id = get_incident_id(**kwargs)
            artifact_id = kwargs.get("artifact_id")  # number
            attachment_id = kwargs.get("attachment_id")  # number
            task_id = kwargs.get("task_id")  # number
            atd_report_type = self.get_select_param(kwargs.get("mcafee_atd_report_type"))  # select
            inputs["macfee_atd_report_type"] = atd_report_type

            log.info("incident_id: %s", incident_id)
            inputs["incident_id"] = incident_id
            if artifact_id is not None:
                log.info("artifact_id: %s", artifact_id)
                inputs["artifact_id"] = artifact_id
            if attachment_id is not None:
                log.info("attachment_id: %s", attachment_id)
                inputs["attachment_id"] = attachment_id
            if task_id is not None:
                log.info("task_id: %s", task_id)
                inputs["task_id"] = task_id

            f_download = _get_file(resilient_client, **kwargs)
            f = f_download["file"]
            file_name = f_download["file_name"]
            yield StatusMessage("File {} downloaded".format(file_name))

            response = submit_file(self, f, file_name)
            check_status_code(response)
            content = response.json()

            atd_task_id = content["results"][0]["taskId"]
            files_wait = content["filesWait"]
            estimated_time = content["estimatedTime"]
            yield StatusMessage("File uploaded to ATD with taskId: {}".format(str(atd_task_id)))
            yield StatusMessage("Files waiting on: {}".format(files_wait))
            yield StatusMessage("Estimated Time: {} minutes".format(estimated_time))

            timeout_seconds = self.timeout_mins * 60
            start = time.time()
            try:
                while check_atd_status(self, atd_task_id) is False:
                    if artifact_id is not None:
                        yield StatusMessage("Analysis on artifact_id {} is still running".format(artifact_id))
                    else:
                        yield StatusMessage("Analysis on attachment_id {} is still running".format(attachment_id))
                    check_timeout(start, self.polling_interval, timeout_seconds)
            except ValueError:
                yield StatusMessage("ATD analysis probably failed, please check ATD system.")
                raise FunctionError()

            yield StatusMessage("Analysis Completed")
            if atd_report_type == "pdf" or atd_report_type == "html":
                yield StatusMessage("Obtaining {} report".format(atd_report_type))
                report_file = create_report_file(file_name, atd_report_type)

            results = get_atd_report(self, atd_task_id, atd_report_type, report_file)

            if report_file is not None:
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
