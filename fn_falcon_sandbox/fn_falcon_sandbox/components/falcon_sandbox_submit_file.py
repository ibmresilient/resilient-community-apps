# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from requests_toolbelt import MultipartEncoder
import json
import time
from resilient_lib import ResultPayload, RequestsCommon
import fn_falcon_sandbox.util.selftest as selftest
from resilient_circuits import (
    ResilientComponent,
    function,
    handler,
    StatusMessage,
    FunctionResult,
    FunctionError,
)
from fn_falcon_sandbox.util.submit_helper import (
    get_submission_queue_size,
    get_environment_id,
    get_runtime_action_script,
    falcon_sandbox_request_header,
    get_file_attachment_and_metadata,
    write_temp_file,
    remove_temp_files,
    get_submission_queue_size,
    is_correct_naming_convention
)
from fn_falcon_sandbox.util.constants import (
    HA_REST_API_URLS,
    HA_LIST_OF_RUNTIME_PARAMS_SUBMIT_FILE,
    HA_COMPLETED_STATUSES,
)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'falcon_sandbox_submit_file"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_falcon_sandbox", {})
        selftest.selftest_function(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_falcon_sandbox", {})

    @function("falcon_sandbox_submit_file")
    def _falcon_sandbox_submit_file_function(self, event, *args, **kwargs):
        """Function: Submit a file to Falcon Sandbox for analysis."""
        try:
            ## Get the function parameters:
            falcon_sandbox_environment = self.get_select_param(kwargs.get("falcon_sandbox_environment"))  # select, values: "Android Static Analysis", "Linux (Ubuntu 16.04, 64 bit)", "Windows 7 32 bit", "Windows 7 32 bit (HWP Support)", "Windows 7 64 bit"
            falcon_sandbox_action_script = self.get_select_param(kwargs.get("falcon_sandbox_action_script"))  # select, values: "Default analysis", "Heavy Anti-Evasion", "Random desktop files", "Random desktop theme", "Open Internet Explorer", "Default browser analysis"
            falcon_sandbox_no_share_third_party = kwargs.get("falcon_sandbox_no_share_third_party")  # boolean
            falcon_sandbox_allow_community_access = kwargs.get("falcon_sandbox_allow_community_access")  # boolean
            falcon_sandbox_comment = kwargs.get("falcon_sandbox_comment")  # text
            falcon_sandbox_priority = kwargs.get("falcon_sandbox_priority")  # number
            falcon_sandbox_environment_variable = kwargs.get("falcon_sandbox_environment_variable")  # text
            falcon_sandbox_custom_run_time = kwargs.get("falcon_sandbox_custom_run_time")  # text
            falcon_sandbox_submit_name = kwargs.get("falcon_sandbox_submit_name")  # text
            falcon_sandbox_custom_date_time = kwargs.get("falcon_sandbox_custom_date_time")  # text
            falcon_sandbox_document_password = kwargs.get("falcon_sandbox_document_password")  # text
            falcon_sandbox_tor_enabled_analysis = kwargs.get("falcon_sandbox_tor_enabled_analysis")  # boolean
            falcon_sandbox_incident_id = kwargs.get("falcon_sandbox_incident_id")  # number
            falcon_sandbox_task_id = kwargs.get("falcon_sandbox_task_id")  # number
            falcon_sandbox_attachment_id = kwargs.get("falcon_sandbox_attachment_id")  # number
            falcon_sandbox_artifact_id = kwargs.get("falcon_sandbox_artifact_id")  # number

            log = logging.getLogger(__name__)
            log.info("falcon_sandbox_environment: %s", falcon_sandbox_environment)
            log.info("falcon_sandbox_action_script: %s", falcon_sandbox_action_script)
            log.info("falcon_sandbox_no_share_third_party: %s", falcon_sandbox_no_share_third_party)
            log.info("falcon_sandbox_allow_community_access: %s", falcon_sandbox_allow_community_access)
            log.info("falcon_sandbox_comment: %s", falcon_sandbox_comment)
            log.info("falcon_sandbox_priority: %s", falcon_sandbox_priority)
            log.info("falcon_sandbox_environment_variable: %s", falcon_sandbox_environment_variable)
            log.info("falcon_sandbox_custom_run_time: %s", falcon_sandbox_custom_run_time)
            log.info("falcon_sandbox_submit_name: %s", falcon_sandbox_submit_name)
            log.info("falcon_sandbox_custom_date_time: %s", falcon_sandbox_custom_date_time)
            log.info("falcon_sandbox_document_password: %s", falcon_sandbox_document_password)
            log.info("falcon_sandbox_tor_enabled_analysis: %s", falcon_sandbox_tor_enabled_analysis)
            log.info("falcon_sandbox_incident_id: %s", falcon_sandbox_incident_id)
            log.info("falcon_sandbox_task_id: %s", falcon_sandbox_task_id)
            log.info("falcon_sandbox_attachment_id: %s", falcon_sandbox_attachment_id)
            log.info("falcon_sandbox_artifact_id: %s", falcon_sandbox_artifact_id)

            API_KEY = self.options.get("falcon_sandbox_api_key")
            API_HOST = self.options.get("falcon_sandbox_api_host")
            FETCH_REP_TIMEOUT = int(self.options.get("fetch_report_timeout"))
            FETCH_REP_STAT_INTRVL = int(self.options.get("fetch_report_status_interval"))
            
            ## This condition will prevent quering Falcon Sandbox for Status in small intervals
            if FETCH_REP_STAT_INTRVL and FETCH_REP_TIMEOUT:
                if FETCH_REP_STAT_INTRVL < 60 or FETCH_REP_TIMEOUT < 60:
                    raise FunctionError(
                        "Error: [App Config] Minimum value for fetch_report_timeout and fetch_report_status_interval should be 60."
                    )
            else:
                raise FunctionError(
                    "Error: [App Config] fetch_report_timeout and fetch_report_status_interval cannot left empty."
                )
            ## Checking and preparing inputs
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

            falcon_sandbox_environment_id = get_environment_id(
                falcon_sandbox_environment
            )
            falcon_sandbox_action_script = get_runtime_action_script(
                falcon_sandbox_action_script
            )

            ## Making sure all param names are following naming conventions
            for p in kwargs:
                if not is_correct_naming_convention(p):
                    FunctionError(
                        "Input parameter name must start with 'falcon_sandbox_'"
                    )

            client = self.rest_client()
            time_now = str(time.time())
            request_common = RequestsCommon(self.options, kwargs)
            pb = ResultPayload("falcon_sandbox_submit_file", **kwargs)

            ## Get the file for submission
            yield StatusMessage(
                "Getting Attachment from Incident {}".format(falcon_sandbox_incident_id)
            )

            attachment, attachment_metadata = get_file_attachment_and_metadata(
                client,
                falcon_sandbox_incident_id,
                falcon_sandbox_artifact_id,
                falcon_sandbox_task_id,
                falcon_sandbox_attachment_id,
            )

            attachment_path, temp_files = write_temp_file(
                attachment, "attachment_{}".format(time_now)
            )

            attachment_name = attachment_metadata.get("name")
            attachment_type = attachment_metadata["content_type"]

            yield StatusMessage(
                "Environment using for analysis: {}".format(falcon_sandbox_environment)
            )

            ## Prepare for submission
            url, http_method = HA_REST_API_URLS.get("submit_file")
            url = url.format(API_HOST)
            form_data = {
                "file": (attachment_name, open(attachment_path, "rb"), attachment_type)
            }

            for p in HA_LIST_OF_RUNTIME_PARAMS_SUBMIT_FILE:
                k = p.split("falcon_sandbox_")[1]
                v = eval(p)
                form_data[k] = v

            submit_payload = MultipartEncoder(form_data)

            submit_header = falcon_sandbox_request_header(API_KEY)
            submit_header["content-type"] = submit_payload.content_type

            ## Submit file to falcon sandbox
            yield StatusMessage("Submitting...")
            response = request_common.execute_call(
                http_method, url, submit_payload, log=log, headers=submit_header
            )
            job_id = response["job_id"]
            url, http_method = HA_REST_API_URLS.get("get_state")
            url = url.format(API_HOST, job_id)
            yield StatusMessage("Successfully Submitted. \n Job ID: {}".format(job_id))

            ## Get submission queue size
            queue_size = get_submission_queue_size(API_HOST, API_KEY)
            if queue_size is not None:
                yield StatusMessage("Current queue size: {}".format(queue_size))

            ## Get Status of Analysis
            req_header = falcon_sandbox_request_header(API_KEY)
            time_running = 0
            while True:
                scan_status = request_common.execute_call(
                    http_method, url, log=log, headers=req_header
                )
                status = scan_status["state"]
                if status in HA_COMPLETED_STATUSES:
                    yield StatusMessage("Scan Completed with status {}".format(status))
                    break
                # Timeout condition
                if FETCH_REP_TIMEOUT <= (time_running * 60):
                    yield FunctionError(
                        "Function Timeout after {} mins".format(time_running)
                    )
                    break

                time.sleep(FETCH_REP_STAT_INTRVL)
                time_running = time_running + FETCH_REP_STAT_INTRVL/60
                yield StatusMessage(
                    "Scan running as {}. Time Elapsed {} mins".format(
                        status, time_running
                    )
                )

            ## Get scan report summary
            url, http_method = HA_REST_API_URLS.get("get_summary")
            url = url.format(API_HOST, job_id)
            scan_report = request_common.execute_call(
                http_method, url, log=log, headers=req_header
            )

            ## Return result to resilient
            results_payload = pb.done(True, scan_report, status)
            yield FunctionResult(results_payload)

        except Exception:
            yield FunctionError()
        finally:
            remove_temp_files(temp_files)