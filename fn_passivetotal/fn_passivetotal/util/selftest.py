# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

import logging
from resilient_lib import RequestsCommon

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    
    app_configs = opts.get("fn_passivetotal", {})

    print(app_configs)

    url = app_configs["passivetotal_base_url"] + app_configs["passivetotal_passive_dns_api_url"]
    data = {'query': '8.8.8.8'}
    auth = (app_configs["passivetotal_username"], app_configs["passivetotal_api_key"])

    try: 
        req = RequestsCommon(opts, app_configs)
        req.execute("get", url, auth=auth, json=data)
        return {"state": "success"}

    except Exception as error:
        return {
            "state": "failure",
            "reason": error
        }
