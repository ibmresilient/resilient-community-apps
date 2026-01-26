from typing import TypedDict


class AIMetadata(TypedDict):
    """Type for AI response metadata"""

    model_id: str
    estimated_cost: float

    created_at: str
    stop_reason: str
    input_tokens: int
    output_tokens: int

