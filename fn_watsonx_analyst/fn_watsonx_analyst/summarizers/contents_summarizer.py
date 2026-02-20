from typing import Union, List

from .generic_summarizer import GenericSummarizer

from fn_watsonx_analyst.types import MessagePayload
from fn_watsonx_analyst.util.ModelTag import AiResponsePurpose
from fn_watsonx_analyst.util.chat_prompting import ChatPrompting

class ContentsSummarizer(GenericSummarizer):
    instruction: List[MessagePayload] = []

    MAX_NEW_TOKENS = 350

    def __init__(
        self,
        data: Union[str, bytes],
        content_type: str,
    ):
        # Build chat messages for content summarization
        chat_prompting = ChatPrompting()
        
        # Prepare file contents with optional content type prefix
        file_data = str(data)

        # Pass file contents as format kwarg for user prompt substitution
        self.instruction = chat_prompting.build_chat_messages(
            purpose=AiResponsePurpose.ARTIFACT_SUMMARY,
            query="",  # Empty query for content summary
            context="",  # Don't use legacy context
            include_relevant_prompts=False,
            file_contents=file_data,  # Will substitute {file_contents} in user prompt
            content_type=content_type
        )

        super().__init__("contents", self.instruction)
