# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2026. All Rights Reserved.
# Generated with resilient-sdk v51.0.7.2.16540

"""AppFunction implementation"""

from datetime import datetime
import json
import re
from typing import List, Optional
from resilient_circuits import FunctionError, app_function, FunctionResult

from fn_watsonx_analyst.types.playbook_execution_schemas import (
    PlaybookAnalysis, PlaybookContext, PlaybookExecutionSummaryData
)
from fn_watsonx_analyst.util.chat_prompting import ChatPrompting
from fn_watsonx_analyst.util.chunking.chunking import Chunking
from fn_watsonx_analyst.util.playbook_sequence_flow import (
    xml_to_playbook_model, model_to_scripts, model_to_sequence_flow
)
from fn_watsonx_analyst.util.rich_text import RichTextHelper
from fn_watsonx_analyst.types.incident import Incident
from fn_watsonx_analyst.types.note import Note
from fn_watsonx_analyst.types.pbx_detail import (
    ActivityMessageTypes,
    PBExecActivity,
    PBExecDetail,
    friendly_name_from_node_type,
)
from fn_watsonx_analyst.types.playbook import (
    ActivationCondition,
    Playbook,
    PlaybookActivationType,
    PlaybookLogicType,
    PlaybookObjectType,
)
from fn_watsonx_analyst.util.ModelTag import AiResponsePurpose
from fn_watsonx_analyst.util.response_helper import ResponseHelper
from fn_watsonx_analyst.util.rest import RestHelper, RestUrls
from fn_watsonx_analyst.util.logging_helper import create_logger
from fn_watsonx_analyst.util.util import format_duration
from fn_watsonx_analyst.util.watsonx_client import WatsonxClient
from fn_watsonx_analyst.watsonx_app_function import WatsonxAppFunction
from fn_watsonx_analyst.util.state_manager import app_state

PACKAGE_NAME = "fn_watsonx_analyst"
FN_NAME = "fn_watsonx_analyst_summarize_playbook_execution"

log = create_logger(__name__)


def friendly_playbook_activities(activities: List[PBExecActivity]) -> str:
    """
    - Task: Notify internal management chain (preliminary)
        - Status: Complete | Started | Canceled
        - Start time: 30/33/2025 12:12:20
        {if messages}
        - Messages:
            - 30/33/2025 12:12:20 - Invoke function
            - ...
    """
    output: List[str] = []

    for activity in activities:
        message_lines = []

        if len(activity["messages"]) > 0:
            message_lines = ["\t- Messages:"]

            for message in activity["messages"]:
                if message["text"] == "No message was specified":
                    message["text"] = (
                        "Critical error in function, failed to create a response. Review the App logs and resilient-scripting.log to learn more."
                    )

                message_lines.append(
                    f"\t- {message['create_date']} - {message['text']}"
                )

        messages = "\n\t".join(message_lines)

        output.append(f"""
- {friendly_name_from_node_type(activity["activity_ref"]["activity_type"])}: {activity["activity_ref"]["node_display_name"]}
    - Status: {activity["status"].capitalize()}
    - Start time: {activity.get("start_time_str", "N/A")}
{messages}""")
    return "\n".join(output)


def friendly_activation_conditions(
    activation_type: PlaybookActivationType,
    logic_type: PlaybookLogicType,
    object_type: PlaybookObjectType,
    custom_condition: Optional[str],
    activation_conditions: List[ActivationCondition],
) -> str:
    def activation_cond_to_str(condition: ActivationCondition) -> str:
        return f"{condition['field_name']} {condition['method']} {'`' + str(condition['value']) + '`' if condition['value'] else ''}"

    object_type_str = object_type.name.capitalize()

    # remove implicit automatic condition
    activation_conditions = [
        cond for cond in activation_conditions if cond["method"] != "object_added"
    ]

    conditions = []
    # if not activation_conditions:
    if activation_type == "manual":
        conditions.append(
            f"Playbook manually invoked on a(n) {object_type_str} by user"
        )
    else:
        conditions.append(f"{object_type_str} was created")

    match logic_type:
        case "advanced":
            if custom_condition:
                numbered_conditions = {}

                for condition in activation_conditions:
                    if "evaluation_id" in condition:
                        numbered_conditions[condition["evaluation_id"]] = condition

                number_token_re = re.compile(r"\b(\d+)\b")

                def repl(m: re.Match) -> str:
                    key = int(m.group(1))
                    if key not in numbered_conditions:
                        raise KeyError(
                            f"Condition {key} does not exist in activation conditions for playbook"
                        )
                    return activation_cond_to_str(numbered_conditions[key])

                return number_token_re.sub(repl, custom_condition)

        case "all":
            conditions.append(
                " AND ".join(
                    [activation_cond_to_str(cond) for cond in activation_conditions]
                )
            )
        case _:  # assume 'all'
            conditions.append(
                " OR ".join(
                    [activation_cond_to_str(cond) for cond in activation_conditions]
                )
            )

    return "\n".join(conditions)


