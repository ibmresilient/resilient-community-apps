from typing import List, TypedDict

from fn_watsonx_analyst.types.artifact import Artifact
from fn_watsonx_analyst.types.incident import Incident
from fn_watsonx_analyst.types.pbx_detail import PBExecDetail


class IncidentFullData(TypedDict):
    """Type to aggregate a full payload"""

    incident: Incident
    pbexec_details: List[PBExecDetail]
    artifacts: List[Artifact]
