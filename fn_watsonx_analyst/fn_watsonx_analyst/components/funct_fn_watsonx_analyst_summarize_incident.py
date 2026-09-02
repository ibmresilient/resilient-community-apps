# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2026. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.0.974

"""AppFunction implementation"""
import json
from typing import ClassVar, List, Tuple

from resilient_circuits import app_function, FunctionResult, FunctionError
from resilient_lib import IntegrationError, validate_fields

from fn_watsonx_analyst.watsonx_app_function import WatsonxAppFunction
from fn_watsonx_analyst.util.response_helper import ResponseHelper
from fn_watsonx_analyst.util.logging_helper import create_logger
from fn_watsonx_analyst.config import load_summarization_config
from fn_watsonx_analyst.util.ContextHelper import ContextHelper
from fn_watsonx_analyst.util.ModelTag import AiResponsePurpose
from fn_watsonx_analyst.util.chunking.chunking import Chunking
from fn_watsonx_analyst.util.chat_prompting import ChatPrompting
from fn_watsonx_analyst.util.rest import RestHelper, RestUrls
from fn_watsonx_analyst.util.watsonx_client import StructuredOutputBase, WatsonxClient
from fn_watsonx_analyst.types.ai_response import AIResponse

from fn_watsonx_analyst.util.state_manager import app_state

FN_NAME = "fn_watsonx_analyst_summarize_incident"

log = create_logger(__name__)

class IncidentTechSummarySchema(StructuredOutputBase):
    artifact_analysis: str
    mitigation_actions: str
    technical_overview: str

    SAMPLE_DATA: ClassVar[dict] = {
        "artifact_analysis": "Lorem ipsum",
        "mitigation_actions": "Lorem ipsum",
        "technical_overview": "Lorem ipsum",
    }

class IncidentExecSummarySchema(StructuredOutputBase):
    attack_summary: str
    defense_summary: str
    situation_summary: str

    SAMPLE_DATA: ClassVar[dict] = {
        "attack_summary": "Lorem ipsum",
        "defense_summary": "Lorem ipsum",
        "situation_summary": "Lorem ipsum",
    }

