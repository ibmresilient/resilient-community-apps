# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.0.974

"""AppFunction implementation"""
import html
import re
from typing import List, Optional, Union

from bs4 import BeautifulSoup
from resilient_circuits import (
    AppFunctionComponent,
    app_function,
    FunctionResult,
    FunctionError,
)

from fn_watsonx_analyst.types import Note, MessagePayload
from fn_watsonx_analyst.types.ai_response import AIResponse
from fn_watsonx_analyst.types.artifact import Artifact
from fn_watsonx_analyst.types.attachment import Attachment
from fn_watsonx_analyst.types.watsonx_responses import WatsonxTextGenerationResponse
from fn_watsonx_analyst.util.response_helper import ResponseHelper
from fn_watsonx_analyst.util.ModelTag import AiResponsePurpose
from fn_watsonx_analyst.util.ContextHelper import ContextHelper
from fn_watsonx_analyst.util.FileParser import FileParser
from fn_watsonx_analyst.util.QueryHelper import QueryHelper
from fn_watsonx_analyst.util.chunking.chunking import Chunking
from fn_watsonx_analyst.util.errors import (
    WatsonxTokenLimitExceededException,
)
from fn_watsonx_analyst.util.logging_helper import create_logger, generate_request_id
from fn_watsonx_analyst.util.prompting import Prompting
from fn_watsonx_analyst.util.rest import RestHelper, RestUrls
from fn_watsonx_analyst.util.state_manager import app_state

PACKAGE_NAME = "fn_watsonx_analyst"
FN_NAME = "fn_watsonx_analyst_converse_via_notes"