class FunctionComponent(WatsonxAppFunction):
    """Component that implements function 'fn_watsonx_analyst_summarize_playbook_execution'"""

    time_format = "%d/%m/%Y %H:%M:%S"

    def format_millis_timestamp(self, millis: int) -> str:
        return datetime.fromtimestamp(millis / 1000).strftime(self.time_format)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Summarize the execution steps of the most recent execution of a given playbook display name in the given incident.
        Inputs:
            -   fn_inputs.fn_watsonx_analyst_playbook_name
            -   fn_inputs.fn_watsonx_analyst_playbook_execution_id
            -   fn_inputs.fn_watsonx_analyst_model_id
            -   fn_inputs.fn_watsonx_analyst_incident_id
        """

        yield self.setup(fn_inputs, AiResponsePurpose.PLAYBOOK_EXECUTION_SUMMARY, FN_NAME)

        inc_id = getattr(fn_inputs, "fn_watsonx_analyst_incident_id", None)
        pb_name = getattr(fn_inputs, "fn_watsonx_analyst_playbook_name", None)
        pb_exec_id = getattr(fn_inputs, "fn_watsonx_analyst_playbook_execution_id", None)

        if not pb_name and not pb_exec_id:
            raise ValueError("Playbook name or execution ID must have a value")

        rh = RestHelper()

        playbook_executions: List[PBExecDetail]
        incident: Incident = rh.do_request(RestUrls.INCIDENT_DETAILS, inc_id=inc_id)
        if pb_exec_id is not None:
            playbook_executions = rh.do_request(
                RestUrls.SPECIFIC_PLAYBOOK_EXECUTION,
                inc_id=inc_id,
                obj_name=int(pb_exec_id),
                workspace_id=incident.get("workspace"),
            )
        else:
            playbook_executions = rh.do_request(
                RestUrls.LATEST_PLAYBOOK_EXECUTION,
                inc_id=inc_id,
                obj_name=pb_name,
                workspace_id=incident.get("workspace"),
            )

        if len(playbook_executions) < 1:
            yield FunctionResult(
                ResponseHelper().error_response(
                    f"Could not find playbook executions for playbook: {pb_name if pb_name else pb_exec_id}"), False)
            return

        for pb_exec in playbook_executions:
            if not pb_name:
                pb_name = pb_exec["playbook"]["display_name"]

            playbook_list: list = rh.do_request(
                RestUrls.PLAYBOOK_BY_NAME,
                obj_name=pb_name
            )

            if not playbook_list or len(playbook_list) == 0:
                yield FunctionResult(
                    ResponseHelper().error_response(f"Could not find playbook with name `{pb_name}`"), False)
                return

            playbook: Playbook = playbook_list[0]

            playbook: Playbook = rh.do_request(
                RestUrls.PLAYBOOK_DETAILS,
                playbook_id=playbook["id"]
            )

            if playbook["type"] == "subplaybook":
                yield FunctionError("Subplaybooks are not supported.")
                return

            if (
                not playbook
                or not playbook["content"]
                or not playbook["content"]["xml"]
            ):
                yield FunctionResult(
                    ResponseHelper().error_response(f"Could not find playbook with name `{pb_name}`"), False)
                return

            pb_context = self.extract_context_from_pb_exec(pb_exec, playbook, incident)

            chat_msgs = ChatPrompting().build_chat_messages(
                query="",
                purpose=AiResponsePurpose.PLAYBOOK_EXECUTION_SUMMARY,
            )

            context_items = pb_context.model_dump()

            # limit input tokens
            ch = Chunking()
            chat_msgs[1]["content"] = ''.join(ch.clamped_chunks_for_model(
                chat_msgs[-1]["content"].format(**context_items), app_state.get().model_id, 0.6))
            response = WatsonxClient().chat(chat_msgs, response_format=PlaybookAnalysis)

            pb_analysis = PlaybookAnalysis.model_validate_json(response["choices"][0]["message"]["content"])
            pb_exec_data = PlaybookExecutionSummaryData(**pb_context.model_dump(), analysis=pb_analysis)

            response["choices"][0]["message"]["content"] = self.format_response(pb_exec_data)


            if playbook["version"] != pb_exec["playbook"]["version"]:
                response["choices"][0]["message"]["content"] += \
                    "\n\nOutput is based on the current playbook definition and may differ from the version that executed.\n\n"

            result = ResponseHelper().text_chat_to_ai_response(response)
            if self.ai_fields_present():
                try:
                    rh.do_request(
                        RestUrls.SET_PLAYBOOK_EXECUTION_AI_SUMMARY,
                        execution_id=pb_exec["id"], body={"ai_summary": json.dumps(result)})
                    result = ResponseHelper().set_insights_added(result)
                except:
                    pass

            yield FunctionResult(result)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

    def extract_context_from_pb_exec(
            self, pb_exec: PBExecDetail, playbook: Playbook, incident: Incident) -> PlaybookContext:
        rh = RestHelper()

        object_type = PlaybookObjectType.DATATABLE # fallback to datatable
        object_str = ""

        try:
            object_type = PlaybookObjectType(playbook["object_type"])
        except:
            pass # object_type is likely datatable
        match object_type:
            case PlaybookObjectType.NOTE:
                if pb_exec["object"].get("object_id") is not None:
                    note: Note = rh.do_request(
                        RestUrls.GET_NOTE,
                        inc_id=incident["id"],
                        note_id=pb_exec["object"].get("object_id", "Unk"),
                    )
                    note_author = note['modify_principal']['display_name']
                    note_text = RichTextHelper().extract_text(note['text'])[:60]

                    object_str = f"Note from {note_author} with contents: {note_text}"
                else:
                    object_str = "Private note."
            case (
                PlaybookObjectType.ARTIFACT
                | PlaybookObjectType.ATTACHMENT
                | PlaybookObjectType.TASK
            ):
                object_str = (
                    object_type.name.capitalize()
                    + ": "
                    + (pb_exec["object"].get("object_name") or "Private object")[:60]
                )
            case PlaybookObjectType.INCIDENT:
                object_str = "Invoked on the incident"
            case PlaybookObjectType.MILESTONE:
                object_str = f'Invoked on Milestone: {(pb_exec["object"].get("object_name") or "Private milestone")[:60]}'
            case _:
                object_str = "Invoked on a data table"

        activation_type = playbook["activation_type"]
        activation_conditions = []
        activation_logic: str = "all"  # default
        custom_condition = None

        if activation_type == "manual":
            if (
                playbook["manual_settings"]
                and playbook["manual_settings"]["activation_conditions"]
            ):
                pb_activation = playbook["manual_settings"][
                    "activation_conditions"
                ]
                activation_conditions = pb_activation["conditions"]
                activation_logic = pb_activation["logic_type"]
        else:
            if (
                playbook["activation_details"]
                and playbook["activation_details"]["activation_conditions"]
            ):
                pb_activation = playbook["activation_details"][
                    "activation_conditions"
                ]
                activation_conditions = pb_activation["conditions"]
                activation_logic = pb_activation["logic_type"]

        if activation_logic == "advanced":
            try:
                if activation_type == "manual":
                    custom_condition = playbook["manual_settings"][
                        "activation_conditions"
                    ]["custom_condition"]
            finally:
                pass

        pb_name = playbook["display_name"]
        pb_desc = playbook.get("description", "N/A")

        execution_activities: List[PBExecActivity] = rh.do_request(
            RestUrls.PLAYBOOK_EXECUTION_ACTIVITIES,
            object_name=pb_name,
            execution_id=pb_exec.get("id")
        )

        activity_messages: List[PBExecActivity] = []

        # an activity should correlate directly to an individual node (e.g., a function)
        for activity in execution_activities["activity_status"]:
            if "node_display_name" not in activity["activity_ref"]:
                # node is end or a gateway - which will have flows which should be used instead
                continue

            # sort messages by date and cast
            messages = activity.get("messages")
            messages = sorted(messages, key=lambda msg: msg.get("create_date"))
            for msg in messages:
                if isinstance(msg["create_date"], (float, int)):
                    msg["create_date"] = self.format_millis_timestamp(msg["create_date"])
                if isinstance(msg["type"], (int)):
                    msg["type"] = ActivityMessageTypes[msg["type"]]

            activity["messages"] = messages
            if "start_time" in activity and isinstance(
                activity["start_time"], (float, int)
            ):
                activity["start_time_str"] = self.format_millis_timestamp(activity["start_time"])

            activity_messages.append(activity)


        activity_messages = sorted(
            activity_messages,
            key=lambda act: act.get("start_time", float("inf")),
        )
        playbook_model = xml_to_playbook_model(playbook["content"]["xml"])
        sequence_flow = model_to_sequence_flow(playbook_model)
        playbook_scripts = model_to_scripts(playbook_model)

        conditions = friendly_activation_conditions(
            activation_type,
            activation_logic,
            object_type,
            custom_condition,
            activation_conditions,
        )

        activities = friendly_playbook_activities(activity_messages)
        pb_outstanding_tasks = ""

        pending_tasks = [
            msg["activity_ref"]["node_display_name"]
                for msg in activity_messages
                if msg["status"] == "pending" and msg["activity_ref"]["activity_type"] == "user_task"]

        if len(pending_tasks) > 0:
            pb_outstanding_tasks = """
