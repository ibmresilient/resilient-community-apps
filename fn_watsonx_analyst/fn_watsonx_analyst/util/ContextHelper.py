import datetime
from enum import Enum
from functools import cache
import os
import re
from typing import List, Optional, Tuple, Union
import jsonpath_ng as jsonpath
from bs4 import BeautifulSoup
from resilient import SimpleClient

from fn_watsonx_analyst.types.artifact import Artifact
from fn_watsonx_analyst.types.attachment import Attachment
from fn_watsonx_analyst.types.incident import Incident
from fn_watsonx_analyst.types.incident_full_data import IncidentFullData
from fn_watsonx_analyst.types.pbx_detail import PBExecDetail
from fn_watsonx_analyst.types.phase import Phase, Task

from fn_watsonx_analyst.util.persistent_org_cache import PersistentCache
from fn_watsonx_analyst.util.rest import RestHelper, RestUrls
from fn_watsonx_analyst.util.util import create_logger


class Templates(Enum):
    """Prompt templates"""

    SUMM_AGGREGATE = "summ/aggregate"
    SUMM_INCIDENT = "summ/incident"
    SUMM_PBEXEC = "summ/pbexec"
    SUMM_ARTIFACT = "summ/artifact"
    SUMM_TASKTREE = "summ/tasktree"
    SUMM_CONTENTS = "summ/contents"
    SUMM_DOCUMENT = "summ/doc"

    REPORT_KEY_POINTS = "report/key_points"
    REPORT_NARRATIVE = "report/narrative"
    REPORT_EXECUTIVE = "report/executive"

    CASE_QNA = "qna/case_qna"
    ARTIFACT_CONTENTS_QNA = "qna/artifact_contents_qna"
    ARTIFACT_METADATA_QNA = "qna/artifact_metadata_qna"
    ALL_ARTIFACTS_QNA = "qna/all_artifacts_qna"
    TASK_QNA = "qna/task_qna"

    ASSESS_SCRIPT = "assess/script"
    ASSESS_META_ARTIFACT = "assess/meta"
    INCIDENT_TYPE = "incident_type"

    DEF_SYSTEM_PROMPT = "def_system_prompt"

log = create_logger(__name__)


