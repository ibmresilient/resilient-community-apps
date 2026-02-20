# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2026. All Rights Reserved.
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
from fn_watsonx_analyst.types.watsonx_responses import WatsonxChatResponse
from fn_watsonx_analyst.util.response_helper import ResponseHelper
from fn_watsonx_analyst.util.ModelTag import AiResponsePurpose
from fn_watsonx_analyst.util.ContextHelper import ContextHelper
from fn_watsonx_analyst.util.FileParser import FileParser
from fn_watsonx_analyst.util.watsonx_client import WatsonxClient
from fn_watsonx_analyst.util.chat_prompting import ChatPrompting
from fn_watsonx_analyst.util.errors import WatsonxTokenLimitExceededException
from fn_watsonx_analyst.util.logging_helper import create_logger, generate_request_id
from fn_watsonx_analyst.util.rest import RestHelper, RestUrls
from fn_watsonx_analyst.util.state_manager import app_state

PACKAGE_NAME = "fn_watsonx_analyst"
FN_NAME = "fn_watsonx_analyst_converse_via_notes"

log = create_logger(__name__)


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'fn_watsonx_analyst_converse_via_notes'"""

    ART_BRACKETS = re.compile(r"\[(.*)\]")

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

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

        self._initialize_app_state(fn_inputs)

        note_id = getattr(fn_inputs, "fn_watsonx_analyst_note_id", None)
        inc_id = getattr(fn_inputs, "fn_watsonx_analyst_incident_id", None)

        if not note_id or not inc_id:
            raise ValueError("Note ID and Incident ID are required for this function")

        self.context_helper = ContextHelper(inc_id=inc_id)

        # Fetch and process notes
        target_note = self._get_target_note(inc_id, note_id)
        note_ancestors = self._find_note_ancestors(inc_id, note_id)
        messages = self._build_message_history(note_ancestors, target_note)

        # Process context (artifacts/attachments or incident data)
        context, purpose, error_msg = self._process_context(target_note, inc_id)
        
        # If there's an error (e.g., empty artifact/attachment), return immediately
        if error_msg:
            yield FunctionResult(ResponseHelper().error_response(error_msg))
            return
        
        # At this point, context and purpose should not be None
        if context is None or purpose is None:
            yield FunctionError(
                ResponseHelper().error_response("Failed to process context")
            )
            return

        # Get chat response with retry logic
        chat_response = self._get_chat_response_with_retry(
            context, purpose, messages, target_note["text"], inc_id
        )

        if chat_response:
            yield FunctionResult(
                ResponseHelper().text_chat_to_ai_response(chat_response)
            )
        else:
            yield FunctionError(
                ResponseHelper().error_response("No response received from watsonx")
            )

    def _initialize_app_state(self, fn_inputs):
        """Initialize application state with function inputs."""
        app_state.get().reset()
        app_state.get().set_model(
            getattr(fn_inputs, "fn_watsonx_analyst_model_id", "ibm/granite-4-h-small")
        )
        app_state.get().opts = self.opts
        app_state.get().res_client = self.rest_client()
        app_state.get().purpose = AiResponsePurpose.NOTE_CONVERSATION
        app_state.get().data_config = getattr(
            fn_inputs, "fn_watsonx_analyst_data_config", "default"
        )

    def _get_target_note(self, inc_id: int, note_id: int) -> dict:
        """Fetch and process the target note."""
        target_note = RestHelper().do_request(
            RestUrls.GET_NOTE, inc_id=inc_id, note_id=note_id
        )
        if not target_note:
            raise ValueError(
                f"note with ID {note_id} could not be found for incident {inc_id}"
            )

        # Store raw text and extract clean text
        target_note["raw_text"] = target_note["text"]
        target_note["text"] = self._extract_text_from_html(target_note["text"])
        return target_note

    def _find_note_ancestors(self, inc_id: int, note_id: int) -> Optional[List[Note]]:
        """Find the ancestor notes for the target note."""
        notes = RestHelper().do_request(RestUrls.GET_INCIDENT_NOTES, inc_id=inc_id)
        if not notes:
            raise ValueError(f"No notes found for incident {inc_id}")

        for root_note in notes:
            if root_note["id"] != note_id:
                note_ancestors = search_children(root_note, note_id)
                if note_ancestors:
                    return note_ancestors
        return None

    def _build_message_history(
        self, note_ancestors: Optional[List[Note]], target_note: dict
    ) -> List[MessagePayload]:
        """Build message history from note ancestors."""
        messages = []

        if not note_ancestors or len(note_ancestors) < 1:
            messages.append(
                WatsonxClient().build_message("user", target_note["text"])
            )
        else:
            for note in note_ancestors:
                role = (
                    "user"
                    if note["modify_principal"]["type"] == "user"
                    else "assistant"
                )
                messages.append({"content": note["text"], "role": role})

        return messages

    def _process_context(
        self, target_note: dict, inc_id: int
    ) -> tuple[Optional[str], Optional[AiResponsePurpose], Optional[str]]:
        """
        Process context from artifacts/attachments or incident data.
        Returns: (context, purpose, error_message)
        If error_message is not None, the caller should return immediately with the error.
        """
        # Check for artifact/attachment references in square brackets
        if "[" in target_note["raw_text"]:
            context, purpose, error_msg = self._process_artifacts_and_attachments(
                target_note["raw_text"], inc_id
            )
            if error_msg:
                return None, None, error_msg
            if context and purpose:
                return context, purpose, None

        # Default to incident context
        context = self.context_helper.format_incident_for_context()
        return context, AiResponsePurpose.NOTE_CONVERSATION, None

    def _process_artifacts_and_attachments(
        self, raw_text: str, inc_id: int
    ) -> tuple[Optional[str], Optional[AiResponsePurpose], Optional[str]]:
        """
        Extract and process artifacts/attachments referenced in the note.
        Returns: (context, purpose, error_message)
        """
        matches = self.ART_BRACKETS.finditer(raw_text)

        for match in matches:
            obj_name = self._extract_object_name(match.group(1))
            log.debug("Found %s", obj_name)

            # Fetch artifact and attachment results
            artifact_results = RestHelper().do_request(
                RestUrls.ARTIFACT_BY_NAME, obj_name=obj_name, inc_id=inc_id
            )
            attachment_results = RestHelper().do_request(
                RestUrls.ATTACHMENT_BY_NAME, obj_name=obj_name, inc_id=inc_id
            )

            # Ensure results are lists
            artifact_results = artifact_results if isinstance(artifact_results, list) else []
            attachment_results = attachment_results if isinstance(attachment_results, list) else []

            metadata_artifact_results = list(filter(lambda x: x.get("attachment", None) is None, artifact_results))

            if not artifact_results and not attachment_results:
                log.warning("No artifact or attachment found for %s", obj_name)
                continue

            # Get contents from artifacts or attachments
            contents = self._get_artifact_contents(
                artifact_results, obj_name, inc_id
            ) or self._get_attachment_contents(attachment_results, obj_name, inc_id)

            # if a metadata artifact:
            if not contents and metadata_artifact_results:
                return metadata_artifact_results[0], AiResponsePurpose.ARTIFACT_META_CONVERSATION, None

            # If no contents found, continue to next match or fallback
            if not contents:
                continue

            # Parse the file contents
            parsed_content = self._parse_file_contents(contents, obj_name)
            if parsed_content == FileParser.PARSED_CONTENT_EMPTY: # send error message
                return None, None, parsed_content
            
            # Check if parsed content is empty
            if not parsed_content or not parsed_content.strip():
                error_msg = f"The artifact or attachment '{obj_name}' could not be parsed or has no readable content."
                log.warning(error_msg)
                return None, None, error_msg
            
            return parsed_content, AiResponsePurpose.ARTIFACT_CONVERSATION, None
        
        return None, None, None


    def _extract_object_name(self, raw_name: str) -> str:
        """Extract and clean object name from HTML."""
        obj_name = self._extract_text_from_html(raw_name).strip()
        return html.unescape(obj_name)

    def _extract_text_from_html(self, html_text: str) -> str:
        """Extract plain text from HTML."""
        return BeautifulSoup.get_text(BeautifulSoup(html_text, "html.parser"))

    def _get_artifact_contents(
        self, artifact_results: list, obj_name: str, inc_id: int
    ) -> Optional[str | bytes]:
        """Get contents from matching artifact."""
        for art in artifact_results:
            if art.get("value") == obj_name and art.get("attachment") is not None:
                contents: str = RestHelper().do_request(
                    RestUrls.ARTIFACT_CONTENTS, inc_id=inc_id, art_id=art["id"]
                ) # type: ignore
                return contents
        return None

    def _get_attachment_contents(
        self, attachment_results: list, obj_name: str, inc_id: int
    ) -> Optional[str | bytes]:
        """Get contents from matching attachment."""
        for att in attachment_results:
            if att["name"] == obj_name:
                contents: str = ""
                if att.get("task_id") is not None:
                    contents = RestHelper().do_request(
                        RestUrls.TASK_ATTACHMENT_CONTENTS,
                        task_id=att["task_id"],
                        attach_id=att["id"],
                    ) # type: ignore
                else:
                    contents = RestHelper().do_request(
                        RestUrls.ATTACHMENT_CONTENTS,
                        inc_id=inc_id,
                        attach_id=att["id"],
                    ) # type: ignore
                return contents
        return None

    def _parse_file_contents(self, contents: str | bytes, obj_name: str) -> Optional[str]:
        """Parse file contents using FileParser."""
        try:
            parser = FileParser()
            parsed = parser.multi_format_parser(data=contents, object_name=obj_name)

            return parsed.strip()
        except ValueError as e:
            log.error("Error parsing file %s: %s", obj_name, e)
            return None

    def _get_chat_response_with_retry(
        self,
        context: str | dict,
        purpose: AiResponsePurpose,
        messages: List[MessagePayload],
        query: str,
        inc_id: int,
    ) -> Optional[WatsonxChatResponse]:
        """Get chat response with retry logic for token limit exceptions."""
        try:
            return get_chat_response(context, purpose, messages, query, inc_id)
        except WatsonxTokenLimitExceededException:
            log.warning(
                "Token limit exceeded. Retrying with lower context threshold."
            )
            try:
                return get_chat_response(
                    context, purpose, messages, query, inc_id, threshold=0.5
                )
            except Exception as e:
                log.error("Retry failed: %s", e)
                raise
        except Exception as e:
            log.error("Chat response failed: %s", e)
            raise


def get_chat_response(
    context: str | dict,
    purpose: AiResponsePurpose,
    messages: List[MessagePayload],
    query: str,
    inc_id: int,
    **kwargs,
) -> WatsonxChatResponse:
    """
    Helper function to build chat messages and call watsonx.ai chat API.
    Useful for retrying with different chunking thresholds, etc.
    """
    app_state.get().purpose = purpose

    # Clean up query
    query = query.replace("@watsonx", "").strip()

    try:
        # Build chat messages using ChatPrompting system
        chat_prompting = ChatPrompting()
        
        # For artifact conversations, pass file contents as format kwarg for system prompt
        if purpose == AiResponsePurpose.ARTIFACT_CONVERSATION and isinstance(context, str):
            chat_messages = chat_prompting.build_chat_messages(
                purpose=purpose,
                query=query,
                context="",  # Don't use legacy context
                previous_messages=messages[:-1] if len(messages) > 1 else None,
                include_relevant_prompts=True,
                file_contents=context,  # Pass as format kwarg for system prompt substitution
            )
        # For metadata artifact conversations, pass artifact data and incident data
        elif purpose == AiResponsePurpose.ARTIFACT_META_CONVERSATION and isinstance(context, dict):
            # Get incident data for context
            from fn_watsonx_analyst.util.ContextHelper import ContextHelper
            inc_data = ""
            if inc_id:
                context_helper = ContextHelper(inc_id=inc_id)
                inc_data = context_helper.format_incident_for_context()
            
            import json
            chat_messages = chat_prompting.build_chat_messages(
                purpose=purpose,
                query=query,
                context="",  # Don't use legacy context
                previous_messages=messages[:-1] if len(messages) > 1 else None,
                include_relevant_prompts=True,
                art_data=json.dumps(context, indent=2),  # Pass artifact data as format kwarg
                inc_data=inc_data,  # Pass incident data as format kwarg
            )
        else:
            # Fallback to incident qna
            context_str = context if isinstance(context, str) else ""
            chat_messages = chat_prompting.build_chat_messages(
                purpose=purpose,
                query=query,
                context=context_str,
                previous_messages=messages[:-1] if len(messages) > 1 else None,
                include_relevant_prompts=True,
            )

        log.info("Attempting chat interaction with %d messages", len(chat_messages))

        client = WatsonxClient()
        return client.chat(chat_messages)

    except Exception as e:
        log.exception("Error during chat response: %s", e)
        raise


def search_children(root_note: Note, target_id: int) -> List[Note]:
    """
    Depth-first search for the note, matching on note id.
    When found the note, return its parents.
    """

    def dfs(note: Note, target_id: int, path: List[Note]) -> bool:
        """Recursive DFS helper."""
        path.append(note)

        if note["id"] == target_id:
            return True

        for child in note["children"]:
            if dfs(child, target_id, path):
                return True

        # Backtrack if target not found in this branch
        path.pop()
        return False

    path = []
    if dfs(root_note, target_id, path):
        return path
    return []
