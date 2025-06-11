from typing import TypedDict


class AIMetadata(TypedDict):
    """Type for AI response metadata"""

    model_id: str
    stop_reason: str
    created_at: str
    generated_token_count: int
    input_token_count: int
