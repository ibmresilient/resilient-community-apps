from typing import Literal, TypedDict

from .principal import Principal
from .playbook import Playbook

class PlaybookTarget(TypedDict):
    """Type for Playbook target object"""

    parent: object
    object_id: int
    object_name: str
    type_id: int
    type_name: str

class PBExecDetail(TypedDict):
    """Type for Playbook execution detail (playbook progress item)"""

    id: int
    incident_id: int

    detail_msg: str
    status: Literal["completed", "error", "running", "cancelled"]

    elapsed_time: int
    start_time: int

    last_activated_by: Principal
    playbook: Playbook
    object: PlaybookTarget
