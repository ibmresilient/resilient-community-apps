# -*- coding: utf-8 -*-
# (c) Copyright IBM Corporation 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_urlhaus
"""

import logging
from fn_urlhaus.components.func_urlhaus import FunctionComponent

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get("fn_urlhaus", {})

    fn = FunctionComponent(opts)

    params = { "urlhaus_artifact_type": "URL",
               "urlhaus_artifact_value": "abc"
             }

    try:
        results = fn._urlhaus_lookup(None, None, params)
        return {"state": "success"}
    except Exception as err:
        print (err)
        return {"state": "failure"}


