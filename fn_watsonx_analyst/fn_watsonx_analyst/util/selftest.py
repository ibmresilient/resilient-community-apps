# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
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

import logging

from requests import RequestException
from fn_watsonx_analyst.util.QueryHelper import QueryHelper
from fn_watsonx_analyst.util.errors import WatsonxApiException

log = logging.getLogger(__name__)


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """

    state = "failure"
    reason = "Check the configuration file for invalid syntax. Ensure that secrets are set for watsonx_endpoint, watsonx_project_id, and watsonx_api_key. Also ensure that the [watsonx_property_labels] section is in the config and valid."

    try:
        models = QueryHelper(opts=opts).get_generation_models()

        if models is None or len(models) == 0:
            raise RequestException

        labels = opts.get("watsonx_property_labels", None)
        if labels is None or not hasattr(labels, "items"):
            raise ValueError

        for key, value in labels.items():
            if not key or not value:
                raise ValueError

        state = ("success",)
        reason = f"Successfully connected to watsonx.ai. Found {len(models)} models with text_generation capability."

    except ValueError:
        reason = "Invalid property labels configuration. " + reason
    except (ConnectionError, RequestException):
        reason = "Error when connecting to watsonx.ai, or bad configuration. " + reason
    except WatsonxApiException as e:
        reason = e.msg + reason
    except Exception as e:
        reason = "Unkown error" + str(e) + reason

    return {"state": state, "reason": reason}
