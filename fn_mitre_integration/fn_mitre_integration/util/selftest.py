# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_mitre_integration
"""

import logging
from fn_mitre_integration.lib import mitre_attack

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get("fn_mitre_integration", {})
    mitre_conn = mitre_attack.MitreAttackConnection()
    try:
        mitre_conn.connect_server()
    except Exception:
        return {"state": "failure"}

    if mitre_conn.composite_ds is not None:
        return {"state": "success"}

    return {"state": "failure"}