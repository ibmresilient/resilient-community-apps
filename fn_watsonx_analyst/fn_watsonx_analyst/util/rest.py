from enum import Enum

from resilient import SimpleClient


class RestUrls(Enum):
    """Enum to determine which URL and method to use for each request"""

    GET_ARTIFACTS = ["POST", "/incidents/{inc_id}/artifacts/query_paged"]

    # include trailing '/' to differentiate from above enum value
    ARTIFACT_BY_NAME = ["POST", "/incidents/{inc_id}/artifacts/query_paged/"]
    INC_ART_ID = ["POST", "/artifacts/{art_id}/related_incident_artifacts/query_paged"]
    ARTIFACT_DETAILS = [
        "GET",
        "/incidents/{inc_id}/artifacts/{art_id}?threat_hit_prop_format=objects&syncHits=true",
    ]
    ARTIFACT_CONTENTS = ["GET", "/incidents/{inc_id}/artifacts/{art_id}/contents"]
    UPDATE_ARTIFACT = [
        "PUT",
        "/incidents/{inc_id}/artifacts/{art_id}?threat_hit_prop_format=objects",
    ]
    GET_GLOBAL_ARTIFACT = ["GET", "/artifacts/{art_id}"]

    INCIDENT_DETAILS = ["GET", "/incidents/{inc_id}"]
    TASK_TREE = ["GET", "/incidents/{inc_id}/tasktree"]

    GET_NOTE = ["GET", "/incidents/{inc_id}/comments/{note_id}"]
    GET_INCIDENT_NOTES = ["GET", "/incidents/{inc_id}/comments"]

    PLAYBOOK_EXECUTIONS = [
        "POST",
        "/playbooks/execution/workspace/{workspace_id}/query_paged?include_activity_error_msg=false",
    ]


class RestHelper:
    """Helper class to perform REST requests to SOAR"""

    def __get_paged_query(
        self, url: RestUrls, inc_id: int = None, length: int = 100, art_name: str = None
    ):
        match url:
            case RestUrls.GET_ARTIFACTS:
                return {
                    "sorts": [{"field_name": "last_modified_time", "type": "desc"}],
                    "start": 0,
                    "length": length,
                    "filters": [{"conditions": []}],
                }

            case RestUrls.INC_ART_ID:
                return {
                    "start": 0,
                    "length": length,
                    "sorts": [],
                    "filters": [{"conditions": []}],
                }

            case RestUrls.ARTIFACT_BY_NAME:
                return {
                    "start": 0,
                    "length": 1,
                    "filters": [
                        {
                            "conditions": [
                                {
                                    "method": "contains",
                                    "field_name": "value",
                                    "value": art_name,
                                }
                            ]
                        }
                    ],
                }

            case RestUrls.PLAYBOOK_EXECUTIONS:
                return {
                    "sorts": [
                        {"field_name": "start_time", "type": "desc"},
                        {"field_name": "status", "type": "asc"},
                    ],
                    "filters": [
                        {
                            "conditions": [
                                {
                                    "method": "equals",
                                    "field_name": "incident_id",
                                    "value": inc_id,
                                },
                                {
                                    "method": "equals",
                                    "field_name": "playbook_type",
                                    "value": "default",
                                },
                                {
                                    "method": "not_contains",
                                    "field_name": "playbook_name",
                                    "value": "watsonx",
                                },  # filter out watsonx playbooks
                            ]
                        }
                    ],
                    "start": 0,
                    "length": length,
                }

    def do_request(self, res_client: SimpleClient, url: RestUrls, **kwargs) -> dict:
        """
        Given the RestUrl enum value, perform the operation, using kwargs as query params.
        Kwargs should generally have at least the incident ID.
        """

        match url.value[0]:
            case "GET":
                match url:
                    case RestUrls.ARTIFACT_CONTENTS:
                        res_client.headers["Accept"] = "text/html"
                        data = res_client.get_content(url.value[1].format(**kwargs))
                        res_client.headers["Accept"] = (
                            "application/json"  # reset headers
                        )
                        try:
                            return data.decode("utf-8")
                        except:
                            return data
                return res_client.get(url.value[1].format(**kwargs))

            case "POST":
                match url:
                    case (
                        RestUrls.ARTIFACT_BY_NAME
                        | RestUrls.GET_ARTIFACTS
                        | RestUrls.PLAYBOOK_EXECUTIONS
                        | RestUrls.INC_ART_ID
                    ):
                        length = kwargs.get("length", 100)
                        res = res_client.post(
                            url.value[1].format(**kwargs),
                            self.__get_paged_query(
                                url,
                                kwargs.get("inc_id", None),
                                length,
                                kwargs.get("art_name", None),
                            ),
                        )["data"]
                        return res

                return res_client.post(url.value[1].format(**kwargs))
            case "PUT":
                return res_client.put(url.value[1].format(**kwargs), kwargs["body"])
            case "PATCH":
                return res_client.patch(url.value[1].format(**kwargs))
