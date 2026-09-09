from typing import Literal, NotRequired, Optional, TypedDict

MessageRole = Literal["system", "assistant", "user"]


class MessagePayload(TypedDict):
    """
    Type hints for chat/note message
    """

    role: MessageRole
    content: str
    reasoning_content: NotRequired[str]
