import datetime
from enum import Enum
from functools import cache
import os
import re
from typing import Any, List, Optional, Tuple, Union
import jsonpath_ng as jsonpath
from resilient import SimpleClient

from fn_watsonx_analyst.config.loaders import load_data_config
from fn_watsonx_analyst.types.artifact import Artifact
from fn_watsonx_analyst.types.attachment import Attachment
from fn_watsonx_analyst.types.incident import Incident
from fn_watsonx_analyst.types.incident_full_data import IncidentFullData
from fn_watsonx_analyst.types.pbx_detail import PBExecDetail
from fn_watsonx_analyst.types.phase import Phase

from fn_watsonx_analyst.util.persistent_org_cache import PersistentCache
from fn_watsonx_analyst.util.rest import RestHelper, RestUrls
from fn_watsonx_analyst.util.logging_helper import create_logger
from fn_watsonx_analyst.util.state_manager import app_state


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
    opts: dict = None

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
        self, inc_id: int = None
    ):
        self.inc_id = inc_id
        self.res_client = app_state.get().res_client
        self.opts = app_state.get().opts

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

    def get_incident_data(self) -> Incident:
        helper = RestHelper()
        inc_data = helper.do_request(
            RestUrls.INCIDENT_DETAILS, inc_id=self.inc_id
        )
        return inc_data

    def __get_data(self):
        helper = RestHelper()
        self.inc_data = self.get_incident_data()

        self.pbx_data = helper.do_request(
            RestUrls.PLAYBOOK_EXECUTIONS,
            inc_id=self.inc_id,
            workspace_id=self.inc_data["workspace"],
        )

        self.art_data = helper.do_request(
            RestUrls.GET_ARTIFACTS, inc_id=self.inc_id
        )

        self.attach_data = helper.do_request(
            RestUrls.GET_ATTACHMENTS, inc_id=self.inc_id
        )

        self.task_data = helper.do_request(
            RestUrls.TASK_TREE, inc_id=self.inc_id
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

    def _timestamp_to_readable(self, unix_timestamp: int) -> str:
        """Converts a Unix millis timestamp to a mixture of ISO 8601 and human readable date string"""
        timestamp = datetime.datetime.fromtimestamp(unix_timestamp / 1000)
        date_1 = timestamp.strftime("%d-%m-%Y")
        date_2 = timestamp.strftime("%A, %B %d, %Y")
        return f"{date_1} ({date_2})"

    def _milliseconds_to_datetime(self, millis: int) -> datetime.datetime:
        return datetime.datetime.fromtimestamp(millis // 1000)

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
                try:
                    jsonpath_expr = jsonpath.parse(path)
                    matches = jsonpath_expr.find(full_data)

                    for match in matches:
                        match.context.value[match.path.fields[-1]] = modify(match.value, group)
                except:
                    # don't interrupt execution
                    log.debug(f'failed to resolve type id for {group}, using jsonpath {path}')

        return full_data

    @cache
    def __severity_code_to_name(self, severity_code: int) -> str:
        """Tries to get the API name for a severity code ID"""
        incident_types = RestHelper().do_request(RestUrls.GET_TYPES, type='incident') or []
        for type in incident_types:
            if type.get('name', '') == 'severity_code':
                for value in type.get('values', []):
                    if value.get('value') == severity_code:
                        return value.get('label')
        return str(severity_code)


    def replace_string_in_values(
        self,
        data: Union[dict[str], List[str]],
        target_string: str,
        replacement_string: str,
    ) -> dict[str]:
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

        config = load_data_config(app_state.get().data_config)

        inc_list = config.get("incident").get("allow_list") or []
        inc_date_list = config.get("incident").get("date_list") or []
        inc_properties_list = config.get("incident").get("properties") or []

        pbx_list = config.get("playbook_executions", {}).get("allow_list") or []
        pbx_pb_list = config.get("playbook_executions", {}).get("playbook_allow_list") or []

        art_list = config.get("artifacts", {}).get("allow_list") or []
        art_date_list = config.get("artifacts", {}).get("date_list") or []
        art_hit_list = config.get("artifacts", {}).get("hit_allow_list") or []
        art_hit_property_blocklist = config.get("artifacts", {}).get("hit_block_list") or []
        art_hit_property_relabel = config.get("artifacts", {}).get("hit_relabel_list") or {}

        attach_list = config.get("attachments", {}).get("allow_list") or []
        attach_date_list = config.get("attachments", {}).get("date_list") or []

        phase_list = config.get("phases", {}).get("allow_list") or []
        phase_relabel_map = config.get("phases", {}).get("relabel_list") or {}
        task_list = config.get("tasks", {}).get("allow_list") or []

        inc = None
        if inc_data:
            inc = self.__mask_data(inc_data, inc_list)
            if "confirmed" in inc:
                inc["incident_disposition"] = (
                    "confirmed" if inc["confirmed"] else "not yet confirmed"
                )
            if 'severity_code' in inc:   
                inc['severity_code'] = self.__severity_code_to_name(inc['severity_code'])


            for field in inc_date_list:
                try:
                    inc[field] = self._timestamp_to_readable(inc[field])
                except:
                    # will raise if null, which can be safely ignored.
                    pass

            if "properties" in inc and inc["properties"]:
                labels = self.__get_property_labels()
                new_props = {}
                for key, val in inc["properties"].items():
                    if "*" in inc_properties_list or key in inc_properties_list:
                        new_props[labels.get(key, key)] = val
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

                # add hits - for each, get the mask of the dictionary
                hits_info = {}
                if "hits" in old and old["hits"]:
                    for i, hit in enumerate(old.get("hits", [])):
                        hit_source = 'Unspecified' # fallback

                        if 'threat_source_id' in hit:
                            hit_source = hit['threat_source_id']
                            if hit_source and isinstance(hit_source, dict):
                                hit_source = hit['threat_source_id'].get('name', hit_source)

                        hit = self.__mask_data(hit, art_hit_list)


                        if isinstance(hit.get("properties"), dict):
                            hit["properties"] = dict(hit["properties"])  # assert type
                            for k, v in hit["properties"].items():
                                if k not in art_hit_property_blocklist:
                                    # if we need to re-key the label, change the key, default to existing
                                    k = art_hit_property_relabel.get(k, k)
                                    hits_info[k] = v

                        else:
                            props = [
                                prop
                                for prop in hit.get("properties", [])
                                if prop
                                and prop.get("name", "") not in art_hit_property_blocklist
                            ]

                            for prop in props:
                                prop_name = prop.get("name", None)
                                if isinstance(prop_name, str):
                                    prop_name = prop_name.lower()
                                else:
                                    continue

                                if prop_name in art_hit_property_relabel:
                                    prop["name"] = art_hit_property_relabel[prop_name]

                            if hit_source in hits_info.keys():
                                if hits_info[hit_source].get('created') > self._milliseconds_to_datetime(hit.get('created')):
                                    continue
                            # if this hit is newer, or first instance for threat source, add it
                            hits_info[hit_source] = {"properties": props, 'created': self._milliseconds_to_datetime(hit.get('created'))}
                        

                properties = []
                for hit in hits_info.values():
                    properties.extend(hit.get('properties'))
                properties.append({'threat_sources': list(hits_info.keys())})

                new["hits"] = properties

                # add content-type if possible
                if "attachment" in old and old["attachment"] and "content_type" in old["attachment"]:
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

            def process_phase(phase: Union[Phase, dict]) -> dict:
                """
                    Return a cleaned phase, with all tasks' fields masked
                """

                new_phase = phase
                new_phase = self.__mask_data(new_phase, phase_list)

                for old_name, new_name in phase_relabel_map.items():
                    new_phase[new_name] = phase[old_name]
                    try:
                        del new_phase[old_name]
                    except KeyError:
                        pass

                tasks = []

                if "child_tasks" in phase:
                    for old_task in phase["child_tasks"]:
                        new_task = old_task
                        new_task = self.__mask_data(new_task, task_list)
                        if "status" in task_list:
                            new_task["complete"] = True if old_task["status"] == "C" else False
                            new_task.pop('status', None) # remove the status key as not needed
                        if new_task:
                            tasks.append(new_task)

                new_phase["tasks"] = tasks

                if "child_cats" in phase and phase["child_cats"]:
                    new_phase["child_phases"] = []
                    for old_child_phase in phase["child_cats"]:
                        new_child_phase = old_child_phase
                        new_child_phase = self.__mask_data(new_child_phase, phase_list)
                        new_phase["child_phases"].append(process_phase(old_child_phase))

                return new_phase

            phases = [process_phase(x) for x in task_data]

        return (inc, pbxs, arts, attachs, phases)

    def __mask_data(self, original: Any, allowed_keys: List[str]):
        return {key: original[key] for key in allowed_keys if key in original}

    def __get_property_labels(self) -> dict:
        if self.opts:
            return self.opts.get("watsonx_property_labels", {})
        log.warning("no opts")
        return {}
