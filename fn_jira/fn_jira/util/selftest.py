# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
"""Function implementation
   test with: resilient-circuits selftest -l fn_jira
"""
import logging
from resilient_lib import RequestsCommon, str_to_bool
from fn_jira.util.helper import CONFIG_DATA_SECTION, validate_app_configs, get_jira_client, format_dict

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())


def print_error(reason, app_configs):
    err_str = "Test Failure! Possible invalid credentials\nReason:\n\t{0}".format(reason)
    err_str += "\n\nApp Configs:"
    err_str += format_dict(app_configs)
    log.error(err_str)


def selftest_function(opts):
    """
    This test will attempt to login to Jira
    """
    app_configs = opts.get(CONFIG_DATA_SECTION, {})
    rc = RequestsCommon(opts, app_configs)

    try:
        valid_app_configs = validate_app_configs(app_configs)

        get_jira_client(valid_app_configs, rc)

        return {"state": "success"}

    except Exception as err:
        print_error(err, app_configs)
        return {"state": "failure", "reason": err}
