# -*- coding: utf-8 -*-

"""
Function implementation test.
Usage: 
    resilient-circuits selftest -l fn_remedy
    resilient-circuits selftest --print-env -l fn_remedy

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

from resilient_lib import RequestsCommon, validate_fields, str_to_bool
from fn_remedy.lib.remedy.RemedyAPIClient import RemedyClient

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

CONFIG_DATA_SECTION = "fn_remedy"
FORM_NAME = "HPD:IncidentInterface_Create"


def selftest_function(opts):
    """
    Tests connectivity to the Remedy API by querying for the schema
    of the standard HPD:IncidentInterface_Create form. The method
    returns success if Remedy gives a 200 Response.
    """
    app_configs = opts.get(CONFIG_DATA_SECTION, {})

    # Get and validate app configs
    validate_fields([
        {"name": "remedy_host", "placeholder": "<example.domain>"},
        {"name": "remedy_user", "placeholder": "<example_user>"},
        {"name": "remedy_password", "placeholder": "xxx"}],
        app_configs)

    host = app_configs.get("remedy_host")
    user = app_configs.get("remedy_user")
    password = app_configs.get("remedy_password")
    port = app_configs.get("remedy_port", None)
    verify = str_to_bool(app_configs.get("verify", "true"))

    rc = RequestsCommon(opts=opts)

    try:
        client = RemedyClient(host, user, password, rc, port=port, verify=verify)
        schema, status_code = client.get_form_schema(FORM_NAME)

        if status_code == 200:
            return {
                "state": "success",
                "reason": "Successfully connected to the Remedy REST API."
            }
        return {
            "state": "failure",
            "reason": "Unexpected response from Remedy: {}".format(status_code)
        }
    except Exception as e:
        return {
            "state": "failure",
            "reason": e
        }
