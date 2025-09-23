from enum import Enum

from fn_watsonx_analyst.util.logging_helper import create_logger
from fn_watsonx_analyst.util.state_manager import app_state

# pylint: disable=line-too-long

log = create_logger(__name__)


class RestUrls(Enum):
    """Enum to determine which URL and method to use for each request"""

    GET_ARTIFACTS = [
        "POST",
        "/incidents/{inc_id}/artifacts/query_paged?threat_hit_prop_format=objects&include_related_incident_count=true&handle_format=objects",
    ]

    # include trailing '/' to differentiate from above enum value
    ARTIFACT_BY_NAME = [
        "POST",
        "/incidents/{inc_id}/artifacts/query_paged/?threat_hit_prop_format=objects&include_related_incident_count=true&handle_format=objects",
    ]
    INC_ART_ID = [
        "POST",
        "/artifacts/{art_id}/related_incident_artifacts/query_paged?threat_hit_prop_format=objects&include_related_incident_count=true&handle_format=objects",
    ]
    ARTIFACT_DETAILS = [
        "GET",
        "/incidents/{inc_id}/artifacts/{art_id}?threat_hit_prop_format=objects&include_related_incident_count=true&handle_format=objects",
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
    PLAYBOOK_EXECUTIONS_1 = [
        "POST",
        "/playbooks/execution/workspace/{workspace_id}/{inc_id}/query_paged",
    ]  # From SOAR v51.0.4.1
    PLAYBOOK_EXECUTIONS_2 = [
        "POST",
        "/playbooks/execution/incident/{inc_id}/query_paged?include_activity_error_msg=false",
    ]  # Up to & including SOAR v51.0.2.1
    PLAYBOOK_EXECUTIONS_3 = [
        "POST",
        "/playbooks/execution/query_paged?include_activity_error_msg=false",
    ]

    ATTACHMENT_BY_NAME = [
        "POST",
        "/incidents/{inc_id}/attachments/query?exclude_mismatch=false&include_tasks=true",
    ]

    ATTACHMENT_DETAILS = ["GET", "/incidents/{inc_id}/attachments/{attach_id}"]
    ATTACHMENT_CONTENTS = [
        "GET",
        "/incidents/{inc_id}/attachments/{attach_id}/contents",
    ]

    TASK_ATTACHMENT_DETAILS = ["GET", "/tasks/{task_id}/attachments/{attach_id}"]
    TASK_ATTACHMENT_CONTENTS = [
        "GET",
        "/tasks/{task_id}/attachments/{attach_id}/contents",
    ]

    GET_ATTACHMENTS = ["GET", "/incidents/{inc_id}/attachments?exclude_mismatch=true"]
    GET_TYPES = ["GET", "/types/{type}/fields"]


class RestHelper:
    """Helper class to perform REST requests to SOAR"""

    playbook_exec_group = [
        RestUrls.PLAYBOOK_EXECUTIONS,
        RestUrls.PLAYBOOK_EXECUTIONS_1,
        RestUrls.PLAYBOOK_EXECUTIONS_2,
        RestUrls.PLAYBOOK_EXECUTIONS_3,
    ]

    def __get_paged_query(
        self, url: RestUrls, inc_id: int = None, length: int = 100, obj_name: str = None
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
                                    "method": "equals",
                                    "field_name": "value",
                                    "value": obj_name,
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

            case RestUrls.ATTACHMENT_BY_NAME:
                return {
                    "conditions": [
                        {"field_name": "name", "method": "equals", "value": obj_name}
                    ]
                }

            case RestUrls.GET_ATTACHMENTS:
                return {
                    "sorts": [{"field_name": "last_modified_time", "type": "desc"}],
                    "start": 0,
                    "length": length,
                    "filters": [{"conditions": []}],
                }

    def do_request(self, url: RestUrls, **kwargs) -> dict:
        """
        Given the RestUrl enum value, perform the operation, using kwargs as query params.
        Kwargs should generally have at least the incident ID.
        """

        log.info("Making %s request for %s", url.value[0], url.name)
        res_client = app_state.get().res_client

        match url.value[0]:
            case "GET":
                match url:
                    case (
                        RestUrls.ARTIFACT_CONTENTS
                        | RestUrls.ATTACHMENT_CONTENTS
                        | RestUrls.TASK_ATTACHMENT_CONTENTS
                    ):
                        res_client.headers["Accept"] = "text/html"
                        data = res_client.get_content(url.value[1].format(**kwargs))
                        res_client.headers["Accept"] = (
                            "application/json"  # reset headers
                        )
                        try:
                            return data.decode("utf-8")
                        except:
                            log.warning(
                                "Unknown encoding for artifact/attachment contents."
                            )
                            return data
                return res_client.get(url.value[1].format(**kwargs))

            case "POST":
                length = kwargs.get("length", 100)

                match url:
                    case (
                        RestUrls.PLAYBOOK_EXECUTIONS
                        | RestUrls.PLAYBOOK_EXECUTIONS_1
                        | RestUrls.PLAYBOOK_EXECUTIONS_2
                        | RestUrls.PLAYBOOK_EXECUTIONS_3
                    ):
                        for i, option in enumerate(self.playbook_exec_group):
                            args = {}
                            if kwargs.get("happy_path"):
                                args = kwargs
                            try:
                                result = res_client.post(
                                    option.value[1].format(**kwargs),
                                    self.__get_paged_query(
                                        RestUrls.PLAYBOOK_EXECUTIONS,
                                        kwargs.get("inc_id", None),
                                        length,
                                        kwargs.get("art_name", None),
                                    ),
                                    skip_retry=[500],
                                    **args,
                                )["data"]
                                return result
                            except:
                                log.warning(
                                    "Failed to get playbook executions using API %s.%s",
                                    option.value[1],
                                    (
                                        " Trying next API..." if i < 2 else ""
                                    ),  # so long as we've not exhausted each API option, say trying next
                                )
                                # ignore and try next
                                pass
                        log.warning("Failed to get playbook executions.")
                        return []

                    case (
                        RestUrls.ARTIFACT_BY_NAME
                        | RestUrls.GET_ARTIFACTS
                        | RestUrls.INC_ART_ID
                        | RestUrls.ATTACHMENT_BY_NAME
                    ):
                        try:
                            res = res_client.post(
                                url.value[1].format(**kwargs),
                                self.__get_paged_query(
                                    url,
                                    kwargs.get("inc_id", None),
                                    length,
                                    kwargs.get("obj_name", None),
                                ),
                            )

                            if url == RestUrls.ATTACHMENT_BY_NAME:
                                return res.get("attachments", [])
                            else:
                                return res.get("data", [])

                            return res
                        except Exception as e:
                            log.exception(
                                "Error fetching %s data from SOAR." % url.name,
                            )
                            # raise Exception("Error fetching %s data from SOAR.", url.name) from e

                return res_client.post(url.value[1].format(**kwargs))
            case "PUT":
                return res_client.put(url.value[1].format(**kwargs), kwargs["body"])
            case "PATCH":
                return res_client.patch(url.value[1].format(**kwargs))
