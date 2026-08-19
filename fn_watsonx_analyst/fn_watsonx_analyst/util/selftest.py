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

from resilient_circuits.helpers import get_resilient_client_for_selftest

from fn_watsonx_analyst.util.errors import WatsonxApiException
from fn_watsonx_analyst.util.logging_helper import create_logger
from fn_watsonx_analyst.util.model_helper import ModelHelper
from fn_watsonx_analyst.util.rest import RestHelper, RestUrls
from fn_watsonx_analyst.util.state_manager import app_state
from fn_watsonx_analyst.util.watsonx_client import WatsonxClient
from fn_watsonx_analyst.watsonx_app_function import WatsonxAppFunction

log = create_logger(__name__)

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """

    state = "failure"
    reason = ""

    try:
        app_state.get().opts = opts
        app_state.get().res_client = get_resilient_client_for_selftest(ALLOW_UNRECOGNIZED=True)

        required_fields = ["watsonx_project_id", "watsonx_endpoint", "watsonx_api_key"]

        if not "fn_watsonx_analyst" in opts:
            reason = "Config does not have an fn_watsonx_analyst section"
            raise ValueError()

        watsonx_config = opts["fn_watsonx_analyst"]
        for field in required_fields:
            if field not in watsonx_config or \
                not watsonx_config.get(field) or \
                str(watsonx_config.get(field, "")).strip() == "":
                reason = f"{field} is empty or missing from fn_watsonx_analyst section in app.config"
                raise ValueError()

        client = WatsonxClient()
        models = client.get_available_models()

        if not client.check_project():
            reason = "Project details could not be retrieved. Check the `watsonx_project_id` field in app.config"
            raise ValueError()

        if WatsonxAppFunction.ai_fields_present():
            model_id = opts["fn_watsonx_analyst"].get("watsonx_model", ModelHelper.get_default_model()["name"])
            if model_id not in models:
                reason = f"Model: {model_id} is not available for the watsonx region, please specify another."
                raise ValueError()

            payload = {
                "provider_type": "watsonx",
                "additional_config": {
                    "base_url": watsonx_config["watsonx_endpoint"],
                    "project_id": watsonx_config["watsonx_project_id"],
                    "model_id": model_id,
                    "api_key_secret": watsonx_config["watsonx_api_key"]
                }
            }
            try:
                response = RestHelper().do_request(RestUrls.STORE_AI_PROVIDER_CONFIG, body=payload)
            except Exception as e:
                reason = "Failed to store AI provider configuration in SOAR " + str(e)
                raise ValueError()

            if response:
                try:
                    RestHelper().do_request(RestUrls.TEST_AI_PROVIDER_CONFIG)
                except Exception as e:
                    reason = "SOAR could not validate the AI Provider configuration, or could not reach IBM Cloud: " + str(e)
                    raise ValueError()

        if not reason:
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
