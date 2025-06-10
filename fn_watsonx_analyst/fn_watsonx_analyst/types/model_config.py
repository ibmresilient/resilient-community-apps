from typing import TypedDict


class ModelConfigOption(TypedDict):
    """Option object for each model"""

    model_name: str
    context_length: int
