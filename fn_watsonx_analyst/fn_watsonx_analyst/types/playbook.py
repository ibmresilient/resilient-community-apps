from typing import Literal, TypedDict

from .text_content import TextContent


class Playbook(TypedDict):
    """Type for the partial playbook used in playbook execution detail"""

    id: int
    display_name: str
    activation_type: Literal["automatic", "manual"]
    description: TextContent
