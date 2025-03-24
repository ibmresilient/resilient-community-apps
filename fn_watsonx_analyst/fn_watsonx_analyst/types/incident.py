from typing import List, TypedDict

from fn_watsonx_analyst.types.artifact import Artifact

from .pii_info import PIIInfo
from .gdpr_info import GDPRInfo


class Incident(TypedDict):
    """Type for incident"""

    id: int
    name: str
    description: str
    org_id: int

    is_scenario: bool
    inc_training: bool
    confirmed: bool

    resolution_summary: any

    addr: str
    city: str

    incident_type_ids: List[int]

    create_date: int
    end_date: int
    due_data: int

    reporter: str

    crimestatus_id: int
    employee_involved: bool

    workspace: dict

    # probably not needed
    playbooks: List[dict]
    actions: List[dict]
    artifacts: List[Artifact]

    severity_code: int
    score: int
    phase_id: int

    pii: PIIInfo
    gdpr: GDPRInfo

    properties: dict
