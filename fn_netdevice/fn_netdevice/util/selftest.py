# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
"""Function implementation
   test with: resilient-circuits selftest -l fn_netdevice
"""

import logging
from fn_netdevice.lib.netmiko_core import execute

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Run through all the defined devices and attempt to connect. The results are returned in a dictionary
    """
    options = opts.get("fn_netdevice", {})

    names = options.get("selftest", None)
    if not names:
        return { "state": "unimplemented"}

    results = {"state": "success"}
    for device in names.split(","):
        try:
            section = device.strip()
            settings = opts.get(section, None)
            if not settings:
                results[section] = {"status": "failure",
                                    "reason": u"section '{}' not found".format(section)
                                   }
                results["state"] = "failure"
            else:
                settings.pop('use_commit', None)  # remove parameters not needed for connection
                result = execute(settings, None, None, False, False)
                results[section] = result
                if result["status"] == "failure":
                    results["state"] = "failure"

        except Exception as err:
            results[section] = {"status": "failure",
                                "reason": str(err)
                               }
            results["state"] = "failure"

    return results