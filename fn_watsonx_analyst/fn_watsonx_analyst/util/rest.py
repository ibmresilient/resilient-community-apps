from enum import Enum
import logging
from typing import List

from resilient import SimpleClient

from fn_watsonx_analyst.types.pbx_detail import PBExecDetail

log = logging.getLogger(__name__)

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
    PLAYBOOK_EXECUTIONS_1 = ["POST", "/playbooks/execution/workspace{workspace_id}/{inc_id}/query_paged"] # From SOAR v51.0.4.1
    PLAYBOOK_EXECUTIONS_2 = ["POST", "/playbooks/execution/incident/{inc_id}/query_paged?include_activity_error_msg=false"] # Up to & including SOAR v51.0.2.1


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

        log.info("Making %s request for %s", url.value[0], url.name )

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
                            log.warning("Unknown encoding for artifact contents.")
                            return data
                return res_client.get(url.value[1].format(**kwargs))

            case "POST":
                length = kwargs.get("length", 100)

                match url:
                    case RestUrls.PLAYBOOK_EXECUTIONS | RestUrls.PLAYBOOK_EXECUTIONS_1 | RestUrls.PLAYBOOK_EXECUTIONS_2:
                        options = [RestUrls.PLAYBOOK_EXECUTIONS, RestUrls.PLAYBOOK_EXECUTIONS_1, RestUrls.PLAYBOOK_EXECUTIONS_2]
                        for option in options:
                            try:
                                return res_client.post(
                                    option.value[1].format(**kwargs),
                                    self.__get_paged_query(
                                        option, kwargs.get("inc_id", None), length, kwargs.get("art_name", None)
                                    ), **kwargs
                                )["data"]

                            except Exception:
                                # ignore and try next
                                pass
                        return []

                    case (
                        RestUrls.ARTIFACT_BY_NAME
                        | RestUrls.GET_ARTIFACTS
                        | RestUrls.INC_ART_ID
                    ):
                        try:
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
                        except Exception:
                            raise Exception("Error fetching %s data from SOAR.", url.name)

                return res_client.post(url.value[1].format(**kwargs))
            case "PUT":
                return res_client.put(url.value[1].format(**kwargs), kwargs["body"])
            case "PATCH":
                return res_client.patch(url.value[1].format(**kwargs))
