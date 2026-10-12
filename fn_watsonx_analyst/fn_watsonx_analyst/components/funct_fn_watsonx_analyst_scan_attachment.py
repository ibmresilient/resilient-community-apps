# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2026. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.2.1096

"""AppFunction implementation"""
import json

from resilient_circuits import (
    app_function,
    FunctionResult,
    FunctionError,
)

from fn_watsonx_analyst.components.funct_fn_watsonx_analyst_scan_artifact import (
    scan_artifact_or_attachment,
)
from fn_watsonx_analyst.types.attachment import Attachment
from fn_watsonx_analyst.util.response_helper import ResponseHelper
from fn_watsonx_analyst.watsonx_app_function import WatsonxAppFunction
from fn_watsonx_analyst.util.ModelTag import AiResponsePurpose
from fn_watsonx_analyst.util.errors import WatsonxApiException
from fn_watsonx_analyst.util.logging_helper import create_logger
from fn_watsonx_analyst.util.rest import RestHelper, RestUrls

FN_NAME = "fn_watsonx_analyst_scan_attachment"

log = create_logger(__name__)


class FunctionComponent(WatsonxAppFunction):
    """Component that implements function 'fn_watsonx_analyst_scan_attachment'"""

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Use watsonx™ to scan an artifact, and assess whether the attachment indicates any malicious activity. Design to work with log files, scripts (e.g. Bash, Python, Lua, Powershell, Perl), but should be able to summarize other textual files.
        Inputs:
            -   fn_inputs.fn_watsonx_analyst_attachment_id
            -   fn_inputs.fn_watsonx_analyst_model_id
            -   fn_inputs.fn_watsonx_analyst_incident_id
            -   fn_watsonx_analyst_task_id
        """

        yield self.setup(fn_inputs, AiResponsePurpose.ARTIFACT_SUMMARY, FN_NAME)

        inc_id = getattr(fn_inputs, "fn_watsonx_analyst_incident_id", None)
        att_id = getattr(fn_inputs, "fn_watsonx_analyst_attachment_id", None)
        task_id = getattr(fn_inputs, "fn_watsonx_analyst_task_id", None)

        err_msg = "Unable to generate attachment summary. "
        try:
            results = scan_artifact_or_attachment(
                inc_id, None, att_id, task_id
            )

            if self.ai_fields_present():
                log.debug(f"Setting ai insights for attachment ID: {att_id}")
                ai_attachment_insights = json.dumps(results)

                helper = RestHelper()
                attachment: Attachment
                inc_attach_id = None
                task_attach_id = None

                if not task_id:
                    attachment = helper.do_request(RestUrls.ATTACHMENT_DETAILS, inc_id=inc_id, attach_id=att_id)
                    inc_attach_id = attachment["id"]
                else:
                    attachment = helper.do_request(RestUrls.TASK_ATTACHMENT_DETAILS, task_id=task_id, attach_id=att_id)
                    task_attach_id = attachment["id"]

                update_body = {
                    "incident_attachment_id": inc_attach_id,
                    "task_attachment_id": task_attach_id,
                    "attach_ai_insights": ai_attachment_insights
                }

                helper.do_request(RestUrls.UPDATE_ATTACHMENT_AI_INSIGHTS, inc_id=inc_id, body=update_body)
                results = ResponseHelper.set_insights_added(results)

            yield FunctionResult(results)
            return
        except ValueError as e:
            err_msg = f"{err_msg}{str(e)}"
            log.exception(err_msg)
        except WatsonxApiException as e:
            err_msg += e.msg
            log.exception("API exception when invoking artifact scan.")
        except Exception as e:
            log.exception("Unkown exception when invoking artifact scan.")
            err_msg += str(e)

        yield FunctionError(err_msg)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")
