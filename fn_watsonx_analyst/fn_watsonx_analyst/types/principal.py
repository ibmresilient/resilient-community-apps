from typing import Literal, TypedDict


class Principal(TypedDict):
    """Type for user/API key principal users"""

    id: int

    name: str
    display_name: str
    type: Literal["user", "api_key"]
