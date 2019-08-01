# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
"""Function implementation
   test with: resilient-circuits selftest -l fn_jira
"""
import logging
import fn_jira.lib.constants as constants
from resilient_lib import validate_fields, MarkdownParser, str_to_bool
from resilient_lib import RequestsCommon

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())

SESSION_PARAM = "rest/auth/1/session"


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

    verify_flag = str_to_bool(options['verify_cert'])

    try:
        req_common = RequestsCommon(opts=opts, function_opts=options)

        resp = req_common.execute_call_v2('post', url, json=payload,
                                                     verify=verify_flag, headers=constants.HTTP_HEADERS)
        resp_json = resp.json()

        jsessionID = constants.HTTP_HEADERS.copy()
        jsessionID['cookie'] = "{}={}".format(resp_json['session']['name'], resp_json['session']['value'])
        resp = req_common.execute_call_v2('delete', url,
                                          verify=verify_flag, headers=jsessionID)
        return {"state": "success"}
    except Exception as e:
        log and log.error(e)
        return {"state": "failure",
                "reason": e
                }
