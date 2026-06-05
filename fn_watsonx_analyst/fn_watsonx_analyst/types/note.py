from typing import List, TypedDict

from fn_watsonx_analyst.types.principal import Principal


class Note(TypedDict):
    """Type for note"""

    id: int
    text: str
    user_name: str
    children: List["Note"]
    create_date: float
    modify_principal: Principal
