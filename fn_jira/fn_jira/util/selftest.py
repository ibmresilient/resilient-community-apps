# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Function implementation
   test with: resilient-circuits selftest -l fn_jira
"""
import logging
import json
from fn_jira.lib.requests_common import execute_call
from fn_jira.lib.resilient_common import parse_bool

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())

SESSION_PARAM = "rest/auth/1/session"
HTTP_HEADERS = {'content-type': 'application/json'}


def selftest_function(opts):
    """
    This test will attempt to login to jira. If successful, the session is ended
    """
    options = opts.get("jira", {})

    # auth/1/session
    url = '/'.join((options['url'], SESSION_PARAM))

    payload = {
        "username": options['user'],
        "password": options['password']
    }

    verify_flag = parse_bool(options['verify_cert'])

    try:
        result = execute_call(log, 'post', url, None, None, json.dumps(payload), verify_flag, HTTP_HEADERS)

        jsessionID = HTTP_HEADERS.copy()
        jsessionID['cookie'] = "{}={}".format(result['session']['name'], result['session']['value'])
        result = execute_call(log, 'delete', url, None, None, None, verify_flag, jsessionID)
        return {"state": "success"}
    except Exception as e:
        log and log.error(e)
        return {"state": "failure",
                "reason": e
                }
