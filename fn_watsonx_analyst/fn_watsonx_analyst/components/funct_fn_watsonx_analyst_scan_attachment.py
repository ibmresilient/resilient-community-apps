# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.2.1096

"""AppFunction implementation"""

from resilient_circuits import (
    AppFunctionComponent,
    app_function,
    FunctionResult,
    FunctionError,
)

from fn_watsonx_analyst.components.funct_fn_watsonx_analyst_scan_artifact import (
    scan_artifact_or_attachment,
)
from fn_watsonx_analyst.util.errors import WatsonxApiException
from fn_watsonx_analyst.util.logging_helper import create_logger, generate_request_id
from fn_watsonx_analyst.util.state_manager import app_state

PACKAGE_NAME = "fn_watsonx_analyst"
FN_NAME = "fn_watsonx_analyst_scan_attachment"

log = create_logger(__name__)


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'fn_watsonx_analyst_scan_attachment'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Use watsonx™ to scan an artifact, and assess whether the attachment indicates any malicious activity. Design to work with log files, scripts (e.g. Bash, Python, Lua, Powershell, Perl), but should be able to summarize other textual files.
        Inputs:
            -   fn_inputs.fn_watsonx_analyst_attachment_id
            -   fn_inputs.fn_watsonx_analyst_model_id
            -   fn_inputs.fn_watsonx_analyst_incident_id
            -   fn_watsonx_analyst_task_id
        """

        _ = generate_request_id()
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        inc_id = getattr(fn_inputs, "fn_watsonx_analyst_incident_id", None)
        att_id = getattr(fn_inputs, "fn_watsonx_analyst_attachment_id", None)
        task_id = getattr(fn_inputs, "fn_watsonx_analyst_task_id", None)

        app_state.get().reset()

        app_state.get().set_model(
            getattr(fn_inputs, "fn_watsonx_analyst_model_id", None)
        )
        app_state.get().opts = self.opts
        app_state.get().res_client = self.rest_client()

        err_msg = "Unable to generate attachment summary. "
        try:
            results = scan_artifact_or_attachment(
                inc_id, None, att_id, task_id
            )

            yield FunctionResult(results)
            return
        except ValueError as e:
            err_msg = f"{err_msg}{str(e)}"
            log.exception(err_msg)
        except WatsonxApiException as e:
            err_msg += e.msg
            log.exception("API exception when invoking artifact scan.")
        except Exception as e:
            log.exception("Unkown exception when invoking artifact scan.")
            err_msg += str(e)

        yield FunctionError(err_msg)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")
