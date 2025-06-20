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
from resilient import SimpleClient

from fn_watsonx_analyst.types import Note, MessagePayload
from fn_watsonx_analyst.types.ai_response import AIResponse
from fn_watsonx_analyst.types.artifact import Artifact
from fn_watsonx_analyst.types.attachment import Attachment
from fn_watsonx_analyst.util.ModelTag import AiResponsePurpose
from fn_watsonx_analyst.util.ModelTag import ModelTag
from fn_watsonx_analyst.util.ContextHelper import ContextHelper
from fn_watsonx_analyst.util.QueryHelper import QueryHelper
from fn_watsonx_analyst.util.chunking.chunking import Chunking
from fn_watsonx_analyst.util.errors import (
    WatsonxApiException,
    WatsonxTokenLimitExceededException,
)
from fn_watsonx_analyst.util.util import create_logger, generate_request_id
from fn_watsonx_analyst.util.prompting import Prompting
from fn_watsonx_analyst.util.rest import RestHelper, RestUrls

PACKAGE_NAME = "fn_watsonx_analyst"
FN_NAME = "fn_watsonx_analyst_converse_via_notes"

log = create_logger(__name__)

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'fn_watsonx_analyst_converse_via_notes'"""


    note_map: dict
    res_client: SimpleClient

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
        """
        _ = generate_request_id()

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        results = {}
        note_id = getattr(fn_inputs, "fn_watsonx_analyst_note_id", None)
        inc_id = getattr(fn_inputs, "fn_watsonx_analyst_incident_id", None)
        model_id = getattr(fn_inputs, "fn_watsonx_analyst_model_id", None)

        res_client = self.rest_client()
        chunks: List[str] = None  # used for rolling back and re-picking top chunks

        # the note with the query for watsonx
        target_note: Note = RestHelper().do_request(
            res_client, RestUrls.GET_NOTE, inc_id=inc_id, note_id=note_id
        )
        if not target_note:
            raise ValueError(
                f"note with ID {note_id} could not be found for incident {inc_id}"
            )

        purpose: AiResponsePurpose = None
        notes: List[Note] = RestHelper().do_request(
            res_client, RestUrls.GET_INCIDENT_NOTES, inc_id=inc_id
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
        target_note["text"] = html.unescape(target_note["text"])

        if not note_ancestors or len(note_ancestors) < 1:
            messages.append(QueryHelper().build_message("user", target_note["text"]))
        else:
            for note in note_ancestors:
                role = "assistant"
                if note["modify_principal"]["type"] == "user":
                    role = "user"
                messages.append({"content": note["text"], "role": role})

        chunker = Chunking(res_client, self.opts)

        # search for artifact/attachment names between square brackets
        # use the original text, to separate HTML (from the rich text)
        # and HTML-escaped user text. This allows us to handle names
        # with weird characters like angle brackets.
        matches = self.ART_BRACKETS.finditer(target_note["raw_text"])
        for match in matches:
            obj_name = match.group(1)

            # take out non-HTML text
            obj_name = BeautifulSoup.get_text(
                BeautifulSoup(obj_name, "html.parser"))
            obj_name = html.unescape(obj_name) # re-escape

            log.debug("Found %s", obj_name)
            artifact_results: List[Artifact] = RestHelper().do_request(
                res_client, RestUrls.ARTIFACT_BY_NAME, obj_name=obj_name, inc_id=inc_id
            )

            attachment_results: List[Attachment] = RestHelper().do_request(
                res_client, RestUrls.ATTACHMENT_BY_NAME, obj_name=obj_name, inc_id=inc_id
            )

            if len(artifact_results) + len(attachment_results) == 0:
                log.warning("No artifact or attachment found for %s", obj_name)
                continue  # skip this artifact tag, try another

            contents: Union[str, dict] = None
            for art in artifact_results:
                if art["value"] == obj_name and art["attachment"]:
                    contents = RestHelper().do_request(
                        res_client,
                        RestUrls.ARTIFACT_CONTENTS,
                        inc_id=inc_id,
                        art_id=art["id"],
                    )

            # instead check attachments
            if not contents:
                for attach in attachment_results:
                    if attach["name"] == obj_name:
                        if attach["task_id"]:
                            contents = RestHelper().do_request(
                                res_client,
                                RestUrls.TASK_ATTACHMENT_CONTENTS,
                                task_id=attach["task_id"],
                                attach_id=attach["id"]
                            )
                        else:
                            contents = RestHelper().do_request(
                                res_client,
                                RestUrls.ATTACHMENT_CONTENTS,
                                inc_id=inc_id,
                                attach_id=attach["id"]
                            )
                        break
            try:
                parser_instance = ContextHelper()
                contents = parser_instance.multi_format_parser(data=contents)
                chunks = chunker.split_data_into_token_chunks(contents)
                purpose = AiResponsePurpose.ARTIFACT_CONVERSATION

            except ValueError:
                contents: AIResponse = AIResponse()
                tag = ModelTag(model_id=model_id, purpose=AiResponsePurpose.ARTIFACT_CONVERSATION)
                contents = {
                    "generated_text": "Parsed content is empty or could not be extracted.",
                    "tag": str(tag)
                }
                success = True
                yield FunctionResult(contents)
                return contents

        if not chunks or not purpose:
            purpose = AiResponsePurpose.NOTE_CONVERSATION
            incident_payload = ContextHelper(
                res_client=res_client, inc_id=inc_id, opts=self.opts
            ).build_full_data()
            chunks = chunker.split_json_to_chunks(incident_payload)

        results: dict = {}
        success = False
        msg = ""

        try:
            results = get_chat_response(
                chunker,
                chunks,
                model_id,
                purpose,
                messages,
                target_note["text"],
                self.opts,
                res_client,
            )
            success = True
        except WatsonxTokenLimitExceededException:
            log.warning("Error for first attempt at note conversation. Trying again with lower context threshold.")
            try:
                results = get_chat_response(
                    chunker,
                    chunks,
                    model_id,
                    purpose,
                    messages,
                    target_note["text"],
                    self.opts,
                    res_client,
                    threshold=0.5
                )
                success = True
            except WatsonxApiException as e:
                log.exception("API Error on retry of note conversation. Not attempting again.")
                msg = e.msg
                success = False
        except WatsonxApiException as e:
            log.exception("API error when invoking note conversation")
            msg = e.msg

        # pylint: disable=broad-exception-caught
        except Exception as e:
            log.exception("Unkown error occured when invoking watsonx.ai.")
            msg = str(e)

        if success:
            yield FunctionResult(results)
        else:
            yield FunctionError(msg)


def get_chat_response(
    chunker: Chunking,
    chunks: List[str],
    model_id: str,
    purpose: AiResponsePurpose,
    messages: List[MessagePayload],
    query: str,
    opts: dict,
    res_client: SimpleClient,
    **kwargs,
) -> AIResponse:
    """
    Helper function to build the prompt, and call watsonx.ai. Useful for retrying with different chunking thresholds,
    etc.
    """

    relevant_chunks = chunker.retrieve_relevant_chunks_watsonx(
        query, chunks, model_id, **kwargs
    )
    data = " ".join(relevant_chunks)
    query = query.replace("@watsonx", "")
    try:
        prompt = Prompting(opts).build_prompt(
            purpose,
            model_id,
            query,
            data,
            chunker,
            messages,
            get_relevant_prompts=purpose == AiResponsePurpose.NOTE_CONVERSATION,
        )

        log.info("Attempting text generation")
        output = QueryHelper(res_client, model_id, opts).text_generation(
            prompt, purpose=purpose
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
    else:
        return []  # Target node not found
