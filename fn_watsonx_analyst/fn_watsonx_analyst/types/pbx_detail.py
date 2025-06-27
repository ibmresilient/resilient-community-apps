from typing import Literal, TypedDict

from .principal import Principal
from .playbook import Playbook


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
