# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2026. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.0.974
# pylint: disable=line-too-long

"""AppFunction implementation"""

import json
from typing import Any, Optional, Union

from fn_watsonx_analyst.types import Attachment
from fn_watsonx_analyst.util import FileParser
from resilient_circuits import (
    AppFunctionComponent,
    app_function,
    FunctionResult,
    FunctionError,
)

from fn_watsonx_analyst.watsonx_app_function import WatsonxAppFunction
from fn_watsonx_analyst.types.ai_response import AIResponse
from fn_watsonx_analyst.util.ArtifactSummaryGenerator import ArtifactSummaryGenerator
from fn_watsonx_analyst.util.ModelTag import AiResponsePurpose
from fn_watsonx_analyst.util.ContextHelper import ContextHelper
from fn_watsonx_analyst.util.chat_prompting import ChatPrompting
from fn_watsonx_analyst.util.chunking.chunking import Chunking
from fn_watsonx_analyst.util.errors import WatsonxApiException
from fn_watsonx_analyst.util.response_helper import ResponseHelper
from fn_watsonx_analyst.util.watsonx_client import WatsonxClient
from fn_watsonx_analyst.util.rest import RestHelper, RestUrls
from fn_watsonx_analyst.util.logging_helper import create_logger, generate_request_id
from fn_watsonx_analyst.util.state_manager import app_state

FN_NAME = "fn_watsonx_analyst_scan_artifact"

log = create_logger(__name__)


class FunctionComponent(WatsonxAppFunction):
    """Component that implements function 'fn_watsonx_analyst_scan_artifact'"""

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
        yield self.setup(fn_inputs, AiResponsePurpose.ARTIFACT_SUMMARY, FN_NAME)

        inc_id = getattr(fn_inputs, "fn_watsonx_analyst_incident_id", None)
        art_id = getattr(fn_inputs, "fn_watsonx_analyst_artifact_id", None)
        err_msg = "Unable to generate artifact summary. "

        try:
            results = scan_artifact_or_attachment(inc_id, art_id, None)

            if self.ai_fields_present():
                log.debug(f"Setting ai insights for artifact ID: {art_id}")
                ai_artifact_insights = json.dumps(results)
                helper = RestHelper()
                artifact = helper.do_request(RestUrls.ARTIFACT_DETAILS, inc_id=inc_id, art_id=art_id)
                artifact["ai_artifact_insights"] = ai_artifact_insights
                helper.do_request(RestUrls.UPDATE_ARTIFACT, inc_id=inc_id, art_id=art_id, body=artifact)
                ResponseHelper.set_insights_added(results)

            yield FunctionResult(results)
            return
        except ValueError as e:
            err_msg = f"{err_msg}{str(e)}"
            log.exception(err_msg)
        except WatsonxApiException as e:
            err_msg += str(e)  # get the string repr
            log.exception("API exception when invoking artifact scan.")
        except Exception as e:
            log.exception(e)
            log.exception("Unkown exception when invoking artifact scan.")
            err_msg += str(e)

        log.error(err_msg)
        yield FunctionError(err_msg)


def scan_artifact_or_attachment(
    inc_id: int,
    art_id: Optional[int],
    att_id: Optional[int],
    task_id: Optional[Union[int, None]] = None,
) -> AIResponse:
    """
    Scan an artifact (file or metadata) or attachment for security threats.
    
    Args:
        inc_id: Incident ID
        art_id: Artifact ID (if scanning artifact)
        att_id: Attachment ID (if scanning attachment)
        task_id: Task ID (if attachment is on a task)
        
    Returns:
        AIResponse with scan results
    """
    try:
        if art_id:
            return _scan_artifact(inc_id, art_id)
        elif att_id:
            return _scan_attachment(inc_id, att_id, task_id)
        else:
            raise ValueError("Either artifact or attachment ID must be provided")
    except Exception:
        log.exception("Failed to generate scan summary")
        raise


def _scan_artifact(inc_id: int, art_id: int) -> AIResponse:
    """Scan an artifact (file or metadata)."""
    artifact: Any = RestHelper().do_request(
        RestUrls.ARTIFACT_DETAILS, inc_id=inc_id, art_id=art_id
    )
    obj_name = artifact.get("value", "Unknown")

    artifact_parse_msg: str | None = None

    # Determine if it's a file artifact or metadata artifact
    if artifact["attachment"]:
        app_state.get().purpose = AiResponsePurpose.ARTIFACT_SUMMARY
        try:
            response = ArtifactSummaryGenerator(inc_id, artifact, None).generate()  # type: ignore
        except ValueError as e:
            artifact_parse_msg = e.msg
            response = _scan_metadata_artifact(inc_id, artifact)
    else:
        response = _scan_metadata_artifact(inc_id, artifact)

    prefix = f"Artifact name: {obj_name}\n"
    if artifact["attachment"] and artifact_parse_msg:
        prefix += artifact_parse_msg + "\n"
    prefix += "\n"

    response["generated_text"] = prefix + response["generated_text"]
    response["raw_output"] = prefix + response["raw_output"]

    return response


