from typing import TypedDict


class ObjectHandle(TypedDict):
    """Type for ObjectHandle (union of ID or API name)"""

    id: int
    name: str
