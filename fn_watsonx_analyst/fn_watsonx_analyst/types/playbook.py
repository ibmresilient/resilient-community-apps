from enum import IntEnum
from typing import Any, List, Literal, Optional, TypedDict, Union

from .text_content import TextContent

class PlaybookObjectType(IntEnum):
    INCIDENT = 0
    TASK = 1
    NOTE = 2
    MILESTONE = 3
    ARTIFACT = 4
    ATTACHMENT = 5
    DATATABLE = -1

PlaybookActivationType = Literal["automatic", "manual"]
PlaybookLogicType = Union[str, Literal['all', 'any', 'advanced']]

class PlaybookContent(TypedDict):
    content_version: Optional[int]
    xml: str

ConditionMethod = Literal[
    "has_a_value",
    "not_has_a_value",
    "equals",
    "contains",
    "not_contains",
    "not_equals",
    "object_added",
]

class ActivationCondition(TypedDict):
    method: ConditionMethod        
    field_name: str
    value: str
    type: Any
    evaluation_id: Any

class PlaybookActivationConditions(TypedDict):
    conditions: List[ActivationCondition]
    logic_type: PlaybookLogicType
    custom_condition: Optional[str] # ex, '1 OR (2 AND 3)'


class PlaybookManualSettings(TypedDict):
    activation_conditions: PlaybookActivationConditions
    view_items: List[dict]

class PlaybookAutomaticSettings(TypedDict):
    activation_conditions: PlaybookActivationConditions
    activation_type: Union[str, Literal['automatic']]


class Playbook(TypedDict):
    """Type for the playbook used in playbook execution detail"""

    id: int
    display_name: str
    activation_type: PlaybookActivationType
    description: TextContent
    content: Optional[PlaybookContent]
    manual_settings: Optional[PlaybookManualSettings]
    activation_details: Optional[PlaybookAutomaticSettings]
    object_type: Optional[Union[int, PlaybookObjectType]]
