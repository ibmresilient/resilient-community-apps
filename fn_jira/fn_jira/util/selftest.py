# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
"""Function implementation
   test with: resilient-circuits selftest -l fn_jira
"""
import logging
import json
from resilient_lib import RequestsCommon, str_to_bool

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

    verify_flag = str_to_bool(options['verify_cert'])

    try:
        req_common = RequestsCommon(opts=opts, function_opts=options)
        result = req_common.execute_call_v2('post', url,  auth=(options['user'], options['password']),
                                               data=json.dumps(payload), verify=verify_flag, headers=HTTP_HEADERS)
        resp = result.json()

        jsessionID = HTTP_HEADERS.copy()
        jsessionID['cookie'] = "{}={}".format(resp['session']['name'], resp['session']['value'])
        result = req_common.execute_call_v2('delete', url, verify=verify_flag, headers=jsessionID)
        return {"state": "success"}
    except Exception as e:
        log and log.error(e)
        return {"state": "failure",
                "reason": e
               }
