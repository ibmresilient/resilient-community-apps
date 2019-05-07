# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from requests_toolbelt import MultipartEncoder
import json
import time
from resilient_lib import ResultPayload
from resilient_circuits import (
    ResilientComponent,
    function,
    handler,
    StatusMessage,
    FunctionResult,
    FunctionError,
)
from fn_falcon_sandbox.util.submit_file_helper import (
    get_submission_queue_size,
    get_attachment_uri,
    get_environment_id,
    get_report_summary,
    get_runtime_action_script,
    falcon_sandbox_request_header,
    get_report_status,
    submit_file_to_falcon_sandbox,
    write_temp_file,
    remove_temp_files,
    LIST_OF_RUNTIME_PARAMS,
)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'falcon_sandbox_submit_file"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_falcon_sandbox", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_falcon_sandbox", {})

    @function("falcon_sandbox_submit_file")
    def _falcon_sandbox_submit_file_function(self, event, *args, **kwargs):
        """Function: Submit a file to Falcon Sandbox for analysis."""
        try:
            ## Get the function parameters:
            falcon_sandbox_environment = self.get_select_param(
                kwargs.get("falcon_sandbox_environment")
            )  # select, values: "Android Static Analysis", "Linux (Ubuntu 16.04, 64 bit)", "Windows 7 32 bit", "Windows 7 32 bit (HWP Support)", "Windows 7 64 bit"
            falcon_sandbox_action_script = self.get_select_param(
                kwargs.get("falcon_sandbox_action_script")
            )  # select, values: "Default analysis", "Heavy Anti-Evasion", "Random desktop files", "Random desktop theme", "Open Internet Explorer", "Default browser analysis"
            falcon_sandbox_no_share_third_party = kwargs.get(
                "falcon_sandbox_no_share_third_party"
            )  # boolean
            falcon_sandbox_allow_community_access = kwargs.get(
                "falcon_sandbox_allow_community_access"
            )  # boolean
            falcon_sandbox_comment = kwargs.get("falcon_sandbox_comment")  # text
            falcon_sandbox_priority = kwargs.get("falcon_sandbox_priority")  # number
            falcon_sandbox_environment_variable = kwargs.get(
                "falcon_sandbox_environment_variable"
            )  # text
            falcon_sandbox_custom_run_time = kwargs.get(
                "falcon_sandbox_custom_run_time"
            )  # text
            falcon_sandbox_submit_name = kwargs.get(
                "falcon_sandbox_submit_name"
            )  # text
            falcon_sandbox_custom_date_time = kwargs.get(
                "falcon_sandbox_custom_date_time"
            )  # text
            falcon_sandbox_offline_analysis = kwargs.get(
                "falcon_sandbox_offline_analysis"
            )  # boolean
            falcon_sandbox_document_password = kwargs.get(
                "falcon_sandbox_document_password"
            )  # text
            falcon_sandbox_tor_enabled_analysis = kwargs.get(
                "falcon_sandbox_tor_enabled_analysis"
            )  # boolean
            falcon_sandbox_incident_id = kwargs.get(
                "falcon_sandbox_incident_id"
            )  # number
            falcon_sandbox_task_id = kwargs.get("falcon_sandbox_task_id")  # number
            falcon_sandbox_attachment_id = kwargs.get(
                "falcon_sandbox_attachment_id"
            )  # number
            falcon_sandbox_artifact_id = kwargs.get(
                "falcon_sandbox_artifact_id"
            )  # number

            log = logging.getLogger(__name__)
            log.info("falcon_sandbox_environment: %s", falcon_sandbox_environment)
            log.info("falcon_sandbox_action_script: %s", falcon_sandbox_action_script)
            log.info(
                "falcon_sandbox_no_share_third_party: %s",
                falcon_sandbox_no_share_third_party,
            )
            log.info(
                "falcon_sandbox_allow_community_access: %s",
                falcon_sandbox_allow_community_access,
            )
            log.info("falcon_sandbox_comment: %s", falcon_sandbox_comment)
            log.info("falcon_sandbox_priority: %s", falcon_sandbox_priority)
            log.info(
                "falcon_sandbox_environment_variable: %s",
                falcon_sandbox_environment_variable,
            )
            log.info(
                "falcon_sandbox_custom_run_time: %s", falcon_sandbox_custom_run_time
            )
            log.info("falcon_sandbox_submit_name: %s", falcon_sandbox_submit_name)
            log.info(
                "falcon_sandbox_custom_date_time: %s", falcon_sandbox_custom_date_time
            )
            log.info(
                "falcon_sandbox_offline_analysis: %s", falcon_sandbox_offline_analysis
            )
            log.info(
                "falcon_sandbox_document_password: %s", falcon_sandbox_document_password
            )
            log.info(
                "falcon_sandbox_tor_enabled_analysis: %s",
                falcon_sandbox_tor_enabled_analysis,
            )
            log.info("falcon_sandbox_incident_id: %s", falcon_sandbox_incident_id)
            log.info("falcon_sandbox_task_id: %s", falcon_sandbox_task_id)
            log.info("falcon_sandbox_attachment_id: %s", falcon_sandbox_attachment_id)
            log.info("falcon_sandbox_artifact_id: %s", falcon_sandbox_artifact_id)

            API_KEY = self.options.get("falcon_sandbox_api_key")
            API_HOST = self.options.get("falcon_sandbox_api_host")
            FETCH_REP_TIMEOUT = self.options.get("fetch_report_timeout")
            falcon_sandbox_environment_id = get_environment_id(
                falcon_sandbox_environment
            )
            falcon_sandbox_action_script = get_runtime_action_script(
                falcon_sandbox_action_script
            )

            ## Checking inputs
            if falcon_sandbox_incident_id is None:
                raise FunctionError(
                    "Error: falcon_sandbox_incident_id must be specified."
                )
            elif (
                falcon_sandbox_attachment_id is None
                and falcon_sandbox_artifact_id is None
            ):
                raise FunctionError(
                    "Error: falcon_sandbox_attachment_id or falcon_sandbox_artifact_id must be specified."
                )
            else:
                yield StatusMessage("> Function inputs OK")

            client = self.rest_client()
            time_now = str(time.time())

            ## Get the file for submission
            yield StatusMessage(
                "Getting Attachment from Incident {}".format(falcon_sandbox_incident_id)
            )
            attachment_uri, attachment_metadata_uri, attachment_src = get_attachment_uri(
                falcon_sandbox_incident_id,
                falcon_sandbox_task_id,
                falcon_sandbox_artifact_id,
                falcon_sandbox_attachment_id,
            )

            try:
                attachment_metadata = client.get(attachment_metadata_uri)
                attachment = client.get_content(attachment_uri)
            except Exception:
                raise FunctionError(
                    "Error fetching Or no attachment found for target {}.".format(
                        attachment_src
                    )
                )

            attachment_path, temp_files = write_temp_file(
                attachment, "attachment_{}".format(time_now)
            )

            ## Since Artifact attachment's metadata json structure is differnt than incident and task
            if attachment_metadata.get("name") is None:
                attachment_metadata = attachment_metadata["attachment"]

            attachment_name = attachment_metadata.get("name")
            attachment_type = attachment_metadata["content_type"]

            yield StatusMessage(
                "Environment using for analysis: {}".format(falcon_sandbox_environment)
            )

            ## Prepare for submission
            form_data = {
                "file": (attachment_name, open(attachment_path, "rb"), attachment_type)
            }
            # Todo - need to discuss about validity of this logic
            for p in LIST_OF_RUNTIME_PARAMS:
                k = p.split("falcon_sandbox_")[1]
                v = eval(p)
                form_data[k] = v

            submit_payload = MultipartEncoder(form_data)

            submit_header = falcon_sandbox_request_header(API_KEY)
            submit_header["content-type"] = submit_payload.content_type

            ## Submit file to falcon sandbox
            yield StatusMessage("Submitting...")
            response = submit_file_to_falcon_sandbox(
                API_HOST, submit_header, submit_payload
            )
            job_id = response["job_id"]
            yield StatusMessage("Successfully Submitted. \n Job ID: {}".format(job_id))

            ## Get Status of Analysis
            has_completed = ["ERROR", "SUCCESS"]
            req_header = falcon_sandbox_request_header(API_KEY)
            completed = False
            time_running = 0
            while not completed:
                scan_status = get_report_status(API_HOST, req_header, job_id)
                status = scan_status["state"]
                if status in has_completed:
                    yield StatusMessage("Scan Completed with status {}".format(status))
                    break
                yield StatusMessage(
                    "Scan running as {} for {} mins".format(status, time_running)
                )
                for i in range(12):
                    time.sleep(5)
                    yield StatusMessage("Time elapsed {} Sec".format((i + 1) * 5))

                time_running = time_running + 1

                # Timeout condition
                if int(FETCH_REP_TIMEOUT) <= (time_running * 60):
                    yield StatusMessage(
                        "Function Timeout after {} mins".format(time_running)
                    )
                    break

            ## Get scan report summary
            scan_report = get_report_summary(API_HOST, req_header, job_id)

            ## Return result to resilient
            pb = ResultPayload("falcon_sandbox_submit_file", **kwargs)
            results_payload = pb.done(True, scan_report, status)
            log.info(results_payload)
            yield FunctionResult(results_payload)

        except Exception:
            yield FunctionError()
        finally:
            remove_temp_files(temp_files)
