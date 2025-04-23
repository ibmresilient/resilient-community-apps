from typing import Literal, TypedDict

MessageRole = Literal["system", "assistant", "user"]


class MessagePayload(TypedDict):
    """
    Type hints for chat/note message
    """

    role: MessageRole
    content: str
