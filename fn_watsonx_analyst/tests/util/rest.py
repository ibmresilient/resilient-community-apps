from unittest.mock import patch
import pytest
from resilient import SimpleClient

from fn_watsonx_analyst.util.rest import RestHelper, RestUrls


sample_data = {
    "data": [
        {
            "id": 2405,
            "playbook": {
                "id": 158,
                "display_name": "kjhkjh",
                "activation_type": "manual",
                "description": None,
                "creator_principal": {
                    "id": 34,
                    "type": "user",
                    "name": "thomas@example.com",
                    "display_name": "Resilient Sysadmin",
                },
                "is_deleted": False,
                "type": "default",
                "version": 71,
            },
            "start_time": 1732120154932,
            "last_activity_time": 1732120155352,
            "last_activity_by": {
                "id": 34,
                "type": "user",
                "name": "thomas@example.com",
                "display_name": "Resilient Sysadmin",
            },
            "elapsed_time": 420,
            "status": "completed",
            "object": {
                "parent": None,
                "object_id": 2414,
                "object_name": "asdf",
                "type_id": 0,
                "type_name": "incident",
            },
            "object_is_deleted": False,
            "incident_id": 2414,
            "detail_msg": None,
        }
    ]
}


def mock_request_post(
    _self,
    uri,
    **kwargs
):
    happy_url: RestUrls = kwargs.get("happy_url", RestUrls.PLAYBOOK_EXECUTIONS)

    if happy_url.value[1].format(**kwargs) == uri:
        return sample_data

    return {
        "success": False,
        "title": None,
        "message": "Internal Server Error",
        "hints": [],
        "error_code": "generic",
    }


class TestRest:
    @pytest.mark.parametrize(
        "input_value",
        [
            RestUrls.PLAYBOOK_EXECUTIONS,
            RestUrls.PLAYBOOK_EXECUTIONS_1,
            RestUrls.PLAYBOOK_EXECUTIONS_2,
        ],
    )
    @patch("resilient.SimpleClient.post", mock_request_post)
    def test_pbx_api_retry(self, input_value):
        client = SimpleClient()
        assert sample_data["data"] == RestHelper().do_request(
            client,
            RestUrls.PLAYBOOK_EXECUTIONS,
            happy_path=input_value,
            workspace_id=0,
            inc_id=0,
        )
