# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.0.974
# pylint: disable=line-too-long

"""AppFunction implementation"""

import json
from typing import Optional, Union

from resilient_circuits import (
    AppFunctionComponent,
    app_function,
    FunctionResult,
    FunctionError,
)
from resilient import SimpleClient

from fn_watsonx_analyst.types.ai_response import AIResponse
from fn_watsonx_analyst.types.artifact import Artifact
from fn_watsonx_analyst.types.attachment import Attachment
from fn_watsonx_analyst.util.ArtifactSummaryGenerator import ArtifactSummaryGenerator
from fn_watsonx_analyst.util.ModelTag import AiResponsePurpose
from fn_watsonx_analyst.util.ModelTag import ModelTag
from fn_watsonx_analyst.util.ContextHelper import ContextHelper, Templates
from fn_watsonx_analyst.util.QueryHelper import QueryHelper
from fn_watsonx_analyst.util.errors import WatsonxApiException
from fn_watsonx_analyst.util.rest import RestHelper, RestUrls
from fn_watsonx_analyst.util.util import create_logger, generate_request_id

PACKAGE_NAME = "fn_watsonx_analyst"
FN_NAME = "fn_watsonx_analyst_scan_artifact"

log = create_logger(__name__)


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'fn_watsonx_analyst_scan_artifact'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Use watsonx to scan an artifact, and assess whether the artifact indicates any malicious activity.
        Designed to work with log files, scripts (e.g. Bash, Python, Lua, Powershell, Perl).
        Inputs:
            -   fn_inputs.fn_watsonx_analyst_artifact_id
            -   fn_inputs.fn_watsonx_analyst_system_prompt
            -   fn_inputs.fn_watsonx_analyst_model_id
            -   fn_inputs.fn_watsonx_analyst_model_id_override
            -   fn_inputs.fn_watsonx_analyst_incident_id
        """
        _ = generate_request_id()

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        inc_id = getattr(fn_inputs, "fn_watsonx_analyst_incident_id", None)
        art_id = getattr(fn_inputs, "fn_watsonx_analyst_artifact_id", None)
        model_id = getattr(fn_inputs, "fn_watsonx_analyst_model_id", None)

        res_client = self.rest_client()

        err_msg = "Unable to generate artifact summary. "
        try:
            results = scan_artifact_or_attachment(
                res_client, inc_id, art_id, None, self.opts, model_id
            )

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

        log.error(err_msg)
        yield FunctionError(err_msg)


def scan_artifact_or_attachment(
    res_client: SimpleClient,
    inc_id: int,
    art_id: Optional[int],
    att_id: Optional[int],
    opts: dict,
    model_id: str,
    task_id: Union[int, None] = None,
) -> AIResponse:
    obj_name: str = "Unknown"
    try:
        response: AIResponse = None
        data = None

        if art_id:
            data: Artifact
            data = RestHelper().do_request(
                res_client, RestUrls.ARTIFACT_DETAILS, inc_id=inc_id, art_id=art_id
            )
            obj_name = data.get("value", "Unknown")
            if data["attachment"]:
                response = ArtifactSummaryGenerator(
                    res_client, inc_id, data, None, model_id, opts
                ).generate()
        elif att_id:
            data: Attachment
            if not task_id:
                data = RestHelper().do_request(
                    res_client,
                    RestUrls.ATTACHMENT_DETAILS,
                    inc_id=inc_id,
                    attach_id=att_id,
                )
            else:
                data = RestHelper().do_request(
                    res_client,
                    RestUrls.TASK_ATTACHMENT_DETAILS,
                    inc_id=inc_id,
                    attach_id=att_id,
                    task_id=task_id,
                )
            obj_name = data.get("name", data.get("value", "Unknown"))

            response = ArtifactSummaryGenerator(
                res_client, inc_id, None, data, model_id, opts
            ).generate()
        if response:
            response["generated_text"] = (
                f"{'Artifact' if art_id else 'Attachment'} name: {obj_name}\n\n"
                + response["generated_text"]
            )
            return response
        data = ""

        prompt = ContextHelper().get_prompt(
            Templates.ASSESS_META_ARTIFACT,
            data=json.dumps(data, indent=2),
            preamble="",
        )
        response = QueryHelper(res_client, model_id, opts).text_generation(
            prompt, purpose=AiResponsePurpose.ARTIFACT_SUMMARY
        )
        return response

    except ValueError:
        tag = ModelTag(model_id=model_id, purpose=AiResponsePurpose.ARTIFACT_SUMMARY)
        msg = f"Parsed content from the {'attachment' if att_id else 'artifact'} '{obj_name}' is empty or could not be extracted."
        response = {
            "generated_text": msg,
            "raw_output": msg,
            "metadata": None,
            "tag": str(tag),
        }
        return response