PENDING TASKS:

Pending tasks added to the incident by this playbook:
    -""" + "\n\t- ".join(pending_tasks)

        incident_types = "None"
        if incident["incident_type_ids"]:
            types = RestHelper().do_request(RestUrls.GET_INCIDENT_TYPES)
            incident_type_names = []
            for typ_id in incident["incident_type_ids"]:
                typ_id = str(typ_id)
                if typ_id in types.keys():
                    incident_type_names.append(types[typ_id]["name"])

            if incident_type_names:
                incident_types = ', '.join(incident_type_names)

        return PlaybookContext(
            playbook_name=pb_name,
            playbook_description=str(pb_desc) or '',
            status=pb_exec["status"],

            incident_ref=f"{incident['id']}: {incident['name']}",
            incident_types=incident_types,

            activation_type=activation_type,
            activation_conditions_str=conditions,
            activated_by_name=pb_exec["last_activity_by"]["display_name"],

            activities_str=activities,
            outstanding_tasks=pb_outstanding_tasks,

            target_type=object_type.name.capitalize(),
            target_object=object_str,

            start_time=self.format_millis_timestamp(pb_exec["start_time"] / 1000) if "start_time" in pb_exec else "N/A",
            duration=format_duration(pb_exec["elapsed_time"]) if "elapsed_time" in pb_exec else "N/A",
            end_time=\
                self.format_millis_timestamp(pb_exec["last_activity_time"]) \
                    if "last_activity_time" in pb_exec and pb_exec["status"] not in ["running"] else "N/A",

            mermaid_diagram=sequence_flow,
            scripts_info="\n".join(playbook_scripts) or ''
        )

    def format_response(self, data: PlaybookExecutionSummaryData) -> str:

        execution_phases = 'N/A'

        if data.analysis.execution_phases:
            accumulated_phases = []
            for phase in data.analysis.execution_phases:
                phase_status = " (Complete)" if phase.is_complete else ""
                phase_str = f"\n**Phase: {phase.phase_name}{phase_status}**\n"

                if phase.conditions:
                    phase_str += "\n\nConditions:\n"
                    for condition in phase.conditions:
                        phase_str += f"\n- {condition}"

                if phase.notes:
                    phase_str += "\n\nNotes:\n"
                    for note in phase.notes:
                        phase_str += f"\n- {note}"

                accumulated_phases.append(phase_str)

            execution_phases = "\n".join(accumulated_phases)

        output = f"""
**Playbook name**: {data.playbook_name}

**Playbook status**: **{data.status}**

**Incident**: {data.incident_ref}

**Playbook object type**: {data.target_type}

**Playbook target**: {data.target_object}

---

### Executive summary

{data.analysis.executive_summary}

---

#### Activation information

{data.analysis.activation_summary}

---

#### Execution flow and playbook branching

{execution_phases}

"""
        if data.status not in ["completed", "canceled", "suspended"]:
            final_step_name = 'Next steps' if data.status == 'running' else 'Recommendations'

            output += f"\n---\n\n#### {final_step_name}\n\n{data.analysis.recommendations}"
        return output
