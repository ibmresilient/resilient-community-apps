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

from fn_watsonx_analyst.types.ai_response import AIResponse
from fn_watsonx_analyst.types.artifact import Artifact
from fn_watsonx_analyst.types.attachment import Attachment
from fn_watsonx_analyst.types.watsonx_responses import WatsonxTextGenerationResponse
from fn_watsonx_analyst.util.ArtifactSummaryGenerator import ArtifactSummaryGenerator
from fn_watsonx_analyst.util.ModelTag import AiResponsePurpose
from fn_watsonx_analyst.util.ContextHelper import ContextHelper
from fn_watsonx_analyst.util.QueryHelper import QueryHelper
from fn_watsonx_analyst.util.chunking.chunking import Chunking
from fn_watsonx_analyst.util.errors import WatsonxApiException
from fn_watsonx_analyst.util.response_helper import ResponseHelper
from fn_watsonx_analyst.util.rest import RestHelper, RestUrls
from fn_watsonx_analyst.util.logging_helper import create_logger, generate_request_id
from fn_watsonx_analyst.util.state_manager import app_state
from fn_watsonx_analyst.util.prompting import Prompting

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

        app_state.get().reset()

        app_state.get().set_model(
            getattr(fn_inputs, "fn_watsonx_analyst_model_id", None)
        )
        app_state.get().opts = self.opts
        app_state.get().res_client = self.rest_client()

        err_msg = "Unable to generate artifact summary. "
        try:
            results = scan_artifact_or_attachment(inc_id, art_id, None)

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
    Abstraction over scanning that can scan either an artifact (file or meta), or attachment.
    """
    obj_name: str = "Unknown"
    try:
        response: WatsonxTextGenerationResponse = None
        data = None

        app_state.get().purpose = AiResponsePurpose.ARTIFACT_SUMMARY
        if art_id:
            data: Artifact
            data = RestHelper().do_request(
                RestUrls.ARTIFACT_DETAILS, inc_id=inc_id, art_id=art_id
            )
            obj_name = data.get("value", "Unknown")
            if data["attachment"]:
                response = ArtifactSummaryGenerator(
                    inc_id,
                    data,
                    None,
                ).generate()
            else:
                # dealing with a metdata artifact
                data: Artifact = data

                state = app_state.get()
                model_id = state.model_id

                # if artifact is metadata only
                context_helper = ContextHelper(inc_id)
                inc_data = context_helper.get_incident_data()

                inc_data, _, art_data, _, _ = context_helper.cleanse_data(
                    inc_data, None, [data], None, None
                )
                inc_data["artifacts"] = art_data
                resolved = context_helper.resolve_type_ids({"incident": inc_data})
                inc_data = resolved["incident"]
                art_data = inc_data["artifacts"][0]
                del inc_data["artifacts"]

                # limit number of tokens used here
                chunker = Chunking()
                art_chunks = chunker.split_data_into_token_chunks(
                    json.dumps(art_data), max_tokens=350
                )
                inc_chunks = chunker.split_data_into_token_chunks(
                    json.dumps(inc_data), max_tokens=350
                )

                # 0.5 and 0.2 share to add to 0.7 of max chunks for model
                art_chunks = chunker.clamped_chunks_for_model(art_chunks, model_id, 0.5)

                inc_query = f"Information related to artifact {obj_name} of type {data['type']}."
                inc_chunks = chunker.retrieve_relevant_chunks_watsonx(
                    inc_query, inc_chunks, None, 0.2
                )

                app_state.get().purpose = AiResponsePurpose.ARITFACT_META_SUMMARY

                prompt = Prompting().build_prompt(
                    query=None,
                    context=None,
                    chunking=None,
                    art_data="".join(art_chunks),
                    inc_data="".join(inc_chunks),
                )

                response = QueryHelper().text_generation(prompt)

        elif att_id:
            data: Attachment
            if not task_id:
                data = RestHelper().do_request(
                    RestUrls.ATTACHMENT_DETAILS,
                    inc_id=inc_id,
                    attach_id=att_id,
                )
            else:
                data = RestHelper().do_request(
                    RestUrls.TASK_ATTACHMENT_DETAILS,
                    inc_id=inc_id,
                    attach_id=att_id,
                    task_id=task_id,
                )
            obj_name = data.get("name", data.get("value", "Unknown"))

            response = ArtifactSummaryGenerator(inc_id, None, data).generate()

        if response:
            # If response is already a fallback dict, skip LLM conversion
            if (
                isinstance(response, dict)
                and "generated_text" in response
                and "results" not in response
            ):
                ai_response = response
            else:
                ai_response = ResponseHelper().text_generation_to_ai_response(response)

            ai_response["generated_text"] = (
                f"{'Artifact' if art_id else 'Attachment'} name: {obj_name}\n\n"
                + ai_response["generated_text"]
            )
            return ai_response

    except Exception:
        log.exception("Failed to generate summary")
        raise
