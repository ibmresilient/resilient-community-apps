from typing import Literal, TypedDict


class TextContent(TypedDict):
    """Type for generic text content for rich text"""

    format: Literal["text", "html", "unkown"]
    content: str