def _scan_attachment(inc_id: int, att_id: int, task_id: Optional[int]) -> AIResponse:
    """Scan an attachment."""
    app_state.get().purpose = AiResponsePurpose.ARTIFACT_SUMMARY

    # Fetch attachment details
    attachment: Any
    if task_id:
        attachment = RestHelper().do_request(
            RestUrls.TASK_ATTACHMENT_DETAILS,
            inc_id=inc_id,
            attach_id=att_id,
            task_id=task_id,
        )
    else:
        attachment = RestHelper().do_request(
            RestUrls.ATTACHMENT_DETAILS,
            inc_id=inc_id,
            attach_id=att_id,
        )

    obj_name = attachment.get("name", attachment.get("value", "Unknown"))
    attachment_parse_msg: str | None = None

    try:
        response = ArtifactSummaryGenerator(inc_id, None, attachment).generate()  # type: ignore
    except ValueError as e:
        attachment_parse_msg = e.msg
        response = _scan_metadata_attachment(inc_id, attachment)

    prefix = f"Attachment name: {obj_name}\n\n"
    if attachment_parse_msg:
        prefix += attachment_parse_msg+ "\n"
    prefix += "\n"

    response["generated_text"] = prefix + response['generated_text']
    response["raw_output"] = prefix + response['raw_output']

    return response


def _scan_metadata_artifact(inc_id: int, artifact: Any) -> AIResponse:
    """Scan a metadata artifact (IP, URL, domain, hash, etc.)."""
    # Get incident context
    context_helper = ContextHelper(inc_id)
    inc_data = context_helper.get_incident_data()
    
    # Cleanse and resolve data
    inc_data, _, art_data, _, _ = context_helper.cleanse_data(
        inc_data, None, [artifact], None, None  # type: ignore
    )
    inc_data["artifacts"] = art_data  # type: ignore
    resolved = context_helper.resolve_type_ids({"incident": inc_data})  # type: ignore
    inc_data = resolved["incident"]  # type: ignore
    art_data: dict = inc_data["artifacts"][0]  # type: ignore
    del inc_data["artifacts"]  # type: ignore

    return _scan_metadata_ioc(inc_data, art_data, art_data["value"], art_data["type"])

def _scan_metadata_attachment(inc_id: int, attachment: Attachment) -> AIResponse:
    context_helper = ContextHelper(inc_id)
    inc_data = context_helper.get_incident_data()

    inc_data, _, _, att_data, _ = context_helper.cleanse_data(
        inc_data, None, None, [attachment], None
    )

    att_data: Attachment = att_data[0]

    return _scan_metadata_ioc(inc_data, att_data, att_data["name"], att_data["content_type"])


def _scan_metadata_ioc(inc_data: dict, ioc_data: dict, ioc_name: str, ioc_type: str) -> AIResponse:
    app_state.get().purpose = AiResponsePurpose.ARTIFACT_META_SUMMARY

    # Chunk the data to fit model context limits
    chunker = Chunking()
    model_id = app_state.get().model_id
    
    art_chunks = chunker.split_data_into_token_chunks(
        json.dumps(ioc_data), max_tokens=350
    )
    inc_chunks = chunker.split_data_into_token_chunks(
        json.dumps(inc_data), max_tokens=350
    )

    # Clamp artifact chunks to 50% of model capacity
    art_chunks = chunker.clamped_chunks_for_model(art_chunks, model_id, 0.5)
    
    # Retrieve relevant incident chunks (20% of model capacity)
    inc_query = f"Information related to artifact {ioc_name} of type {ioc_type}"
    inc_chunks = chunker.retrieve_relevant_chunks_watsonx(
        inc_query, inc_chunks, None, 0.2
    )

    # Prepare data for user prompt substitution
    art_data_str = chr(10).join(art_chunks)
    inc_data_str = chr(10).join(inc_chunks)

    # Build chat messages and get response
    chat_prompting = ChatPrompting()
    chat_messages = chat_prompting.build_chat_messages(
        purpose=AiResponsePurpose.ARTIFACT_META_SUMMARY,
        query="",
        previous_messages=None,
        art_data=art_data_str,
        inc_data=inc_data_str
    )

    return ResponseHelper().text_chat_to_ai_response(WatsonxClient().chat(chat_messages))


