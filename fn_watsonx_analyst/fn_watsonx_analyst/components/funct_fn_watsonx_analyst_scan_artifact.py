# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.0.974
# pylint: disable=line-too-long

"""AppFunction implementation"""

import json

from resilient_circuits import (
    AppFunctionComponent,
    app_function,
    FunctionResult,
    FunctionError,
)
from resilient import SimpleClient

from fn_watsonx_analyst.types.ai_response import AIResponse
from fn_watsonx_analyst.types.artifact import Artifact
from fn_watsonx_analyst.util.ArtifactSummaryGenerator import ArtifactSummaryGenerator
from fn_watsonx_analyst.util.ModelTag import AiResponsePurpose
from fn_watsonx_analyst.util.ContextHelper import ContextHelper, Templates
from fn_watsonx_analyst.util.QueryHelper import QueryHelper
from fn_watsonx_analyst.util.errors import WatsonxApiException
from fn_watsonx_analyst.util.rest import RestHelper, RestUrls
from fn_watsonx_analyst.util.util import create_logger, generate_request_id

PACKAGE_NAME = "fn_watsonx_analyst"
FN_NAME = "fn_watsonx_analyst_scan_artifact"

log = create_logger(__name__)


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'fn_watsonx_analyst_scan_artifact'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Use watsonx™ to scan an artifact, and assess whether the artifact indicates any malicious activity. 
        Designed to work with log files, scripts (e.g. Bash, Python, Lua, Powershell, Perl).
        Inputs:
            -   fn_inputs.fn_watsonx_analyst_artifact_id
            -   fn_inputs.fn_watsonx_analyst_system_prompt
            -   fn_inputs.fn_watsonx_analyst_model_id
            -   fn_inputs.fn_watsonx_analyst_model_id_override
            -   fn_inputs.fn_watsonx_analyst_incident_id
        """
        _ = generate_request_id()

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        inc_id = getattr(fn_inputs, "fn_watsonx_analyst_incident_id", None)
        art_id = getattr(fn_inputs, "fn_watsonx_analyst_artifact_id", None)
        model_id = getattr(fn_inputs, "fn_watsonx_analyst_model_id", None)

        res_client = self.rest_client()

        err_msg = "Unable to generate artifact summary. "
        try:
            results = scan_artifact(res_client, inc_id, art_id, self.opts, model_id)

            yield FunctionResult(results)
            return
        except ValueError:
            err_msg = f"{err_msg}Check app.config for any misconfigurations, and ensure token usage has not been exceeded."
            log.exception(err_msg)
        except WatsonxApiException as e:
            err_msg += e.msg
            log.exception("API exception when invoking artifact scan.")
        except Exception as e:
            log.exception("Unkown exception when invoking artifact scan.")
            err_msg += str(e)

        log.error(err_msg)
        yield FunctionError(err_msg)


def scan_artifact(
    res_client: SimpleClient,
    inc_id: int,
    art_id: int,
    opts: dict,
    model_id="ibm/granite-13b-chat-v2",
) -> AIResponse:
    response: AIResponse = None
    artifact_data: Artifact = RestHelper().do_request(
        res_client, RestUrls.ARTIFACT_DETAILS, inc_id=inc_id, art_id=art_id
    )
    if artifact_data["attachment"]:
        response = ArtifactSummaryGenerator(
            res_client, inc_id, artifact_data, model_id, opts
        ).generate()
    else:
        artifact_data["incident_name"] = artifact_data["inc_name"]
        keys_to_keep = ["value", "description", "incident_name", "global_artifact"]
        artifact_data = {
            key: artifact_data[key] for key in keys_to_keep if key in artifact_data
        }

        prompt = ContextHelper().get_prompt(
            Templates.ASSESS_META_ARTIFACT,
            data=json.dumps(artifact_data, indent=2),
            preamble="",
        )
        response = QueryHelper(res_client, model_id, opts).text_generation(
            prompt, purpose=AiResponsePurpose.ARTIFACT_SUMMARY
        )
    response["generated_text"] = (
        f"Artifact name: {artifact_data['value']}\n\n" + response['generated_text']
    )
    return response
