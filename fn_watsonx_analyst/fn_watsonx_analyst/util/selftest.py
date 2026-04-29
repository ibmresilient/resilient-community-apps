# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2026. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.0.974

"""
Function implementation test.
Usage: 
    resilient-circuits selftest -l fn-watsonx
    resilient-circuits selftest --print-env -l fn-watsonx

Return examples:
    return {
        "state": "success",
        "reason": "Successful connection to third party endpoint"
    }

    return {
        "state": "failure",
        "reason": "Failed to connect to third party endpoint"
    }
"""

from requests import RequestException
from fn_watsonx_analyst.util.errors import WatsonxApiException
from fn_watsonx_analyst.util.logging_helper import create_logger
from fn_watsonx_analyst.util.state_manager import app_state
from fn_watsonx_analyst.util.watsonx_client import WatsonxClient

log = create_logger(__name__)


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """

    state = "failure"
    # pylint: disable=line-too-long
    reason = "Check the configuration file for invalid syntax. Ensure that secrets are set for watsonx_endpoint, watsonx_project_id, and watsonx_api_key. Also ensure that the [watsonx_property_labels] section is in the config and valid."

    try:
        app_state.get().opts = opts
        client = WatsonxClient()

        client.get_available_models()

        if not client.check_project():
            reason = "Project details could not be retrieved. Check the `watsonx_project_id` field in app.config"
        else:
            state = "success"
            reason = "Successfully connected to watsonx.ai."

    except ValueError:
        reason = "Invalid property labels configuration. " + reason
    except (ConnectionError, RequestException):
        reason = "Error when connecting to watsonx.ai, or bad configuration. " + reason
    except WatsonxApiException as e:
        reason = e.msg + " " + reason
    except Exception as e:
        reason = "/n".join(["Unknown error", str(e), reason])

    return {"state": state, "reason": reason}