log = create_logger(__name__)


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'fn_watsonx_analyst_converse_via_notes'"""

    note_map: dict

    ART_BRACKETS = re.compile(r"\[(.*)\]")
    ART_HTML = re.compile(r">([a-zA-Z0-9._-]+)</.*")

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.note_map = {}

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Allow conversation in an incident's Notes tab. Will take previous notes as context.
        Inputs:
            -   fn_inputs.fn_watsonx_analyst_note_id
            -   fn_inputs.fn_watsonx_analyst_incident_id
            -   fn_inputs.fn_watsonx_analyst_system_prompt
            -   fn_inputs.fn_watsonx_analyst_model_id
            -   fn_inputs.fn_watsonx_analyst_model_id_override
            -   fn_inputs.fn_watsonx_analyst_data_config
        """
        _ = generate_request_id()
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        app_state.get().reset()

        app_state.get().set_model(getattr(fn_inputs, "fn_watsonx_analyst_model_id", None))
        app_state.get().opts = self.opts
        app_state.get().res_client = self.rest_client()

        app_state.get().purpose = AiResponsePurpose.NOTE_CONVERSATION  # placeholder for error messages
        app_state.get().data_config = getattr(fn_inputs, "fn_watsonx_analyst_data_config", None)

        results = {}
        note_id = getattr(fn_inputs, "fn_watsonx_analyst_note_id", None)
        inc_id = getattr(fn_inputs, "fn_watsonx_analyst_incident_id", None)

        chunks: List[str] = None  # used for rolling back and re-picking top chunks

        # the note with the query for watsonx
        target_note: Note = RestHelper().do_request(
            RestUrls.GET_NOTE, inc_id=inc_id, note_id=note_id
        )
        if not target_note:
            raise ValueError(
                f"note with ID {note_id} could not be found for incident {inc_id}"
            )

        purpose: Union[AiResponsePurpose, None] = None
        notes: List[Note] = RestHelper().do_request(
            RestUrls.GET_INCIDENT_NOTES, inc_id=inc_id
        )
        note_ancestors: Optional[List[Note]] = None

        for root_note in notes:
            # root_note is a note with no parents
            if root_note["id"] != note_id:
                note_ancestors = search_children(root_note, note_id)
                if note_ancestors:
                    # we found our note history
                    # target note should be last in the list
                    break

        messages: List[MessagePayload] = []

        # unescape HTML escaped strings (like &, <, >, %, etc.)
        target_note["raw_text"] = target_note["text"]
        target_note["text"] = BeautifulSoup.get_text(BeautifulSoup(target_note["text"], "html.parser"))

        if not note_ancestors or len(note_ancestors) < 1:
            messages.append(QueryHelper().build_message("user", target_note["text"]))
        else:
            for note in note_ancestors:
                role = "assistant"
                if note["modify_principal"]["type"] == "user":
                    role = "user"
                messages.append({"content": note["text"], "role": role})

        chunker = Chunking()

        # search for artifact/attachment names between square brackets
        # use the original text, to separate HTML (from the rich text)
        # and HTML-escaped user text. This allows us to handle names
        # with weird characters like angle brackets.
        if "[" in target_note["raw_text"]:
            err_response = FunctionResult(
                ResponseHelper().error_response("Parsed content is empty or could not be extracted."))

            matches = self.ART_BRACKETS.finditer(target_note["raw_text"])
            for match in matches:
                obj_name = match.group(1)

                # take out non-HTML text
                obj_name = BeautifulSoup.get_text(BeautifulSoup(obj_name, "html.parser")).strip()
                obj_name = html.unescape(obj_name)  # re-escape

                log.debug("Found %s", obj_name)
                artifact_results: List[Artifact] = RestHelper().do_request(
                    RestUrls.ARTIFACT_BY_NAME, obj_name=obj_name, inc_id=inc_id
                )

                attachment_results: List[Attachment] = RestHelper().do_request(
                    RestUrls.ATTACHMENT_BY_NAME, obj_name=obj_name, inc_id=inc_id
                )
                if len(artifact_results) + len(attachment_results) == 0:
                    log.warning("No artifact or attachment found for %s", obj_name)
                    continue  # skip this artifact tag, try another

                contents: Union[dict, str] = None
                for art in artifact_results:
                    if art.get("value") == obj_name and art.get("attachment") is not None:
                        contents = RestHelper().do_request(
                            RestUrls.ARTIFACT_CONTENTS,
                            inc_id=inc_id, art_id=art["id"]
                        )
                        if not contents or not contents.strip():
                            yield err_response
                            return
                        else:
                            break

                if not contents:
                    for att in attachment_results:
                        if att["name"] == obj_name:
                            if att.get("task_id", None) is not None:
                                contents = RestHelper().do_request(
                                    RestUrls.TASK_ATTACHMENT_CONTENTS,
                                    task_id=att["task_id"], attach_id=att["id"]
                                )
                            else:
                                contents = RestHelper().do_request(
                                    RestUrls.ATTACHMENT_CONTENTS,
                                    inc_id=inc_id, attach_id=att["id"]
                                )
                            if not contents or not contents.strip():
                                yield err_response
                                return

                if contents:
                    try:
                        parser_instance = FileParser()
                        contents = parser_instance.multi_format_parser(
                            data=contents, object_name=obj_name
                        )
                        contents = contents.strip()
                        chunks = chunker.split_data_into_token_chunks(contents)
                        purpose = AiResponsePurpose.ARTIFACT_CONVERSATION

                    except ValueError:
                        yield err_response
                        return

        if not purpose:
            purpose = AiResponsePurpose.NOTE_CONVERSATION
            incident_payload = ContextHelper(
                inc_id=inc_id
            ).build_full_data()
            chunks = chunker.split_json_to_chunks(incident_payload)

        results: AIResponse = None
        success = False
        err_msg = "Unknown error, please review logs for further information."

        try:
            results = get_chat_response(
                chunker,
                chunks,
                purpose,
                messages,
                target_note["text"],
            )
            success = True
        except WatsonxTokenLimitExceededException:
            try:
                log.warning(
                    "Error for first attempt at note conversation. Trying again with lower context threshold."
                )
                results = get_chat_response(
                    chunker,
                    chunks,
                    purpose,
                    messages,
                    target_note["text"],
                    threshold=0.5
                )
                success = True
            except Exception as e:
                err_msg = str(e)
        except Exception as e:
            err_msg = str(e)
        finally:
            if not success:
                yield FunctionError(ResponseHelper().error_response(err_msg))
            else:
                yield FunctionResult(ResponseHelper().text_generation_to_ai_response(results))


def get_chat_response(
    chunker: Chunking,
    chunks: List[str],
    purpose: AiResponsePurpose,
    messages: List[MessagePayload],
    query: str,
    **kwargs,
) -> WatsonxTextGenerationResponse:
    """
    Helper function to build the prompt, and call watsonx.ai. Useful for retrying
    with different chunking thresholds, etc.
    """
    app_state.get().purpose = purpose

    relevant_chunks = chunker.retrieve_relevant_chunks_watsonx(
        query, chunks, **kwargs
    )
    data = " ".join(relevant_chunks)
    query = query.replace("@watsonx", "")
    try:
        prompt = Prompting().build_prompt(
            query,
            data,
            messages,
            get_relevant_prompts=True
        )

        log.info("Attempting text generation")
        output = QueryHelper().text_generation(
            prompt
        )
        return output

    except Exception as e:
        raise e

def search_children(root_note: Note, target_id: int) -> List[Note]:
    """
    Depth-first search for the note, matching on note id.
    When found the note, return its parents.
    """

    def dfs(note: Note, target_id: int, path):
        # Add the current node to the path (ancestors)
        path.append(note)

        # If we found the node, return True
        if note["id"] == target_id:
            return True

        for child in note["children"]:
            if dfs(child, target_id, path):
                return True
        # If the target note is not found in this branch, backtrack by removing the node from the path
        path.pop()
        return False

    path = []
    if dfs(root_note, target_id, path):
        return path  # This will return the ancestors + the target node itself
    return []  # Target node not found
