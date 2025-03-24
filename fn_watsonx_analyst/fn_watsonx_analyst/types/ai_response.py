from typing import TypedDict

from fn_watsonx_analyst.types.ai_metadata import AIMetadata


class AIResponse(TypedDict):
    """Type for an AI response object"""

    generated_text: str
    raw_output: str
    tag: str
    metadata: AIMetadata
