# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-

from resilient_lib import validate_fields, str_to_bool

CONFIG_DATA_SECTION = "fn_jira"

def validate_app_configs(app_configs):
    valid_app_configs = validate_fields([
        {"name": "url", "placeholder": "https://<jira url>"},
        {"name": "user", "placeholder": "<jira user>"},
        {"name": "password", "placeholder": "<jira user password>"},
        {"name": "verify_cert"}
    ], app_configs)

    valid_app_configs["verify_cert"] = str_to_bool(valid_app_configs.get("verify_cert"))

    return valid_app_configs