class ContextHelper:
    """
    Can fetch and process context data for generic Q&A
    """

    res_client: SimpleClient = None

    inc_id: Optional[int] = None
    ws_id: Optional[int] = None

    inc_data: Incident = None
    art_data: List[Artifact] = []
    attach_data: List[Attachment] = []
    pbx_data: List[PBExecDetail] = []
    task_data: List[any] = []

    full_data: IncidentFullData = None

    date_fmt = "%Y-%m-%d %H:%M:%S"

    def __init__(
        self, res_client: SimpleClient = None, inc_id: int = None, opts: dict = {}
    ):
        self.res_client = res_client
        self.inc_id = inc_id
        self.opts = opts

    def build_full_data(self) -> IncidentFullData:
        """
        Fetches Incident, 100 Artifacts, and 100 Playbook Executions, and builds them to a single payload object
        """
        self.__get_data()
        self.inc_data, self.pbx_data, self.art_data, self.attach_data, self.task_data = self.cleanse_data(
            self.inc_data, self.pbx_data, self.art_data, self.attach_data, self.task_data
        )
        self.inc_data["artifacts"] = self.art_data or []
        self.inc_data["attachments"] = self.attach_data or []
        self.inc_data["playbook_executions"] = self.pbx_data or []
        self.inc_data["tasktree"] = self.task_data or []
        self.full_data = self.resolve_type_ids({"incident": self.inc_data})
        self.full_data = self.replace_string_in_values(self.full_data, 'Attachment', 'File') # Fix: SOARAPPS-8551
        self.full_data = self.replace_string_in_values(self.full_data, 'Artifact', 'File') # Fix: SOARAPPS-8551

        return self.full_data

    def __get_data(self):
        helper = RestHelper()
        self.inc_data = helper.do_request(
            self.res_client, RestUrls.INCIDENT_DETAILS, inc_id=self.inc_id
        )
        self.pbx_data = helper.do_request(
            self.res_client,
            RestUrls.PLAYBOOK_EXECUTIONS,
            inc_id=self.inc_id,
            workspace_id=self.inc_data["workspace"],
        )
        self.art_data = helper.do_request(
            self.res_client, RestUrls.GET_ARTIFACTS, inc_id=self.inc_id
        )
        self.attach_data = helper.do_request(
            self.res_client, RestUrls.GET_ATTACHMENTS, inc_id=self.inc_id
        )
        self.task_data = helper.do_request(
            self.res_client, RestUrls.TASK_TREE, inc_id=self.inc_id
        )

    def get_prompt(self, tmpl: Templates, **kwargs) -> str:
        """
        Builds prompt from template file and returns it, formatting the prompt template with kwargs
        """
        prompt_txt = ""
        prompt_dir = os.path.dirname(__file__)
        prompt_dir = os.path.join(prompt_dir, "data/prompts")
        try:
            prompt_path = os.path.join(prompt_dir, tmpl.value + ".txt")
            f = open(prompt_path, "r", encoding="utf-8")
            prompt_txt = f.read()
        except Exception as e:
            log.warning("Failed to get prompt path at %s", prompt_path)
            raise e
        finally:
            f.close()

        prompt_txt = prompt_txt.format(**kwargs)
        return prompt_txt

    def multi_format_parser(self, data: str) -> str:
        """Formats the input into text and removes the extra empty lines."""
        try:
            import tika
            tika.initVM()
            from tika import parser
            # Ensure data is not empty after stripping
            if not data or not data.strip():
                raise ValueError("Input data is empty or contains only whitespace.")

            parsed_doc = parser.from_buffer(data)

            # Ensure parsed content is not None
            if parsed_doc.get("content") is None:
                raise ValueError("Parsed content is empty or could not be extracted.")

            # Check if the content type is HTML
            if "metadata" in parsed_doc and "Content-Type" in parsed_doc["metadata"]:
                content_type = parsed_doc["metadata"]["Content-Type"]
                if "text/plain" in content_type: # Note: tika doesn't show text/html but text/plain
                    soup = BeautifulSoup(parsed_doc["content"], "html.parser")
                    parsed_doc["content"] = soup.get_text(separator="\n")  # Extract text only

            # Clean up extra newlines
            cleaned_text = re.sub(r'\n+', '\n', parsed_doc["content"]).strip()
            return cleaned_text

        except ValueError as ve:
            log.error("Validation error: %s", ve)
            raise

        except Exception as e:  
            log.exception("An error occurred during user file parsing: %s", e)
            raise

    def _timestamp_to_readable(self, unix_timestamp: int) -> str:
        """Converts a Unix millis timestamp to a mixture of ISO 8601 and human readable date string"""
        timestamp = datetime.datetime.fromtimestamp(unix_timestamp / 1000)
        date_1 = timestamp.strftime("%d-%m-%Y")
        date_2 = timestamp.strftime("%A, %B %d, %Y")
        return f"{date_1} ({date_2})"

    def resolve_type_ids(self, full_data: IncidentFullData) -> IncidentFullData:
        """Goes through payload to replace Type ID references, with the Type's name"""

        @cache
        def normalize(value: Union[str, int]) -> Union[str, int]:
            """Convert digity strings to ints"""
            if isinstance(value, int) or (isinstance(value, str) and value.isdigit()):
                return int(value)

            # if not an int or digit, just return as-is (it's probably the type's name already...)
            return value

        @cache
        def type_id_to_name(type_id: Union[int, str], type_group: str) -> str:
            """Using Org data, search for the Type name"""
            type_id = normalize(type_id)
            if isinstance(type_id, str):
                return type_id
            try:
                types = PersistentCache("org").get_data(self.res_client, "org", None).get(type_group, {})
                for key, type_obj in types.items():
                    if key == str(type_id):
                        return type_obj.get("name", str(type_id))
            except Exception: # pylint: disable=broad-except
                pass
            log.warning("Couldn't find type name for type ID %d", type_id)
            return str(type_id)

        def modify(value, type_group: str):
            """Convert type ID to name, if possible"""
            if value is None:
                return str(value)

            if isinstance(value, list):
                output = []
                for item in value:
                    output.append(type_id_to_name(normalize(item), type_group))
                return output

            return type_id_to_name(normalize(value), type_group)

        conf = {
            "incident_types": [
                "$.incident.incident_type_ids",
            ],
            "incident_artifact_types": [
                "$.incident.artifacts[*].type"
            ]
        }

        for group, paths in conf.items():
            for path in paths:
                jsonpath_expr = jsonpath.parse(path)
                matches = jsonpath_expr.find(full_data)

                for match in matches:
                    match.context.value[match.path.fields[-1]] = modify(match.value, group)

        return full_data

    def replace_string_in_values(self, data: Union[dict[str], List[str]], target_string:str, replacement_string:str) -> dict[str]:
        """
        Recursively traverses a nested dictionary and replaces occurrences of
        `target_string` (case-insensitive) in string values with `replacement_string`.

        Args:
            data (dict or list): The nested dictionary or list to process.
            target_string (str): The string to be replaced (case-insensitive).
            replacement_string (str): The string to replace with.

        Returns:
            dict or list: The updated nested dictionary or list.
        """
        try:
            pattern = re.compile(rf'\b{re.escape(target_string)}\b', re.IGNORECASE)  # Case-insensitive pattern

            if isinstance(data, dict):
                # If it's a dictionary, iterate over its keys and recursively call the function
                return {key: self.replace_string_in_values(value, target_string, replacement_string) for key, value in data.items()}

            elif isinstance(data, list):
                # If it's a list, process each element recursively
                return [self.replace_string_in_values(item, target_string, replacement_string) for item in data]

            elif isinstance(data, str) and pattern.search(data):
                # If it's a string and matches the pattern, replace it
                return pattern.sub(replacement_string, data)

            return data  # Return unchanged if not a match
        except Exception as e:
                log.exception(
                    "An error occurred while flattening a nested json: %s",
                    e
                )
                raise

    def cleanse_data(
        self,
        inc_data: Optional[Incident],
        pbx_data: Optional[List[PBExecDetail]],
        art_data: Optional[List[Artifact]],
        attach_data: Optional[List[Attachment]],
        task_data: Optional[List[Phase]],
    ) -> Tuple[Incident, List[PBExecDetail], List[Artifact], List[Attachment], List[Phase]]:
        """
        Pre-process data to only include specific fields
        """
        inc_list = [
            "name",
            "description",
            "confirmed",
            "addr",
            "city",
            "start_date",
            "inc_start",
            "discovered_date",
            "creator_principal",
            "reporter",
            "state",
            "country",
            "zip",
            "workspace",
            "members",
            "negative_pr_likely",
            "assessment",
            "properties",
            "inc_last_modified_date",
            "incident_type_ids"
        ]
        inc_date_list = [
            "start_date",
            "inc_start",
            "discovered_date",
            "inc_last_modified_date",
        ]

        pbx_list = ["last_activated_by", "status", "object", "elapsed_time", "playbook"]
        pbx_pb_list = ["display_name", "description", "activate_type"]
        art_list = ["value", "type", "related_incident_count"]
        art_date_list = ["created", "last_modified_time"]
        attach_list = ["value", "related_incident_count", "name","content_type"]
        attach_date_list = ["created"]
        phase_list = []  # fields are set manually below
        task_list = ["name", "active", "required"]

        inc = None
        if inc_data:
            inc = self.__mask_data(inc_data, inc_list)
            inc["incident_disposition"] = (
                "confirmed" if inc["confirmed"] else "not yet confirmed"
            )
            for field in inc_date_list:
                try:
                    inc[field] = self._timestamp_to_readable(inc[field])
                except:
                    # will raise if null, which can be safely ignored.
                    pass

            if inc["properties"]:
                labels = self.__get_property_labels()
                new_props = {}
                for key, val in inc["properties"].items():
                    if key in labels.keys():
                        new_props[labels[key]] = val
                    else:
                        new_props[key] = val

                inc["properties"] = new_props
        pbxs = []
        if pbx_data:
            for old in pbx_data:
                new: PBExecDetail = old
                new = self.__mask_data(new, pbx_list)
                new["playbook"] = self.__mask_data(new["playbook"], pbx_pb_list)
                pbxs.append(new)

        arts = []
        if art_data:
            for old in art_data:
                new: Artifact = old
                new = self.__mask_data(new, art_list)

                # add content-type if possible
                if old["attachment"] and old["attachment"]["content_type"]:
                    new["content-type"] = old["attachment"]["content_type"]

                for field in art_date_list:
                    try:
                        new[field] = self._timestamp_to_readable(old[field])
                    except:
                        # will raise if null or not timestamp
                        pass
                arts.append(new)

        attachs = []
        if attach_data:
            for old in attach_data:
                new: Attachment = old
                new = self.__mask_data(new, attach_list)
                for field in attach_date_list:
                    try:
                        new[field] = self._timestamp_to_readable(old[field])
                    except:
                        # will raise if null or not timestamp
                        pass
                attachs.append(new)

        phases = []
        if task_data:
            for old_phase in task_data:
                new_phase: Phase = old_phase
                new_phase = self.__mask_data(new_phase, phase_list)
                new_phase["phase_name"] = old_phase["name"]
                tasks = []
                for old_task in old_phase["child_tasks"]:
                    new_task: Task = old_task
                    new_task = self.__mask_data(new_task, task_list)
                    new_task["complete"] = True if old_task["status"] == "C" else False
                    tasks.append(new_task)

                new_phase["tasks"] = tasks
                phases.append(new_phase)

        return (inc, pbxs, arts, attachs, phases)

    def __mask_data(self, original: dict, allowed_keys: List[str]):
        return {key: original[key] for key in allowed_keys if key in original}

    def __get_property_labels(self) -> dict:
        if self.opts:
            return self.opts.get("watsonx_property_labels", {})
        log.warning("no opts")
        return {}
