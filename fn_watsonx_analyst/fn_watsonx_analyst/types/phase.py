import re
from typing import List, Literal, TypedDict

from fn_watsonx_analyst.types.text_content import TextContent


class Task(TypedDict):
    """Type for incident task"""

    name: str
    inc_id: int

    active: bool
    required: bool

    instructions: TextContent
    status: Literal["O", "C"]


class Phase(TypedDict):
    """Type for incident phase"""

    name: str
    child_tasks: List[Task]
