from typing import List

from resilient import SimpleClient

from fn_watsonx_analyst.summarizers.generic_summarizer import GenericSummarizer
from fn_watsonx_analyst.types import MessagePayload
from fn_watsonx_analyst.util.ModelTag import AiResponsePurpose
from fn_watsonx_analyst.util.chat_prompting import ChatPrompting


class DocumentSummarizer(GenericSummarizer):
    instruction: List[MessagePayload] = []

    def __init__(
        self,
        data: str,
        content_type: str,
    ):
        # Build chat messages for document summarization
        chat_prompting = ChatPrompting()
        
        # Prepare file contents with optional content type prefix
        file_data = data
        if content_type:
            file_data = f"Content Type: {content_type}\n\n{file_data}"
        
        # Pass file contents as format kwarg for user prompt substitution
        self.instruction = chat_prompting.build_chat_messages(
            purpose=AiResponsePurpose.ARTIFACT_SUMMARY,
            query="Summarize this document section.",
            context="",  # Don't use legacy context
            include_relevant_prompts=False,
            file_contents=file_data  # Will substitute {file_contents} in user prompt
        )
        
        self.MAX_NEW_TOKENS = 200
        super().__init__("document", self.instruction)
