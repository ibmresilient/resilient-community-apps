import datetime
from enum import Enum
import logging
import os
from typing import List, Optional, Tuple
import json

from resilient import SimpleClient

from fn_watsonx_analyst.types.artifact import Artifact
from fn_watsonx_analyst.types.incident import Incident
from fn_watsonx_analyst.types.incident_full_data import IncidentFullData
from fn_watsonx_analyst.types.pbx_detail import PBExecDetail
from fn_watsonx_analyst.types.phase import Phase, Task

from fn_watsonx_analyst.util.rest import RestHelper, RestUrls


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


log = logging.getLogger(__name__)

class ContextHelper:
    """
    Can fetch and process context data for generic Q&A
    """

    res_client: SimpleClient = None

    inc_id: Optional[int] = None
    ws_id: Optional[int] = None

    inc_data: Incident = None
    art_data: List[Artifact] = []
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
        self.inc_data, self.pbx_data, self.art_data, self.task_data = self.cleanse_data(
            self.inc_data, self.pbx_data, self.art_data, self.task_data
        )
        self.inc_data["artifacts"] = self.art_data or []
        self.inc_data["playbook_executions"] = self.pbx_data or []
        self.inc_data["tasktree"] = self.task_data or []

        self.full_data = {"incident": self.inc_data}
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

    def _timestamp_to_readable(self, unix_timestamp: int) -> str:
        """Converts a Unix millis timestamp to a mixture of ISO 8601 and human readable date string"""
        timestamp = datetime.datetime.fromtimestamp(unix_timestamp / 1000)
        date_1 = timestamp.strftime("%d-%m-%Y")
        date_2 = timestamp.strftime("%A, %B %d, %Y")
        return f"{date_1} ({date_2})"

    def cleanse_data(
        self,
        inc_data: Optional[Incident],
        pbx_data: Optional[List[PBExecDetail]],
        art_data: Optional[List[Artifact]],
        task_data: Optional[List[Phase]],
    ) -> Tuple[Incident, List[PBExecDetail], List[Artifact], List[Phase]]:
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
                new_props = dict()
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
                for field in art_date_list:
                    try:
                        new[field] = self._timestamp_to_readable(old[field])
                    except:
                        # will raise if null or not timestamp
                        pass
                arts.append(new)

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

        return (inc, pbxs, arts, phases)

    def __mask_data(self, original: dict, allowed_keys: List[str]):
        return {key: original[key] for key in allowed_keys if key in original}

    def __get_property_labels(self) -> dict:
        if self.opts:
            return self.opts.get("watsonx_property_labels", {})
        log.warning("no opts")
        return {}
