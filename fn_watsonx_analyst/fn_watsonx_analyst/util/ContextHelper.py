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
from fn_watsonx_analyst.util.data.incident_template import INCIDENT_TEMPLATE


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

    full_data: IncidentFullData | None = None

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

        return self.full_data

    def format_incident_for_context(self) -> str:
        """
        Formats incident data using the incident template for better context in conversations.
        Returns a formatted string with all incident details.
        """
        # Get all the data we need
        if not self.full_data:
            self.build_full_data()

        # Get organization and workspace names
        org_name = "N/A"
        workspace_name = "Default workspace"
        workspace_id = "N/A"
        try:
            org_data = PersistentCache("org").get_data(self.res_client, "org", None)
            if org_data and "org_info" in org_data and "name" in org_data["org_info"]:
                org_name = org_data["org_info"]["name"]
        except Exception:
            log.debug("Could not retrieve organization name")

        try:
            # Get workspace name from incident data
            if self.inc_data and "workspace" in self.inc_data:
                workspace_id = self.inc_data["workspace"]

                for workspace in RestHelper().do_request(RestUrls.GET_WORKSPACES)["entities"]:
                    if str(workspace["id"]) == str(workspace_id):
                        workspace_name = workspace["display_name"]
        except Exception:
            log.debug("Could not retrieve workspace name")

        # Format members list - include owner and creator in the analysts list
        members_list = []
        owner = None
        creator = None
        members = []
        members_str = "No users assigned to this incident"
        
        if self.full_data and "incident" in self.full_data:
            incident_data = self.full_data["incident"]
        else:
            raise ValueError()
        incident_types = incident_data.get('incident_type_ids', "N/A")

        if "owner_id" in incident_data:
            owner = incident_data.get("owner_id", "N/A")
        if "creator_id" in incident_data:
            creator = incident_data.get("creator_id", "N/A")
        if "members" in incident_data:
            members = incident_data.get("members", [])

        all_members = set()
        all_members.update([creator, owner, *members])
        try:
            all_members.remove(None) # guard removal of None, as if not present, will get KeyError
        except:
            pass

        users = RestHelper().do_request(RestUrls.SEARCH_PRINCIPALS, user_ids=list(all_members))
        user_map = {}
        for user in users:
            if "result" in user and "id" in user["result"]:
                user_map[user["result"]["id"]] = user["result"].get("display_name", user["result"]["id"])

        if owner in user_map:
            members_list.append(f"Owner: {user_map[owner]}")
        if creator in user_map:
            members_list.append(f"Creator: {user_map[creator]}")
        
        if not members:
            members_list.append("- No incident members assigned")
        else:
            members_list.append("- Incident members:")
            for member in members:
                if member in user_map:
                    members_list.append(f"\t- {user_map[member]}")
                else:
                    members_list.append(f"\t- User/Principal with ID: `{member}`")

        members_str = "\n".join(members_list)

        # Format artifacts by type
        artifacts_section = "No artifacts found for this incident"
        if "artifacts" in incident_data:
            artifacts_by_type = {}
            # for artifact in self.art_data:
            for artifact in incident_data.get("artifacts", []):
                art_type = artifact.get("type", {}).get("name")
                if isinstance(art_type, dict):
                    art_type = art_type.get("name", "Unknown")

                if art_type not in artifacts_by_type:
                    artifacts_by_type[art_type] = []

                art_info = f"- Value: `{artifact.get('value', 'N/A')}`"
                if artifact.get("description", ''):
                    art_info += f"\n\t- Description:\n\t{artifact.get('description', 'N/A')}"

                if "hits" in artifact and artifact["hits"] is not None:
                    if len(artifact.get("hits", 0)) > 1:
                        art_info += "\n\t- Hits:"
                        for hit in artifact.get("hits", []):
                            if "name" in hit and "value" in hit:
                                art_info += f"\n\t\t- {hit.get('name', 'N/A')}: {hit.get('value', 'N/A')}"

                artifacts_by_type[art_type].append(art_info)

            if artifacts_by_type:
                sections = []
                for art_type, artifacts in artifacts_by_type.items():
                    section = f"#### `{art_type}` Artifacts:\n\n" + "\n\n".join(artifacts)
                    sections.append(section)
                artifacts_section = "\n".join(sections)

        # Format tasks by phase
        tasks_section = "No tasks found for this incident."
        if self.task_data:
            tasks_by_phase = {}

            def extract_tasks_from_phase(phase, phase_name=None):
                """Recursively extract tasks from phases"""
                current_phase_name = phase_name or phase.get("phase_name", "Unknown Phase")

                if current_phase_name not in tasks_by_phase:
                    tasks_by_phase[current_phase_name] = []

                # Add tasks from this phase
                for task in phase.get("tasks", []):
                    task_status = task.get("status", "Unknown")

                    owner = user_map.get(task.get("owner_id", 0), "Unassigned")

                    task_info = {
                        "name": task.get("name", "Unnamed Task"),
                        "status": task_status,
                        "owner": owner,
                        "required": task.get("required", False),
                        "due_date": task.get("due_date", "N/A"),
                        "description": task.get("instructions", {}).get("content") if task.get("instructions") and "content" in task["instructions"] else None
                    }
                    tasks_by_phase[current_phase_name].append(task_info)

                # Process child phases recursively
                for child_phase in phase.get("child_cats", []):
                    extract_tasks_from_phase(child_phase, child_phase.get("name", "Unknown Phase"))

            # Extract tasks from all phases
            for phase in self.task_data:
                extract_tasks_from_phase(phase)

            if tasks_by_phase:
                sections = []
                for phase_name, tasks in tasks_by_phase.items():
                    if tasks:
                        section = f"\n#### Phase: {phase_name}\n"
                        for task in tasks:
                            task_str = f"\n**Task: {task.get('name', 'N/A')}**\n"
                            task_str += f"- Status: {task.get('status', 'N/A')}\n"
                            task_str += f"- Assigned to: {task['owner']}\n"
                            task_str += f"- Required: {'Yes' if task.get('required', False) else 'No'}\n"
                            if 'due_date' in task and task['due_date']:
                                due_date = self._timestamp_to_readable(task['due_date'])
                                task_str += f"- Due Date: {due_date}\n"
                            if task['description']:
                                task_str += f"- Description: {task.get('description', 'N/A')}\n"
                            section += task_str
                        sections.append(section)
                tasks_section = "\n".join(sections)

        playbook_executions = "No playbooks have been executed on this incident yet."
        pbx_data: List[PBExecDetail] = incident_data.get("playbook_executions", [])
        if pbx_data:
            pb_sections = []

            for pbx in pbx_data:
                pb_name = pbx['playbook'].get('display_name', "N/A")
                pbx_status = pbx.get("status", "N/A")
                pbx_start_time = pbx.get("start_time", "N/A")
                pbx_object = pbx.get("object", {})
                pbx_target = f"{pbx_object.get('type_name', 'N/A').capitalize()}: `{pbx_object.get('object_name', 'N/A')}`"

                pb_sections.append(f"- Playbook: {pb_name}\n\t- Status: {pbx_status}\n\t- Started at: {pbx_start_time}\n\t- Targeting: {pbx_target}")
            playbook_executions = "\n\n".join(pb_sections)

        # Format timeline dates
        def format_date_line(field_name, label):
            if self.inc_data and field_name in self.inc_data and self.inc_data[field_name]:
                try:
                    date_str = self._timestamp_to_readable(self.inc_data[field_name])
                except:
                    date_str = self.inc_data[field_name]
                return f"{label}: {date_str}"
            return ""

        timeline_parts = [
            format_date_line("discovered_date", "Incident discovered at"),
            format_date_line("create_date", "Incident created at"),
            format_date_line("end_date", "Incident closed at"),
            format_date_line("inc_last_modified_date", "Incident details last modified at"),
            format_date_line("start_date", "Investigation started at"),
        ]
        timeline_str = "\n".join([part for part in timeline_parts if part])

        custom_properties_section = ""
        for ikey, ivalue in self.inc_data.get("properties", {}).items():
            custom_properties_section += f"- {ikey}: {ivalue}\n"
        
        if custom_properties_section:
            custom_properties_section = f"### Custom Incident Properties\n\n{custom_properties_section}"

        # Build the template data dictionary
        template_data = {
            "inc_id": self.inc_id,
            "org_name": org_name,
            "workspace_name": workspace_name,
            "workspace_id": workspace_id,
            "inc_name": self.inc_data.get("name", "N/A") if self.inc_data else "N/A",
            "severity_code": self.__severity_code_to_name(self.inc_data.get("severity_code")) if self.inc_data and "severity_code" in self.inc_data else "N/A",
            "incident_types": incident_types,
            "inc_enabled": "Enabled" if self.inc_data and self.inc_data.get("enabled", True) else "Disabled",
            "inc_disposition": "Confirmed" if self.inc_data and self.inc_data.get("confirmed", False) else "Unconfirmed",
            "inc_description": self.inc_data.get("description", "N/A") if self.inc_data else "N/A",
            "training_line": "\nTraining incident\n" if self.inc_data and self.inc_data.get("training", False) else "",
            "inc_address": self.inc_data.get("addr", "N/A") if self.inc_data else "N/A",
            "inc_city": self.inc_data.get("city", "N/A") if self.inc_data else "N/A",
            "inc_state": self.inc_data.get("state", "N/A") if self.inc_data else "N/A",
            "inc_zip": self.inc_data.get("zip", "N/A") if self.inc_data else "N/A",
            "timeline": timeline_str if timeline_str else "No timeline information available",
            "members": members_str,
            "artifacts_section": artifacts_section,
            "tasks_section": tasks_section,
            "playbook_executions": playbook_executions,
            "custom_properties_section": custom_properties_section,
        }

        # Format using the template
        formatted_text = INCIDENT_TEMPLATE.format(**template_data)
        return formatted_text

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
        date_1 = timestamp.strftime("%H:%M %d-%m-%Y")
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
        pbx_date_list = config.get("playbook_executions", {}).get("date_list") or []

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
                    if field in inc_list:
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
                new["playbook"] = self.__mask_data(new.get("playbook", {}), pbx_pb_list)
                for field in pbx_date_list:
                    try:
                        if field in pbx_list:
                            new[field] = self._timestamp_to_readable(old[field])
                    except:
                        # will raise if null or not timestamp
                        pass

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
                        if field in art_list:
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
                        if field in attach_list:
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
                        task_status = "Unknown"
                        
                        if "status" in task_list:
                            match old_task['status']:
                                case "O":
                                    task_status = "Open (on-time)"
                                case "D":
                                    task_status = "Potential delay"
                                case "C":
                                    task_status = "Closed"
                                case "R":
                                    task_status = "At risk"
                                case "S":
                                    task_status = "Suspended"
                        
                        new_task["status"] = task_status

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