class FunctionComponent(WatsonxAppFunction):
    """Component that implements function 'fn_watsonx_analyst_summarize_incident'"""

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Generate an incident summary of a given type.
        Inputs:
            -   fn_inputs.fn_watsonx_analyst_summary_type
            -   fn_inputs.fn_watsonx_analyst_model_id
            -   fn_inputs.fn_watsonx_analyst_incident_id
            -   fn_inputs.fn_watsonx_analyst_data_config
        """
        try:
            # Validate required inputs
            validate_fields([
                "fn_watsonx_analyst_summary_type",
                "fn_watsonx_analyst_model_id",
                "fn_watsonx_analyst_incident_id",
                "fn_watsonx_analyst_data_config"
            ], fn_inputs)

            summary_type = fn_inputs.fn_watsonx_analyst_summary_type
            inc_id = fn_inputs.fn_watsonx_analyst_incident_id

            yield self.setup(fn_inputs, AiResponsePurpose.INCIDENT_SUMMARY, FN_NAME)
            app_state.get().data_config = fn_inputs.fn_watsonx_analyst_data_config

            # 1. Load incident context as JSON
            context_helper = ContextHelper(inc_id=inc_id)
            incident_payload = context_helper.build_full_data()

            # 2. Chunk incident context for processing
            chunker = Chunking()
            chunks = chunker.split_json_to_chunks(incident_payload)

            # 3. Set up summarizer prompt components
            # Load summarisation config
            config = load_summarization_config()

            # Validate summary_type
            summary_type_lower = summary_type.lower()
            summary_types_config = config.get("summary_types", {})
            if summary_type_lower not in summary_types_config:
                raise ValueError(
                    f"Unknown summary type '{summary_type}'. Available types: {', '.join(summary_types_config.keys())}")

            # Assemble context and user message
            context = " ".join(chunks)

            system_prompt_parts = []

            # Add relevant fields info if present
            if config.get("relevant_fields_info"):
                system_prompt_parts.append(config["relevant_fields_info"])

            # Add the main system prompt for the summary type
            system_prompt_parts.append(summary_types_config[summary_type_lower]["system_prompt"])

            system_prompt = "\n\n".join(system_prompt_parts)

            # Build user message with help text and context
            user_message_parts = []

            if config.get("help_user_text"):
                user_message_parts.append(config["help_user_text"])

            user_message_parts.append(f"Provide a {summary_type} summary of this incident.")
            user_message_parts.append(f"\nIncident Data:\n{context}")

            user_message = "\n\n".join(user_message_parts)

            # 4. Build chat messages using ChatPrompting
            chat_prompting = ChatPrompting()
            messages = chat_prompting.build_simple_chat(
                system_prompt=system_prompt,
                user_message=user_message
            )

            response_format = IncidentTechSummarySchema if summary_type_lower == "technical" \
                else IncidentExecSummarySchema

            # 5. Generate summary via WatsonX using chat API
            response = WatsonxClient().chat(messages, response_format=response_format)

            # 6. Prepend Incident name, Incident types, and Incident severity to the summary
            incident_name = incident_payload.get('incident', {}).get('name', 'Unknown')
            incident_types: List[str]
            incident_type_ids = incident_payload.get('incident', {}).get('incident_type_ids')

            # Convert to list of strings and handle empty/None values
            incident_types = [str(type_id) for type_id in incident_type_ids] if incident_type_ids else ['Unknown']
            incident_severity = incident_payload.get('incident', {}).get('severity_code', 'Unknown')

            postfix = ''
            if summary_type_lower == 'technical':
                prefix = f"**Technical Summary**: {incident_name}\n\n**Incident Type(s)**: {', '.join(incident_types)}\n\n**Incident Severity**: {incident_severity}\n"
                tasktree = incident_payload.get('incident').get('tasktree', [])

                def traverse_tasktree(tasktree: dict, parent: str = '') -> Tuple[dict, dict]:
                    complete_tasktree = {}
                    incomplete_tasktree = {} # phase: [tasks]
                    for phase in tasktree:

                        phase_name = phase.get('phase_name')
                        if parent:
                            phase_name = parent + ' - ' + phase_name

                        complete_tasktree[phase_name] = {'tasks': [], 'child_phases': []}
                        incomplete_tasktree[phase_name] = {'tasks': [], 'child_phases': []}

                        for task in phase.get('tasks', []):
                            if task.get("status", "") == "Closed":
                                complete_tasktree[phase_name]['tasks'].append(task.get('name'))
                            else:
                                incomplete_tasktree[phase_name]['tasks'].append(task.get('name'))
                        complete_children, incomplete_children = traverse_tasktree(
                            phase.get('child_phases', []), parent=phase_name)

                        complete_tasktree[phase_name]['child_phases'] = complete_children
                        incomplete_tasktree[phase_name]['child_phases'] = incomplete_children
                    return complete_tasktree, incomplete_tasktree


                output = []
                complete_tasks = True

                for tasktree in traverse_tasktree(tasktree):
                    if len(tasktree) > 0:
                        output.append('\n')

                    if complete_tasks:
                        output.append('\n**Completed tasks**:')
                    else:
                        output.append('\n**Incomplete tasks**:')
                    complete_tasks = not complete_tasks

                    def add_phase(phase: dict, indent=0):
                        # add phase (recurses into child_phases) to output
                        if len(phase.get('tasks', [])) > 0:
                            output.append(f'\n{"- " * indent}**Phase: ' + phase.get('phase_name', 'Unknown') + '**')
                            for task in phase['tasks']:
                                output.append("\n" + "\t" * indent + "- Task: " + str(task))

                        for child_phase_name, child_phase in phase.get('child_phases', {}).items():
                            child_phase['phase_name'] = child_phase_name
                            add_phase(child_phase)

                    for phase_name, phase in tasktree.items():
                        phase['phase_name'] = phase_name
                        add_phase(phase)

                postfix = '\n'.join(output)
            else:
                prefix = f"""**Executive Summary**:
{incident_name}

**Incident Type(s)**: {', '.join(incident_types)}

**Incident Severity**: {incident_severity}
"""

            # Modify the chat response content
            inc_analysis = response_format.model_validate_json(response["choices"][0]["message"]["content"])

            if response_format == IncidentTechSummarySchema:
                data = {
                    'Technical overview': inc_analysis.technical_overview,
                    'Artifact analysis': inc_analysis.artifact_analysis,
                    'Mitigation actions': inc_analysis.mitigation_actions
                }
            else:
                data = {
                    'Situation summary': inc_analysis.situation_summary,
                    'Attack summary': inc_analysis.attack_summary,
                    'Defense summary': inc_analysis.defense_summary
                }

            output = prefix + '\n' + '\n'.join([f"\n#### {key}\n\n{val}" for key, val in data.items()]) + '\n' + postfix
            response['choices'][0]['message']['content'] = output


            # 7. Respond using chat response handler
            result: AIResponse = ResponseHelper().text_chat_to_ai_response(
                response
            )

            if self.ai_fields_present():
                log.debug(f"Setting ai insights for incident ID: {inc_id}")
                summ_key = "ai_exec_summary" if summary_type_lower == "executive" else "ai_tech_summary"

                helper = RestHelper()
                inc = helper.do_request(RestUrls.INCIDENT_DETAILS, inc_id=inc_id)
                inc[summ_key] = json.dumps(result)
                helper.do_request(RestUrls.UPDATE_INCIDENT, inc_id=inc_id, body=inc)
                result = ResponseHelper.set_insights_added(result)

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")
            yield FunctionResult(result)

        except IntegrationError as e:
            log.exception("IntegrationError in summarization function")
            yield FunctionError(str(e))

        except Exception as e:
            log.exception("Unexpected error in summarization function")
            yield FunctionError(str(e))
