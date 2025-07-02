from typing import TypedDict

from fn_watsonx_analyst.types.object_handle import ObjectHandle
from fn_watsonx_analyst.types.principal import Principal
from fn_watsonx_analyst.types.text_content import TextContent
from .attachment import Attachment

class GlobalArtifact(TypedDict):
    id: int
    value: str
    description: TextContent
    creator: Principal
    type: ObjectHandle
    properties: any


class Artifact(GlobalArtifact):

    inc_id: int
    inc_name: str
    related_incident_count: int

    global_info: GlobalArtifact

    value: str
    attachment: Attachment

    created: int
    last_modified_time: int

    pending_scan_result: any

    findings_count: int
    enrichments_count: int
