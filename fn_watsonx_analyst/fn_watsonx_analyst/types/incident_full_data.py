from typing import List, TypedDict

from fn_watsonx_analyst.types.artifact import Artifact
from fn_watsonx_analyst.types.attachment import Attachment
from fn_watsonx_analyst.types.incident import Incident
from fn_watsonx_analyst.types.pbx_detail import PBExecDetail

class WrappedIncidentFullData(Incident):
    playbook_executions: List[PBExecDetail]
    artifacts: List[Artifact]
    attachments: List[Attachment]
    tasktree: List[dict]

class IncidentFullData(TypedDict):
    """Type to aggregate a full payload"""

    incident: WrappedIncidentFullData
