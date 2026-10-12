from typing import List, Literal, Optional, TypedDict, Union

from .principal import Principal
from .playbook import Playbook

# Note: seems to be for conditions
ActivityType = Literal[
    'function', 'script', 'user_task', 'sub_playbook', 
    'parallel_gateway', 'inclusive_gateway', 'exclusive_gateway', 'flow'
]

ActivityStatus = Union[Literal[
    "complete",
    "error",
    "timeout",
    "canceled",
    "pending" 
], str] # allow to change the word for LLM

ActivityMessageTypes = [
    "info",
    "error",
    "warning"
]

def friendly_name_from_node_type(node_type: ActivityType) -> str:
    return node_type.replace("_", " ").replace("user", "").strip().capitalize()

class PlaybookExecutionObject(TypedDict):
    object_id: int
    object_name: str

class PBExecDetail(TypedDict):
    """Type for Playbook execution detail (playbook progress item)"""

    id: int
    incident_id: int

    detail_msg: str
    status: Literal["completed", "error", "running", "cancelled"]

    elapsed_time: int
    start_time: int

    last_activity_by: Principal
    playbook: Playbook
    object: Optional[PlaybookExecutionObject]

class ActivityRef(TypedDict):
    """Type for PBExec activity node reference"""
    node_id: int
    activity_id: Optional[int]
    node_display_name: Optional[str]

    activity_type: ActivityType

class ActivityMsg(TypedDict):
    """Type for PBExec activity message"""
    text: str
    type: Union[int, str]

    create_date: Union[float, str]

class MiniPlaybookRef(TypedDict):
    """Type for PBExec activity message"""
    id: int
    display_name: str
    subplaybooks: list
    version: int

class PBExecActivity(TypedDict):
    activity_ref: ActivityRef
    messages: List[ActivityMsg]
    playbook_ref: MiniPlaybookRef
    sequence_counter: int
    start_time: Union[float, str]
    status: ActivityStatus

    def __repr__(self) -> str:
        activity_type = self['activity_ref']['activity_type']
        friendly_activity_type = friendly_name_from_node_type(activity_type)
        if activity_type in ['parallel_gateway', 'inclusive_gateway', 'exclusive_gateway', 'flow']:
            return f'{friendly_activity_type} {self["status"]}'
        return f'{friendly_activity_type}: {self["activity_ref"]["node_display_name"]} {self["status"]}'

class PBExecActivities(TypedDict):
    activity_status: List[PBExecActivity]

