from typing import TypedDict


class Attachment(TypedDict):
    """Type for artifact attachment"""

    id: int
    type: str = "artifact"

    name: str
    uuid: str

    content_type: str

    created: int
    size: int
