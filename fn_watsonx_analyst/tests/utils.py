import json
from typing import Literal

from fn_watsonx_analyst.util.rest import RestUrls

# uncomment once python version upgraded
# UPDATE_FIELD: Literal[RestUrls.UPDATE_INCIDENT, RestUrls.UPDATE_ARTIFACT, RestUrls.UPDATE_ATTACHMENT]

def were_ai_fields_updated(call_tracker: list, url: RestUrls, obj_id: int, obj_field: str, field: str) -> dict:
    """Returns the object for the given URL hit"""
    update_calls = [(uri, kwargs) for uri, kwargs in call_tracker if uri == url]
    
    if len(update_calls) == 0:
        return None

    _, call_kwargs = update_calls[0]

    if obj_id:
        assert call_kwargs.get(obj_field) == obj_id

    assert "body" in call_kwargs

    body = call_kwargs["body"]
    assert field in body


    summary_data = json.loads(body[field])

    assert all(key in summary_data for key in ["generated_text", "raw_output", "metadata"])
    assert all(key in summary_data.get("metadata") for key in ["model_id", "created_at"])
    return summary_data
