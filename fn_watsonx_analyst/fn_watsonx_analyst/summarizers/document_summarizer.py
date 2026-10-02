from typing import List

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
       
        # Pass file contents as format kwarg for user prompt substitution
        self.instruction = chat_prompting.build_chat_messages(
            purpose=AiResponsePurpose.ARTIFACT_SUMMARY,
            query="Summarize this document section.",
            context="",  # Don't use legacy context
            include_relevant_prompts=False,
            file_contents=data,  # Will substitute {file_contents} in user prompt
            content_type=content_type
        )
        
        self.MAX_NEW_TOKENS = 200
        super().__init__("document", self.instruction)
