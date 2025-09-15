# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.0.974

"""AppFunction implementation"""

from typing import List, Tuple

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult, FunctionError
from resilient_lib import IntegrationError, validate_fields

from fn_watsonx_analyst.types import incident
from fn_watsonx_analyst.util.response_helper import ResponseHelper
from fn_watsonx_analyst.util.logging_helper import create_logger, generate_request_id
from fn_watsonx_analyst.config import load_summarization_config
from fn_watsonx_analyst.util.ContextHelper import ContextHelper
from fn_watsonx_analyst.util.QueryHelper import QueryHelper
from fn_watsonx_analyst.util.ModelTag import AiResponsePurpose
from fn_watsonx_analyst.util.chunking.chunking import Chunking
from fn_watsonx_analyst.util.prompting import Prompting
from fn_watsonx_analyst.types.ai_response import AIResponse

from fn_watsonx_analyst.util.state_manager import app_state

PACKAGE_NAME = "fn_watsonx_analyst"
FN_NAME = "fn_watsonx_analyst_summarize_incident"

log = create_logger(__name__)

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'fn_watsonx_analyst_summarize_incident'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

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
        _ = generate_request_id()
        try:
            yield self.status_message(f"Starting App Function: '{FN_NAME}'")

            # Validate required inputs
            validate_fields([
                "fn_watsonx_analyst_summary_type",
                "fn_watsonx_analyst_model_id",
                "fn_watsonx_analyst_incident_id",
                "fn_watsonx_analyst_data_config"
            ], fn_inputs)

            summary_type = fn_inputs.fn_watsonx_analyst_summary_type
            inc_id = fn_inputs.fn_watsonx_analyst_incident_id

            app_state.get().reset()

            app_state.get().res_client = self.rest_client()
            app_state.get().set_model(fn_inputs.fn_watsonx_analyst_model_id)
            app_state.get().opts = self.opts
            app_state.get().purpose = AiResponsePurpose.INCIDENT_SUMMARY
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
                raise ValueError(f"Unknown summary type '{summary_type}'. Available types: {', '.join(summary_types_config.keys())}")

            # Assemble context and prompt
            context = " ".join(chunks)
            query = f"Provide a {summary_type} summary of this incident."

            # 4. Build prompt by extracting values from summarization config
            prompting = Prompting()
            prompt = prompting.build_prompt(
                query=query,
                context=context,
                messages=config["help_user_text"],
                relevant_fields_info = config["relevant_fields_info"],
                system_prompt=summary_types_config[summary_type_lower]["system_prompt"],
                max_token_limit=config.get("default_max_token_limit", 800))

            # 5. Generate summary via WatsonX
            response = QueryHelper().text_generation(
                prompt,
            )

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
                            if task.get('complete') == True:
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
                            output.append(f'\n{"- " * indent}**Phase: ' + phase.get('phase_name', 'idk') + '**')
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
                prefix = f"**Executive Summary**: {incident_name}\n\n**Incident Type(s)**: {', '.join(incident_types)}\n\n**Incident Severity**: {incident_severity}\n"
            response['results'][0]['generated_text'] = prefix + '<br>' + response['results'][0]['generated_text'] + '\n' + postfix

            # 7. Respond
            result: AIResponse = ResponseHelper().text_generation_to_ai_response(
                response
            )
            
            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")
            yield FunctionResult(result)

        except IntegrationError as e:
            log.exception("IntegrationError in summarization function")
            yield FunctionError(str(e))

        except Exception as e:
            log.exception("Unexpected error in summarization function")
            yield FunctionError(str(e))
