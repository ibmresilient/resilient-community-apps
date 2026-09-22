from typing import TypedDict, Optional


class Attachment(TypedDict):
    """Type for artifact attachment"""

    id: int
    task_id: Optional[int]
    type: str = "artifact"

    name: str
    uuid: str

    content_type: str

    created: int
    size: int
